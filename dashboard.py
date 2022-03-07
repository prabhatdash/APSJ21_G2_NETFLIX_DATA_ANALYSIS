import textblob as tb
import matplotlib.pyplot as plt
import numpy as np
import functions

def dashboard():
    print("WELCOME TO OUR ANALYSIS")
    print('#'*100)
    print("Enter the 'DIGITS' assigned to the given queries to operate further\n"
          "1.ENTER MOVIE NAME TO FIND IT'S RELEASE DATE   \n"
          "2.ENTER MOVIE NAME TO FIND IT'S COUNTRY OF ORIGIN   \n"
          "3.ENTER MOVIE NAME TO FIND IT'S RATINGS   \n"
          "4.ENTER MOVIE NAME TO FIND IT'S DURATION IN MINUTES   \n"
          "5.GET THE GRAPH OF YEARS 2015-2020 AND THEIR MOVIE RELEASE COUNT   \n"
          "6.GET THE GRAPH OF FAMOUS DIRECTORS AND  THEIR MOVIE RELEASE COUNT   \n"
          "7.GRAPH OF DIFFERENT COUNTRY AND THEIR MOVIE RELEASES COUNT   \n")
    "\n"
    inp=int(input())

    if inp==1:
        functions.movie_name()
    if inp==2:
        functions.movie_country()
    if inp==3:
        functions.movie_ratings()
    if inp==4:
        functions.movie_duration()
    if inp==5:
        functions.yvm_graph()
    if inp==6:
        functions.dvm_graph()
    if inp==7:
        functions.cvm_graph()


dashboard()