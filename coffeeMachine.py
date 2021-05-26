from display import display
from outlet import outlet

class coffeeMachine:
    noOfOutlets = 1
    availIngredients ={}
    beverageMap ={}
    ingred_threshold = 0
    outlets= {}
    freeOutlets = []
    display = display()
    def __init__(self,beverageMap,outletN,availIngredients,ingred_threshold):
        self.beverageMap = beverageMap
        self.noOfOutlets= outletN
        self.availIngredients = availIngredients
        self.ingred_threshold = ingred_threshold

        for i in range(0,outletN):
            self.outlets[i]= outlet(i)
            self.freeOutlets.append(i)

    #adds Ingredients to coffeeMachine
    def addIngredient(self,ingredientName,quantity):
        self.availIngredients[ingredientName]+= quantity

    #checks if Ingredients are sufficient for this beverage or not
    def checkAvailablity(self,beverageName):
        beverage = self.beverageMap[beverageName]
        for ingredientName in list(beverage.ingredientList.keys()):
            if(beverage.ingredientList[ingredientName]> self.availIngredients[ingredientName]):
                self.display.setMessage(beverageName + " cannot be prepared because item "+ ingredientName + " is not sufficient")
                return False
        return True
    
    #Gets the ingredients needed to prepare beverage
    def fetchIngredients(self,beverageName):
        beverage = self.beverageMap[beverageName]
        for ingredientName in list(beverage.ingredientList.keys()):
            self.availIngredients[ingredientName] -= beverage.ingredientList[ingredientName]

    #checks if the Ingredients are not running low
    def checkIngredientsForThreshold(self):
        for Ingredient in self.availIngredients:
            if(self.availIngredients[Ingredient] < self.ingred_threshold):
                self.display.setMessage(Ingredient + " is running low")
        pass           

    #Prepares and dispenses the beverage
    def makeBeverage(self,beverageName):
        if(beverageName not in list(self.beverageMap.keys())):
            self.display.setMessage(beverageName + " is invalid input")
            return
        if(self.checkAvailablity(beverageName)):
            if(len(self.freeOutlets)!=0):
                outletID = self.freeOutlets.pop()
                outlet = self.outlets[outletID]
                outlet.engage()
                self.fetchIngredients(beverageName)
                beverage = self.beverageMap[beverageName]
                beverage.prepBeverage()
                self.display.setMessage(beverageName + " is prepared")
                self.display.setMessage("Please collect your beverage from outlet Number : " + str(outletID))
                outlet.dispenseBev(beverageName)
                self.display.setMessage(beverageName + " is dispensed..")
                self.freeOutlets.append(outletID)
                self.checkIngredientsForThreshold()
            else:
                self.display.setMessage("All outlets are currently engaged...please wait!!")
