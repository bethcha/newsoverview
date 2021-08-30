# newsoverview
News at a glance.

This is my first program and it might be a bit messy but I hope to improve it as my skills develop! If you'd like anything added/edited or would like to add/edit something yourself, just let me know.

## About
This package is perfect for when you need to have an overview of what's going on in the world.

It's a simple bit of code which uses a news scraper to search Google News, and provides the titles, dates, links and if necessary, a translation of the title at the bottom. 
The news searches are sorted into different categories, also referred to as classes. These classes include:
  * CoronavirusNews, Protests, TravelWarnings, TerrorNews, EnglishWorldNews, and TranslatedWorldNews

Certain countries and languages are not currently present in this program; as EnglishWorldNews and TranslatedWorldNews use specific country-language combinations found in GoogleNews to search for geo-specific headlines. However, if you would like a country-language combination added to these classes, let me know.

All languages and countries follow a two-character code system (eg. Ukraine and russian = UK and ru). There is an attached file named countries_and_lang.txt with all countries and languages in this format. This is because Google News uses these labelling conventions. 


#### Please note that titles in languages other than english are translated, which means that these functions take slightly longer to run. 

#
## Contents: 
### newsoverview
### About
### Installation Guide
### Usage
### Further Usage
#### * EnglishWorldNews
#### * TranslatedWorldNews
#### * CoronavirusNews
#### * TravelWarnings
#### * Protests
#### * TerrorNews
### License

#
## Installation Guide
1. First things first: you need to install 'newsoverview'.
```
install newsoverview  # in PyCharm you can right click on this to install
C:> py -m pip install newsoverview  # windows command/terminal
$ python -m pip install newsoverview  # mac and linux
```

2. Import the program and its classes: 
```python
import newsoverview
from newsoverview import CoronavirusNews, EnglishWorldNews, Protests, TravelWarnings, TerrorNews, TranslatedWorldNews 
```

3. Fix `pygooglenews`:

There is one line of code that needs editing for `pygooglenews` to work properly. This error is in the module `feedparser.py`. There are two ways to fix this problem; you can either:

  * Run the program and use the error to navigate to `feedparser.py` 
    * OR
  * Search for `feedparser.py` in your interpreter
    * OR
  * Manually navigate to `feedparser.py` by going to the library root and finding the module:
    * venv > lib > site-packages > feedparser.py  
    * *it is __not__ in the* `feedparser` *folder, it will be at the bottom of the site-packages folder.*
   
Once you are in the `feedparser.py` module, navigate to line 93 and replace: 

`_base64decode = getattr(base64, 'decodebytes', base64.decodestring)` **with** `base64.decodebytes` 

Congrats! You just fixed `pygooglenews`

4. Give it a go!

Lets find the top news stories happening in the UK:

```python
news = EnglishWorldNews()  # assigning the EnglishWorldNews class to the variable 'news'
news.uk()  # calling the function 'uk()' from the EnglishWorldNews class 
```

#
## Usage 
Installing the package:
```python
pip install newsoverview
from newsoverview import CoronavirusNews, EnglishWorldNews, Protests, TravelWarnings, TerrorNews, TranslatedWorldNews 
```
* Finding UK top news:
```python
uk_news = EnglishWorldNews().uk()
```

* Finding all **protest** news released in the past 12 hours:
```python
protests = Protests().call_protests()
````
**Please note that titles in languages other than english are translated, which means that these functions take slightly longer to run**

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

* Finding **geo-specific headlines** reported in *english*-speaking countries by continent:
```python
news = EnglishWorldNews()
news.europe()  # UK, Ireland and Latvia
news.asia()  # includes India, Pakistan, Philippines, Singapore, etc
news.africa()  # includes Zimbabwe, South Africa, Kenya, Ethiopia, etc
news.americas()  # only N. America; USA and Canada
news.oceana()  # New Zealand and Australia
``` 

* Finding **geo-specific headlines** reported in *non-english*-speaking countries by continent:
```python
tr_news = TranslatedWorldNews()
tr_news.europe_tr()  # includes Russia, Serbia, Sweden, Greece, Belgium, Italy, etc
tr_news.america_n_tr()  # USA (spanish), Canada (french) and Cuba
tr_news.america_s_tr()  # includes Mexico, Peru, Brazil, Argentina, Chile, etc
tr_news.asia_tr()  # includes China, India, Lebanon, Vietnam, Indonesia, Israel, etc
tr_news.africa_tr()  # Morocco, Senegal and Egypt

# Includes specific MENA region function if needed:
tr_news.mena_tr()  # Egypt, Lebanon, Morocco, Saudi Arabia, United Arab Emirates & Israel
```

#
## Usage (advanced)

### EnglishWorldNews Class
Show a list of all *countries* listed in the `EnglishWorldNews` Class:
```python
en_news = EnglishWorldNews()
en_country_list = en_news.en_list()
```
To call news from individual countries, follow the format `en_news.country()`, eg for Tanzanian headlines, call  en_news.tanzania()`. All countries will follow this format.

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
To call news from individual countries, follow the format `tr_news.country()`, eg for Slovakian headlines, call `tr_news.slovakia()`. All countries will follow this format. 

Be aware that some countries may have a suffix where they speak more than one language recognised by Google News, eg for Belgium. 
You can call `tr_news.belgium_fr()` for Belgian headlines in french, or `tr_news.belgium_nl()` for Belgian headlines in dutch. 

### CoronavirusNews Class
Show a list of all *languages* listed in the `CoronavirusNews` Class:
```python
covid = CoronavirusNews()
covid_lang_list = covid.covid_list()
```
To call news from individual languages, follow the format `covid.language_covid()`, eg for arabic headlines, call `covid.ar_covid()`. All languages will follow this format.

### TravelWarnings Class
Show a list of all *languages* listed in the `TravelWarnings` Class:
```python
travel = TravelWarnings()
aero_lang_list = travel.lang_aeroplanes()  # for aeroplane and flight-related news
travel_lang_list = travel.lang_travel_restrictions()  # for travel restrictions and border closure-related news
# they both use the same languages
```
To call news for an individual language in the aeroplane catagory, follow the format `travel.language_aeroplanes()`, eg for russian headlines, call `travel.ru_aeroplanes()`. To call news for an individual language in the travel_restrictions catagory, follow the format `travel.language_travel_restrictions()`, eg for portuguese headlines, call `travel.pt_travel_restrictions()` All languages will follow this format.

Furthermore, you can call both `aeroplanes` and `travel_restrictions` together for a particular language using `travel.call_language()`. If you wanted the french travel news, you can simply use `travel.call_fr()`. 

### Protests Class
Show a list of all *languages* listed in the `Protests` Class:
```python
protests = Protests()
protests_lang_list = protests.lang_protests()
```
To call news from individual languages, follow the format `protests.language_protests()`, eg for german headlines, call `protests.de_protests()`. All languages will follow this format.

### TerrorNews Class
Show a list of the functions used in the `TerrorNews` Class:
```python
terror = TerrorNews()
terror_functions = terror.terror_search()
```
This class only searches in english, and searches for keywords, groups, and terror-related activities occuring in the past 12 hours. 

To call all three of these functions, simply use `terror.terror_news()` and it will output terror-related news articles published in the past 12 hours. 


#
## License
This project is licensed under the terms of the MIT License
