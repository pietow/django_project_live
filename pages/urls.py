from django.urls import path
from .views import HomePageView, AboutPageView, homePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("home2/", homePageView, name="home2"),
]