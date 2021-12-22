# newsoverview
News at a glance.

This is my first program, and it might be a bit messy, but I hope to improve it as my skills develop! If you'd like anything added/edited or would like to add/edit something yourself, just let me know.

## About
This module is perfect for when you need to have an overview of what's going on in the world.

It's a simple bit of code which uses a news scraper to search Google News, and provides the titles, dates, links and if necessary, a translation of the title at the bottom. 
The news searches are sorted into different categories, also referred to as classes. These classes include:
  * CoronavirusNews, Protests, TravelWarnings, TerrorNews, EnglishWorldNews, and TranslatedWorldNews

Certain countries and languages are not currently present in this program; as EnglishWorldNews and TranslatedWorldNews use specific country-language combinations found in GoogleNews to search for geo-specific headlines. However, if you would like a country-language combination added to these classes, let me know.

All languages and countries follow a two-character code system (e.g. Ukraine and Russian = UK and ru). There is an attached file named `countries_and_lang.txt` with all countries and languages in this format. This is because Google News uses these labelling conventions. 


#### Please note that titles in languages other than English are translated, which means that these functions take slightly longer to run. 

#
## Contents: 
### [newsoverview](https://github.com/bethcha/newsoverview#newsoverview)
### [About](https://github.com/bethcha/newsoverview#about)
### [Installation Guide](https://github.com/bethcha/newsoverview#installation-guide-1)
### [Usage](https://github.com/bethcha/newsoverview#usage-1)
### [Usage (advanced)](https://github.com/bethcha/newsoverview#usage-advanced)
#### * [EnglishWorldNews](https://github.com/bethcha/newsoverview#englishworldnews-class)
#### * [TranslatedWorldNews](https://github.com/bethcha/newsoverview#translatedworldnews-class)
#### * [SimpleSearch](https://github.com/bethcha/newsoverview#simplesearch-class)
#### * [CoronavirusNews](https://github.com/bethcha/newsoverview#coronavirusnews-class)
#### * [TravelWarnings](https://github.com/bethcha/newsoverview#travelwarnings-class)
#### * [Protests](https://github.com/bethcha/newsoverview#protests-class)
#### * [TerrorNews](https://github.com/bethcha/newsoverview#terrornews-class)
#### * [HospitalNews](https://github.com/bethcha/newsoverview#hospitalnews-class)
#### * [KWSearch](https://github.com/bethcha/newsoverview#kwsearch-class)
### [License](https://github.com/bethcha/newsoverview#license-1)
### [Links](https://github.com/bethcha/newsoverview#links)

#
## Installation Guide
1. First things first: you need to install 'newsoverview'.
```
pip install newsoverview  
C:> py -m pip install newsoverview  # windows command/terminal
$ python -m pip install newsoverview  # mac and linux
```
[PyPi](https://pypi.org/project/newsoverview/), [GitHub](https://github.com/bethcha/newsoverview), [Colab](https://colab.research.google.com/drive/12_2TFrRHNydzZ0qFwwG1fcluAhBZvDii?usp=sharing)


2. Import the program and its classes: 
```python
import newsoverview
from newsoverview import CoronavirusNews, EnglishWorldNews, Protests, TravelWarnings, TerrorNews, TranslatedWorldNews, SimpleSearch, HospitalNews, KWSearch 
```

3. Fix `feedparser.py`:

**You only need to do this step if you've run step 4, and you get an error relating to `feedparser.py`. This error links to all modules called with this function, and when it's been fixed it will go away**


There is one line of code that needs editing for `newsoverview` to work properly through `pygooglenews`. **This error is in the module `feedparser.py`.**

There are two ways to fix this problem; you can either:

  * Run the program and use the error to navigate to `feedparser.py` 
    * OR
  * Search for `feedparser.py` in your interpreter
    * OR
  * Manually navigate to `feedparser.py` by going to the library root and finding the module:
    * venv > lib > site-packages > feedparser.py  
    * *it is __not__ in the* `feedparser` *folder, it will be at the bottom of the site-packages folder.*
   
Once you are in the `feedparser.py` module, navigate to line 93 and replace: 

`_base64decode = getattr(base64, 'decodebytes', base64.decodestring)` **with** `base64.decodebytes` 

Congrats! You just fixed `pygooglenews`,

4. Give it a go!

Let's find the top news stories happening in the UK:

```python
news = EnglishWorldNews()  # assigning the EnglishWorldNews class to the variable 'news'
news.uk()  # calling the function 'uk()' from the EnglishWorldNews class 
```
Or, let's find the most recent news about the paralympics:
```python
my_search = SimpleSearch()
paralympics = my_search.en_search(query='paralympics')
```

#
## Usage 
Installing the module:
```python
pip install newsoverview
from newsoverview import CoronavirusNews, EnglishWorldNews, Protests, TravelWarnings, TerrorNews, TranslatedWorldNews, SimpleSearch, HospitalNews, KWSearch 
```
* Finding top news in Asia (English) (**quick start**):
```python
asia_news = EnglishWorldNews().asia()
```

### Main Functions used:

* Finding all **protest** news released in the past 12 hours:
```python
protests = Protests().call_protests()
````
**Please note that titles in languages other than English are translated, which means that these functions take slightly longer to run**

* Finding all **aeroplane, flight,** and **travel restriction**-related news in the past 12 hours:
```python
travel = TravelWarnings()
flights = travel.aeroplane_disruptions()  # aeroplanes and flight-related news
travel_disruptions = travel.travel_restrictions()  # travel restriction-related news
```

* Finding **coronavirus** and **lockdown**-related news reported in the last **1 hour**:
```python
covid = CoronavirusNews()
covid.coronavirus()  # covid-related news 
covid.lockdown()  # lockdown-related news
```

* Finding all **terror**-related news reported in the last 12 hours:
```python
terror = TerrorNews().terror_search()
```

* Finding all **incident**-related news reported in the last 10 hours:
```python
incidents = KWSearch().incidents_reports()
```

* Finding **geo-specific headlines** reported in *English*-speaking countries by continent:
```python
news = EnglishWorldNews()
news.europe()  # UK, Ireland and Latvia
news.asia()  # includes India, Pakistan, Philippines, Singapore, etc
news.africa()  # includes Zimbabwe, South Africa, Kenya, Ethiopia, etc
news.americas()  # only N. America; USA and Canada
news.oceana()  # New Zealand and Australia
``` 

* Finding **geo-specific headlines** reported in *non-English*-speaking countries by continent:
```python
tr_news = TranslatedWorldNews()
tr_news.europe_tr()  # includes Russia, Serbia, Sweden, Greece, Belgium, Italy, etc
tr_news.america_n_tr()  # USA (Spanish), Canada (French) and Cuba
tr_news.america_s_tr()  # includes Mexico, Peru, Brazil, Argentina, Chile, etc
tr_news.asia_tr()  # includes China, India, Lebanon, Vietnam, Indonesia, Israel, etc
tr_news.africa_tr()  # Morocco, Senegal and Egypt

# Includes specific MENA (Middle East and North Africa) region function if needed:
tr_news.mena_tr()  # Egypt, Lebanon, Morocco, Saudi Arabia, United Arab Emirates & Israel
```

* Using **your own query** to search for news:
All results will be searched for in the **past 24 hours**.  

For the translated search, you need to import GoogleNews. This is because GoogleNews is a parameter that can to be altered with each query, so you can pass specific country/language combinations to refine your news to that country/language. 

*However,* if you are unsure of a country/language combination, **use `country='GB'` or `country='US'`** as almost all languages can be searched from these countries.

More information is provided below in SimpleSearch Class.
```python
from pygooglenews import GoogleNews  # if you're using the translated search, you need to import GoogleNews to make a country-language combination.
my_search = SimpleSearch()
my_search.en_search(query='football')  # English search of the query 'football'
my_search.tr_search(gn=GoogleNews(lang='hi', country='IN'), query='फ़ुटबॉल')  # gives a translated search of the query 'football' in Hindi (hi), as if you're searching in India (IN)
```

#
## Usage (advanced)

### EnglishWorldNews Class
Show a list of all *countries* listed in the `EnglishWorldNews` Class:
```python
en_news = EnglishWorldNews()
en_country_list = en_news.en_list()
```
To call news from individual countries, follow the format `en_news.country()`, e.g.  for Tanzanian headlines, call  en_news.tanzania()`. All countries will follow this format.

You can create your own custom `en_news` function, for example:
```python
def my_countries():
    print("UK headlines")
    en_news.uk()
    print("Canada headlines")
    en_news.canada()
    print("India headlines")
    en_news.india()
    print("Zimbabwe headlines")
    en_news.zimbabwe()

my_countries()  # call your function to print your own list of desired countries
```

### TranslatedWorldNews Class
Show a list of all *countries* listed in the `TranslatedWorldNews` Class:
```python
tr_news = TranslatedWorldNews()
tr_country_list = tr_news.tr_list()
```
To call news from individual countries, follow the format `tr_news.country()`, e.g.  for Slovakian headlines, call `tr_news.slovakia()`. All countries will follow this format. 

Be aware that some countries may have a suffix where they speak more than one language recognised by Google News, e.g.  for Belgium. 
You can call `tr_news.belgium_fr()` for Belgian headlines in French, or `tr_news.belgium_nl()` for Belgian headlines in Dutch. 

### SimpleSearch Class
You can find the correct country/language combinations by going to Google News, and scrolling down to the bottom to 'Language & Region' to see which combinations are supported.

All country codes and language codes are provided in the `countries_and_lang.txt` file
The `en_search` default is using GoogleNews in the UK (country='GB'). The code for this is `gn=GoogleNews(lang='en', country='GB')`


### CoronavirusNews Class
Show a list of all *languages* listed in the `CoronavirusNews` Class:
```python
covid = CoronavirusNews()
covid_lang_list = covid.covid_list()
```
To call news from individual languages, follow the format `covid.language_covid()`, e.g.  for Arabic headlines, call `covid.ar_covid()`. All languages will follow this format.

### TravelWarnings Class
Show a list of all *languages* listed in the `TravelWarnings` Class:
```python
travel = TravelWarnings()
aero_lang_list = travel.lang_aeroplanes()  # for aeroplane and flight-related news
travel_lang_list = travel.lang_travel_restrictions()  # for travel restrictions and border closure-related news
# they both use the same languages
```
To call news for an individual language in the aeroplane category, follow the format `travel.language_aeroplanes()`, e.g. for Russian headlines, call `travel.ru_aeroplanes()`. 

To call news for an individual language in the travel_restrictions category, follow the format `travel.language_travel_restrictions()`, e.g.  for Portuguese headlines, call `travel.pt_travel_restrictions()` All languages will follow this format.

Furthermore, you can call both `aeroplanes` and `travel_restrictions` together for a particular language using `travel.call_language()`. If you wanted the French travel news, you can simply use `travel.call_fr()`. 

### Protests Class
Show a list of all *languages* listed in the `Protests` Class:
```python
protests = Protests()
protests_lang_list = protests.lang_protests()
```
To call news from individual languages, follow the format `protests.language_protests()`, e.g. for German headlines, call `protests.de_protests()`. All languages will follow this format.

### TerrorNews Class
Show a list of the functions used in the `TerrorNews` Class:
```python
terror = TerrorNews()
terror_functions = terror.terror_search()
```
This class only searches in English, and searches for keywords, groups, and terror-related activities  occurring within the past 12 hours. 

To call all three of these functions, simply use `terror.terror_news()` and it will output terror-related news articles published in the past 12 hours. 

### HospitalNews Class
Calling the function to see if any hospital-related news has been reported in the past 12 hours, and see which languages are included in the search:
```python
hospital_news = HospitalNews().call_hospitals()
hospital_langs = HospitalNews().lang_hospitals()
```

### KWSearch Class
Keywords for incident, raid, hostage, and clash-related news; only in English:
```python
incidents = KWSearch().incidents_reports()
```
includes `incidents()`, `raids()`, `hostages()`, and `clashes()` within the `KWSearch()` class.
#
## License
This project is licensed under the terms of the MIT License

### Links
[Github](https://github.com/bethcha/newsoverview), [PyPi](https://pypi.org/project/newsoverview/), [Colab](https://colab.research.google.com/drive/12_2TFrRHNydzZ0qFwwG1fcluAhBZvDii?usp=sharing)