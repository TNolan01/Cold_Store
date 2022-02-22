class Dimensions:
    def __init__(self, measurement, dist):
        self.measurement = measurement
        self.dist = dist

    def validator(self):
        while True:
            try:
              value = float(input())
            except ValueError:
                print("Sorry, please enter a numerical value.\n")
                continue
            if value < 0:
                print("Sorry, you must enter a positive numerical value.\n")
                continue
            else:
                return value
    
    def room(self):
        m1 = Dimensions("Length", 0.0)
        m1.dist = Dimensions.validator("Please enter the length of the coldroom in metres :\n " )
        m2 = Dimensions("Width", 0.0)
        m2.dist = Dimensions.validator("Please enter the width of the coldroom in metres :\n ")
        m3 = Dimensions("height", 0.0)
        m3.dist = Dimensions.validator("Please enter the height of the coldroom in metres :\n ")
    
        
 
Dimensions.room("Please enter details for coldroom")
room = Dimensions()
print (room)

