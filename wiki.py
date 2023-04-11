#this file is used to get subsections from an article
import wikipediaapi
import random

articles = ["Basketball", "Soccer", "Football" , "Tennis", "Baseball", "Golf"]
valid = []
#insert all subaritlces into valid
for section in articles:
    dic = {}
    dic["Sport"] = section
    wiki = wikipediaapi.Wikipedia('en')
    page = wiki.page(section)
    for subsection in page.sections:
        if subsection.title in ["See also", "References", "Further Reading", "External links" ]:
            continue
        if len(subsection.text) >= 35:
            dic["Subsection"] = subsection.title
            dic["Text"] = subsection.text
            valid.append(dic)
print(len(valid))
def get_title():
    return
def get_sub_article():
    return
def get_text():
    return
def get_random_article_index():
    num =  random.randint(0,len(valid) - 1)
    return num

def get_len(subsec):
    return len(subsec)
