from django.urls import path
from .views import FootballListView, FootballDetailsView


urlpatterns = [
    path('',FootballListView.as_view(),name='football'),
    path('<int:pk>', FootballDetailsView.as_view(), name='football_details_api'),
    ]

