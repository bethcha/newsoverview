from deep_translator import GoogleTranslator
from pygooglenews import GoogleNews

tr = GoogleTranslator(source='auto', target='en')


class TranslatedWorldNews:

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

    def france(self):
        """France's headlines"""
        gn = GoogleNews(lang='fr', country='FR')
        self.tr_s(search=gn.geo_headlines('France'))

    def canada_fr(self):
        """Canada's french headlines"""
        gn = GoogleNews(lang='fr', country='CA')
        self.tr_s(search=gn.geo_headlines('canada'))

    def belgium_fr(self):
        """Belgium's headlines"""
        gn = GoogleNews(lang='fr', country='BE')
        self.tr_s(search=gn.geo_headlines('belgique'))

    def morocco_fr(self):
        """Morocco's headlines"""
        gn = GoogleNews(lang='fr', country='MA')
        self.tr_s(search=gn.geo_headlines('maroc'))

    def switzerland_fr(self):
        """Switzerland's headlines"""
        gn = GoogleNews(lang='fr', country='CH')
        self.tr_s(search=gn.geo_headlines('suisse'))

    def senegal(self):
        """Senegal's headlines"""
        gn = GoogleNews(lang='fr', country='SN')
        self.tr_s(search=gn.geo_headlines('Sénégal'))

    def germany(self):
        """Germany's headlines"""
        gn = GoogleNews(lang='de', country='DE')
        self.tr_s(search=gn.geo_headlines('Deutschland'))

    def austria(self):
        """Austria's headlines"""
        gn = GoogleNews(lang='de', country='AT')
        self.tr_s(search=gn.geo_headlines('österreich'))

    def switzerland_de(self):
        """Switzerland's headlines"""
        gn = GoogleNews(lang='de', country='CH')
        self.tr_s(search=gn.geo_headlines('schweiz'))

    def spain(self):
        """Spain's headlines"""
        gn = GoogleNews(lang='es', country='GB')
        self.tr_s(search=gn.geo_headlines('España'))

    def argentina(self):
        """Argentina's headlines"""
        gn = GoogleNews(lang='es', country='AR')
        self.tr_s(search=gn.geo_headlines('argentina'))

    def chile(self):
        """Chile's headlines"""
        gn = GoogleNews(lang='es', country='CL')
        self.tr_s(search=gn.geo_headlines('chile'))

    def colombia(self):
        """Colombia's headlines"""
        gn = GoogleNews(lang='es', country='CO')
        self.tr_s(search=gn.geo_headlines('colombia'))

    def cuba(self):
        """Cuba's headlines"""
        gn = GoogleNews(lang='es', country='CU')
        self.tr_s(search=gn.geo_headlines('cuba'))

    def usa_es(self):
        """America's spanish headlines"""
        gn = GoogleNews(lang='es', country='US')
        self.tr_s(search=gn.geo_headlines('estados unidos'))

    def mexico(self):
        """Mexico's headlines"""
        gn = GoogleNews(lang='es', country='MX')
        self.tr_s(search=gn.geo_headlines('México'))

    def peru(self):
        """Peru's headlines"""
        gn = GoogleNews(lang='es', country='PE')
        self.tr_s(search=gn.geo_headlines('Perú'))

    def venezuela(self):
        """Venezuela's headlines"""
        gn = GoogleNews(lang='es', country='VE')
        self.tr_s(search=gn.geo_headlines('venezuela'))

    def indonesia(self):
        """Indonesia's headlines"""
        gn = GoogleNews(lang='id', country='ID')
        self.tr_s(search=gn.geo_headlines('indonesia'))

    def czechia(self):
        """Czechia's headlines"""
        gn = GoogleNews(lang='cs', country='CZ')
        self.tr_s(search=gn.geo_headlines('Česko'))

    def italy(self):
        """Italy's headlines"""
        gn = GoogleNews(lang='it', country='IT')
        self.tr_s(search=gn.geo_headlines('Italia'))

    def lithuania(self):
        """Lithuania's headlines"""
        gn = GoogleNews(lang='lt', country='LT')
        self.tr_s(search=gn.geo_headlines('Lietuva'))

    def hungary(self):
        """Hungary's headlines"""
        gn = GoogleNews(lang='hu', country='HU')
        self.tr_s(search=gn.geo_headlines('Magyarország'))

    def belgium_nl(self):
        """Belgium's headlines"""
        gn = GoogleNews(lang='nl', country='BE')
        self.tr_s(search=gn.geo_headlines('belgië'))

    def netherlands(self):
        """Netherlands' headlines"""
        gn = GoogleNews(lang='nl', country='NL')
        self.tr_s(search=gn.geo_headlines('nederland'))

    def norway(self):
        """Norway's headlines"""
        gn = GoogleNews(lang='no', country='NO')
        self.tr_s(search=gn.geo_headlines('norge'))

    def poland(self):
        """Poland's headlines"""
        gn = GoogleNews(lang='pl', country='PL')
        self.tr_s(search=gn.geo_headlines('polska'))

    def brazil_pt(self):
        """Brazil's headlines"""
        gn = GoogleNews(lang='pt', country='BR')
        self.tr_s(search=gn.geo_headlines('brasil'))

    def portugal(self):
        """Portugal's headlines"""
        gn = GoogleNews(lang='pt', country='PT')
        self.tr_s(search=gn.geo_headlines('portugal'))

    def romania(self):
        """Romania's headlines"""
        gn = GoogleNews(lang='ro', country='RO')
        self.tr_s(search=gn.geo_headlines('România'))

    def slovakia(self):
        """Slovakia's headlines"""
        gn = GoogleNews(lang='sk', country='SK')
        self.tr_s(search=gn.geo_headlines('slovensko'))

    def slovenia(self):
        """Slovenia's headlines"""
        gn = GoogleNews(lang='sl', country='SI')
        self.tr_s(search=gn.geo_headlines('slovenija'))

    def sweden(self):
        """Sweden's headlines"""
        gn = GoogleNews(lang='sv', country='SE')
        self.tr_s(search=gn.geo_headlines('sverige'))

    def vietnam(self):
        """Vietnam's headlines"""
        gn = GoogleNews(lang='vi', country='VN')
        self.tr_s(search=gn.geo_headlines('Việt Nam'))

    def turkey(self):
        """Turkey's headlines"""
        gn = GoogleNews(lang='tr', country='TR')
        self.tr_s(search=gn.geo_headlines('Türkiye'))

    def greece(self):
        """Greece's headlines"""
        gn = GoogleNews(lang='el', country='GR')
        self.tr_s(search=gn.geo_headlines('Ελλάδα'))

    def bulgaria(self):
        """Bulgaria's headlines"""
        gn = GoogleNews(lang='bg', country='BG')
        self.tr_s(search=gn.geo_headlines('България'))

    def russia(self):
        """Russia's headlines"""
        gn = GoogleNews(lang='ru', country='RU')
        self.tr_s(search=gn.geo_headlines('Россия'))

    def ukraine_ru(self):
        """Ukraine's russian headlines"""
        gn = GoogleNews(lang='ru', country='UA')
        self.tr_s(search=gn.geo_headlines('Украина'))

    def serbia(self):
        """Serbia's headlines"""
        gn = GoogleNews(lang='sr', country='CS')
        self.tr_s(search=gn.geo_headlines('Србија'))

    def ukraine_uk(self):
        """Ukraine's ukrainian headlines"""
        gn = GoogleNews(lang='uk', country='UA')
        self.tr_s(search=gn.geo_headlines('Україна'))

    def israel_he(self):
        """Israel's headlines"""
        gn = GoogleNews(lang='he', country='IL')
        self.tr_s(search=gn.geo_headlines('ישראל'))

    def uae_ar(self):
        """United Arab Emirates' headlines"""
        gn = GoogleNews(lang='ar', country='AE')
        self.tr_s(search=gn.geo_headlines('الإمارات العربية المتحدة'))

    def saudi(self):
        """Saudi Arabia's headlines"""
        gn = GoogleNews(lang='ar', country='SA')
        self.tr_s(search=gn.geo_headlines('المملكة العربية السعودية'))

    def lebanon(self):
        """Lebanon's headlines"""
        gn = GoogleNews(lang='ar', country='LB')
        self.tr_s(search=gn.geo_headlines('لبنان'))

    def egypt(self):
        """Egypt's headlines"""
        gn = GoogleNews(lang='ar', country='EG')
        self.tr_s(search=gn.geo_headlines('مصر'))

    def india_en(self):
        """India's english headlines"""
        gn = GoogleNews(lang='en', country='IN')
        self.s(search=gn.geo_headlines('india'))

    def india_mr(self):
        """India's marathi headlines"""
        gn = GoogleNews(lang='mr', country='IN')
        self.tr_s(search=gn.geo_headlines('भारत'))

    def india_hi(self):
        """India's hindi headlines"""
        gn = GoogleNews(lang='hi', country='IN')
        self.tr_s(search=gn.geo_headlines('भारत'))

    def bangladesh(self):
        """Bangladesh's headlines"""
        gn = GoogleNews(lang='bn', country='BD')
        self.tr_s(search=gn.geo_headlines('বাংলাদেশ'))

    def india_ta(self):
        """India's tamil headlines"""
        gn = GoogleNews(lang='ta', country='IN')
        self.tr_s(search=gn.geo_headlines('இந்தியா'))

    def india_te(self):
        """India's telugu headlines"""
        gn = GoogleNews(lang='te', country='IN')
        self.tr_s(search=gn.geo_headlines('భారతదేశం'))

    def india_ml(self):
        """India's malayalam headlines"""
        gn = GoogleNews(lang='ml', country='IN')
        self.tr_s(search=gn.geo_headlines('ഇന്ത്യ'))

    def thailand(self):
        """Thailand's headlines"""
        gn = GoogleNews(lang='th', country='TH')
        self.tr_s(search=gn.geo_headlines('ไทย'))

    def china(self):
        """China's headlines"""
        gn = GoogleNews(lang='zh', country='CN')
        self.tr_s(search=gn.geo_headlines('中国'))

    def taiwan(self):
        """Taiwan's headlines"""
        gn = GoogleNews(lang='zh', country='TW')
        self.tr_s(search=gn.geo_headlines('台灣'))

    def hong_kong(self):
        """Hong Kong's headlines"""
        gn = GoogleNews(lang='zh', country='HK')
        self.tr_s(search=gn.geo_headlines('香港'))

    def japan(self):
        """Japan's headlines"""
        gn = GoogleNews(lang='ja', country='JP')
        self.tr_s(search=gn.geo_headlines('日本'))

    def korea_s(self):
        """Republic of Korea's (south Korea) headlines"""
        gn = GoogleNews(lang='ko', country='KR')
        self.tr_s(search=gn.geo_headlines('대한민국'))

    def europe_tr(self):
        print("\nFrance geo-specific headlines:")
        self.france()
        print("\nItaly geo-specific headlines:")
        self.italy()
        print("\nBelgium (french) geo-specific headlines:")
        self.belgium_fr()
        print("\nBelgium (dutch) geo-specific headlines:")
        self.belgium_nl()
        print("\nGermany geo-specific headlines:")
        self.germany()
        print("\nAustria geo-specific headlines:")
        self.austria()
        print("\nSpain geo-specific headlines:")
        self.spain()
        print("\nPortugal geo-specific headlines:")
        self.portugal()
        print("\nSwitzerland (french) geo-specific headlines:")
        self.switzerland_fr()
        print("\nSwitzerland (german) geo-specific headlines:")
        self.switzerland_de()
        print("\nCzechia geo-specific headlines:")
        self.czechia()
        print("\nLithuania geo-specific headlines:")
        self.lithuania()
        print("\nHungary geo-specific headlines:")
        self.hungary()
        print("\nNetherlands geo-specific headlines:")
        self.netherlands()
        print("\nNorway geo-specific headlines:")
        self.norway()
        print("\nPoland geo-specific headlines:")
        self.poland()
        print("\nRomania geo-specific headlines:")
        self.romania()
        print("\nSlovakia geo-specific headlines:")
        self.slovakia()
        print("\nSlovenia geo-specific headlines:")
        self.slovenia()
        print("\nSweden geo-specific headlines:")
        self.sweden()
        print("\nTurkey geo-specific headlines:")
        self.turkey()
        print("\nGreece geo-specific headlines:")
        self.greece()
        print("\nBulgaria geo-specific headlines:")
        self.bulgaria()
        print("\nRussia geo-specific headlines:")
        self.russia()
        print("\nUkraine (russian) geo-specific headlines:")
        self.ukraine_ru()
        print("\nUkraine (ukrainian) geo-specific headlines:")
        self.ukraine_uk()
        print("\nSerbia geo-specific headlines:")
        self.serbia()

    def america_n_tr(self):
        print("\nCanada (french) geo-specific headlines:")
        self.canada_fr()
        print("\nUSA (spanish) geo-specific headlines:")
        self.usa_es()
        print("\nCuba geo-specific headlines:")
        self.cuba()

    def america_s_tr(self):
        print("\nArgentina geo-specific headlines:")
        self.argentina()
        print("\nChile geo-specific headlines:")
        self.chile()
        print("\nColombia geo-specific headlines:")
        self.colombia()
        print("\nMexico geo-specific headlines:")
        self.mexico()
        print("\nPeru geo-specific headlines:")
        self.peru()
        print("\nVenezuela geo-specific headlines:")
        self.venezuela()
        print("\nBrazil geo-specific headlines:")
        self.brazil_pt()

    def asia_tr(self):
        print("\nIndonesia geo-specific headlines:")
        self.indonesia()
        print("\nVietnam geo-specific headlines:")
        self.vietnam()
        print("\nUnited Arab Emirates geo-specific headlines:")
        self.uae_ar()
        print("\nIsrael geo-specific headlines:")
        self.israel_he()
        print("\nSaudi Arabia geo-specific headlines:")
        self.saudi()
        print("\nLebanon geo-specific headlines:")
        self.lebanon()
        print("\nIndia (marathi) geo-specific headlines:")
        self.india_mr()
        print("\nIndia (hindi) geo-specific headlines:")
        self.india_hi()
        print("\nIndia (tamil) geo-specific headlines:")
        self.india_ta()
        print("\nIndia (telugu) geo-specific headlines:")
        self.india_te()
        print("\nIndia (malayalam) geo-specific headlines:")
        self.india_ml()
        print("\nBangladesh geo-specific headlines:")
        self.bangladesh()
        print("\nThailand geo-specific headlines:")
        self.thailand()
        print("\nChina geo-specific headlines:")
        self.china()
        print("\nTaiwan geo-specific headlines:")
        self.taiwan()
        print("\nHong Kong geo-specific headlines:")
        self.hong_kong()
        print("\nJapan geo-specific headlines:")
        self.japan()
        print("\nRepublic of Korea (south) geo-specific headlines:")
        self.korea_s()

    def africa_tr(self):
        print("\nMorocco (french) geo-specific headlines:")
        self.morocco_fr()
        print("\nSenegal geo-specific headlines:")
        self.senegal()
        print("\nEgypt geo-specific headlines:")
        self.egypt()

    def mena_tr(self):
        print("\nEgypt geo-specific headlines:")
        self.egypt()
        print("\nLebanon geo-specific headlines:")
        self.lebanon()
        print("\nMorocco (french) geo-specific headlines:")
        self.morocco_fr()
        print("\nSaudi Arabia geo-specific headlines:")
        self.saudi()
        print("\nUnited Arab Emirates geo-specific headlines:")
        self.uae_ar()
        print("\nIsrael geo-specific headlines:")
        self.israel_he()

    def india_languages(self):
        print("\nIndia (english) geo-specific headlines:")
        self.india_en()
        print("\nIndia (marathi) geo-specific headlines:")
        self.india_mr()
        print("\nIndia (hindi) geo-specific headlines:")
        self.india_hi()
        print("\nIndia (tamil) geo-specific headlines:")
        self.india_ta()
        print("\nIndia (telugu) geo-specific headlines:")
        self.india_te()
        print("\nIndia (malayalam) geo-specific headlines:")
        self.india_ml()
        print("\nBangladesh geo-specific headlines:")
        self.bangladesh()

    def countries_news(self):
        tr_list = {
            "Europe:": ["austria, belgium_fr, belgium_nl, bulgaria, czechia, france, germany, "
                        "greece, hungary, italy, lithuania, netherlands, norway, poland, portugal,"
                        " romania, serbia, slovakia, slovenia, spain, sweden, switzerland_de, "
                        "switzerland_fr, turkey, ukraine_ru, ukraine_uk,"],
            "Asia:": ["bangladesh, china, hong_kong, india_hi, india_ml, india_mr, india_ta,"
                      " india_te, indonesia, israel_he, japan, korea_s, lebanon, saudi, taiwan, "
                      "thailand, uae_ar, vietnam"],
            "Africa:": ["egypt, morocco_fr, senegal"],
            "North America:": ["canada_fr, cuba, usa_es,"],
            "South America:": ["argentina, brazil_pt, chile, colombia, mexico, peru, venezuela, "],
            "MENA region:": ["egypt, israel_he, lebanon, morocco_fr, saudi, uae_ar, "]}
        print(tr_list)
