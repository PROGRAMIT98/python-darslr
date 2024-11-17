from django.urls import path
from .views import HomePageView, AboutPageView, About2PageView, DonPageView

urlpatterns = [
    path('Don/',DonPageView.as_view(),name='Don'),
    path('about2/',About2PageView.as_view(),name='about2'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('',HomePageView.as_view(),name='home'),
]