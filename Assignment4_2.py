from nltk import ngrams
# file = open("/home/exam/Desktop/NLP_LAB75/al.txt")
file = open("/content/SampleNLP.txt")
for i in file.readlines():
  cumulative = i
  sentences = i.split(".")
  counter = 0
  for sentence in sentences:
    print("For sentence", counter + 1, ", trigrams are: ")
    trigrams = ngrams(sentence.split(" "), 3)
    for grams in trigrams:
      print(grams)
      counter += 1
      print()


# OUTPUT
# For sentence 1 , trigrams are: 
# ('"While', 'unigram', 'model')

# ('unigram', 'model', 'sentences')

# ('model', 'sentences', 'will')

# ('sentences', 'will', 'only')

# ('will', 'only', 'exclude')

# ('only', 'exclude', 'the')

# ('exclude', 'the', 'UNK')

# ('the', 'UNK', 'token,')

# ('UNK', 'token,', 'models')

# ('token,', 'models', 'will')

# ('models', 'will', 'also')

# ('will', 'also', 'exclude')

# ('also', 'exclude', 'all')

# ('exclude', 'all', 'other')

# ('all', 'other', 'words')

# ('other', 'words', 'already')

# ('words', 'already', 'in')

# ('already', 'in', 'the')

# ('in', 'the', 'sentence')

# For sentence 20 , trigrams are: 
# ('NTK', 'provides', 'another')

# ('provides', 'another', 'function')

# ('another', 'function', 'everygrams')

# ('function', 'everygrams', 'that')

# ('everygrams', 'that', 'converts')

# ('that', 'converts', 'a')

# ('converts', 'a', 'sentence')

# ('a', 'sentence', 'into')

# ('sentence', 'into', 'unigram,')

# ('into', 'unigram,', 'bigram,')

# ('unigram,', 'bigram,', 'trigram,')

# ('bigram,', 'trigram,', 'and')

# ('trigram,', 'and', 'so')

# ('and', 'so', 'on')

# ('so', 'on', 'till')

# ('on', 'till', 'the')

# ('till', 'the', 'ngrams,')

# ('the', 'ngrams,', 'where')

# ('ngrams,', 'where', 'n')

# ('where', 'n', 'is')

# ('n', 'is', 'the')

# ('is', 'the', 'length')

# ('the', 'length', 'of')

# ('length', 'of', 'the')

# ('of', 'the', 'sentence')

# For sentence 45 , trigrams are: 
# ('', 'In', 'short,')

# ('In', 'short,', 'this')

# ('short,', 'this', 'function')

# ('this', 'function', 'generates')

# ('function', 'generates', 'ngrams')

# ('generates', 'ngrams', 'for')

# ('ngrams', 'for', 'all')

# ('for', 'all', 'possible')

# ('all', 'possible', 'values')

# ('possible', 'values', 'of')

# ('values', 'of', 'n')

