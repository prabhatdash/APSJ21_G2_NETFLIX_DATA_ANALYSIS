import mysql.connector as mc
dbc = mc.connect(host="localhost",user="root",passwd="root",database="netflix_data_analysis")
cursor=dbc.cursor()



