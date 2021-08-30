from pygooglenews import GoogleNews


class EnglishWorldNews:

    def s(self, search):
        """Basic search function for world news"""
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

    def uk(self):
        """UK headlines"""
        gn = GoogleNews(lang='en', country='GB')
        self.s(search=gn.geo_headlines('united kingdom'))

    def ireland(self):
        """Ireland's headlines"""
        gn = GoogleNews(lang='en', country='IE')
        self.s(search=gn.geo_headlines('ireland'))

    def india(self):
        """India's headlines"""
        gn = GoogleNews(lang='en', country='IN')
        self.s(search=gn.geo_headlines('india'))

    def pakistan(self):
        """Pakistan's headlines"""
        gn = GoogleNews(lang='en', country='PK')
        self.s(search=gn.geo_headlines('pakistan'))

    def usa(self):
        """'America's headlines"""
        gn = GoogleNews(lang='en', country='US')
        self.s(search=gn.geo_headlines('united states'))

    def canada(self):
        """Canada's headlines"""
        gn = GoogleNews(lang='en', country='CA')
        self.s(search=gn.geo_headlines('canada'))

    def australia(self):
        """Australia's headlines"""
        gn = GoogleNews(lang='en', country='AU')
        self.s(search=gn.geo_headlines('australia'))

    def new_zealand(self):
        """New Zealand's headlines"""
        gn = GoogleNews(lang='en', country='NZ')
        self.s(search=gn.geo_headlines('new zealand'))

    def israel(self):
        """Israel's headlines"""
        gn = GoogleNews(lang='en', country='IL')
        self.s(search=gn.geo_headlines('israel'))

    def botswana(self):
        """Botswana's headlines"""
        gn = GoogleNews(lang='en', country='BW')
        self.s(search=gn.geo_headlines('botswana'))

    def ethiopia(self):
        """Ethiopia's headlines"""
        gn = GoogleNews(lang='en', country='ET')
        self.s(search=gn.geo_headlines('ethiopia'))

    def ghana(self):
        """Ghana's headlines"""
        gn = GoogleNews(lang='en', country='GH')
        self.s(search=gn.geo_headlines('ghana'))

    def kenya(self):
        """Kenya's headlines"""
        gn = GoogleNews(lang='en', country='KE')
        self.s(search=gn.geo_headlines('kenya'))

    def namibia(self):
        """Namibia's headlines"""
        gn = GoogleNews(lang='en', country='NA')
        self.s(search=gn.geo_headlines('namibia'))

    def nigeria(self):
        """Nigeria's headlines"""
        gn = GoogleNews(lang='en', country='NG')
        self.s(search=gn.geo_headlines('nigeria'))

    def indonesia(self):
        """Indonesia's headlines"""
        gn = GoogleNews(lang='en', country='ID')
        self.s(search=gn.geo_headlines('indonesia'))

    def latvia(self):
        """Latvia's headlines"""
        gn = GoogleNews(lang='en', country='LV')
        self.s(search=gn.top_news())

    def malaysia(self):
        """Malaysia's headlines"""
        gn = GoogleNews(lang='en', country='MY')
        self.s(search=gn.geo_headlines('malaysia'))

    def philippines(self):
        """Philippines's headlines"""
        gn = GoogleNews(lang='en', country='PH')
        self.s(search=gn.geo_headlines('philippines'))

    def singapore(self):
        """Singapore's headlines"""
        gn = GoogleNews(lang='en', country='SG')
        self.s(search=gn.geo_headlines('singapore'))

    def south_africa(self):
        """South Africa's headlines"""
        gn = GoogleNews(lang='en', country='ZA')
        self.s(search=gn.top_news())

    def tanzania(self):
        """Tanzania's headlines"""
        gn = GoogleNews(lang='en', country='TZ')
        self.s(search=gn.geo_headlines('tanzania'))

    def uganda(self):
        """uganda's headlines"""
        gn = GoogleNews(lang='en', country='UG')
        self.s(search=gn.geo_headlines('uganda'))

    def zimbabwe(self):
        """Zimbabwe's headlines"""
        gn = GoogleNews(lang='en', country='ZW')
        self.s(search=gn.geo_headlines('zimbabwe'))

    def europe(self):
        print("UK geo-specific headlines:")
        self.uk()
        print("\n\nIreland geo-specific headlines:")
        self.ireland()
        print("\n\nLatvia top-news headlines:")
        self.latvia()

    def asia(self):
        print("India geo-specific headlines:")
        self.india()
        print("\n\nIndonesia geo-specific headlines:")
        self.indonesia()
        print("\n\nIsrael geo-specific headlines:")
        self.israel()
        print("\n\nMalaysia geo-specific headlines:")
        self.malaysia()
        print("\n\nPakistan geo-specific headlines:")
        self.pakistan()
        print("\n\nPhilippines geo-specific headlines:")
        self.philippines()
        print("\n\nSingapore geo-specific headlines:")
        self.singapore()

    def africa(self):
        print("Zimbabwe geo-specific headlines:")
        self.zimbabwe()
        print("\n\nUganda geo-specific headlines:")
        self.uganda()
        print("\n\nTanzania geo-specific headlines:")
        self.tanzania()
        print("\n\nSouth African geo-specific headlines:")
        self.south_africa()
        print("\n\nBotswana geo-specific headlines:")
        self.botswana()
        print("\n\nEthiopia geo-specific headlines:")
        self.ethiopia()
        print("\n\nGhana geo-specific headlines:")
        self.ghana()
        print("\n\nKenya geo-specific headlines:")
        self.kenya()
        print("\n\nNamibia geo-specific headlines:")
        self.namibia()
        print("\n\nNigeria geo-specific headlines:")
        self.nigeria()

    def americas(self):
        print("America top-news headlines:")
        self.usa()
        print("\n\nCanadian geo-specific headlines:")
        self.canada()

    def oceana(self):
        print("New Zealand geo-specific headlines:")
        self.new_zealand()
        print("\n\nAustralia geo-specific headlines:")
        self.australia()

    def en_list(self):
        en_lists = {
            "Europe:": ["ireland, latvia, uk"],
            "Asia:": ["india, indonesia, israel, malaysia, pakistan, philippines, singapore"],
            "Africa:": ["botswana, ethiopia, ghana, kenya, namibia, nigeria, south_africa, "
                        "tanzania, uganda, zimbabwe"],
            "America:": ["canada, usa"],
            "Oceana:": ["australia, new_zealand"]}
        print(en_lists)
