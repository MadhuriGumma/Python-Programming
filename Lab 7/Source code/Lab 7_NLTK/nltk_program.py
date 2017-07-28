#import modules
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag

#Read file
my_file=open("my_data")
s=my_file.read()

#Remove all meaningless words
removableWords = set(stopwords.words('english'))
words_split = word_tokenize(s)
usefulWords = [w for w in words_split if not w in removableWords]
for w in words_split:
    if w not in removableWords:
        usefulWords.append(w)
print("Tokenized:")
print ("*****************************")
print(words_split)
print("Removing articles like a,the,an:")
print ("**********************************")
print(usefulWords)

#lemmetization
list_values1=[]
for i in usefulWords:
    lemmatizer = WordNetLemmatizer()
    l=lemmatizer.lemmatize(i,pos='v')
    list_values1.append(l)
print("lemmatized words:")
print ("****************************")
print(list_values1)


#Using POS, remove all the verbs
o=pos_tag(usefulWords)
print("POS tagging:")
print ("*******************")
print(o)
list_values2=[]
list_values3=[]
for (m,n) in o:
    if (n != 'VB') and (n != 'VBD') and (n != 'VBG') and (n != 'VBN') and (n != 'VBP') and (n != 'VBZ') and (n != ',') and (n != '.'):
        list_values2.append(m)
print("removing verbs:")
print ("***********************")
print(list_values2)

#Calculate the word frequency of the remaining words
import collections
counter=collections.Counter(list_values2)
print("count of words:")
print ("***********************")
print(counter)

#Summary consisting of sentences with most repeated words.
print("Summary:")
print ("***********************")
for l in open("my_data"):
    if (("clumsy" in l) or ("deduction" in l) or ("process" in l) or ("careless" in l) or ("lately" in l)):
        print(l)