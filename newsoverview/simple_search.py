from deep_translator import GoogleTranslator
from pygooglenews import GoogleNews

tr = GoogleTranslator(source='auto', target='en')


class SimpleSearch:
    def s(self, query):
        """basic search, use the input 'query=' to search"""
        stories = []
        gn = GoogleNews(lang='en', country='GB')
        search = gn.search(query, when='24h')
        news_item = search['entries']
        for item in news_item:
            story = {
                'Title: ': item.title,
                'Time:  ': item.updated,
                'Link:  ': item.link
            }
            stories.append(story)
        for i, story in enumerate(stories):
            print("ARTICLE: ", i)
            for key, value in story.items():
                print(key, value)

    def tr_s(self, gn, query):
        """Translates searches from source language to english. Initiate GoogleNews and use the
        'query=' to type your query"""
        stories = []
        search = gn.search(query, when='24h')
        news_item = search['entries']
        for item in news_item:
            story = {
                'Title: ': item.title,
                'Time:  ': item.updated,
                'Link:  ': item.link
            }
            stories.append(story)
        for i, story in enumerate(stories):
            print("ARTICLE: ", i)
            for key, value in story.items():
                x = story.get('Title: ')
                translation = tr.translate(x)
                print(key, value)
            print("Translation: ", translation)

    def en_search(self, query):
        self.s(query)

    def tr_search(self, gn, query):
        gn = gn
        self.tr_s(gn, query)
