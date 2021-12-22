from pygooglenews import GoogleNews


class KWSearch:
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

    def incidents(self):
        gn = GoogleNews(lang='en', country='GB')
        self.s(search=gn.search('accident OR incident OR assassinated OR murdered OR dead OR '
                                'killed', when='10h'))

    def clashes(self):
        gn = GoogleNews(lang='en', country='GB')
        self.s(search=gn.search('clashes OR fight OR shot OR stabbed', when='10h'))

    def raids(self):
        gn = GoogleNews(lang='en', country='GB')
        self.s(search=gn.search('raided OR police OR bust', when='10h'))

    def hostages(self):
        gn = GoogleNews(lang='en', country='GB')
        self.s(search=gn.search('intitle:hostage OR intitle:hostages OR captive', when='10h'))

# putting it all together:

    def incidents_reports(self):
        print("Incident-related keywords found in the news over the last 10 hours:")
        self.incidents()
        print("\nRaid-related activities found in the news over the last 12 hours:")
        self.raids()
        print("\nHostage-related activities found in the news over the last 12 hours:")
        self.hostages()
        print("\nClash-related keywords in the news in the last 10 hours:")
        self.clashes()
