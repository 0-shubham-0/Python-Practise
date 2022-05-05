import nltk

text = "Today is a great day. It is even better than yesterday. And yesterday was the best day ever."

# sentence tokenize
from nltk.tokenize import sent_tokenize

tokenized_sent = sent_tokenize(text)
# print(tokenized_sent)
# word tokenize
tokenized_word = nltk.word_tokenize(text)
# print(tokenized_word)

# get synonyms, antonyms, definitions
# from nltk.corpus import wordnet
# syn=wordnet.synsets('like')
# print(syn)
# print(syn[1].definition())


# stemming 2 types - over, under


from nltk.stem.porter import *

porterStemmer = PorterStemmer()

sentence = "Provision Maximum multiply owed caring on go gone going was this"
wordList = nltk.word_tokenize(sentence)

stemWords = [porterStemmer.stem(word) for word in wordList]

print(' '.join(stemWords))

from nltk.stem.snowball import SnowballStemmer

snowBallStemmer = SnowballStemmer("english")

sentence = "Provision but Maximum multiply owed caring on go gone going was this believes"
wordList = nltk.word_tokenize(sentence)
stemWords = [snowBallStemmer.stem(word) for word in wordList]

print(' '.join(stemWords))


stemmer2 = SnowballStemmer("english", ignore_stopwords=True)
stemWords = [stemmer2.stem(word) for word in wordList]

print(' '.join(stemWords))

from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
l_words=[lemmatizer.lemmatize(word) for word in wordList]
print(' '.join(l_words))


from nltk.corpus import stopwords
stopwords.words('english')
stopwords=set(stopwords.words('english'))
words=nltk.word_tokenize(sentence)
wordsFiltered=[]
for w in wordList:
    if w not in stopwords:
        wordsFiltered.append(w)
print(wordsFiltered)