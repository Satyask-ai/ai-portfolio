
from django.shortcuts import render

def home(request):
    # --- CONFIGURATION ---
    # Once you deploy Streamlit, paste the URL here!
    # Example: "https://surendra-ai-lab.streamlit.app"
    STREAMLIT_URL = "https://your-new-app-name.streamlit.app" 

    profile = {
        "name": "KADA SATYA SURENDRA",
        "title": "Senior AI Engineer",
        "location": "USA",
        "email": "skada544@gmail.com",
        "phone": "+1 (734) 743-1032",
        "summary": "Senior AI/ML Engineer with 10+ years of experience. Expert in LangGraph, Multi-Agent Orchestration,RAG implementations and HIPAA-compliant AI systems."
    }

    # Split skills for better UI layout
    skills = {
        "ai": [
            "LangGraph", "Multi-Agent Systems", "Ragas (Eval)", 
            "Watcher Agents", "LLMOps", "OpenAI GPT-4", "RAG"
        ],
        "engineering": [
            "Python", "FastAPI", "Docker", "CI/CD", 
            "UV Package Manager", "PostgreSQL", "Azure/AWS"
        ]
    }

    experience = [
        {
            "role": "Senior AI Engineer",
            "company": "Epic Systems",
            "date": "Jan 2024 – Present",
            "details": [
                "Led the strategic roadmap for the C-Suite, successfully pitching and executing the enterprise transition from legacy RAG systems (Phase 4) to autonomous agents (Phase 6)..",
                "Reduced the time-to-market for new clinical intake systems from 4 weeks to 3 days by standardizing agent configuration templates..",
                "Mentored a team of 3 junior AI developers, upskilling them in graph-based orchestration and LLMOps best practices.",
                "Architected a 5-node multi-agent ecosystem using LangGraph, successfully transitioning the client from disjointed, single-agent chatbots to a cohesive, enterprise-grade AI workforce..",
                "Scaled the multi-agent system to successfully handle 10,000+ concurrent patient intake queries with sub-2-second latency..",
                "Engineered the central \"Orchestrator Agent\" with dynamic routing capabilities, improving task delegation accuracy to specialized sub-agents (Researcher, Reviewer, Auditor) by 85%.",
                "Eliminated infinite agent loops by 60% through the design of strict cyclical graph constraints and deterministic edge-condition routing within LangGraph.",
                "Designed a seamless Human-in-the-Loop (HITL) interface utilizing LangGraph's native checkpointing, allowing medical professionals to pause, review, and approve critical AI decisions"
            ]
        },
        {
            "role": "AI Engineer",
            "company": "Morgan Stanley",
            "date": "July 2022 – Jan 2024",
            "details": [
                "Saved an estimated $800,000+ annually in operational costs by replacing legacy, labor-intensive keyword searches with a highly accurate semantic AI engine.",
                "Pioneered the early adoption of LangChain and ReAct frameworks within the enterprise, establishing the engineering blueprint for future AI projects.",
                "Accelerated the client intake process by 300%, automating the initial parsing and verification of complex financial profiles.",
                "Architected an enterprise-grade RAG pipeline using early-stage LangChain to process and index millions of dense financial PDFs with 99% data-extraction accuracy.",
                "Built a robust microservices architecture using FastAPI to securely expose LLM agents to internal financial dashboards",
            ]
        },
        {
            "role": "Machine Learning Engineer",
            "company": "Cigna Healthcare",
            "date": "Sep 2020 – June 2022",
            "details": [
                "Slashed manual Subject Matter Expert (SME) review time by 50% by deploying an AI-driven documentation review system for strict medical device audits",
                "Mitigated regulatory compliance risks by achieving a 92% accuracy rate in automatically identifying non-compliances in complex Computer System Validation (GAMP 5) documents",
                "Accelerated the FDA approval process by automating the drafting and cross-referencing of dense medical device quality engineering documentation",
                "Saved over $150,000 in cloud compute costs by pioneering the early adoption of Parameter-Efficient Fine-Tuning (PEFT) instead of full-model retraining.",
                "Streamlined global regulatory audits by unifying siloed documentation across FDA 21 CFR Part 820, ISO 13485, and ISO 14971 standards into a single, searchable AI engine.",


            ]
        }
    ]

    context = {
        'profile': profile,
        'experience': experience,
        'skills': skills,
        'streamlit_url': STREAMLIT_URL, # Passes the link to the template
    }
    return render(request, 'index.html', context)