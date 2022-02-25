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
        """
        function to intake length, width and height of the 
        cold room. This will calculate volume and surface area
        also.
        """
        print("Please enter the length of the coldroom in metres : ")
        m1.dist = Dimensions.validator(self)
        print("Please enter the Width of the coldroom in metres : ")
        m2.dist = Dimensions.validator(self)
        print("Please enter the height of the coldroom in metres : ")
        m3.dist = Dimensions.validator(self)
        print("The", m1.measurement, "you entered is", m1.dist, "metres.")
        print("The", m2.measurement, "you entered is", m2.dist, "metres.")
        print("The", m3.measurement, "you entered is", m3.dist, "metres.")
        Dimensions.yes_no("Are entered values correct, please enter yes or no ? \n") 
        return
        

    def yes_no(prompt):
        """
        Function to check for and validate a yes or no
        response from user.
    
        """
        yes = {'yes'}
        no = {'no'}
        while True:
            try:
                value = input(prompt)
            except ValueError:
                print("That aint right")
                continue
            if value in yes:
                print("Calculating volume.....")
                m4.dist = Dimensions.volume(m1.dist, m2.dist, m3.dist)
                print("Calculated volume......", m4.dist, "metres cubed.")
                Dimensions.area(m1.dist, m2.dist, m3.dist)
                break
            elif value in no:
                Dimensions.room("Please input correct measurements.")
                break
            else: 
                print("Please respond with a yes or no answer.")
    

    def volume(length, height, width):
        """
        Function to calculate volume of the room
        """
        m4.dist = length * height * width
        return m4.dist

    
    def area(length, height, width):
        """
        Function to calculate surface area of the room
        """
        list = []
        m5.dist = (((length * height)*2) + ((width * height)*2)) + (length * width) 
        m6.dist = (length * width)
        print ("Total surface area of roof and walls is", m5.dist, "metres sqaured")
        print ("Total surface area of the floor is", m6.dist, "metres squared")

def temperature(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Sorry, I do not understand.")
            print("Please enter a numerical value.")
            continue
        else:
            return value



"""
Start of program.
"""
m1 = Dimensions("Length", 0.0)
m2 = Dimensions("Width", 0.0)
m3 = Dimensions("Height", 0.0)
m4 = Dimensions("Volume", 0.0)
m5 = Dimensions("Area",0.0)
m6 = Dimensions("Floor", 0.0)
Dimensions.room('')
""" print (m4.dist) """
room_temp = temperature("Please enter temperature of the room in °C : ")



