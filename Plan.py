import pandas as pd
from CordinateStruct import CordinatesStruct

class Plan:
    def __init__(self, df, ):
        self.df = df

    def display_plan(self):
        print("--------Attraction List -------")
        print(self.df["name"])
        print("-------------------------------")
        df_num = len(self.df)


    def confirm_plan(self):
        print("Are you happy with this plan? (1) --> Yes / (0) --> No")
        key = int(input())
        if (key == 1):
            print("Thank you for choosing Moskva Pass")
            exit()
        else:
            self.cancel_plan()

    def cancel_plan(self):
        print("We are sorry")
        exit()


