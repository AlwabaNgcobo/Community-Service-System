from django.db import models

class Issue(models.Model):
    STATUS_CHOICES = [
        ("open", "Open"),
        ("in_progress", "In Progress"),
        ("resolved", "Resolved"),
    ]
    TYPE_CHOICES = [
        ("water", "Water"),
        ("electricity", "Electricity"),
        ("road", "Road"),
        ("waste", "Waste"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    issue_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="water")
    location = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="issue_images/", blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.status}] {self.title}"