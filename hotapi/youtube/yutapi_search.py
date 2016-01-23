import os
import json
import requests
from urllib import urlencode

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search?%s"


class Video:
    def __init__(self, title, description, url, publication_date):
        self.title = title
        self.description = description
        self.url = url
        self.publication_date = publication_date

    def display(self):
        print '{0}\n{1}\n{2}\n{3}'.format(self.title.encode('utf-8'), self.url,
                                          self.publication_date,
                                          self.description.encode('utf-8'))
        print '------------------------------------------------'


def get_api_key(name):
    filename = os.path.join(BASE_DIR, 'keys', 'apikeys.json')
    with open(filename, 'r') as fhandler:
        keys = json.loads(fhandler.read())
        return keys[name]['apikey']


def call_yt_api(key, q, part="snippet", max_results=5):
    query_string = urlencode({'part': part, "q": q, "key": key, "maxResults": max_results})
    url = YOUTUBE_SEARCH_URL % query_string

    videos = []

    try:
        res = requests.get(url)
        json_resp = json.loads(res.text)
        print 'Page Info'
        print 'total results', json_resp['pageInfo']['totalResults']
        print '----------------------------------------\n'

        # get items
        items = json_resp['items']
        for item in items:
            if item['id']['kind'] == 'youtube#video':
                videos.append({'videoId': item['id']['videoId'], 'snippet': item['snippet']})

        return videos

    except requests.exceptions.HTTPError as e:
        print 'A HTTP error occured:\n Error Message:\n%s' % e
        exit(1)


def main():
    api_request = ''
    while len(api_request) == 0:
        api_request = raw_input("Enter the API you want to perform query to: ")

    # get the api key
    api_key = get_api_key(api_request)

    yt_search = ''
    while len(yt_search) == 0:
        yt_search = raw_input("Enter your search : ")

    if api_request == 'youtube':
        yt_videos = call_yt_api(key=api_key, q=yt_search, max_results=10)
        for video in yt_videos:
            title = video['snippet']['title']
            url = 'https://www.youtube.com/watch?v=' + video['videoId']
            publication_date = video['snippet']['publishedAt']
            description = video['snippet']['description']

            (Video(title=title, url=url, publication_date=publication_date, description=description)).display()


if __name__ == "__main__":
    main()