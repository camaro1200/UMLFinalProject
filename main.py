from User import UserInitializer
from CordinateStruct import CordinatesStruct
from User import UserStruct
import pandas as pd
from PlanBuilder import PlanBuilder

from firebase import firebase
firebase = firebase.FirebaseApplication("https://hackmoscow-5a42c.firebaseio.com/", None)


user_init = UserInitializer()
user_init.create_user_auto(name="paul", phone="123456", email="paul@gmail.com", password="123")
user_init.create_user_auto(name="u2", phone="2", email="2@gmail.com", password="2")

while True:
    print("Login (1) or Register (2) ")
    key = input()
    if key == "1":
        print("enter name")
        name = input()
        print("enter password")
        passwrd = input()
        #if user_init.verify_user(name="paul", password="123") == 1:
            #user_init.authenciate()
        if user_init.verify_user(name, passwrd) == 1:
            user_init.authenciate()
    if key == "2":
        user_init.create_user()
        user_init.authenciate()
    if key == "3":
        user_init.display_users()
    if key == "4":
        exit()








