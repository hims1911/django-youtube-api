from rest_framework.serializers import ModelSerializer
from .models import VideoInformation


class VideoInformationSerliazer(ModelSerializer):
	
	class Meta:
		model = VideoInformation
		fields = '__all__'