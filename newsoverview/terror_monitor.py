from pygooglenews import GoogleNews
gn = GoogleNews(lang='en', country='GB')


class TerrorNews:
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

    def terror(self):
        """finds stories mentioning terrorist-related keywords in the past 12 hours"""
        self.s(search=gn.search('terrorism OR terror attack OR terrorist OR terrorists OR '
                                'extremism OR extremists OR radicalisation OR militant group',
                                when='12h'))

    def terror_events(self):
        """finds stories mentioning terrorist-related activities in the past 12 hours"""
        self.s(search=gn.search('bomb OR grenade attack OR blast OR mass shooting OR explosion OR'
                                'civilians+killed OR suspicious+package', when='12h'))

    def terror_groups(self):
        """searches for news regarding some well-known terror groups in the past 12 hours"""
        self.s(search=gn.search('al qaeda OR al-qaeda OR jihadist OR jihadists OR taliban OR boko '
                                'haram OR isis OR isil OR lashkar e taiba', when='12h'))

    def terror_news(self):
        print("Terrorist-related keywords found in the news over the last 12 hours:")
        self.terror()
        print("\nTerror groups found in the news:")
        self.terror_groups()
        print("\nTerrorist-related activities found in the news over the last 12 hours:")
        self.terror_events()

    def terror_search(self):
        t_list = {
            "Terror keywords": "terror()",
            "Terror groups": "terror_groups()",
            "Terror activities": "terror_events()"
        }
        print(t_list)
