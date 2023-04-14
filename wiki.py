#this file is used to get subsections from an article
import wikipediaapi
import random 
import data
import app

articles = ["Basketball", "Soccer", "Football" , "Tennis", "Baseball", "Golf"]

#insert all subaritlces into valid
def get_list():
    valid = []
    for section in articles:
        dic = {}
        wiki = wikipediaapi.Wikipedia('en')
        page = wiki.page(section)
        for subsection in page.sections:
            if subsection.title in ["See also", "References", "Further reading", "External links"]:
                continue
            if len(subsection.text) >= 35:
                text = subsection.text
                text.replace("\n", " ")
                
                dic["Sport"] = section
                dic["Subsection"] = subsection.title
                dic["Text"] = text
                valid.append(dic)
                dic = {}
    return valid
#get random value from list

def wiki_get_sport():
    return data.wiki[app.get_random()]["Sport"]

def wiki_sub_article():
    return data.wiki[app.get_random()]["Subsection"]

def wiki_text():
    return data.wiki[app.get_randomget_random()]["Text"]

def wiki_len():
    return len(data.wiki[app.get_random()]["Text"])
