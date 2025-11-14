from django.urls import path
from .views import home, JobList, JobDetail

app_name = "jobs"

urlpatterns = [
    path("", home, name="home"),
    path("jobs/", JobList.as_view(), name="job_list"),
    path("jobs/<int:pk>/", JobDetail.as_view(), name="job_detail"),
]
