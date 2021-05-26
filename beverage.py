class beverage:
    beverageName = ''
    ingredientList = {}
    preparationTime =0
    def __init__(self,bevName,bevReceipe,preparationTime):
        self.beverageName = bevName
        self.ingredientList = bevReceipe
        self.preparationTime = preparationTime

    #Interface only defination as per beverage
    #how to prepare a beverage
    def prepBeverage(self):
        pass