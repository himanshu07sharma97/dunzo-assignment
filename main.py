import requests
import time
import json
import display
import outlet
import beverage
from coffeeMachine import coffeeMachine
 
def main():
    preparationTime =1
    ingred_threshold = 250
    
    #input from API
    inputData = requests.get("https://api.npoint.io/e8cd5a9bbd1331de326a").json()

    #input for TestCases
    '''
    inputData = dict({
            "machine": {
                "outlets": {
                "count_n": 3
                },
                "total_items_quantity": {
                "hot_water": 500,
                "hot_milk": 500,
                "ginger_syrup": 100,
                "sugar_syrup": 100,
                "tea_leaves_syrup": 100
                },
                "beverages": {
                "hot_tea": {
                    "hot_water": 200,
                    "hot_milk": 100,
                    "ginger_syrup": 10,
                    "sugar_syrup": 10,
                    "tea_leaves_syrup": 30
                },
                "hot_coffee": {
                    "hot_water": 100,
                    "ginger_syrup": 30,
                    "hot_milk": 400,
                    "sugar_syrup": 50,
                    "tea_leaves_syrup": 30
                },
                "black_tea": {
                    "hot_water": 300,
                    "ginger_syrup": 30,
                    "sugar_syrup": 50,
                    "tea_leaves_syrup": 30
                },
                "green_tea": {
                    "hot_water": 100,
                    "ginger_syrup": 30,
                    "sugar_syrup": 50,
                    "green_mixture": 30
                }
                }
            }
            })
        '''
    #Gettting Inputs from User
    outletN = inputData["machine"]["outlets"]["count_n"]
    beverageNames = list((inputData["machine"]["beverages"]).keys()) 
    ingredients = inputData["machine"]["total_items_quantity"]

    beverageMap ={}

    for beverageName in beverageNames:
        bevIngredients = inputData["machine"]["beverages"][beverageName]
        
        #preparing bevarage for the new child bevarage class
        def prep(self):
            time.sleep(preparationTime)
            
        #Constructor for the new child bevarage class
        def bev_init(self,bevName,bevReceipe,preparationTime):
            self.beverageName = bevName
            self.ingredientList = bevReceipe
            self.preparationTime = preparationTime

        #create a new child class for the specific bevarage
        bev = type(beverageName, (), 
              {"beverageName":beverageName,
              "__init__": bev_init,
               "prepBeverage": prep})
        product = bev(beverageName,bevIngredients,preparationTime)

        #mapping beverage with its object
        beverageMap[beverageName] = product
    
    #Create coffeee Machine object 
    machine = coffeeMachine(beverageMap,outletN,ingredients,ingred_threshold)
    for beverageName in beverageNames:
        machine.makeBeverage(beverageName) # requesting for beverages

    machine.makeBeverage("choleBathure") # case for Invalid item
    machine.makeBeverage(beverageName) #case for unavailable ingredients
    #add ingredients
    machine.addIngredient('hot_water',200)   #case for addding ingredient
    machine.addIngredient('sugar_syrup',100)
    #after adding Ingredients try to make again
    machine.makeBeverage(beverageName)

    

if __name__=="__main__":
    main()
