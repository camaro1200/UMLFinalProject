from CordinateStruct import CordinatesStruct
from Plan import Plan
import pandas as pd
from firebase import firebase

firebase = firebase.FirebaseApplication("https://hackmoscow-5a42c.firebaseio.com/", None)


def request_category():
    list = []
    #print("____________ # Location during day [1-5] _____________")
    #location_num = input()
    print("____________ # unique Categories [1-5] _____________")
    category_num = int(input())
    print("____________ Pick Categories_____________")
    print("(0) Aquapark")
    print("(1) Botanical Garden")
    print("(2) Cinema")
    print("(3) Cultural Heritage")
    print("(4) Ice Rink")
    print("(5) Library")
    print("(6) Museum")
    print("(7) Recreational Areas")
    print("(8) Theater")
    print("(9) Exhibition Halls")
    list = [input('Enter a value: ') for i in range(category_num)]
    return list, category_num


class PlanBuilder:
    cord = CordinatesStruct
    element_list = [[3,'/Aquapark/', '/ObjectName'], [6,'/BotanicalGarden/', '/FullName'],
                    [9,'/Cinema/', '/CommonName'], [10,'/CulturalHeritage/', '/ObjectNameOnDoc'],
                    [10,'/IceRinks/', '/ObjectName']]

    def display(self, cord):
        print(cord.display_cord)

    def make_plan(self):
        list, category_num = request_category()

        column_names = ["cordinates", "id", "lenght", "name"]
        result_df = pd.DataFrame(columns=column_names)

        for j in range(category_num):
            df = pd.DataFrame(columns=column_names)
            element = int(list[j])
            for i in range(self.element_list[element][0]):
                str1 = self.element_list[element][1]
                str2 = str(i)
                str3 = '/geoData'
                fin_str = str1 + str2 + str3
                # print(fin_str)
                res = firebase.get(fin_str, "")

                str_name = self.element_list[element][2]
                fin_str_name = str1 + str2 + str_name
                name = str(firebase.get(fin_str_name, ""))
                #print(fin_str_name)
                #print("name = ", name)

                #print(res)
                check = res[res.find("=") + 1:res.find(",")]
                #print(check)
                if check == "MultiPoint":
                    fin_res = res[res.find("[") + 2:res.find("]")].split(", ")
                elif check == "Polygon":
                    fin_res = res[res.find("[") + 3:res.find("]")].split(", ")
                elif check == "MultiPolygon":
                    fin_res = res[res.find("[") + 4:res.find("]")].split(", ")
                else:
                    fin_res = res[res.find("[")+1:res.find("]")].split(", ")
                #print(fin_res)
                point = CordinatesStruct(float(fin_res[0]), float(fin_res[1]))
                dist = self.cord.calucate_dist(point)
                df.loc[i] = [point, i, dist, str(name)]
            temp_df = df[df.lenght == df.lenght.min()]
            result_df = result_df.append(temp_df)
            #self.cord = temp_df[temp_df.cordinates]
            #print(temp_df)

        #print(result_df)
        #print(len(result_df))

        p = Plan(result_df)
        p.display_plan()
        p.confirm_plan()
        return result_df
