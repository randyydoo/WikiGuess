import openai

openai.api_key = "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"
prompt = "Can you give me a name for my pet Golden Retriever"
res = openai.Completion.create(engine = "text-davinci-001", prompt = prompt, max_tokens = 10)
print(res.text)
