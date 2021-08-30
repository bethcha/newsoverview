from deep_translator import GoogleTranslator
from pygooglenews import GoogleNews

tr = GoogleTranslator(source='auto', target='en')


class CoronavirusNews:
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

    def en_covid(self):
        """For english covid and lockdown news found in the past one hour"""
        gn = GoogleNews(lang='en', country='GB')
        print("English covid-related news occurring in the past 1 hour:")
        self.s(search=gn.search('intitle:coronavirus OR covid', when='1h'))
        print("\nEnglish lockdown-related news occurring in the past 1 hour:")
        self.s(search=gn.search('intitle:lockdown OR restrictions', when='1h'))

    def fr_covid(self):
        """For french covid and lockdown news found in the past one hour"""
        gn = GoogleNews(lang='fr', country='GB')
        print("\nFrench-based coronavirus news in the past 1 hour")
        self.tr_s(search=gn.search('intitle:coronavirus', when='1h'))
        print("\nFrench-based lockdown news in the past 1 hour")
        self.tr_s(search=gn.search('intitle:confinement OR restrictions', when='1h'))

    def pt_covid(self):
        """For portuguese covid and lockdown news found in the past one hour"""
        gn = GoogleNews(lang='pt', country='GB')
        print("\nPortuguese-based covid news in the past 1 hour")
        self.tr_s(search=gn.search('intitle:coronavírus', when='1h'))
        print("\nPortuguese-based lockdown news in the past 1 hour")
        self.tr_s(search=gn.search('intitle:confinamento OR restrições', when='1h'))

    def es_covid(self):
        """For spanish covid and lockdown news found in the past one hour"""
        gn = GoogleNews(lang='es', country='GB')
        print("\nSpanish-based covid news in the past 1 hour")
        self.tr_s(search=gn.search('intitle:coronavirus', when='1h'))
        print("\nSpanish-based lockdown news in the past 1 hour")
        self.tr_s(search=gn.search('intitle:cierre de emergencia OR restricciones', when='1h'))

    def de_covid(self):
        """For german covid and lockdown news found in the past one hour"""
        gn = GoogleNews(lang='de', country='GB')
        print("\nGerman-based covid news in the past 1 hour")
        self.tr_s(search=gn.search('intitle:coronavirus', when='1h'))
        print("\nGerman-based lockdown news in the past 1 hour")
        self.tr_s(search=gn.search('intitle:Abriegelung OR Einschränkungen', when='1h'))

    def ru_covid(self):
        """For russian covid and lockdown news found in the past one hour"""
        gn = GoogleNews(lang='ru', country='GB')
        print("\nRussian-based covid news in the past 1 hour")
        self.tr_s(search=gn.search('intitle:коронавирус', when='1h'))
        print("\nRussian-based lockdown news in the past 1 hour")
        self.tr_s(search=gn.search('карантин OR ограничения', when='1h'))

    def ar_covid(self):
        """For arabic covid and lockdown news found in the past one hour"""
        gn = GoogleNews(lang='ar', country='GB')
        print("\nArabic-based covid news in the past 1 hour")
        self.tr_s(search=gn.search('مرض فيروس كورونا OR فيروس كورونا', when='1h'))
        print("\nArabic-based lockdown news in the past 1 hour")
        self.tr_s(search=gn.search('إغلاق OR قيود', when='1h'))

    def coronavirus(self):
        """For all covid and lockdown news found in the past one hour"""
        gn = GoogleNews(lang='en', country='GB')
        print("\nEnglish covid-related news occuring in the past 1 hour:")
        self.s(search=gn.search('intitle:coronavirus OR covid', when='1h'))
        gn = GoogleNews(lang='fr', country='GB')
        print("\nFrench-based coronavirus news in the past 1 hour:")
        self.tr_s(search=gn.search('intitle:coronavirus', when='1h'))
        gn = GoogleNews(lang='es', country='GB')
        print("\nSpanish-based covid news in the past 1 hour:")
        self.tr_s(search=gn.search('intitle:coronavirus', when='1h'))
        gn = GoogleNews(lang='pt', country='GB')
        print("\nPortuguese-based covid news in the past 1 hour:")
        self.tr_s(search=gn.search('intitle:coronavírus', when='1h'))
        gn = GoogleNews(lang='de', country='GB')
        print("\nGerman-based covid news in the past 1 hour:")
        self.tr_s(search=gn.search('intitle:coronavirus', when='1h'))
        gn = GoogleNews(lang='ru', country='GB')
        print("\nRussian-based covid news in the past 1 hour:")
        self.tr_s(search=gn.search('intitle:коронавирус', when='1h'))
        gn = GoogleNews(lang='ar', country='GB')
        print("\nArabic-based covid news in the past 1 hour")
        self.tr_s(search=gn.search('intitle:مرض فيروس كورونا OR فيروس كورونا', when='1h'))

    def lockdown(self):
        """For all covid and lockdown news found in the past one hour"""
        gn = GoogleNews(lang='en', country='GB')
        print("\nEnglish lockdown-related news occuring in the past 1 hour:")
        self.s(search=gn.search('intitle:lockdown OR restrictions', when='1h'))
        gn = GoogleNews(lang='fr', country='GB')
        print("\nFrench-based lockdown news in the past 1 hour:")
        self.tr_s(search=gn.search('intitle:confinement OR restrictions', when='1h'))
        gn = GoogleNews(lang='es', country='GB')
        print("\nSpanish-based lockdown news in the past 1 hour:")
        self.tr_s(search=gn.search('cierre de emergencia OR restricciones', when='1h'))
        gn = GoogleNews(lang='pt', country='GB')
        print("\nPortuguese-based lockdown news in the past 1 hour:")
        self.tr_s(search=gn.search('intitle:confinamento OR restrições', when='1h'))
        gn = GoogleNews(lang='de', country='GB')
        print("\nGerman-based lockdown news in the past 1 hour:")
        self.tr_s(search=gn.search('intitle:Abriegelung OR Einschränkungen', when='1h'))
        gn = GoogleNews(lang='ru', country='GB')
        print("\nRussian-based lockdown news in the past 1 hour:")
        self.tr_s(search=gn.search('карантин OR ограничения', when='1h'))
        gn = GoogleNews(lang='ar', country='GB')
        print("\nArabic-based lockdown news in the past 1 hour")
        self.tr_s(search=gn.search('إغلاق OR قيود', when='1h'))

    def covid_list(self):
        languages = {"Arabic": "ar_covid()",
                     "English": "en_covid()",
                     "French": "fr_covid()",
                     "German": "de_covid()",
                     "Portuguese": "pt_covid()",
                     "Russian": "ru_covid()",
                     "Spanish": "es_covid()"
                     }
        print(languages)
