
# coding: utf-8

# In[10]:

import re 
import csv
import json
import nltk
import sklearn
import pandas as pd
from pprint import pprint
from bs4 import BeautifulSoup 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
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
        
        
with open('drama_love_reviews_100.json') as json_data:
    posReviewsDrama = json.load(json_data)
    
with open('drama_hate_reviews_100.json') as json_data:
    negReviewsDrama = json.load(json_data)
    
with open('action_love_reviews_100.json') as json_data:
    posReviewsAction = json.load(json_data)
    
with open('action_hate_reviews_100.json') as json_data:
    negReviewsAction  = json.load(json_data)
    
with open('horror_hate_reviews_100.json') as json_data:
    negReviewsHorror  = json.load(json_data) 
    
with open('horror_love_reviews_100.json') as json_data:
    posReviewsHorror  = json.load(json_data) 
    
with open('romance_hate_reviews_100.json') as json_data:
    negReviewsRomance  = json.load(json_data)     
    
with open('romance_love_reviews_100.json') as json_data:
    posReviewsRomance  = json.load(json_data) 
    
with open('Sci-Fi_love_reviews_100.json') as json_data:
    posReviewsSci  = json.load(json_data) 
    
with open('Sci-Fi_hate_reviews_100.json') as json_data:
    negReviewsSci  = json.load(json_data) 


#     
# '''
# posReList = []
# for reviewlist in posReviewsDrama + posReviewsHorror + posReviewsAction + posReviewsSci + posReviewsRomance:
#     if reviewlist is not None:
#         for review in reviewlist:
#             posReList.append([review['review'],review['categorie']])
#             
# posReviews = pd.DataFrame(posReList,columns=['reviews', 'sentiment'])
# posReviews = posReviews.drop_duplicates()
# 
# negReList = []
# for reviewlist in  negReviewsAction + negReviewsHorror +negReviewsDrama +negReviewsRomance + negReviewsSci:
#     if reviewlist is not None:
#         for review in reviewlist:
#             negReList.append([review['review'],review['categorie']])
#             
# negReviews = pd.DataFrame(negReList,columns=['reviews', 'sentiment'])
# negReviews = negReviews.drop_duplicates()
# 
# pos_train, pos_test = train_test_split(posReviews, test_size = 0.3)
# neg_train, neg_test = train_test_split(negReviews, test_size = 0.3)
# 
# train = pos_train.append(neg_train, ignore_index=True)
# test = pos_test.append(neg_test, ignore_index=True)
# 
# train = train.reset_index(drop=True)
# train['id'] = train.index
# 
# 
# test = test.reset_index(drop=True)
# test['id'] = test.index
# 
# print('train data size..',train.shape,'..\n')
# print('test data size..',test.shape,'..\n')
# 
# 
# def textPrepocess(movieReviews):
#     movieReviews = movieReviews.lower()
#     movieReviews = re.sub("[^a-zA-Z]",' ',movieReviews)
#     movieReviews = (" ".join(movieReviews.split()))
#     return movieReviews
# 
# train['reviews'] = train['reviews'].apply(textPrepocess)
# test['reviews'] = test['reviews'].apply(textPrepocess)
# 
# print('all data has been imported..\n')
# 
# '''

# ### add titles

# posTitlesList = []
# for reviewlist in posReviewsDrama + posReviewsHorror + posReviewsAction + posReviewsSci + posReviewsRomance:
#     if reviewlist is not None:
#         for review in reviewlist:
#             posTitlesList.append([review['title'],review['categorie']])
#             
# posTitles = pd.DataFrame(posTitlesList,columns=['reviews', 'sentiment'])
# posTitles = posTitles.drop_duplicates()
# 
# negTitlesList = []
# for reviewlist in  negReviewsAction + negReviewsHorror +negReviewsDrama +negReviewsRomance + negReviewsSci:
#     if reviewlist is not None:
#         for review in reviewlist:
#             negTitlesList.append([review['title'],review['categorie']])
#             
#             
# negTitles = pd.DataFrame(negTitlesList,columns=['reviews', 'sentiment'])
# negTitles = negTitles.drop_duplicates()
# pos_review_title = posTitles.append(posReviews, ignore_index=True)
# neg_review_title = negTitles.append(negReviews, ignore_index=True)
# 
# pos_train_title, pos_test_title = train_test_split(pos_review_title, test_size = 0.3)
# neg_train_title, neg_test_title = train_test_split(neg_review_title, test_size = 0.3)
# 
# train_title = pos_train_title.append(neg_train_title, ignore_index=True)
# test_title = pos_test_title.append(neg_test_title, ignore_index=True)
# 
# train_title = train_title.reset_index(drop=True)
# train_title['id'] = train_title.index
# 
# 
# test_title = test_title.reset_index(drop=True)
# test_title['id'] = test_title.index
# 
# print('train with titles data size..',train_title.shape,'..\n')
# print('test with titles data size..',test_title.shape,'..\n')
# 
# 
# train_title['reviews'] = train_title['reviews'].apply(textPrepocess)
# test_title['reviews'] = test_title['reviews'].apply(textPrepocess)
# 
# print('all data with titles has been imported..\n')

# In[11]:

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

print('train data size..',train.shape,'..\n')
print('test data size..',test.shape,'..\n')


def textPrepocess(movieReviews):
    movieReviews = movieReviews.lower()
    movieReviews = re.sub("[^a-zA-Z]",' ',movieReviews)
    movieReviews = (" ".join(movieReviews.split()))
    return movieReviews

train['reviews'] = train['reviews'].apply(textPrepocess)
test['reviews'] = test['reviews'].apply(textPrepocess)

print('all data has been imported..\n')

