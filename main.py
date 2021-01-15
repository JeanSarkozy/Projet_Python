# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 00:21:15 2020

@author: Chloé et Pierre
"""
    
# import des librairies
import praw
import datetime as dt
import urllib.request
import xmltodict   
from classe import *
import pandas 
from PIL import Image
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt



#-------Création du Corpus 

corpus = Corpus("Corona")


reddit = praw.Reddit(client_id='0AlqCfHuOc5Hkg', client_secret='80PspjYMdTvF91ti9qZeWzAS2BU', user_agent='Reddit Irambique')
hot_posts = reddit.subreddit('Coronavirus').hot(limit=500)
for post in hot_posts:
    datet = dt.datetime.fromtimestamp(post.created)
    txt = post.title + ". "+ post.selftext
    
    doc = RedditDocument(datet,
                   post.title,
                   post.author_fullname,
                   txt,
                   post.url,0)
    
    corpus.add_doc(doc)

url = 'http://export.arxiv.org/api/query?search_query=all:covid&start=0&max_results=500'
data =  urllib.request.urlopen(url).read().decode()
docs = xmltodict.parse(data)['feed']['entry']



for i in docs:
    datet = dt.datetime.strptime(i['published'], '%Y-%m-%dT%H:%M:%SZ')
    try:
        author = [aut['name'] for aut in i['author']][0]
    except:
        author = i['author']['name']
    txt = i['title']+ ". " + i['summary']   
    doc = ArxivDocument(datet,
                   i['title'],
                   author,
                   txt,
                   i['id'],0
                   )
    
    corpus.add_doc(doc)

print("Création du corpus, %d documents et %d auteurs" % (corpus.ndoc,corpus.naut))

print()

print("Corpus trié par titre (4 premiers)")
res1 = corpus.sort_title(4)
print(res1)
    
print()

print("Corpus trié par date (4 premiers)")
res = corpus.sort_date(4)
print(res)

print()

print("Enregistrement du corpus sur le disque...")
corpus.save("Corona.crp")


#------ traitement et creation du corpus commun ainsi que des corpus Reddit & Arxiv
ch = ""
ch_reddit = ""
ch_arxiv = ""


for  i in range (corpus.ndoc) :    
    doc = corpus.get_doc(i)
    ch += doc.get_text()
    if doc.getType() == "reddit" : 
        ch_reddit += doc.get_text()
    else :
        ch_arxiv += doc.get_text()


#-------Nettoyage des données 
ch = nettoyer_texte(ch)
ch_reddit = nettoyer_texte(ch_reddit)
ch_arxiv = nettoyer_texte(ch_arxiv)

stopword = ["i", "me", "my", "myself", "we", "our", 
            "ours", "ourselves", "you", "your", "yours"
            , "yourself", "yourselves", "he", "him", 
            "his", "himself", "she", "her", "hers", 
            "herself", "it", "its", "itself", "they", 
            "them", "their", "theirs", "themselves", 
            "what", "which", "who", "whom", "this", "that", "these", 
            "those", "am", "is", "are", "was", "were", "be", "been", 
            "being", "have", "has", "had", "having", "do", "does", 
            "did", "doing", "a", "an", "the", "and", "but", "if", 
            "or", "because", "as", "until", "while", "of", "at", "by", 
            "for", "with", "about", "against", "between", "into", "through", 
            "during", "before", "after", "above", "below", "to", "from", "up", 
            "down", "in", "out", "on", "off", "over", "under", "again", "further", 
            "then", "once", "here", "there", "when", "where", "why", "how", "all", 
            "any", "both", "each", "few", "more", "most", "other", "some", "such", 
            "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", 
            "s", "t", "can", "will", "just", "don", "should", "now","u","may","also","us","ai","e"]

chaine = []
chaine = ch.split(" ")


filtered_sentence = [w for w in chaine if w not in stopword]

ch = (" ").join(filtered_sentence)




wordlist = []

wordlist = ch.split(" ")

while "" in wordlist:
    wordlist.remove("")
    

vocabulaire = set(wordlist) 

#-------Création du data frame
data_mot = pandas.DataFrame(columns=['vocab','occurrence','frequence'])

i = 0
for word in vocabulaire : 
    data_mot.loc[i,'vocab'] = word    
    wordlist.count(word)
    data_mot.loc[i,'occurrence'] = wordlist.count(word)
    data_mot.loc[i,'frequence'] = wordlist.count(word)/len(wordlist)
    i += 1

data_mot = data_mot.sort_values(by = 'frequence',ascending = False)


#-------Recupération des dates des articles
ch2=[]
mots_utiles=["vaccine","pandemic","patients","pneumonia","deaths"]
evolution_mot = pandas.DataFrame(columns=["mot clé","date"])
            
compt=0
for i in range(corpus.ndoc):
    doc2 = corpus.get_doc(i)
    article = ""
    article = doc2.get_text()
    for j in mots_utiles : 
        if j in article:
            evolution_mot.loc[compt,'mot clé'] = j
            evolution_mot.loc[compt,'date']=doc2.get_date()
            compt+=1


evolution_mot = evolution_mot.sort_values(by = ['mot clé','date'],ascending = True)
evolution_mot_vaccine=evolution_mot.loc[evolution_mot['mot clé']=='vaccine',:]
evolution_mot_pandemic=evolution_mot.loc[evolution_mot['mot clé']=='pandemic',:]
evolution_mot_patients=evolution_mot.loc[evolution_mot['mot clé']=='patients',:]
evolution_mot_pneumonia=evolution_mot.loc[evolution_mot['mot clé']=='pneumonia',:]
evolution_mot_deaths=evolution_mot.loc[evolution_mot['mot clé']=='deaths',:]

grp1 = evolution_mot_vaccine.groupby(pandas.Grouper(key='date',freq='M')).count()
grp2 = evolution_mot_deaths.groupby(pandas.Grouper(key='date',freq='M')).count()
grp3 = evolution_mot_patients.groupby(pandas.Grouper(key='date',freq='M')).count()
grp4 = evolution_mot_pneumonia.groupby(pandas.Grouper(key='date',freq='M')).count()
grp5 = evolution_mot_deaths.groupby(pandas.Grouper(key='date',freq='M')).count()

grp1.loc[:,"mois"] = ['Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre','Janvier']
grp2.loc[:,"mois"] = ['Décembre','Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre','Janvier']
grp3.loc[:,"mois"] = ['Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre','Janvier']
grp4.loc[:,"mois"] = ['Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']
grp5.loc[:,"mois"] = ['Décembre','Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre','Janvier']

"""
histogramme(grp1)
histogramme(grp2)
histogramme(grp3)
histogramme(grp4)
histogramme(grp5)
"""
          
#--------Creation nuage de mots 
nuage_mots(ch)
nuage_mots(ch_reddit)
nuage_mots(ch_arxiv)

