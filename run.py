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
        m1 = Dimensions("Length", 0.0)
        print("Please enter the length of the coldroom in metres : ")
        m1.dist = Dimensions.validator(self)
        print("The", m1.measurement, "you entered is", m1.dist, "metres.")
        m2 = Dimensions("Width", 0.0)
        print("Please enter the Width of the coldroom in metres : ")
        m2.dist = Dimensions.validator(self)
        print("The", m2.measurement, "you entered is", m2.dist, "metres.")
        m3 = Dimensions("height", 0.0)
        print("Please enter the height of the coldroom in metres : ")
        m3.dist = Dimensions.validator(self)
        print("The", m3.measurement, "you entered is", m3.dist, "metres.")
        Dimensions.yes_no("Are entered values correct, please enter yes or no ? \n")
        

    def yes_no(prompt):
        """
        Function to check for and validate a yes or no
        response from user.
    
        """
        yes = {'y', 'ye', 'yes', ''}
        no = {'n', 'no'}
        while True:
            try:
                value = input(prompt)
            except ValueError:
                print("That aint right")
                continue
            if value in yes:
                return
            elif value in no:
                print("Please input correct data.")
                Dimensions.room('')
            else:
                print("Please respond with a yes or no answer.")
    

    def volume():
        






"""
Start of program.
"""
 
Dimensions.room('')
