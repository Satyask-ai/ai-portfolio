# Create your models here.
from django.db import models

class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=100) # e.g., "Jan 2024 - Present"
    description = models.TextField() # General summary
    bullets = models.TextField(help_text="Enter each bullet point on a new line")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order']

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    year = models.CharField(max_length=50)

class TechnicalSkill(models.Model):
    category = models.CharField(max_length=100) # e.g., "LLM Orchestration"
    tools = models.TextField() # e.g., "LangGraph, LangChain, Ragas"