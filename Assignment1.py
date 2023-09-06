#import libraries
import spacy
nlp = spacy.load("en_core_web_sm")

#taking input
about_text = (
    "Joe waited for the train."
    "The train was late."
    "Mary and Samantha took the bus. "
    " I looked for Mary and Samantha at the bus station."
    )
about_doc = nlp(about_text)


#Sentence Detection
print("Sentence Detection___")
sentences = list(about_doc.sents)
len(sentences)
2
for sentence in sentences:
    print(f"{sentence[:5]}...")
    
    
#Tokenization
print("Tokenization___")
for token in about_doc:
  print (token, token.idx)
  
  
#Stop Words
print("Stop Words___")
import spacy
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)

for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)


#Lemmatization
print("Lemmatization___")
for token in about_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")


#Part-of-Speech
print("Part-of-Speech___")
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )


# Sentence Detection___
# 4
# Joe waited for the train...
#  The train was late...
#  Mary and Samantha took the bus...
#  I looked for Mary and Samantha at the bus station...

# Tokenization___
# Joe 0
# waited 4
# for 11
# the 15
# train 19
# . 24
#   25
# The 26
# train 30
# was 36
# late 40
# . 44
# Mary 46
# and 51
# Samantha 55
# took 64
# the 68
# bus 72
# . 75
#   76
# I 77
# looked 79
# for 86
# Mary 90
# and 95
# Samantha 100
# at 110
# the 113
# bus 117
# station 121
# . 128

# Stop Words____
# 297
# below
# whereas
# anything
# nor
# at
# nine
# other
# was
# someone
# sometimes

# Lemmatization____
#              waited : wait
#                late : late
#                 bus : bus
#              looked : look
#              station : station

# Part-of-Speech____
# TOKEN: Joe
# =====
# TAG: NNP      POS: PROPN
# EXPLANATION: noun, proper noun, singular

# TOKEN: waited
# =====
# TAG: VBD      POS: VERB
# EXPLANATION: verb, past tense

# TOKEN: for
# =====
# TAG: IN       POS: ADP
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: the
# =====
# TAG: DT       POS: DET
# EXPLANATION: determiner

# TOKEN: train
# =====
# TAG: NN       POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: .
# =====
# TAG: .        POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer

# TOKEN: The
# =====
# TAG: DT       POS: DET
# EXPLANATION: determiner

# TOKEN: train
# =====
# TAG: NN       POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: was
# =====
# TAG: VBD      POS: VERB
# EXPLANATION: verb, past tense

# TOKEN: late
# =====
# TAG: JJ       POS: ADJ
# EXPLANATION: adjective

# TOKEN: .
# =====
# TAG: .        POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer

# TOKEN: Mary
# =====
# TAG: NNP      POS: PROPN
# EXPLANATION: noun, proper noun, singular

# TOKEN: and
# =====
# TAG: CC       POS: CCONJ
# EXPLANATION: conjunction, coordinating

# TOKEN: Samantha
# =====
# TAG: NNP      POS: PROPN
# EXPLANATION: noun, proper noun, singular

# TOKEN: took
# =====
# TAG: VBD      POS: VERB
# EXPLANATION: verb, past tense

# TOKEN: the
# =====
# TAG: DT       POS: DET
# EXPLANATION: determiner

# TOKEN: bus
# =====
# TAG: NN       POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: .
# =====
# TAG: .        POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer

# TOKEN:  
# =====
# TAG: _SP      POS: SPACE
# EXPLANATION: space

# TOKEN: I
# =====
# TAG: PRP      POS: PRON
# EXPLANATION: pronoun, personal

# TOKEN: looked
# =====
# TAG: VBD      POS: VERB
# EXPLANATION: verb, past tense

# TOKEN: for
# =====
# TAG: IN       POS: ADP
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: Mary
# =====
# TAG: NNP      POS: PROPN
# EXPLANATION: noun, proper noun, singular

# TOKEN: and
# =====
# TAG: CC       POS: CCONJ
# EXPLANATION: conjunction, coordinating

# TOKEN: Samantha
# =====
# TAG: NNP      POS: PROPN
# EXPLANATION: noun, proper noun, singular

# TOKEN: at
# =====
# TAG: IN       POS: ADP
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: the
# =====
# TAG: DT       POS: DET
# EXPLANATION: determiner

# TOKEN: bus
# =====
# TAG: NN       POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: station
# =====
# TAG: NN       POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: .
# =====
# TAG: .        POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer
