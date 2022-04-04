import spacy
from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_md")


bitcoin_names = [
"Bitcoin",
"BTC",
"Ethereum",
"ETH",
"Tether",
"USDT",
"BNB",
"USD Coin",
"USDC",
"Cardano",
"ADA",
"Solana",
"SOL",
"XRP",
"Terra",
"LUNA",
"Polkadot",
"DOT",
]

doc1 = nlp("Solana was trading close to 15% higher on Tuesday, as crypto markets were mostly in the green to start February")
patterns = [[{"TEXT": bitcoin_name}] for bitcoin_name in bitcoin_names]

matcher = Matcher(nlp.vocab)
matcher.add("coinNames", patterns)

for mid, start, end in matcher(doc1):
  print(start, end, doc1[start:end])



patterns = [{"TAG": {"IN": ["VB", "VBD", "VBG", "VBN", "VBP"]}, "LEMMA":{"NOT_IN": ["be"]}}]

matcher = Matcher(nlp.vocab)
matcher.add("verbs", [patterns])

for mid, start, end in matcher(doc1):
  print(start, end, doc1[start:end])


for mid, start, end in matcher(doc1):
  span = doc1[start:end]
  child = span[0].children
  print(span, list(child))


for ent in doc1.ents:
  print(ent, ent.label_)

print(doc1[9], doc1[9].head.head)
print(doc1[5], doc1[5].head.head.head)
print(doc1[-1], doc1[-1].head)
