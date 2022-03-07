import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
df=pd.read_csv("dataset.csv",engine="python")

years=df['country'].value_counts()



def movie_name():
    a=str(input("ENTER MOVIE NAME TO FIND IT'S RELEASE DATE"))
    details=df[df['title']==a]
    for i in details['release date']:
        print(i)



def movie_country():
    b=str(input("ENTER MOVIE NAME TO FIND IT'S COUNTRY OF ORIGIN"))
    details=df[df['title']==b]
    for i in details['country']:
        print(i)

def movie_ratings():
    c=str(input("ENTER MOVIE NAME TO FIND IT'S RATINGS"))
    details=df[df['title']==c]
    for i in details['ratings']:
        print(i)


def movie_duration():
    d=str(input("ENTER MOVIE NAME TO FIND IT'S DURATION IN MINUTES"))
    details=df[df['title']==d]
    for i in details['duration(min)']:
        print(i,'min')

def yvm_graph():
    ndy=['2015','2016','2017','2018','2019','2020']
    ndc=[54,84,97,107,97,82]
    plt.bar(ndy, ndc, width=0.4,color='b')
    plt.ylabel('MOVIES COUNT', size=10, color='r')
    plt.xlabel('RELEASE YEAR', size=10, color='r')
    plt.title('GRAPH OF YEARS AND  THEIR MOVIE RELEASE COUNT ', size=15, color='r')
    plt.show()

def dvm_graph():
    ndd=['Jay Karas','S.S. Rajamouli','Detlev Buck','Rajkumar Santoshi','Michael Bay']
    ndm=[7,7,4,3,3]
    plt.figure(figsize=(12, 7))
    plt.bar(ndd, ndm, width=0.4,color='y')
    plt.ylabel('MOVIES COUNT', size=10, color='k')
    plt.xlabel('DIRECTORS', size=10, color='k')
    plt.title('GRAPH OF DIRECTORS AND  THEIR MOVIE RELEASE COUNT ', size=15, color='r')
    plt.show()

def cvm_graph():
    cn=['INDIA','U.S','U.K','CANADA','EGYPT']
    cnc=[114,273,29,19,14]
    plt.bar(cn, cnc, width=0.4,color='m')
    plt.ylabel('MOVIES COUNT', size=10, color='g')
    plt.xlabel('COUNTRY', size=10, color='g')
    plt.title('GRAPH OF COUNTRY AND THEIR MOVIE RELEASES COUNT ', size=15, color='r')
    plt.show()

