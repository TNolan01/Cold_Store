import colorama
from colorama import Fore

class Dimensions:
    def __init__(self, measurement, dist):
        self.measurement = measurement
        self.dist = dist

    def validator(self):
        while True:
            try:
                value = float(input())
            except ValueError:
                print(Fore.RED + "Sorry, please enter a numerical value.\n" + Fore.WHITE)
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
        yes = {"yes", "y"}
        no = {"no", "n"}
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
        m5.dist = (((length * height) * 2) + ((width * height) * 2)) + (length * width)
        m6.dist = length * width
        print("Total surface area of roof and walls is", m5.dist, "metres sqaured")
        print("Total surface area of the floor is", m6.dist, "metres squared")


def temperature(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Sorry, I do not understand...")
            print("Please enter a numerical value.")
            continue
        else:
            return value


def insulation(prompt):
    panel_type = [
        {"Type": "80mm PIR Panel", "U_Value": 0.26},
        {"Type": "100mm PIR Panel", "U_Value": 0.21},
        {"Type": "150mm PIR Panel", "U_Value": 0.15},
        {"Type": "200mm PIR Panel", "U_Value": 0.10},
    ]

    print(f'1. {panel_type[0]["Type"]}')
    print(f'2. {panel_type[1]["Type"]}')
    print(f'3. {panel_type[2]["Type"]}')
    print(f'4. {panel_type[3]["Type"]}')
    while True:
        try:
            panel = int(input(prompt))
        except ValueError:
            print("Please select an option between 1 and 4. ")
            continue
        if panel not in range(1, 5):
            print(
                "Please select an option between 1 and 4, your number is outside of range."
            )
            continue
        elif panel == 1:
            u_valve = panel_type[0]["U_Value"]
        elif panel == 2:
            u_valve = panel_type[1]["U_Value"]
        elif panel == 3:
            u_valve = panel_type[2]["U_Value"]
        else:
            panel == 4
            u_valve = panel_type[3]["U_Value"]
        return u_valve
        break


def floor(prompt):
    yes = {"yes", "y"}
    no = {"no", "n"}
    while True:
        try:
            value = input(prompt)
        except ValueError:
            print("Please enter yes or no.")
            continue
        if value in yes:
            value = 0.28
            return value
        elif value in no:
            value = 1.0
            return value
        else:
            print("Has the room got floor insulation? ")
            print("Please enter yes or no. ")


class Heat_load:
    def __init__(self, source, heat_load):
        self.source = source
        self.heat_load = heat_load

    def product_calc():
        print("Please enter quantity of product entering room in kg: ")
        product_qty = Dimensions.validator(input)
        product_temp = temperature("Please enter temperature of product in ºC: ")
        hl1.heat_load = ((product_qty * 1.9) / 3600) + (
            product_qty * (product_temp - room_temp) / 3600
        )
        return abs(hl1.heat_load)

    def people():
        print(
            "Are there any people working in this room ?\n" "Please enter yes or no. "
        )
        yes = {"yes", "y"}
        no = {"no", "n"}
        while True:
            try:
                value = input()
            except ValueError:
                print("Please enter yes or no. ")
                continue
            if value in yes:
                while True:
                    try:
                        value = int(input("How many people are working in the room ? "))
                    except ValueError:
                        print("Please enter a numerical value for quantity of people.")
                        continue
                    if value < 0:
                        print("The value must be a whole, positive number.")
                        continue
                    else:
                        hl2.heat_load = (value * 6 * 270) / 1000
                        return hl2.heat_load
                        break
            elif value in no:
                hl2.heat_load = 1.0
                return hl2.heat_load
                break
            else:
                print("Please enter yes or no. ")

    def air_changes():
        """
        Function to calculate air infiltration load.
        Intake no. of air changes, room volume and room temperature.
        """
        print(
            "Please enter approximate number of door\n" "openings in a 24 hour period. "
        )
        value = Dimensions.validator(input)
        hl3.heat_load = (value * m4.dist * 2 * (20-room_temp))/3600  # calculate air changes in the room 
        return round(abs(hl3.heat_load,))


class Transmission:
    def room_load_calc():
        """
        Function to calculate the transmission load of the room.
        """
        total_room_area = m5.dist + m6.dist  # walls, floor and ceiling surface area 
        ceil_wall = (panel * total_room_area * room_temp * 24)/1000  # transmission load for walls and ceiling
        floor = (m6.dist * floor_rating * room_temp * 24)/1000  # transmission load for floor
        value = ceil_wall + floor # complete transmission load for entire room
        return abs(value)


    def total_duty():
        """
        Function to add all heat loads together and then calculate the required refrigeration duty.
        """
        total_duty = ((hl1.heat_load + hl2.heat_load + hl3.heat_load + transmission_load) * 1.2) / 14  # add all heat loads, add 20% and divide by 14hours, which is average run time in 24hour day
        return round(total_duty, 2)
        print("The kilowatt duty, kW, of the required refrigeration\n" "equipment necessary for this cold store is\n", round(total_duty, 2),"kW")
"""
Start of program.
"""
m1 = Dimensions("Length", 0.0)
m2 = Dimensions("Width", 0.0)
m3 = Dimensions("Height", 0.0)
m4 = Dimensions("Volume", 0.0)
m5 = Dimensions("Area", 0.0)
m6 = Dimensions("Floor", 0.0)
hl1 = Heat_load("Product", 0.0)
hl2 = Heat_load("People", 0.0)
hl3 = Heat_load("Air", 0.0)

Dimensions.room("")
""" print (m4.dist) """
room_temp = temperature("Please enter temperature of the room in °C : ")
panel = insulation("Please select panel size from which room is constructed.")
floor_rating = floor("Is the floor insulated ? \n" "Please enter yes or no. ")
hl1.heat_load = Heat_load.product_calc()
hl2.heat_load = Heat_load.people()
hl3.heat_load = Heat_load.air_changes()
transmission_load = Transmission.room_load_calc()
print(transmission_load)
total_duty = Transmission.total_duty()
print(total_duty)





