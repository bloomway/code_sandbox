# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re, sys


class Crawler(object):

    def __init__(self):
        super(Crawler, self).__init__()

    def get_animes(self, seeds):

        animes = {}
        pattern = seeds[0] + 'anime/[\w+-?]+/$'
        res = requests.get(seeds.pop())
        if res.status_code != 200:
            print 'request failed'
            exit()
        else:
            print 'request succeed'
            soup = BeautifulSoup(res.text, 'html5lib')
            aside_tag = soup.find('aside', id='liste_anime_widget-2')
            for h3_tag in aside_tag.find_all('h3'):
                for link in h3_tag.next_sibling.find_all('a'):
                    href = link.get('href')
                    title = link['title']
                    if not re.search(pattern, href) is None:
                        animes[title] = href
        return animes

    def meta(self, url):
        """
        For each url, retreives all the metadata (under the 'article' tag) relates to it
        e.g of metadata:

            - resume
            - annee de production
            - genre
            - episodes
        :param url:
        :return:
        """


class Article:
    """
    This article represents an hinata online article
    """
    def __init__(self, title, genre, year_of_prod, resume, nb_of_episodes):
        self.title = title
        

def main():
    seeds = ['http://hinata-online-community.fr/']
    crawler = Crawler()
    links = crawler.get_animes(seeds=seeds)
    print "number", len(links)
    """for title, href in links.items():
        print '{0} - {1}'.format(title.encode('utf-8'), href) """

if __name__ == '__main__':
   main()

