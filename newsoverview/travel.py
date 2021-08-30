from deep_translator import GoogleTranslator
from pygooglenews import GoogleNews

tr = GoogleTranslator(source='auto', target='en')


class TravelWarnings:

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

    def en_travel_restrictions(self):
        """News about travel restrictions and border closures announced in the last 12 hours"""
        gn = GoogleNews(lang='en', country='GB')
        self.s(search=gn.search('travel restrictions OR closed border OR travel advisory '
                                'OR travelers stranded OR travel rules OR borders open',
                                when='12h'))

    def en_aeroplanes(self):
        """aeroplanes and flight-related travel warnings in the last 12 hours"""
        gn = GoogleNews(lang='en', country='GB')
        self.s(search=gn.search('travel+ban OR travel restriction OR travel warning OR air'
                                ' traffic control OR fight cancellation OR airport closed',
                                when='12h'))

    def fr_aeroplanes(self):
        """aeroplanes and flight-related travel warnings in the last 12 hours"""
        gn = GoogleNews(lang='fr', country='GB')
        self.tr_s(search=gn.search('restrictions de voyage OR interdiction de voyager OR '
                                   'interdiction de vol', when='12h'))

    def fr_aeroplanes_i(self):
        """aeroplanes and flight-related travel warnings in the last 12 hours"""
        gn = GoogleNews(lang='fr', country='GB')
        self.tr_s(search=gn.search('retard de vol OR contrôle du trafic aérien OR aéroport '
                                   'fermé', when='12h'))

    def fr_travel_restrictions(self):
        """aeroplanes and flight-related travel warnings in the last 12 hours"""
        gn = GoogleNews(lang='fr', country='GB')
        self.tr_s(search=gn.search('frontière fermée OR recommandations aux voyageurs OR '
                                   'frontière ouverte', when='12h'))

    def de_aeroplanes(self):
        """aeroplanes and flight-related travel warnings in the last 12 hours"""
        gn = GoogleNews(lang='de', country='GB')
        self.tr_s(search=gn.search('Reiseverbot OR Reisebeschränkungen OR Reisewarnung OR '
                  'Luftraumüberwachung OR Flug storniert OR Flughafen geschlossen', when='12h'))

    def de_travel_restrictions(self):
        """aeroplanes and flight-related travel warnings in the last 12 hours"""
        gn = GoogleNews(lang='de', country='GB')
        self.tr_s(search=gn.search('geschlossene Grenze OR Reisetipps OR Reiseregeln OR Grenzen '
                                   'offen', when='12h'))

    def pt_aeroplanes(self):
        """aeroplanes and flight-related travel warnings in the last 12 hours"""
        gn = GoogleNews(lang='pt', country='GB')
        self.tr_s(search=gn.search('proibição de viajar OR aviso de viagem', when='12h'))
        # OR restrição de viagens

    def pt_aeroplanes_i(self):
        """aeroplanes and flight-related travel warnings in the last 12 hours"""
        gn = GoogleNews(lang='pt', country='GB')
        self.tr_s(search=gn.search('atraso de vôo OR aeroporto fechado', when='12h'))
        # atraso de vôo OR aeroporto fechado OR controle de tráfego aéreo

    def pt_travel_restrictions(self):
        """aeroplanes and flight-related travel warnings in the last 12 hours"""
        gn = GoogleNews(lang='pt', country='GB')
        self.tr_s(search=gn.search('restrições a viajar OR conselhos de viagem', when='12h'))
        # restrições a viajar OR fronteira fechada OR conselhos de viagem '
        #                        'OR egras de viagem

    def pt_travel_restrictions_i(self):
        """aeroplanes and flight-related travel warnings in the last 12 hours"""
        gn = GoogleNews(lang='pt', country='GB')
        self.tr_s(search=gn.search('fronteira fechada OR egras de viagem', when='12h'))

    def es_aeroplanes(self):
        """aeroplanes and flight-related travel warnings in the last 12 hours"""
        gn = GoogleNews(lang='es', country='GB')
        self.tr_s(search=gn.search('prohibicion+de+viajar OR aeropuerto cerrado OR control de '
                                   'tráfico aéreo OR cancelación del vuelo', when='12h'))
    # prohibicion+de+viajar OR prohibición de vuelo OR restricción de viaje OR '
    #                        'advertencia de viaje OR vuelo demorado OR aeropuerto cerrado OR '
    #                        'interrupción de vuelo OR control de tráfico aéreo OR cancelación
    #                        del vuelo', when='12h')

    def es_travel_restrictions(self):
        """News about travel restrictions and border closures announced in the last 12 hours"""
        gn = GoogleNews(lang='es', country='GB')
        self.tr_s(search=gn.search('restricciones de viaje OR frontera cerrada OR asesoramiento '
                                   'de viaje OR reglas de viaje OR fronteras abiertas', when='12h'))

    def ru_aeroplanes(self):
        """aeroplanes and flight-related travel warnings in the last 12 hours"""
        gn = GoogleNews(lang='ru', country='GB')
        self.tr_s(search=gn.search('запрет на путешествия OR ограничения на путешествия',
                                   when='12h'))

    def ru_aeroplanes_i(self):
        """aeroplanes and flight-related travel warnings in the last 12 hours"""
        gn = GoogleNews(lang='ru', country='GB')
        self.tr_s(search=gn.search('рейс отменен OR аэропорт закрыт', when='12h'))
        # запрет на путешествия OR ограничения на путешествия OR предупреждение о путешествии OR'
        #                        ' управление воздушным движением OR рейс отменен OR аэропорт закрыт

    def ru_travel_restrictions(self):
        """aeroplanes and flight-related travel warnings in the last 12 hours"""
        gn = GoogleNews(lang='ru', country='GB')
        self.tr_s(search=gn.search('рекомендации по путешествиям OR правила путешествия OR'
                                   'границы открыты', when='12h'))

    def ar_aeroplanes(self):
        """aeroplanes and flight-related travel warnings in the last 12 hours"""
        gn = GoogleNews(lang='ar', country='GB')
        self.tr_s(search=gn.search(' حظر الطيران', when='12h'))
    #     self.tr_s(search=gn.search('حظر السفر '
    #                                    'OR القيود المفروضة على السفر OR إلغاء الرحلة OR '
    #                                    'مراقبة الملاحة الجوية', when='12h'))

    def ar_travel_restrictions(self):
        """aeroplanes and flight-related travel warnings in the last 12 hours"""
        gn = GoogleNews(lang='ar', country='GB')
        self.tr_s(search=gn.search('قواعد السفر OR الحدود مغلقة OR فتح الحدود', when='12h'))

# calling individual countries:
    def call_en(self):
        print("Aeroplane and flight-related travel news occurring in the past 12 hours:")
        self.en_aeroplanes()
        print("\nTravel restriction-related news occurring in the past 12 hours:")
        self.en_travel_restrictions()

    def call_fr(self):
        print("French aeroplane and flight-related travel news occurring in the past 12 hours:")
        self.fr_aeroplanes(), self.fr_aeroplanes_i()
        print("\nFrench travel restriction-related news occurring in the past 12 hours:")
        self.fr_travel_restrictions()

    def call_de(self):
        print("German aeroplane and flight-related travel news occurring in the past 12 hours:")
        self.de_aeroplanes()
        print("\nGerman travel restriction-related news occurring in the past 12 hours:")
        self.de_travel_restrictions()

    def call_es(self):
        print("Spanish aeroplane and flight-related travel news occurring in the past 12 hours:")
        self.es_aeroplanes()
        print("\nSpanish travel restriction-related news occurring in the past 12 hours:")
        self.es_travel_restrictions()

    def call_pt(self):
        print("Portuguese aeroplane and flight-related travel news occurring in the past 12 hours:")
        self.pt_aeroplanes(), self.pt_aeroplanes_i()
        print("\nPortuguese travel restriction-related news occurring in the past 12 hours:")
        self.pt_travel_restrictions(), self.pt_travel_restrictions_i()

    def call_ru(self):
        print("Russian aeroplane and flight-related travel news occurring in the past 12 hours:")
        self.ru_aeroplanes(), self.ru_aeroplanes_i()
        print("\nRussian travel restriction-related news occurring in the past 12 hours:")
        self.ru_travel_restrictions()

    def call_ar(self):
        print("Arabic aeroplane and flight-related travel news occurring in the past 12 hours:")
        self.ar_aeroplanes()
        print("\nArabic travel restriction-related news occurring in the past 12 hours:")
        self.ar_travel_restrictions()

    def aeroplane_disruptions(self):
        """Aeroplane and flight-related news for all languages in the past 12 hours!"""
        print("\nAeroplane and flight-related travel news occurring in the past 12 hours:")
        self.en_aeroplanes()
        print("\nFrench aeroplane and flight-related travel news occurring in the past 12 hours:")
        self.fr_aeroplanes(), self.fr_aeroplanes_i()
        print("\nGerman aeroplane and flight-related travel news occurring in the past 12 hours:")
        self.de_aeroplanes()
        print("\nSpanish aeroplane and flight-related travel news occurring in the past 12 hours:")
        self.es_aeroplanes()
        print("\nPortuguese aeroplane and flight-related travel news occurring in the past 12 "
              "hours:")
        self.pt_aeroplanes(), self.pt_aeroplanes_i()
        print("\nRussian aeroplane and flight-related travel news occurring in the past 12 hours:")
        self.ru_aeroplanes(), self.ru_aeroplanes_i()
        print("\nArabic aeroplane and flight-related travel news occurring in the past 12 hours:")
        self.ar_aeroplanes()

    def travel_restrictions(self):
        print("\nTravel restriction-related news occurring in the past 12 hours:")
        self.en_travel_restrictions()
        print("\nFrench travel restriction-related news occurring in the past 12 hours:")
        self.fr_travel_restrictions()
        print("\nGerman travel restriction-related news occurring in the past 12 hours:")
        self.de_travel_restrictions()
        print("\nSpanish travel restriction-related news occurring in the past 12 hours:")
        self.es_travel_restrictions()
        print("\nPortuguese travel restriction-related news occurring in the past 12 hours:")
        self.pt_travel_restrictions(), self.pt_travel_restrictions_i()
        print("\nRussian travel restriction-related news occurring in the past 12 hours:")
        self.ru_travel_restrictions()
        print("\nArabic travel restriction-related news occurring in the past 12 hours:")
        self.ar_travel_restrictions()

    def lang_aeroplanes(self):
        aeroplanes = {
            "Arabic": "ar_aeroplanes()",
            "English": "en_aeroplanes()",
            "French": "fr_aeroplanes()",
            "German": "de_aeroplanes()",
            "Portuguese": "pt_aeroplanes()",
            "Russian": "ru_aeroplanes()",
            "Spanish": "es_aeroplanes()",
        }
        print(aeroplanes)

    def lang_travel_restrictions(self):
        travel_restrictions = {
            "Arabic": "ar_travel_restrictions()",
            "English": "en_travel_restrictions()",
            "French": "fr_travel_restrictions()",
            "German": "de_travel_restrictions()",
            "Portuguese": "pt_travel_restrictions()",
            "Russian": "ru_travel_restrictions()",
            "Spanish": "es_travel_restrictions()",
        }
        print(travel_restrictions)
