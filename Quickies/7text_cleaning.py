import spacy
nlp = spacy.load("en_core_web_md")


text = "\n\n\nI went there after 3 years. At my 3th year,,, I wrote this abbrev. list one by one. So that you can all read. One of you asked me why??? I told them I\n emailed them, they answered me with their website and told me\n their name\t."

doc = nlp(text)
print(doc[0])
print(doc[0].is_space)
tokens = [token for token in doc if not token.is_space]
print(tokens)


ok_punct = "!?$%+"
tokens = [token for token in doc if not ((token.is_punct and token.text not in ok_punct) or token.is_space)]
print(tokens)

tokens = [token.lower_ for token in doc if not ((token.is_punct and token.text not in ok_punct) or token.is_space)]
print(tokens)

abbrevs = {
'abbrev': 'abbreviation',
'dr': 'doctor',
'mr': 'mister'
}
tokens = [abbrevs.get(token, token) for token in tokens]
print(tokens)
