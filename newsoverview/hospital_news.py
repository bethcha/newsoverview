from deep_translator import GoogleTranslator
from pygooglenews import GoogleNews

tr = GoogleTranslator(source='auto', target='en')


class HospitalNews:
    def s(self, search):
        """Basic search for english-speaking countries."""
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
        """Basic search for non-english speaking countries.
        Translated title is underneath the link."""
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

    def en_hospitals(self):
        gn = GoogleNews(lang='en', country='GB')
        self.s(search=gn.search('intitle:hospital fire OR intitle:hospital accident OR '
                                'intitle:hospital explosion OR hospital closed',
                                when='12h'))

    def fr_hospitals(self):
        gn = GoogleNews(lang='fr', country='GB')
        self.tr_s(search=gn.search('hôpital incendie OR hôpital accident OR explosion hôpital '
                                   'OR hôpital fermé', when='12h'))

    def de_hospitals(self):
        gn = GoogleNews(lang='de', country='GB')
        self.tr_s(search=gn.search('Krankenhausbrand Feuer OR Krankenhausbrand OR Krankenhausunfall'
                                   ' OR Krankenhausexplosion OR Krankenhaus geschlossen',
                                   when='12h'))

    def es_hospitals(self):
        gn = GoogleNews(lang='es', country='GB')
        self.tr_s(search=gn.search('incendio del hospital OR accidente de hospital OR explosión '
                                   'del hospital OR hospital cerrado', when='12h'))

    def pt_hospitals(self):
        gn = GoogleNews(lang='pt', country='GB')
        self.tr_s(search=gn.search('incêndio hospitalar OR acidente de hospital OR explosão de'
                                   ' hospital OR hospital fechado', when='12h'))

    def ru_hospitals(self):
        gn = GoogleNews(lang='ru', country='GB')
        self.tr_s(search=gn.search('больничный пожар OR несчастный случай в больнице OR взрыв в '
                                   'больнице OR больница закрыта', when='12h'))

    def ar_hospitals(self):
        gn = GoogleNews(lang='ar', country='GB')
        self.tr_s(search=gn.search('OR حادث المستشفى OR حريق المستشفى  انفجار OR المستشفى '
                                   'OR المستشفى مغلق', when='12h'))

# putting it all together:
    def call_hospitals(self):
        print("\nHospital-related incidences reported in the past 12 hours:")
        self.en_hospitals()
        print("\nFrench Hospital-related incidences reported in the past 12 hours:")
        self.fr_hospitals()
        print("\nGerman Hospital-related incidences reported in the past 12 hours:")
        self.de_hospitals()
        print("\nSpanish Hospital-related incidences reported in the past 12 hours:")
        self.es_hospitals()
        print("\nPortuguese Hospital-related incidences reported in the past 12 hours:")
        self.pt_hospitals()
        print("\nRussian Hospital-related incidences reported in the past 12 hours:")
        self.ru_hospitals()
        print("\nArabic Hospital-related incidences reported in the past 12 hours:")
        self.ar_hospitals()

    def lang_hospitals(self):
        hospitals = {
            "Arabic": "ar_hospitals()",
            "English": "en_hospitals()",
            "French": "fr_hospitals()",
            "German": "de_hospitals()",
            "Portuguese": "pt_hospitals()",
            "Russian": "ru_hospitals()",
            "Spanish": "es_hospitals()",
        }
        print(hospitals)
