import openai
import random 
import os
import data
import app


def get_articles():
    list1 = []
    gpt_dic = {}
    openai.api_key = "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"
    for article in data.wiki:
        #change prompt
        api_prompt = """For an article about "ARTICLE", make a subsection about "HEADER" that is about COUNT characters long. Write it in a style similar to a section in on Wikipedia."""
        api_prompt = api_prompt.replace("ARTICLE", article["Sport"])
        api_prompt = api_prompt.replace("HEADER", article["Subsection"])
        api_prompt = api_prompt.replace("COUNT", str(len(article["Text"])))

        res = openai.Completion.create(engine = "text-davinci-001", prompt = api_prompt, max_tokens = 1024)
        text = res.choices[0].text
        text = text.replace("\n", " ")

        gpt_dic["Sport"] = article["Sport"]
        gpt_dic["Subsection"] = article["Subsection"]
        gpt_dic["Text"] = text
        list1.append(gpt_dic)
        gpt_dic = {}
    return list1
    

def gpt_sport():
    return data.gpt[app.get_random()]["Sport"]

def gpt_sub_article():
    return data.gpt[app.get_random()]["Subsection"]

def gpt_text():
    return data.gpt[app.get_random()]["Text"]

def gpt_len():
    return len(data.gpt[app.get_random()]["Text"])
