# -*- coding: utf-8 -*-

import nltk
import os
import sys

from nltk.corpus import PlaintextCorpusReader
corpus_root = 'textfiles/'
newcorpus = PlaintextCorpusReader(corpus_root, '.*')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import defaultdict

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
stop_words = set(stopwords.words('english'))
import string


def main():

    print()
    print("This is a simple text file statistic python script." )
    print("coded for Research Methodology subject." )
    print("Made by Varga Endre FJFAKM, EKE-GTK, Business Informatics." )
    print("Github: https://github.com/vargaendre84/stat4")
    print()

    print("The corpus contains these files " )
    print(newcorpus.fileids())

    print("Select the filename which you want to process with its number:")
    print("the minimum number you can choose is: 1")
    print("the maximum number you can choose is: ",len(newcorpus.fileids()))
    
    while True:
      try:
        index = int(input('Type a number of your choice: [1 for 1st text, 2 for 2nd, ...]: '),10)
      except ValueError:
        print("Wrong input")
        continue
      if index < 0 or index > len(newcorpus.fileids())+1 : print("Wrong input")
      else: break
    
    index -= 1
    print()
    print()
    print("You selected the following file:",newcorpus.fileids()[index])
    print()

    print("Processing file. It may take a while...")
    print()
    print()
    
    wtokens = newcorpus.words(newcorpus.fileids()[index]) 
    filteredtokens = [word for word in wtokens if word.isalpha()]
    
    statwords = []  
    for w in filteredtokens:
      if w not in stop_words : statwords.append(w)  
          
        
    print("The number of Tokens: ",len(wtokens))  
    print("The number of Filtered Tokens (Without punctuation): ",len(filteredtokens))  
    print("The number of words (without stopwords): ",len(statwords))    
       
    wfreq = nltk.FreqDist(statwords)
    print()   
    userword = input('Type the word you want to know of its frequency:')
    print()
    print("The frequency of the word '%s' : " %userword,wfreq[userword])
    print("Number of unique words in text",len(wfreq) )    
    print()
    
    while True:
      try:
        usernumber = int(input('Add how many common words you want to list! '),10)
      except ValueError:
        print("Wrong input")
        continue
      else: break
    
    print("The %d most common words: " %usernumber,wfreq.most_common(usernumber))

    print()
    wfreq2 = nltk.FreqDist(wtokens)
    sentcount = wfreq2['.'] + wfreq2['?'] + wfreq2['!']
    print("The number of sentences: ",sentcount)
    print("Average sentence length in number of words: ",len(wtokens)/sentcount)    
    
    print()

    while True:
      try:
        usernumber = int(input('Add the minimum length of words you want to list! '),10)
      except ValueError:
        print("Wrong input")
        continue
      else: break
    
    print("The minimum %d character long words: " % usernumber)
    [w for w in wfreq if len(w) >= usernumber]       
    long = [w for w in wfreq if len(w) >= usernumber] 
    for w in long :
        print(w +" Length: %d" %len(w) +" Count: %d " %wfreq[w])  
    


if __name__ == "__main__":
    main()
    
    