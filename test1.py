#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk
import re
from poids import *
from data import *
f=open("offre1.txt","r")
ch_offer=f.read()

def langues(ch_offer):
    lang=[]
    to=ch_offer.split()
    for l1 in l_langues:
        for l2 in to:
            if (l2.find(l1[1:len(l1)])!=-1):
                lang.append(l1)
    return lang
def langages(ch_offer):
    plang=[]
    to=ch_offer.split()
    for l1 in l_langages:
        for l2 in to:
            if (l1.lower()==l2.lower()):
                plang.append(l1)
                break
    return plang     
def logiciels(ch_offer):
    log=[]
    to=ch_offer.split()
    for l1 in l_logiciels:
        for l2 in to:
            if (l2.lower()==l1.lower()):
                log.append(l1)
                break
    return log

def connaissances(ch_offer):
    conn=[]
    to=ch_offer.split()
    for l1 in l_connaissances:
        if(ch_offer.find(l1)!=-1):
                conn.append(l1)
    
    print(conn)
    return conn
lo=logiciels(ch_offer)
print (lo)