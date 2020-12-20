from CordinateStruct import CordinatesStruct
from PlanBuilder import PlanBuilder

user_list = []

class UserStruct:
    def __init__(self, name, phone, email, password):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password


class UserInitializer:

    def verify_user(self, name, password):
        for user in user_list:
            if user.name == name and user.password == password:
                print("success")
                return 1
        print("failure")
        return 0

    def display_users(self):
        for user in range(user_list):
            print(user)

    def create_user(self):
        print("enter your name")
        name = input()
        print("enter your phone")
        phone = input()
        print("enter your email")
        email = input()
        print("enter your password")
        password = input()
        new_user = UserStruct(name, phone, email, password)
        user_list.append(new_user)

    def create_user_auto(self, name, phone, email, password):
        new_user = UserStruct(name, phone, email, password)
        user_list.append(new_user)
        return user_list

    def authenciate(self):
        var1, var2 = [float(x) for x in input("Enter location cord here: ").split()]
        v = CordinatesStruct(var1, var2)
        #v = CordinatesStruct(0, 0)
        p = PlanBuilder()
        p.cord = v
        p.make_plan()
        #print(v.display_cord())
        return 1




