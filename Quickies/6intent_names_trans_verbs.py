import spacy
nlp = spacy.load("en_core_web_md")

doc = nlp("find a flight from washington to sf")

for token in doc:
  if token.dep_ == "dobj":
    print(token.head.text + token.text.capitalize())


doc = nlp("Show all flights and meals from Berlin to Rome")

for token in doc:
  if token.dep_ == "dobj":
    dobj = token
    conj = [t.text for t in token.conjuncts]
    verb = dobj.head
    print(verb, dobj, conj)
