
from django.shortcuts import render

def home(request):
    # Your Resume Data (Hardcoded for simplicity)
    profile = {
        "name": "KADA SATYA SURENDRA",
        "title": "Lead AI Orchestration Engineer",
        "location": "USA",
        "email": "skada544@gmail.com",
        "phone": "+1 (734) 743-1032",
        "summary": "Senior AI/ML Engineer with 10+ years of experience. Expert in LangGraph, Multi-Agent Orchestration, and HIPAA-compliant AI."
    }

    experience = [
        {
            "role": "Lead AI Orchestration Engineer",
            "company": "Epic Systems",
            "date": "Jan 2024 – Present",
            "details": [
                "Architected a 5-node multi-agent ecosystem using LangGraph, handling 10,000+ queries.",
                "Designed 'Watcher Agents' to validate actions, achieving 100% HIPAA compliance.",
                "Reduced clinical hallucination rates by 40% using automated Ragas evaluation pipelines."
            ]
        },
        {
            "role": "Senior AI Engineer",
            "company": "Morgan Stanley",
            "date": "July 2022 – Jan 2024",
            "details": [
                "Saved $800k+ annually by replacing keyword search with semantic AI engines.",
                "Built an Autonomous Financial Agent using ReAct framework for complex audit inquiries.",
                "Scaled RAG pipeline to process millions of financial PDFs with 99% accuracy."
            ]
        },
        {
            "role": "Machine Learning Engineer",
            "company": "Cigna Healthcare",
            "date": "Sep 2020 – June 2022",
            "details": [
                "Fine-tuned BERT models for FDA 21 CFR Part 820 compliance.",
                "Slashed cloud costs by $150k using Parameter-Efficient Fine-Tuning (PEFT)."
            ]
        }
    ]

    skills = [
        "LangGraph & Multi-Agent Systems",
        "OpenAI (GPT-4) & LLMOps",
        "RAG & Vector DBs (Pinecone)",
        "HIPAA & FDA Compliance",
        "Python, Docker, & CI/CD"
    ]

    context = {
        'profile': profile,
        'experience': experience,
        'skills': skills
    }
    return render(request, 'index.html', context)