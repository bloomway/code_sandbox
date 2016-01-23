import os
import json
import requests
from urllib import urlencode
import util

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search?%s"
YOUTUBE_VIDEOS_URL = "https://www.googleapis.com/youtube/v3/videos?%s"


class Statistic:
    def __init__(self, view_count, like_count, dislike_count, favorite_count, comment_count):
        self.view_count = view_count
        self.like_count = like_count
        self.dislike_count = dislike_count
        self.favorite_count = favorite_count
        self.comment_count = comment_count

    def rate(self, satisfaction):
        """
        Computes the rate satisfaction
        :param satisfaction:
        :return:
        """
        if satisfaction:
            return float(self.like_count)/float(self.view_count)
        else:
            return float(self.dislike_count)/float(self.view_count)


class Video:
    def __init__(self, title, description, url, publication_date, statistic):
        self.title = title
        self.description = description
        self.url = url
        self.publication_date = publication_date
        self.statistic = statistic

    def display(self):
        print 'title: {0}\nurl: {1}\npublication date: {2}\n description:\n {3}'.format(self.title.encode('utf-8'),
                                                                                        self.url,
                                                                                        self.publication_date,
                                                                                        self.description.encode('utf-8'))
        print ''
        print 'Statistics'
        print 'views: {0}\nlike: {1}\ndislike: {2}\nfavorite: {3}\ncomments: {4}\n'.format(self.statistic.view_count,
                                                                                           self.statistic.like_count,
                                                                                           self.statistic.dislike_count,
                                                                                           self.statistic.favorite_count,
                                                                                           self.statistic.comment_count)
        print '------------------------------------------------'


def call_yt_search_api(key, q, part="snippet", max_results=5):
    query_string = urlencode({'part': part,
                              "q": q,
                              "key": key,
                              "maxResults": max_results})

    url = YOUTUBE_SEARCH_URL % query_string

    videos_id = []

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
                videos_id.append(item['id']['videoId'])

        return ','.join(videos_id)

    except requests.exceptions.HTTPError as e:
        print 'A HTTP error occured:\n Error Message:\n%s' % e
        exit(1)


def call_yt_videos_api(key, video_id, part="snippet", max_results=5):
    query_string = urlencode({'part': part,
                              "id": video_id,
                              "key": key,
                              "maxResults": max_results})

    url = YOUTUBE_VIDEOS_URL % query_string
    videos = []

    try:
        res = json.loads((requests.get(url)).text)
        items = res['items']
        for item in items:

            # extract basics information

            title = item['snippet']['title']
            url = 'https://www.youtube.com/watch?v=' + item['id']
            publication_date = item['snippet']['publishedAt']
            description = item['snippet']['description']

            # extract statistics related to a video

            view_count = item['statistics']['viewCount']
            like_count = item['statistics']['likeCount']
            dislike_count = item['statistics']['dislikeCount']
            favorite_count = item['statistics']['favoriteCount']
            comment_count = item['statistics']['commentCount']

            statistic = Statistic(view_count=view_count, like_count=like_count, dislike_count=dislike_count,
                                  comment_count=comment_count, favorite_count=favorite_count)

            v = Video(title=title, url=url, description=description, publication_date=publication_date,
                      statistic=statistic)
            videos.append(v)

        return videos

    except requests.HTTPError as e:
        print e
        exit(1)


def main():
    api_request = raw_input("Enter the API you want to perform query to: ")
    if len(api_request) == 0:
        api_request = 'youtube'

    # get the api key
    api_key = util.get_api_key(api_request)

    yt_search = ''
    while len(yt_search) == 0:
        yt_search = raw_input("Enter your search : ")

    if api_request == 'youtube':
        videos_id = call_yt_search_api(key=api_key, q=yt_search)
        print 'videos id', videos_id

        part = util.get_str_from_lst('snippet', 'statistics')
        if len(videos_id) != 0:
            yt_videos = call_yt_videos_api(key=api_key, video_id=videos_id, part=part)

            for video in yt_videos:
                video.display()
                satisfied_rate = video.statistic.rate(True) * 100
                unsatisfied_rate = video.statistic.rate(False) * 100
                print "videos of %s has been seen %s times on YouTube" % (yt_search, int(video.statistic.view_count))
                print "with a satisfaction of {0}% and {1}% unsatisfaction".format(satisfied_rate, unsatisfied_rate)
                print ''


if __name__ == "__main__":
    main()
