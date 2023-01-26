import random
import json
import pickle 
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

import tensorflow 
from tensorflow import keras
from keras.models import Model
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Activation
from keras.layers import Dropout
from keras.optimizers import SGD

lemmatizer = WordNetLemmatizer

intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.tokenize(pattern)
        words.append(word_list)
        documents.append((word_list), intent['tag'])
        if intent['tag'] not in classes:
            classes.append(intent['tag'])