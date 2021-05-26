class outlet:
    outletID =0 
    status = "free"

    def __init__(self,outletID):
        self.outletID = outletID

    #engage the Outlet for user
    def engage(self):
        status = "using"
    
    #dispense beverage
    def dispenseBev(self,BevName):
        self.disengage()
    
    #disengage the Outlet
    def disengage(self):
        status = "free"
