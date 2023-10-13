from django.urls import path
from .views import HomePageView, AboutPageView, homePageView, practice_view
from .views import DashboardView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("home2/", homePageView, name="home2"),
    path("practice", practice_view, name="practice"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]
