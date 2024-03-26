# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render

# Create your views here.
# views.py

from django.http import HttpResponse
from django.views import View
from .utils import fetch_latest_videos
from .models import Video
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Q


#FetchLatestVideosView - view to fetch videos from youtube
class FetchLatestVideosView(View):
    def get(self, request):
        # Define your API keys
        api_keys = [
            # Add more google api keys as needed
        ]
        query = 'india'

        # Try each API key until one succeeds or all fail
        for i in range(len(api_keys)):
            api_key = api_keys[i]
            try:
                fetch_latest_videos(api_key, query)
                # If successful, move the key to the end of the list
                api_keys.append(api_keys.pop(i))
                return HttpResponse(
                    content=json.dumps({'status': 'success'}),
                    content_type='application/json'
                )
            except Exception as e:
                # If the API key is exhausted, move it to the end of the list and try the next one
                if 'quotaExceeded' in str(e):
                    api_keys.append(api_keys.pop(i))
                    continue
                else:
                    # If another error occurs, return an error response
                    return HttpResponse(
                        content=json.dumps({'status': 'error', 'message': str(e)}),
                        status=500,
                        content_type='application/json'
                    )

        # If all keys are exhausted, return an error response
        return HttpResponse(
            content=json.dumps({'status': 'error', 'message': 'All API keys are exhausted.'}),
            status=500,
            content_type='application/json'
        )

#VideoList - view to fetch all stored information from the database
class VideoList(View):
    def get(self, request):
        videos = Video.objects.all().order_by('-publishedDateTime')
        page_number = request.GET.get('page', 1)
        per_page = request.GET.get('per_page', 10)
        paginator = Paginator(videos, per_page)
        
        page_obj = paginator.page(page_number)
        
        data = [{"title": v.title, "description": v.description, "published_dateTime": v.publishedDateTime, "thumbnail_url": v.thumbnailsUrls, "channel_id": v.channel_id, "channel_title": v.channel_title, "video_id":v.video_id} for v in page_obj.object_list]
        payload = {
            "page": {
                "current": page_obj.number,
                "has_next": page_obj.has_next(),
                "has_previous": page_obj.has_previous(),
            },
            "data": data
        }
        return JsonResponse(payload)

#VideoSearch - view to search videos from the stored postgres database
class VideoSearch(View):
    def get(self, request):
        query = request.GET.get('q', '')
        # use icontains instead of contains to match substrings
        videos = Video.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        ).distinct()
        page_number = request.GET.get('page', 1)
        per_page = request.GET.get('per_page', 10)
        paginator = Paginator(videos, per_page)
        page_obj = paginator.page(page_number)
        data = [{"title": v.title, "description": v.description, "published_datetime": v.publishedDateTime, "thumbnail_url": v.thumbnailsUrls, "channel_id": v.channel_id, "channel_title": v.channel_title, "video_id":v.video_id} for v in page_obj.object_list]
        payload = {
            "page": {
                "current": page_obj.number,
                "has_next": page_obj.has_next(),
                "has_previous": page_obj.has_previous(),
            },
            "data": data
        }
        return JsonResponse(payload)
