import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
df=pd.read_csv("dataset.csv",engine="python")


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
movie_ratings()

def movie_duration():
    d=str(input("ENTER MOVIE NAME TO FIND IT'S DURATION IN MINUTES"))
    details=df[df['title']==d]
    for i in details['duration(min)']:
        print(i,'min')

def tfs_graph():
    list = df['Price'] * df['Qty']
    df['FPrice'] = list
    # 1
    prod_sales = pd.DataFrame(df.groupby('Item_Name').sum()['FPrice'])
    # Top 5 sales ie By Price
    prod_sales.sort_values(by=['FPrice'], inplace=True, ascending=False)
    top_prods = prod_sales.head(5)
    l1 = []
    l2 = []
    for i in top_prods.iterrows():
        l1.append(i[0])
        l2.append(i[1][0])
    plt.bar(l1, l2, width=0.5)
    plt.ylabel('Price', size=10, color='g')
    plt.xlabel('Item Name', size=10, color='b')
    plt.title('Graph of Top five products per price ', size=15, color='r')
    plt.show()
