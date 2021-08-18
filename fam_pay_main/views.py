from django.shortcuts import render
from django.http import HttpResponse
from .models import VideoInformation
from .serializers import VideoInformationSerliazer
from rest_framework import generics
from rest_framework.views import exception_handler


class VideoInformationView(generics.ListAPIView):
	queryset = VideoInformation.objects.all()
	serializer_class = VideoInformationSerliazer

	def get_queryset(self):
		queryset = self.queryset.all()
		description = self.request.query_params.get('description', None)
		title = self.request.query_params.get('title', None)

		if title:
			title = title.lower()
			queryset = queryset.filter(title__icontains=title)

		if description:
			description = description.lower()
			queryset = queryset.filter(description__icontains=title)

		return queryset
