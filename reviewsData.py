
# coding: utf-8

# In[2]:

import re 
import csv
import json
import nltk
import sklearn
import pandas as pd
from pprint import pprint
from bs4 import BeautifulSoup 
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
pd.set_option("display.max_colwidth",-1)

def rescue_code(function):
    import inspect
    get_ipython().set_next_input("".join(inspect.getsourcelines(function)[0]))
    
def tic():
    #Homemade version of matlab tic and toc functions
    import time
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()

def toc():
    import time
    if 'startTime_for_tictoc' in globals():
        print("Elapsed time is " + str(time.time() - startTime_for_tictoc) + " seconds..\n")
    else:
        print("Toc: start time not set...\n")


# In[ ]:

with open('data/drama_love_reviews_100.json') as json_data:
    posReviewsDrama = json.load(json_data)
    
with open('data/drama_love_reviews_100.json') as json_data:
    posReviewsDrama = json.load(json_data)
    
with open('data/drama_hate_reviews_100.json') as json_data:
    negReviewsDrama = json.load(json_data)
    
with open('data/action_love_reviews_100.json') as json_data:
    posReviewsAction = json.load(json_data)
    
with open('data/action_hate_reviews_100.json') as json_data:
    negReviewsAction  = json.load(json_data)
    
with open('data/horror_hate_reviews_100.json') as json_data:
    negReviewsHorror  = json.load(json_data) 
    
with open('data/horror_love_reviews_100.json') as json_data:
    posReviewsHorror  = json.load(json_data) 
    
with open('data/romance_hate_reviews_100.json') as json_data:
    negReviewsRomance  = json.load(json_data)     
    
with open('data/romance_love_reviews_100.json') as json_data:
    posReviewsRomance  = json.load(json_data) 
    
with open('data/Sci-Fi_love_reviews_100.json') as json_data:
    posReviewsSci  = json.load(json_data) 
    
with open('data/Sci-Fi_hate_reviews_100.json') as json_data:
    negReviewsSci  = json.load(json_data) 
posReList = []
for reviewlist in posReviewsDrama + posReviewsHorror + posReviewsAction + posReviewsSci + posReviewsRomance:
    if reviewlist is not None:
        for review in reviewlist:
            posReList.append([review['review'],review['title'],review['categorie']])
            
posReviews = pd.DataFrame(posReList,columns=['reviews','title','sentiment'])
posReviews = posReviews.drop_duplicates()
posReviews["reviews"] = posReviews["reviews"].map(str) + posReviews["title"]
posReviews = posReviews.drop('title',1)

negReList = []
for reviewlist in  negReviewsAction + negReviewsHorror +negReviewsDrama +negReviewsRomance + negReviewsSci:
    if reviewlist is not None:
        for review in reviewlist:
            negReList.append([review['review'],review['title'],review['categorie']])
            
negReviews = pd.DataFrame(negReList,columns=['reviews','title', 'sentiment'])
negReviews = negReviews.drop_duplicates()
negReviews["reviews"] = negReviews["reviews"].map(str) + negReviews["title"]
negReviews = negReviews.drop('title',1)

pos_train, pos_test = train_test_split(posReviews, test_size = 0.3)
neg_train, neg_test = train_test_split(negReviews, test_size = 0.3)

train = pos_train.append(neg_train, ignore_index=True)
test = pos_test.append(neg_test, ignore_index=True)

train = train.reset_index(drop=True)
train['id'] = train.index


test = test.reset_index(drop=True)
test['id'] = test.index

print('train data size:',train.shape,'..\n')
print('test data size:',test.shape,'..\n')

'''
def textPrepocess(movieReviews):
    movieReviews = movieReviews.lower()
    movieReviews = re.sub("[^a-zA-Z]",' ',movieReviews)
    movieReviews = (" ".join(movieReviews.split()))
    return movieReviews

train['reviews'] = train['reviews'].apply(textPrepocess)
test['reviews'] = test['reviews'].apply(textPrepocess)

print('all data has been imported..\n')
'''


# 
# 
# 
# ### Unlabeled dataset for word2vec
# 
# 
# 

# In[6]:

with open('data/Adventure_hate_reviews_100.json') as json_data:
    negReviewsAdv  = json.load(json_data) 
    
with open('data/Adventure_love_reviews_100.json') as json_data:
    posReviewsAdv  = json.load(json_data) 
    
with open('data/Fantasy_hate_reviews_100.json') as json_data:
    negReviewsFan  = json.load(json_data) 
    
with open('data/Fantasy_love_reviews_100.json') as json_data:
    posReviewsFan  = json.load(json_data) 
    
with open('data/Mystery_hate_reviews_100.json') as json_data:
    negReviewsMys = json.load(json_data) 
    
with open('data/Mystery_love_reviews_100.json') as json_data:
    posReviewsMys = json.load(json_data) 
    
with open('data/Comedy_hate_reviews_100.json') as json_data:
    negReviewsCom = json.load(json_data) 
    
with open('data/Comedy_love_reviews_100.json') as json_data:
    posReviewsCom = json.load(json_data) 
    
with open('data/Family_hate_reviews_100.json') as json_data:
    negReviewsFam = json.load(json_data) 
    
with open('data/Family_love_reviews_100.json') as json_data:
    posReviewsFam = json.load(json_data)     

posRe = []
for reviewlist in posReviewsAdv + posReviewsFan + posReviewsCom + posReviewsMys + posReviewsFam:
    if reviewlist is not None:
        for review in reviewlist:
            posRe.append([review['review'],review['title']])
                              #,review['categorie']])
            
pos_Reviews = pd.DataFrame(posRe,columns=['reviews','title'])
                                             #,'sentiment'])
pos_Reviews = pos_Reviews.drop_duplicates()
pos_Reviews["reviews"] = pos_Reviews["reviews"].map(str) + pos_Reviews["title"]
pos_Reviews = pos_Reviews.drop('title',1)

negRe = []
for reviewlist in  negReviewsAdv + negReviewsFan +negReviewsCom +negReviewsMys + negReviewsFam:
    if reviewlist is not None:
        for review in reviewlist:
            negRe.append([review['review'],review['title']])
                              #,review['categorie']])#
            
neg_Reviews = pd.DataFrame(negRe,columns=['reviews','title'])
                                             #'sentiment'])
neg_Reviews = neg_Reviews.drop_duplicates()
neg_Reviews["reviews"] = neg_Reviews["reviews"].map(str) + neg_Reviews["title"]
neg_Reviews = neg_Reviews.drop('title',1)


unlabeled_reviews = pos_Reviews.append(neg_Reviews, ignore_index=True)


unlabeled_reviews = unlabeled_reviews.reset_index(drop=True)
unlabeled_reviews['id'] = unlabeled_reviews.index



print('Unlabeled train data size :',unlabeled_reviews.shape,'..\n')

