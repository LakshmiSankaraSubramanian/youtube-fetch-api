# utils.py

import requests
from datetime import datetime, timedelta
from .models import Video

def fetch_latest_videos(api_key, query):
    # Check if there are any existing records
    existing_videos = Video.objects.order_by('-publishedDateTime')
    if existing_videos.exists():
        # Fetch only records published after the latest record's publishedDateTime
        published_after = existing_videos.first().publishedDateTime.isoformat('T') + 'Z'
    else:
        # Fetch everything if there are no existing records
        published_after = (datetime.now() - timedelta(days=7)).isoformat('T') + 'Z'

    
    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&order=date&q={}&type=video&publishedAfter={}&key={}&maxResults=50".format(query, published_after, api_key)
    try:
        response = requests.get(url)
        response.raise_for_status()  # raise exception for HTTP errors
        data = response.json()

        # Extract video details and store them in the database
        for item in data.get('items', []):
            video_data = item['snippet']
            Video.objects.update_or_create(
                title=video_data['title'],
                description=video_data['description'],
                publishedDateTime=video_data['publishedAt'],
                thumbnailsUrls=video_data['thumbnails']['default']['url'],
                channel_id = video_data['channelId'],
                channel_title = item['snippet']['channelTitle'],
                video_id = item['id']['videoId']
            )
        return True
    
    except (requests.exceptions.RequestException, ValueError) as e:
        # Log or handle the exception
        print("Request error occurred: {}".format(e))
        return False

