from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Issue
from .forms import IssueForm


@login_required(login_url="/users/login/")
def report_issue(request):
    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("reports:track_issue")
    else:
        form = IssueForm()

    return render(request, "reports/report_issue.html", {"form": form})


@login_required(login_url="/users/login/")
def track_issue(request):
    issues = Issue.objects.order_by("-created_at")
    return render(request, "reports/track_issue.html", {"issues": issues})


def track_issue(request):
    issues = Issue.objects.order_by("-created_at")
    return render(request, "reports/track_issue.html", {"issues": issues})