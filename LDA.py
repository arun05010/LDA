import gensim
from nltk.corpus import reuters
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import matplotlib.pyplot as plt

# Tokenize when it finds any non word character like space; but can split don't to 'don' and 't'
tokenizer = RegexpTokenizer(r'\w+')  # create English stop words list

en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

# List of documents
documents = reuters.fileids()
print(str(len(documents)) + " documents");

# List of categories
categories = reuters.categories();
print(str(len(categories)) + " categories");

# Documents in a category
category_docs = reuters.fileids("acq");

# Retrieving content of the documents.
document_words = reuters.words(category_docs[0]);
print(reuters.raw(category_docs[0]));
print(document_words);

# Instantiating list of list
the_tokens = []

# Converting letters to lower case
# Tokenizing the sentences
# Removing stopping words
# Stemming the words and storing it in list of lists "the_tokens" for item in category_docs:
doc = reuters.raw(item)
raw = doc.lower()
tokens = tokenizer.tokenize(raw)
stopped_tokens = [i for i in tokens if not i in en_stop]
texts = [p_stemmer.stem(i) for i in stopped_tokens]
print number
print texts

# Creating dictionary of words
dictionary = corpora.Dictionary(the_tokens)
print dictionary

# Creating corpus with documents to bag of words function
corpus = [dictionary.doc2bow(text) for text in the_tokens]
print corpus

# Performing LDA
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=12, id2word=dictionary, passes=20)
print(ldamodel.print_topics(num_topics=12, num_words=3))
flag_list = []
for i in corpus:
    flag_list.append(len(ldamodel[i]))

plt.hist(flag_list, histtype='bar')
plt.title("Reuters")
plt.xlabel("Number of topics")
plt.ylabel("Number of documents")
plt.show()