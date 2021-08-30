from deep_translator import GoogleTranslator
from pygooglenews import GoogleNews

tr = GoogleTranslator(source='auto', target='en')


class Protests:
    def s(self, search):
        """basic search"""
        stories = []
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

    def tr_s(self, search):
        """Translates searches from source language to english"""
        stories = []
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

    def en_protests(self):
        gn = GoogleNews(lang='en', country='GB')
        self.s(search=gn.search('protest OR demonstration OR riot OR rally OR strike OR walkout',
                                when='12h'))

    def fr_protests(self):
        gn = GoogleNews(lang='fr', country='GB')
        self.tr_s(search=gn.search('manifestation OR la grève', when='12h'))

    def de_protests(self):
        gn = GoogleNews(lang='de', country='GB')
        self.tr_s(search=gn.search('die Protestaktion OR protestieren OR Demonstration',
                                   when='12h'))
    # 'die Protestaktion OR protestieren OR Demonstration OR die Kundgebung OR die Manifestation',

    def es_protests(self):
        gn = GoogleNews(lang='es', country='GB')
        self.tr_s(search=gn.search('protesta OR declaración de averías OR demostración OR la '
                                   'manifestación OR Huelga OR salir', when='12h'))

    def pt_protests(self):
        gn = GoogleNews(lang='pt', country='GB')
        self.tr_s(search=gn.search('demonstração OR o comício OR manifestação', when='12h'))

    def ru_protests(self):
        gn = GoogleNews(lang='ru', country='GB')
        self.tr_s(search=gn.search('протест OR проявление OR забастовка', when='12h'))

    def ar_protests(self):
        gn = GoogleNews(lang='ar', country='GB')
        self.tr_s(search=gn.search('ناكف OR مظاهرة', when='12h'))

# putting it all together:
    def call_protests(self):
        print("\nProtests reported in the past 12 hours:")
        self.en_protests()
        print("\nFrench protests reported in the past 12 hours:")
        self.fr_protests()
        print("\nGerman protests reported in the past 12 hours:")
        self.de_protests()
        print("\nSpanish protests reported in the past 12 hours:")
        self.es_protests()
        print("\nPortuguese protests reported in the past 12 hours:")
        self.pt_protests()
        print("\nRussian protests reported in the past 12 hours:")
        self.ru_protests()
        print("\nArabic protests reported in the past 12 hours:")
        self.ar_protests()

    def lang_protests(self):
        protests = {
            "Arabic": "ar_protests()",
            "English": "en_protests()",
            "French": "fr_protests()",
            "German": "de_protests()",
            "Portuguese": "pt_protests()",
            "Russian": "ru_protests()",
            "Spanish": "es_protests()",
        }
        print(protests)
