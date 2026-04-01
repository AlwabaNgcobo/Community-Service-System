from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
    path("", views.report_issue, name="report_issue"),
    path("track", views.track_issue, name="track_issue"),
]
