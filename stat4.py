# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import stopwords
from collections import defaultdict
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

import os
from nltk.corpus import PlaintextCorpusReader
corpus_root = 'textfiles/'
newcorpus = PlaintextCorpusReader(corpus_root, '.*')
import sys

def main():

    print()
    print("This is a simple text file statistic python script." )
    print("coded for Research Methodology subject." )
    print("Made by Varga Endre FJFAKM, EKE-GTK, Business Informatics." )
    print()

    print("The corpus contains these files " )
    print(newcorpus.fileids())

    print("Select the filename which you want to process with its number:")
    print("the minimum number you can choose is: 1")
    print("the maximum number you can choose is: ",len(newcorpus.fileids()))
    index = int(input('Type a number of your choice: 1 for 1st text, 2 for 2nd, ...'),10)
    index -= 1
    print()
    print()
    print("You selected the following file:",newcorpus.fileids()[index])
    print()

    print("Processing file. It may take a while...")
    print()
    print()
    

    wtokens = newcorpus.words(newcorpus.fileids()[index])

    
    
    
    print("The number of tokens: ",len(wtokens))     # Number of words in text
    wfreq = nltk.FreqDist(wtokens)
    print()
    
    userword = input('Type the word you want to know of its frequency:')
    print()
    print("The frequency of the word '%s' : " %userword,wfreq[userword])
    print("Number of unique words in text",len(wfreq) )     # Number of unique words in text
    print()
    print("Add how many common words you want to list! ")
    usernumber = int(input("Type only number!"),10)
    print("The %d most common words: " %usernumber,wfreq.most_common(usernumber))

    print()
    sentcount = wfreq['.'] + wfreq['?'] + wfreq['!']  # Assuming every sentence ends with ., ! or ?
    print("The number of sentences: ",sentcount)
    print("Average sentence length in number of words: ",len(wtokens)/sentcount )    # Average sentence length in number of words
    
    print()
    print("Add the minimum length of words you want to list!")
    usernumber = int(input("Type only number!"),10)
    print("The minimum %d character long words: " % usernumber)
    [w for w in wfreq if len(w) >= usernumber]       # all long character words
    long = [w for w in wfreq if len(w) >= usernumber] 
    for w in long :
        print(w +" Length: %d" %len(w) +" Count: %d " %wfreq[w])  
    


if __name__ == "__main__":
    main()
    
    
    
#internet sources used for this program:
#https://www.learnpython.org/en/Variables_and_Types
#https://www.w3schools.com/python/python_file_open.asp
#https://stackoverflow.com/questions/20449427/how-can-i-read-inputs-as-numbers
#https://ncona.com/2012/02/python-lesson-getting-user-input-through-the-console-bonus-handling-an-exception/
#http://www.pitt.edu/~naraehan/presentation/Text_Processing_Workshop.html
#https://stackoverflow.com/questions/4951751/creating-a-new-corpus-with-nltk#
#https://www.nltk.org/book/
#http://users.itk.ppke.hu/~sikbo/nltk/index.php