import requests
import webbrowser
import json
import nltk.data
import os
import numpy as np
import pickle 

os.chdir(r'C:\Users\Raymond\Desktop\chatbots\chatbot')

# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# fp = open("t8.shakespeare.txt")
# data = fp.read()
# # print('\n-----\n'.join(tokenizer.tokenize(data)))
# shakespeare = tokenizer.tokenize(data)
# shakespeare = [elem for elem in shakespeare if len(elem) < 40 and len(elem) > 15]
# with open("shakespeare_tokenized.txt", "wb") as fp:   #Pickling
# 	pickle.dump(shakespeare, fp)

with open("shakespeare_tokenized.txt", "rb") as fp:   # Unpickling
	shakespeare = pickle.load(fp)

with open('memes.json') as f:
    data = json.load(f)
memes = data['data']['memes']
meme_ids = [elem['id'] for elem in memes]
random_id = np.random.choice(meme_ids)

text0 = np.random.choice(shakespeare)
text1 = np.random.choice(shakespeare)
print(text0,text1)

# g = requests.get("https://api.imgflip.com/get_memes")
# print(g.text)

r = requests.post("https://api.imgflip.com/caption_image",data={'template_id':random_id, 
	'username':'raymondhfeng1998', 'password':'f,z=[T3TYjrv7S)r', 'text0':text0, 'text1':text1})
print(r.text)
url = r.json()['data']['url']
print(url)
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)