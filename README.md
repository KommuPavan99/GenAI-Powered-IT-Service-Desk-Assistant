<h1 align="center">🤖 GenAI-Powered IT Service Desk Assistant</h1>

<p align="center">
<b>A Modern AI-Powered IT Service Desk Web Application</b><br><br>

Developed using <b>Django</b> and a <b>Local Large Language Model (Microsoft Phi-3 Mini)</b> running through <b>Ollama</b>, this application automates IT incident management, knowledge retrieval, and intelligent troubleshooting while keeping all AI processing completely offline for enhanced privacy, security, and cost efficiency.
</p>

<hr>

<h2>📌 Introduction</h2>

<p align="justify">
The <b>GenAI-Powered IT Service Desk Assistant</b> is an intelligent web application developed to modernize IT support operations by combining traditional <b>IT Service Management (ITSM)</b> with the capabilities of <b>Generative Artificial Intelligence</b>.
</p>

<p align="justify">
The application enables users to create IT incidents, search a centralized Knowledge Base, and receive AI-generated troubleshooting recommendations through a locally hosted Large Language Model. Rather than relying solely on predefined documentation, the system intelligently combines existing organizational knowledge with AI-generated technical guidance to improve issue resolution.
</p>

<p align="justify">
Unlike cloud-based AI platforms, this project utilizes <b>Microsoft Phi-3 Mini</b> running locally using <b>Ollama</b>. Since all inference is performed on the user's machine, the application provides complete data privacy, offline accessibility, reduced operational cost, and eliminates dependency on external AI APIs.
</p>

<hr>

<h2>📌 Project Overview</h2>

<p align="justify">
The application serves as a centralized IT Service Desk platform that simplifies incident management and technical support. Users can create support tickets, browse troubleshooting documentation, search existing Knowledge Base articles, and interact with an intelligent AI assistant capable of understanding natural language.
</p>

<p align="justify">
Whenever a user submits an IT issue, the system first searches the Knowledge Base for matching solutions. If no suitable solution is available, the request is automatically forwarded to the locally hosted Microsoft Phi-3 Mini model through Ollama, which generates structured troubleshooting recommendations.
</p>

<p align="justify">
The Django Administration Dashboard allows administrators to manage incidents, Knowledge Base articles, and system data efficiently. This hybrid architecture combines rule-based information retrieval with Large Language Models, improving troubleshooting accuracy while reducing incident resolution time.
</p>

<hr>

<h2>✨ Key Features</h2>

<ul>

<li>🏠 Modern and responsive Home Page</li>

<li>📊 Interactive Dashboard displaying incident statistics and system overview</li>

<li>📝 Incident Creation and Management module</li>

<li>📚 Centralized Knowledge Base for troubleshooting articles</li>

<li>🔍 Intelligent Knowledge Base Search using keyword matching</li>

<li>🤖 AI-powered IT Assistant supporting natural language queries</li>

<li>🧠 Local AI integration using Ollama and Microsoft Phi-3 Mini</li>

<li>⚡ Automatic Incident Categorization</li>

<li>🔥 Automatic Priority Prediction</li>

<li>👨‍💼 Django Administration Dashboard</li>

<li>📱 Responsive Bootstrap-based User Interface</li>

<li>🔒 Completely Offline AI Processing (No Cloud APIs)</li>

</ul>

<hr>

<h2>🛠️ Technologies Used</h2>

<p>
The project integrates modern web technologies with Artificial Intelligence to build an intelligent IT Service Desk platform.
</p>

<ul>

<li><b>Python</b> — Backend Programming Language</li>

<li><b>Django</b> — Python Web Framework</li>

<li><b>SQLite</b> — Relational Database</li>

<li><b>HTML5</b> — Web Page Structure</li>

<li><b>CSS3</b> — Styling and Layout</li>

<li><b>Bootstrap 5</b> — Responsive UI Framework</li>

<li><b>JavaScript</b> — Client-side Interactivity</li>

<li><b>Ollama</b> — Local AI Runtime</li>

<li><b>Microsoft Phi-3 Mini</b> — Local Large Language Model</li>

</ul>

<hr>

<h2>🤖 Local AI Setup</h2>

<p>
The AI Assistant runs entirely on the local computer using <b>Ollama</b> and the <b>Microsoft Phi-3 Mini</b> language model. Since no cloud services are used, all user queries remain private and the application continues to function even without an internet connection after the model has been downloaded.
</p>


<hr>

<h2 align="center">🖥️ Project User Interface</h2>
<h2 align="center">🖥️ Project User Interface</h2>

<p align="center">
The following screenshots showcase the complete user interface and workflow of the <b>GenAI-Powered IT Service Desk Assistant</b>. Built with <b>Bootstrap 5</b>, the application offers a clean, responsive, and user-friendly experience across all modules.
</p>

<p align="justify">
The interface guides users through the complete IT support process, including incident creation, dashboard monitoring, Knowledge Base management, intelligent search, and AI-powered troubleshooting. The application first searches the Knowledge Base for existing solutions and then leverages the locally hosted <b>Microsoft Phi-3 Mini</b> model through <b>Ollama</b> to generate intelligent troubleshooting recommendations when needed.
</p>

<p align="justify">
The screenshots below demonstrate each module in sequence, highlighting the application's intuitive design, seamless navigation, and complete workflow from incident reporting to AI-generated technical support.
</p>

<hr>


<hr>

<hr>

<h3>1️⃣ Home Page (Index)</h3>

<p align="justify">
The Home Page serves as the entry point of the application. It introduces users to the GenAI-Powered IT Service Desk Assistant and provides quick navigation to the Dashboard, Incident Management, Knowledge Base, Search functionality, and AI Assistant. The clean and responsive design ensures an intuitive user experience across different devices.
</p>

<img src="servicedesk/Project User Interface/Index.png" width="100%">

<hr>

<h3>2️⃣ Dashboard</h3>

<p align="justify">
The Dashboard provides a comprehensive overview of the IT Service Desk by displaying important metrics such as total incidents, open incidents, resolved incidents, and Knowledge Base records. It serves as the central control panel from which administrators and users can monitor support activities and quickly access different application modules.
</p>

<img src="servicedesk/Project User Interface/Dashboard.png" width="100%">

<hr>

<h3>3️⃣ Create New Incident</h3>

<p align="justify">
This module allows users to submit IT support requests by entering an incident title and description. The application automatically predicts the incident category and priority using predefined business rules, helping support teams organize and prioritize issues more efficiently.
</p>

<img src="servicedesk/Project User Interface/New Incident.png" width="100%">

<hr>

<h3>4️⃣ Knowledge Base</h3>

<p align="justify">
The Knowledge Base stores predefined troubleshooting articles for commonly occurring IT problems. Administrators can continuously update these articles through the Django Administration Dashboard, allowing users to access reliable technical documentation before escalating issues.
</p>

<img src="servicedesk/Project User Interface/Knowledge Base.png" width="100%">

<hr>

<h3>5️⃣ Search Knowledge Base</h3>

<p align="justify">
Users can search the Knowledge Base using keywords related to their issue. The intelligent search feature quickly retrieves relevant troubleshooting articles, enabling users to resolve common problems independently without creating additional support tickets.
</p>

<img src="servicedesk/Project User Interface/Search Knowledge Base-1.png" width="100%">

<hr>

<h3>6️⃣ Search Results</h3>

<p align="justify">
The Search Results page displays all matching Knowledge Base articles based on the user's search query. Multiple relevant solutions can be reviewed, allowing users to choose the most appropriate troubleshooting procedure for their technical issue.
</p>

<img src="servicedesk/Project User Interface/Search Knowledge Base-2.png" width="100%">

<hr>

<h3>7️⃣ AI Assistant</h3>

<p align="justify">
The AI Assistant enables users to describe IT problems in natural language without requiring technical terminology. This conversational interface improves accessibility and allows users to receive intelligent troubleshooting guidance through an easy-to-use chat interface.
</p>

<img src="servicedesk/Project User Interface/AI Assistant.png" width="100%">

<hr>

<h3>8️⃣ AI Processing</h3>

<p align="justify">
When a user submits a query, the application first searches the Knowledge Base for relevant troubleshooting articles. If sufficient information is unavailable, the request is automatically forwarded to the locally hosted Microsoft Phi-3 Mini model running through Ollama. The AI then generates detailed troubleshooting recommendations while ensuring that all processing remains completely offline.
</p>

<img src="servicedesk/Project User Interface/AI Assistant-1.png" width="100%">

<hr>

<h3>9️⃣ AI Response</h3>

<p align="justify">
The AI Response page presents structured troubleshooting guidance generated by combining Knowledge Base information with AI-generated recommendations. This hybrid approach provides users with reliable organizational knowledge enhanced by contextual AI insights, improving both the quality and efficiency of technical support.
</p>

<img src="servicedesk/Project User Interface/AI Response.jpeg" width="100%">

<h2>👨‍💻 Author</h2>

<p>

<b>Kommu Pavan Kumar</b><br>
B.Tech – Computer Science and Engineering

</p>

<hr>

<h2 align="center">⭐ If you found this project useful, don't forget to star this repository!</h2>

<p align="center">
Thank you for visiting this project. Your support and feedback are greatly appreciated. ⭐
</p>
