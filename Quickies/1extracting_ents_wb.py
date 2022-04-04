from bs4 import BeautifulSoup
import requests

def url_to_text(url):
  res = requests.get(url)
  html = res.text
  soup = BeautifulSoup(html, 'html5lib')
  for script in soup(["script", "style", 'aside']):
    script.extract()
    text = soup.get_text()
  return " ".join(text.split())

article = url_to_text("https://eu.usatoday.com/story/news/nation/2022/02/01/fertilizer-plant-fire-explosions-winston-salem-evacuations/9295905002/")
print(article)

import spacy
nlp = spacy.load("en_core_web_md")
doc = nlp(article)

print(doc.ents)

for ent in doc.ents:
  print(ent.text, ent.label_)


from collections import Counter
labels = [ent.label_ for ent in doc.ents]
counts = Counter(labels)
print(counts)

spacy.explain("GPE")
