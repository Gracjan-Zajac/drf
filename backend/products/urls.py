import imp
from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductCeateAPIView.as_view()),
    path("<int:pk>/", views.ProductDetailAPIView.as_view()),
]
