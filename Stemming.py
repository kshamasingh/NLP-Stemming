#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 23:09:45 2021

@author: kshama.singh
"""

import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

paragraph = open("../Stemming/Stemming.txt", 'r').read()
#print(paragraph)

# Preparing the sentences
def processData_SentencesTokenize(paragraph):
    sentences = nltk.sent_tokenize(paragraph)
    return sentences


# Preparing the words
def processData_WordTokenize(paragraph):
    words = nltk.word_tokenize(paragraph)
    return words

# Preparing the dataset
def processData_dataset(sentences, words, stemmer):
    for i in range(len(sentences)):
        word = nltk.word_tokenize(sentences[i])
        word = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
        sentences[i] = ' '.join(words)
    return sentences

sentences = processData_SentencesTokenize(paragraph);

words = processData_WordTokenize(paragraph);

stemmer = PorterStemmer()

dataset = processData_dataset(sentences, words, stemmer);

#print(dataset)