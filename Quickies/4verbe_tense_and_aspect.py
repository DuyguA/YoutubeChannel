import spacy
nlp = spacy.load("en_core_web_md")

sent1 = "I flew to Rome."
sent2 = "I'm flying to Rome."
sent3 = "I will fly to Rome."

doc1 = nlp(sent1)
doc2 = nlp(sent2)
doc3 = nlp(sent3)

for doc in [doc1, doc2, doc3]:
  print([(w.text, w.lemma_) for w in doc if w.tag_== 'VBG' or w.tag_== 'VB'])
