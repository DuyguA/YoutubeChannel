import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_md")
matcher = Matcher(nlp.vocab)

doc1 = nlp("I spent 200$ on my books.")
pattern = [{"IS_DIGIT": True}, {"IS_CURRENCY": True}]
matcher.add("money", [pattern])
matches = matcher(doc1)

for mid, start, end in matches:
  print(start, end, doc1[start:end])


doc2 =nlp("Your flight costs £20. You can buy extra leg space for £5")
pattern2 = [{"IS_CURRENCY": True}, {"IS_DIGIT": True}]
matcher.add("money2", [pattern2])
matches = matcher(doc2)

for mid, start, end in matches:
  print(start, end, doc2[start:end])


doc3 = nlp("200$ is stolen from my account")
matches = matcher(doc3)

for mid,start,end in matches:
  match = doc3[start:end]
  curr_tok = match[-1]
  print(curr_tok.dep_, curr_tok.head, curr_tok.head.lemma_)
