from django.contrib import admin
from .models import Issue


def resolve_issue(modeladmin, request, queryset):
    queryset.update(status="resolved")
resolve_issue.short_description = "Mark selected issues as resolved"


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("title", "description")
    actions = [resolve_issue]
