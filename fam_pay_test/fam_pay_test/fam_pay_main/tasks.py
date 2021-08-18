import requests
import json
import datetime
from fam_pay_main.models import VideoInformation

from fam_pay_test.celery import app


@app.task()
def fetch_youtube_data():
	current_start_date = VideoInformation.objects.all().first() 

	if current_start_date:
		current_start_date = current_start_date.published_at
	else:
		current_start_date = datetime.datetime.now() - datetime.timedelta(days=10)

	end_date = datetime.datetime.now()

	query = "football"

	kwargs = {'part': 'snippet', 'maxResults': 50, 'q': query, 'order': 'date',
	          'publishedAfter': current_start_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
	          'publishedBefore': end_date.strftime("%Y-%m-%dT%H:%M:%SZ"), 
	          'type': 'video'}

	url = "https://www.googleapis.com/youtube/v3/search?key=AIzaSyC4vXJM59XLuxk_xh-J7s5S-mn2PrHFSPU"

	payload={}
	headers = {}

	response = requests.request("GET", url, headers=headers, params=kwargs)
	results = json.loads(response.text)
	print("done 1")
	count = 1
	while 1:
		count = count + 1
		data = results['items']
		for item in data:
			video_data = {}
			video_data['video_id'] = item['id']['videoId']
			video_data['channel_id'] = item['snippet']['channelId']
			video_data['title'] = item['snippet']['title']
			video_data['description'] = item['snippet']['description']
			video_data['published_at'] = item['snippet']['publishedAt']
			video_data['thumbnail_url'] = item['snippet']['thumbnails']['default']['url']
			VideoInformation.objects.create(**video_data)

		print(results.get('nextPageToken'))

		if results.get('nextPageToken') is None:
			break

		kwargs['pageToken'] = results['nextPageToken']
		response = requests.request("GET", url, headers=headers, params=kwargs)
		results = json.loads(response.text)
		print(count)


