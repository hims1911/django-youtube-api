from django.db import models


class VideoInformation(models.Model):
	video_id = models.CharField(max_length=30)
	title = models.TextField(blank=True)
	description = models.TextField(blank=True)
	channel_id = models.CharField(max_length=30)
	published_at = models.DateTimeField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	thumbnail_url = models.URLField(blank=True)

	class Meta:
		ordering = ['-published_at']

	def __str__(self):
		return str(self.published_at) + " " + str(self.title)