from django.urls import path
from . import views

urlpatterns = [
	path('videos/', views.VideoInformationView.as_view())
]
