import mysql.connector as db
import smtplib
import random
mydb=db.connect(host="localhost",passwd="root",user="root",database="netflix_data_analysis")
mycursor=mydb.cursor()


def user_auth():
   count=None
   email = input("Enter your email to login")
   fetch_query = "select * from reg_users;"
   mycursor.execute(fetch_query)
   for i in mycursor:
       if i[2] == email:
           print("Login Successful !")
           import dashboard
           count = 1
           break
   if count == 0:
       print("Login Error !")
print("#"*88)
print("******************* Enter 1 to LOGIN or 2 to REGISTER for new users *******************")
print("#"*88)
inp=int(input())
count=0
if inp==1:
   user_auth()
elif inp==2:
   name = input("ENTER YOUR NAME: ")
   email = input("ENTER YOUR EMAIL: ")
   otp = str(random.randint(100000,1000000))
   SUBJECT = "OTP for Login"
   TEXT = "HEY "+name+'!'"\r\n""\r\n"'Your OTP for login is: ' + otp+ "\r\n""\r\n"'Please enter the otp for further verification'"\r\n""\r\n"'Thank you !'
   s = smtplib.SMTP('smtp.gmail.com', 587)
   s.starttls()
   s.login('group2@apsjorhat.org', 'apsj#12345678')
   message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
   s.sendmail('group2@apsjorhat.org', email, message)
   s.quit()
   print("An OTP was sent to the entered email address")
   answer=int(input("Please enter the otp for verification"))
   if answer == int(otp) :
       query = "insert into reg_users (name,email) values (" + "'" + name + "'"+"," + "'" + email + "'" + ");"
       mycursor.execute(query)
       mydb.commit()
       print("You have been successfully registered. Now please follow the instructions to successfully Login ")
       user_auth()
   else:
       print('Login failed. Please Try Again')

