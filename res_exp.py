
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()


import os


import numpy as np
import tflearn
import tensorflow as tf
import random
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.logging.set_verbosity(tf.logging.ERROR)
import warnings
warnings.filterwarnings("ignore")






# restore all of our data structures
import pickle
data = pickle.load( open( "training_data", "rb" ) )
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']


import json
with open('json/results.json') as json_file:
	intents = json.load(json_file)
	#print ("json data12334445")
	#print (intents)
	
	

net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)


model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
tf.logging.set_verbosity(tf.logging.ERROR)



def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
				
                    pass #print ("found in bag: %s" % w)

    return(np.array(bag))
	
	
	
	
	

model.load('./model.tflearn')




context = {}

ERROR_THRESHOLD = 0.25
def classify(sentence):
		
		results = model.predict([bow(sentence, words)])[0]
		
	
	
		results = [[i,r] for i,r in enumerate(results)if (r>ERROR_THRESHOLD)]
		if(0==len(results)):
			return 0;
		else:
			# sort by strength of probability
			results.sort(key=lambda x: x[1], reverse=True)
			return_list = []
			for r in results:
				return_list.append((classes[r[0]], r[1]))
			# return tuple of intent and probability
			return return_list
	
def response(sentence, userID='123', show_details=False):
    results = classify(sentence)
    if results==0:
        return("i didn't get you, can you be more specific? :)")
        # if we have a classification then find the matching intent tag
    if results:
        # loop as long as there are matches to process
        while results:
            for i in intents['intents']:
                # find a tag matching the first result
                if i['tag'] == results[0][0]:
                    # set context for this intent if necessary
                    if 'context_set' in i:
                        #if show_details: #print ('context:', i['context_set'])
                        context[userID] = i['context_set']

                    # check if this intent is contextual and applies to this user's conversation
                    if not 'context_filter' in i or \
                        (userID in context and 'context_filter' in i and i['context_filter'] == context[userID]):
                        if show_details:
                            pass						#print ('tag:', i['tag'])
                        print (random.choice(i['responses']))
                        return(random.choice(i['responses']))

            results.pop(0)
			
			
			
			
			


	
'''
while(True):
	print("welcome to the credit card help desk,ask your queries here :)")
	ques=input()
	#classify('is your shop open today?')





	response(ques)
	print("do you want to continue ??(y/n)")
	c=input()
	if c=='n':
		break'''

#response("yr,htduydtufy")
