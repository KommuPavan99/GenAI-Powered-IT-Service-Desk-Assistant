from ollama import chat


MODEL_NAME = "phi3:mini"


SYSTEM_PROMPT = """
You are an experienced IT Service Desk Engineer.

Your responsibilities include:

• Troubleshooting IT incidents
• Windows support
• Linux support
• Network issues
• Printer issues
• Software installation
• Active Directory
• Microsoft Office
• VPN
• Email issues
• Password reset
• Hardware diagnostics
• Service Desk best practices

Rules:

1. Answer only IT-related questions.
2. Be professional.
3. Be concise.
4. Provide step-by-step troubleshooting.
5. If the problem cannot be solved remotely, recommend contacting the IT Administrator.
6. Never invent information.
"""


def ask_llm(prompt):
    """
    Ask the local Phi-3 model.
    """

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def categorize_incident(title, description):
    """
    Uses Phi-3 to classify an incident.

    Returns:
        Category
        Priority
    """

    prompt = f"""
You are an IT Incident Classifier.

Title:
{title}

Description:
{description}

Choose ONE category from:

Hardware
Software
Network
Security
Email
Printer
Database
Account
Cloud
Other

Choose ONE priority from:

Low
Medium
High
Critical

Return ONLY this format:

Category: <category>
Priority: <priority>
"""

    result = ask_llm(prompt)

    category = "Software"
    priority = "Medium"

    for line in result.splitlines():

        if line.lower().startswith("category:"):
            category = line.split(":", 1)[1].strip()

        elif line.lower().startswith("priority:"):
            priority = line.split(":", 1)[1].strip()

    return category, priority


def generate_resolution(title, description):
    """
    Generate a troubleshooting guide.
    """

    prompt = f"""
Create an IT troubleshooting guide.

Incident Title:
{title}

Incident Description:
{description}

Provide:

1. Possible Cause

2. Troubleshooting Steps

3. Resolution

4. Prevention Tips
"""

    return ask_llm(prompt)


def summarize_incident(title, description):
    """
    Generate a short summary.
    """

    prompt = f"""
Summarize this IT incident in less than 50 words.

Title:
{title}

Description:
{description}
"""

    return ask_llm(prompt)