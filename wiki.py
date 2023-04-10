#this file is used to get subsections from an article
import wikipediaapi
import random

articles = ["Basketball", "Soccer", "Football" , "Tennis", "Baseball", "Golf"]

#find random article
def get_random():
    return random.randint(0,len(articles) - 1)
def get_subtitles():
    valid = []
    for article in articles:
        wiki = wikipediaapi.Wikipedia('en')
        page = wiki.page(article)
        for subsection in page.sections:
            if subsection.title in ["See also", "References", "Further Reading", "External links" ]:
                continue
            if len(subsection.text) >= 35:
                valid.append(subsection.text)


