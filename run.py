import colorama
import gspread
from colorama import Fore
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('calc_data')

room = SHEET.worksheet('room')
test_data = room.get_all_values()

class Dimensions:
    """
    Class to handle the measurements of the cold room.
    """
    def __init__(self, measurement, dist):
        self.measurement = measurement
        self.dist = dist

    def validator(self):
        """
        Function to validate a positive numerical input.
        """
        while True:
            try:
                value = float(input())
            except ValueError:
                print(Fore.RED + "Sorry, please enter a numerical value.\n" + Fore.WHITE)
                continue
            if value < 0:
                print(Fore.RED + "Sorry, you must enter a positive numerical value.\n" + Fore.WHITE)
                continue
            else:
                return value

    def room(self):
        """
        function to intake length, width and height of the
        cold room. This will calculate volume and surface area
        also.
        """
        print(Fore.BLUE + "Please enter the length of the coldroom in metres : " + Fore.WHITE)
        m1.dist = Dimensions.validator(self)
        room.update_cell(3, 3, m1.dist)
        print(Fore.BLUE + "Please enter the width of the coldroom in metres : " + Fore.WHITE)
        m2.dist = Dimensions.validator(self)
        room.update_cell(3, 2, m2.dist)
        print(Fore.BLUE + "Please enter the height of the coldroom in metres : " + Fore.WHITE)
        m3.dist = Dimensions.validator(self)
        room.update_cell(3, 1, m3.dist)
        print(Fore.BLUE + "The", m1.measurement, "you entered is" + Fore.WHITE, m1.dist, Fore.BLUE + "metres." + Fore.WHITE)
        print(Fore.BLUE + "The", m2.measurement, "you entered is" + Fore.WHITE, m2.dist, Fore.BLUE + "metres." + Fore.WHITE)
        print(Fore.BLUE + "The", m3.measurement, "you entered is" + Fore.WHITE, m3.dist, Fore.BLUE + "metres." + Fore.WHITE)
        Dimensions.yes_no(Fore.BLUE + "Are entered values correct, please enter yes or no ? \n" + Fore.WHITE)
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
                print(Fore.RED + "Please enter yes or no." + Fore.WHITE)
                continue
            if value.lower() in yes:
                print(Fore.BLUE + "Calculating volume....." + Fore.WHITE)
                m4.dist = Dimensions.volume(m1.dist, m2.dist, m3.dist) # call to function to calculate room volume
                print(Fore.BLUE + "Calculated volume......" + Fore.WHITE, m4.dist, Fore.BLUE + "metres cubed." + Fore.WHITE)
                Dimensions.area(m1.dist, m2.dist, m3.dist) # call to function to calculate surface area of the room
                break
            elif value.lower() in no:
                Dimensions.room(Fore.BLUE + "Please input correct measurements." + Fore.WHITE)
                break
            else:
                print(Fore.RED + "Please respond with a yes or no answer." + Fore.WHITE)

    def volume(length, height, width):
        """
        Function to calculate volume of the room
        """
        m4.dist = length * height * width
        room.update_cell(5, 3, m4.dist)
        return m4.dist

    def area(length, height, width):
        """
        Function to calculate surface area of the room
        """
        m5.dist = (((length * height) * 2) + ((width * height) * 2)) + (length * width) # area of ceiling and walls
        m6.dist = length * width # area of floor space
        room.update_cell(5, 1, m5.dist)
        room.update_cell(5, 2, m6.dist)
        print(Fore.BLUE + "Total surface area of roof and walls is" + Fore.WHITE, round(m5.dist, 2), Fore.BLUE + "metres sqaured")
        print("Total surface area of the floor is" + Fore.WHITE, round(m6.dist, 2), Fore.BLUE + "metres squared" + Fore.WHITE)


def temperature(prompt):
    """
    Function to check value is acceptable temperature value.
    """
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print(Fore.RED + "Sorry, I do not understand...")
            print("Please enter a numerical value." + Fore.WHITE)
            continue
        else:
            return value


def insulation(prompt):
    """
    Function for user to select the thickness off panel which the room is constructed from.
    """
    panel_type = [
        {"Type": "80mm PIR Panel", "U_Value": 0.26}, # panel materials as associated U value.
        {"Type": "100mm PIR Panel", "U_Value": 0.21},
        {"Type": "150mm PIR Panel", "U_Value": 0.15},  # the thicker to panel the better the U value.
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
            print(Fore.BLUE + "Please select an option between 1 and 4. " + Fore.WHITE)
            continue
        if panel not in range(1, 5):
            print(Fore.RED + 
                "Please select an option between 1 and 4, your number is outside of range." + Fore.WHITE
            )
            continue
        elif panel == 1:
            room.update_cell(3, 4, "80mm PIR")
            u_valve = panel_type[0]["U_Value"]
        elif panel == 2:
            room.update_cell(3, 4, "100mm PIR")
            u_valve = panel_type[1]["U_Value"]
        elif panel == 3:
            room.update_cell(3, 4, "150mm PIR")
            u_valve = panel_type[2]["U_Value"]
        else:
            panel == 4
            room.update_cell(3, 4, "200mm PIR")
            u_valve = panel_type[3]["U_Value"]
        return u_valve
        break


def floor(prompt):
    """
    Function to ask user is the room has an insulated floor and apply an appropriate U value to it.
    """
    yes = {"yes", "y"}
    no = {"no", "n"}
    while True:
        try:
            value = input(prompt)
        except ValueError:
            print(Fore.BLUE + "Please enter yes or no." + Fore.WHITE)
            continue
        if value.lower() in yes:
            value = 0.28  # if the floor is insulated it is given a superior insulation value.
            room.update_cell(3, 5, "Yes")
            return value
        elif value.lower() in no:
            value = 1.0
            room.update_cell(3, 5, "No")
            return value
        else:
            print(Fore.BLUE + "Has the room got floor insulation? ")
            print("Please enter yes or no. " + Fore.WHITE)


class Heat_load:
    """
    Class to handle heat loads from people, product and air changes, relevant data and calculations.
    """
    def __init__(self, source, heat_load):
        self.source = source
        self.heat_load = heat_load

    def product_calc():
        """
        Function to intake quantity of product entering the room every 24 hours and calculate heat load.
        """    
        print(Fore.BLUE + "Please enter quantity of product entering room in kg: " + Fore.WHITE)
        product_qty = Dimensions.validator(input)  # validate the quantity entered.
        room.update_cell(7, 2, product_qty)
        product_temp = temperature(Fore.BLUE + "Please enter temperature of product in °C: " + Fore.WHITE) # call function to intake the temperature of product and check it.
        room.update_cell(7, 3, product_temp)
        hl1.heat_load = ((product_qty * 1.9) / 3600) + (
            product_qty * (product_temp - room_temp) / 3600
        ) # calculation of heat load of product
        room.update_cell(9, 4, abs(hl1.heat_load))
        return abs(hl1.heat_load)

    def people():
        """
        Function to check if there are people working in the room and calculate any heat generated.
        """ 
        print(Fore.BLUE +
            "Are there any people working in this room ?\n" "Please enter yes or no. " + Fore.WHITE)
        yes = {"yes", "y"}
        no = {"no", "n"}
        while True:
            try:
                value = input()
            except ValueError:
                print(Fore.BLUE + "Please enter yes or no. " + Fore.WHITE)
                continue
            if value.lower() in yes:
                while True:
                    try:
                        value = int(input(Fore.BLUE + "How many people are working in the room ? " + Fore.WHITE))
                    except ValueError:
                        print(Fore.RED + "Please enter a numerical value for quantity of people." + Fore.WHITE)
                        continue
                    if value < 0:
                        print(Fore.RED + "The value must be a whole, positive number." + Fore.WHITE)
                        continue
                    else:
                        hl2.heat_load = (value * 6 * 270) / 1000  # calculate the heat generated by person or peopls
                        room.update_cell(7, 4, value)
                        room.update_cell(9, 2, hl2.heat_load)
                        room.update_cell(7, 4, "Yes")
                        return hl2.heat_load
                        break
            elif value.lower() in no:
                hl2.heat_load = 1.0
                room.update_cell(9, 2, hl2.heat_load)
                room.update_cell(7, 4, "No" )

                return hl2.heat_load
                break
            else:
                print(Fore.RED + "Please enter yes or no. " + Fore.WHITE)

    def air_changes():
        """
        Function to calculate air infiltration load.
        Intake no. of air changes, room volume and room temperature.
        """
        print(Fore.BLUE + 
            "Please enter approximate number of door\n" "openings in a 24 hour period. " + Fore.WHITE
        )
        value = Dimensions.validator(input)
        room.update_cell(7, 5, value)
        hl3.heat_load = (value * m4.dist * 2 * (20-room_temp))/3600  # calculate air changes in the room 
        room.update_cell(9, 3, hl3.heat_load)
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
        room.update_cell(9, 5, abs(value))
        return abs(value)


    def total_duty():
        """
        Function to add all heat loads together and then calculate the required refrigeration duty.
        """
        total_duty = ((hl1.heat_load + hl2.heat_load + hl3.heat_load + transmission_load) * 1.2) / 12  # add all heat loads, add 20% and divide by 12hours, which is average run time in 24hour day
        room.update_cell(9, 5, total_duty)
        print(Fore.BLUE + "The kilowatt duty, kW, of the required refrigeration\n" "equipment necessary for this cold store is\n" + Fore.WHITE, round(total_duty, 2),"kW")

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

print("****Welcome to Cold Store Duty Calculation****")
print("Please enter the required data to calculate the kilowatt, kW,\n"
        "duty of the equipment needed to cool the room down to the\n"
        "required temperature.")
Dimensions.room("")
room_temp = temperature(Fore.BLUE + "Please enter temperature of the room in °C : " + Fore.WHITE)
panel = insulation(Fore.BLUE + "Please select panel size from which room is constructed. : " + Fore.WHITE)
floor_rating = floor(Fore.BLUE + "Is the floor insulated ? \n" "Please enter yes or no. : " + Fore.WHITE)
hl1.heat_load = Heat_load.product_calc()
hl2.heat_load = Heat_load.people()
hl3.heat_load = Heat_load.air_changes()
transmission_load = Transmission.room_load_calc()
total_duty = Transmission.total_duty()






