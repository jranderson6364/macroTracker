import csv
import re

class Food():
    def __init__(self,name,s,k,c,p,f) -> None:
        self.name = name
        self.size = s
        self.kcal = k
        self.carbs = c
        self.protein = p
        self.fat = f


    def logFood(self,date,size) -> None:
        #if size := r"(n)*(s/g/oz)":
        pass

        

def main():
    foodList = pullFoods()
    logFood(foodList)

def logFood(foodList):
    date = input("Date: ")
    name = input("Food").lower().strip()
    size = input("Size")
    for food in foodList:
        if food.name == name:
            food.logFood(date,size)


#def addFood():
    

    



def pullFoods():
    foodsList = []
    with open('foods.csv',"r") as file:
        data = list(csv.reader(file))
        for row in data[1:]:
            try:
                name,size,kcal,carb,protein,fat   = row
                food = Food(name,size,kcal,carb,protein,fat)
                foodsList.append(food)
            except IndexError:
                print("Error with",row[0])
                pass
        
    return foodsList

#def macroTotals():




if __name__ == "__main__":
    main()