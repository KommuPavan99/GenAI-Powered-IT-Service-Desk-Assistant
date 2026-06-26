from django.shortcuts import render, redirect
from django.db.models import Q

from .forms import IncidentForm
from .models import Incident, KnowledgeArticle
from .ai_engine import ask_llm, categorize_incident


def format_solution(content):
    """
    Format solution text into readable lines.
    """

    if not content:
        return ""

    content = content.replace("\r\n", "\n")

    sentences = []

    for part in content.split("."):
        part = part.strip()

        if part:
            sentences.append(part + ".")

    return "\n".join(sentences)


def home(request):

    return render(
        request,
        "index.html"
    )


# --------------------------------------------------
# Simple Incident Categorization
# --------------------------------------------------

def categorize_incident(title, description):

    text = (title + " " + description).lower()

    category = "Software"
    priority = "Medium"

    if any(word in text for word in [
        "password",
        "login",
        "authentication",
        "account"
    ]):
        category = "Account"

    elif any(word in text for word in [
        "printer",
        "mouse",
        "keyboard",
        "monitor",
        "battery",
        "screen"
    ]):
        category = "Hardware"

    elif any(word in text for word in [
        "wifi",
        "network",
        "internet",
        "vpn",
        "lan"
    ]):
        category = "Network"

    if any(word in text for word in [
        "urgent",
        "critical",
        "down",
        "server",
        "cannot work"
    ]):
        priority = "High"

    return category, priority


# --------------------------------------------------
# Create Incident
# --------------------------------------------------

def create_incident(request):

    if request.method == "POST":

        form = IncidentForm(request.POST)

        if form.is_valid():

            incident = form.save(commit=False)

            category, priority = categorize_incident(
                incident.title,
                incident.description
            )

            incident.category = category
            incident.priority = priority

            incident.save()

            return redirect("incident_list")

    else:

        form = IncidentForm()

    return render(
        request,
        "incident_form.html",
        {
            "form": form
        }
    )


# --------------------------------------------------
# Incident List
# --------------------------------------------------

def incident_list(request):

    incidents = Incident.objects.all().order_by("-created_at")

    total_incidents = incidents.count()

    open_incidents = incidents.filter(
        status="Open"
    ).count()

    solved_incidents = incidents.filter(
        status="Solved"
    ).count()

    total_articles = KnowledgeArticle.objects.count()

    return render(
        request,
        "incident_list.html",
        {
            "incidents": incidents,
            "total_incidents": total_incidents,
            "open_incidents": open_incidents,
            "solved_incidents": solved_incidents,
            "total_articles": total_articles,
        }
    )


# --------------------------------------------------
# Knowledge Base
# --------------------------------------------------

def knowledge_base(request):

    articles = KnowledgeArticle.objects.all()

    for article in articles:

        article.formatted_content = format_solution(
            article.content
        )

    return render(
        request,
        "knowledge_base.html",
        {
            "articles": articles
        }
    )


# --------------------------------------------------
# Search Knowledge Base
# --------------------------------------------------

def search_knowledge(request):

    query = request.GET.get("q", "")

    articles = []

    if query:

        articles = KnowledgeArticle.objects.filter(

            Q(title__icontains=query)
            |
            Q(category__icontains=query)
            |
            Q(content__icontains=query)

        )

        for article in articles:

            article.formatted_content = format_solution(
                article.content
            )

    return render(
        request,
        "search_knowledge.html",
        {
            "articles": articles,
            "query": query
        }
    )


# --------------------------------------------------
# AI Assistant
# --------------------------------------------------

def ai_assistant(request):

    answer = None
    found = False
    source = None

    if request.method == "POST":

        query = request.POST.get(
            "query",
            ""
        ).strip()

        # ---------- Search Knowledge Base First ----------

        article = KnowledgeArticle.objects.filter(

            Q(title__icontains=query)
            |
            Q(category__icontains=query)
            |
            Q(content__icontains=query)

        ).first()

        if article:

            answer = format_solution(
                article.content
            )

            found = True
            source = "Knowledge Base"

        else:

            # ---------- Ask Local Phi-3 ----------

            try:

                answer = ask_llm(query)

                answer = format_solution(answer)

                found = True
                source = "Phi-3 (Local Ollama)"

            except Exception as e:

                answer = (
                    "Local AI service is unavailable.\n\n"
                    "Please ensure:\n\n"
                    "1. Ollama is running.\n"
                    "2. Phi-3 model is installed.\n"
                    "3. Command 'ollama run phi3:mini' works.\n\n"
                    f"Technical Error:\n{str(e)}"
                )

                found = False
                source = "System"

    return render(
        request,
        "ai_assistant.html",
        {
            "answer": answer,
            "found": found,
            "source": source
        }
    )