# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import codecs
#f = codecs.open("Church of the Annunciation.html", 'r', 'utf-8')
#print(f.read());
#s=f.read();

from textblob.classifiers import NaiveBayesClassifier
import requests
import numpy as np
from bs4 import BeautifulSoup
import csv

#i=10340;
i=12248;
s=i;
f=13249;
data=[];
out=[];
#while i<14668:
while i<s+1000:
    #project="https://abstracts.societyforscience.org/Home/FullAbstract?ISEFYears=0%2C&Category=Any%20Category&AllAbstracts=True&FairCountry=Any%20Country&FairState=Any%20State&ProjectId="+str(i)+"";
    project="https://abstracts.societyforscience.org/Home/FullAbstract?ISEFYears=0%2C&Category=Any%20Category&AllAbstracts=True&FairCountry=Any%20Country&FairState=Any%20State&ProjectId="+str(i)+"";
    page = requests.get(project)
    soup = BeautifulSoup(page.content, "lxml")
    mydivs = soup.findAll("div", {"class": "col-sm-12"})
    mydivs=soup.findAll("p")
    print(i)
#1,2,3,4,5
    w=0;
    for x in range(1,9):
        
        if(x<len(mydivs)):
            if(x==1):
                data.append([]);
                out.append([])
            if((str(mydivs[x]).find("Science Service")<0 and str(mydivs[x]).find("background-color: lightblue")<0)):
                data[i-s].append(mydivs[x]);
            if(str(mydivs[x]).find("Awards Won:")>-1):
                data[i-s].append("win");
                out[len(out)-1].append("win");
                out[len(out)-1].append(mydivs[x]);
                w=1;
        else:
            if(w==0):
                data[i-s].append("lose");
                #data[i-10340][x-1]=mydivs[x];
        #print(data[i-s])
    i=i+1;
data2=[];
k=10668;

#print(len(data[2]))  
#print(data) 


#print(st[st.index("br")+4:-4])



train=[];
#print(len(data[0]))
#print(data[0][0])
#print(mydivs[0])
for x in range(0,int(len(data)/2)):
    train.append([]);
    train[x].append(str(data[x][len(data[x])-2]));
    train[x].append(str(data[x][len(data[x])-1]));
    #print(train[x])
    if(train[x]==[]):
        train.pop(x);
test=[];
for x in range(int(len(data)/2),len(data)-1):
    test.append([]);
    test[x-int(len(data)/2)].append(str(data[x-int(len(data)/2)][len(data[x-int(len(data)/2)])-2]));

    if(test[x-int(len(data)/2)]==[]):
        test.pop(x);
#myFile = open('data.csv', 'w')
#with myFile:
 #   writer = csv.writer(myFile)
 #   writer.writerows(train)


cl = NaiveBayesClassifier(train)
count=0;
z=0;
for x in range(0,len(test)):
    predicted=cl.classify(str(data[x][len(data[x])-2]));
    real=str(data[x][len(data[x])-1])
    print("real: "+real+" Pred: "+predicted)
    if(real==predicted):
        count=count+1;
    z=z+1;
    #print(str(out[x])+" "+str(x+i))
    #if(x<len(data)):
        #print(str(data[x]))
    print()

#rint(str(data[x][len(data[x])-2]));
#cl.accuracy(test)
print(count/z)
cl.show_informative_features(5);