from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("home/", views.Index.as_view(), name="index"),
    path("home/member/<pk>", views.MemberDetail.as_view(), name="member-detail"),
]