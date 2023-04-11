import openai
import random 
import os
import data 
list1 = []
def get_articles():
    api_prompt = """For an article about "ARTICLE", make a section titled "HEADER" that is about COUNT characters long. The section is a part of a larger article about "ARTICLE".  Send only the section and omit the section's header and try to keep it in one paragraph. Write it in the style of an encyclopedia."""
    openai.api_key = os.environ["api_key"]
    for article in data.wiki:
        dic = {}
        #change prompt 
        api_prompt = api_prompt.replace("ARTICLE", article["Sport"])
        api_prompt = api_prompt.replace("HEADER", article["Subsection"])
        api_prompt = api_prompt.replace("COUNT", str(len(article["Text"])))

        res = openai.Completion.create(engine = "text-davinci-001", prompt = api_prompt, max_tokens = 1024)
        text = res.choices[0].text
        text = text.replace("\n", "")
        dic["Sport"] = article["Sport"]
        dic["Subsection"] = article["Subsection"]
        dic["Text"] = text
        list1.append(dic)

def gpt_sport():
    return data.gpt[get_random()]["Sport"]

def gpt_sub_article():
    return data.gpt[get_random()]["Subsection"]

def gpt_text():
    return data.gpt[get_random()]["Text"]

def gpt_len()
    return len(data.gpt[num]["Text"])
