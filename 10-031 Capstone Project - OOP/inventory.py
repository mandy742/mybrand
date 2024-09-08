
# The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        """
        We create Attributes within the class shoe

        We set self to country,code,product,cost,quantity
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # This method gets the cost of the shoe.
    def get_cost(self):
        """
         Returns the cost of the shoe.

        float: The cost of the shoe.
        """
        return self.cost

    # This method gets the quantity of each shoe
    def get_quantity(self):
        """
        Returns the quantity of the shoe.

        int: The quantity of the shoe.
        """
        return self.quantity

    # This method returns detail info of each shoe.
    def __str__(self):
        """
        Returns a detailed string representation of the shoe.

        str: A formatted string with shoe details.
        """
        return (f"\ncountry:{self.country}\n"
                f"\nShoe Code: {self.code}\n"
                f"Shoe Name: {self.product}\n"
                f"Shoe Cost: {self.cost}\n"
                f"Quantity: {self.quantity}\n")


# The list will be used to store a list of shoes.
shoe_list = []
# Functions outside the class
# This function will open the file inventory.txt
# and read the data from this file, then create a shoes object with this data
# and append this object into the shoes list. One line in this file represents
# data to create one object of shoes. use the try-except in this function
# for error handling.


def read_shoes_data():
    """
    Reads data from the "inventory.txt" file and creates shoe objects.

    FileNotFoundError: If the inventory file is not found.
    """
    try:
        with open("inventory.txt", "r") as shoe_list_inventory:
            shoe_list_inside_file = shoe_list_inventory.readlines()
        # Remember to skip the first line using your code using 1.
        # create a loop.
        for line in range(1, len(shoe_list_inside_file)):
            country, code, product, cost, quantity = shoe_list_inside_file[line].strip("\n").split(",")

            shoes = Shoe(country, code, product, float(cost), int(quantity))
            shoe_list.append(shoes)
        # print("Data read from 'inventory.txt' and added to shoe_list")
        # create an object named shoes.
        # call the shoe class
        # append it to shoe list

    except FileNotFoundError:
        print("inventory file not found. Please try again!!")


read_shoes_data()


# This function will allow a user to capture data
# about a shoe and use this data to create a shoe object
# and append this object inside the shoe list.
def capture_shoes():
    """
    User Captures New Shoes with following info:
    Country, code, product, cost, quantity

    Captured shoes store in the inventory.txt
    """
    try:
        shoe_country = input("Please enter the country: ")
        shoe_code = input("Please enter  the code: ")
        shoe_product = input("Please enter the shoe name: ")
        shoe_cost = float(input("Please enter the cost: "))
        shoe_quantity = int(input("Please enter the quantity: "))

        shoes_captured = Shoe(shoe_country, shoe_code, shoe_product,
                              shoe_cost, shoe_quantity)
        shoe_list.append(shoes_captured)
        # Writing the updated shoe list to the inventory.txt
        with open("inventory.txt", "w") as file:
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
    except ValueError:
        print("""invalid input.please enter a
              numeric value for cost and quantity""")


# Creating a variable called obj_data for shoe object
# This will take all intake of shoe objects
# It will be updated inside the shoe list

def update():
    """
    Created obj_data Variable

    Updated Shoe data stored in the inventory file
    """
    obj_data = "country,code,product,cost,quantity"
    # create a for loop to iterate over shoe list
    for shoe in shoe_list:
        obj_data += f"\n{shoe.country}, {shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}"
        # open our inventory file and write.
    with open("inventory.txt", "w") as shoe_list_inventory:
        shoe_list_inventory.write(obj_data)


# This function will iterate over the shoes list and
# print the details of the shoes returned from the __str__
def view_all():
    """
    Views all shoes in the inventory file.
    """
    with open("inventory.txt", "r") as file:
        for line in file:
            (shoe_country, shoe_code, shoe_product,
             shoe_cost, shoe_quantity) = line.split(",")
            print(f"""
                  shoe_country = {shoe_country}
                  shoe_code = {shoe_code}
                  shoe_product = {shoe_product}
                  shoe_cost = {shoe_cost}
                  shoe_quantity = {shoe_quantity}""")


# This function will find the shoe object with the lowest quantity,
# which is the shoes that need to be re-stocked. Ask the user if they
# want to add this quantity of shoes and then update it.
# This quantity should be updated on the file for this shoe.
# shoe_index is a counter initialize to 0
# initialize quantity float with a large value.
# This will ensure that the first shoe value is always smaller.
def re_stock():
    """
    Restock the minimum quantity if user permits.
    """
    min_qty = float("inf")
    shoe_index = 0

    # making a loop to iterate to the shoe list.
    for i, shoe in enumerate(shoe_list):
        if shoe.quantity < min_qty:
            min_qty = shoe.quantity
            shoe_index = i

    if shoe_index != -1:
        print(f"Lowest quantity shoe: {shoe_list[shoe_index].product}")
        additional_quantity = int(input("""do you want to restock:
                                        How many more shoes do you want to add?
                                         """))
        shoe_list[shoe_index].quantity += additional_quantity

        # Update the inventory.txt file
        with open("inventory.txt", "w") as file:
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
    else:
        print("No shoes found in the inventory.")


# This function will search for a shoe from the list
# using the shoe code and return this object so that it will be printed.
# Will use a for loop for shoe code
# if statement calls shoe code and if its the same as users
# code it will be returned.
def search_shoe(shoe_code):
    """
    Search for shoe using a shoe code
    Returns the shoe
    """
    for shoe in shoe_list:
        if shoe.code == shoe_code:
            return shoe
    return None


# This function will calculate the total value for each item.
# Please keep the formula for value in mind: value = cost * quantity.
# Print this information on the console for all the shoes.
# Created a for loop to iterate through the shoe list
def value_per_item():
    """
    Returns total value per shoe

    """
    for shoe in shoe_list:
        total_value = shoe.cost * shoe.quantity
        print(f"{shoe.product} ({shoe.code}): value: {total_value:.2f}\n")


# Write code to determine the product with the highest quantity and
# print this shoe as being for sale.
# will create a counter called shoe index initialized with a valid index.
# create another maximum quantity.
def highest_qty():
    """Finding the highest quantity

    Return shoe with the maximum quantity
    """
    # Initialize with a small value
    max_quantity = float('-inf')
    shoe_index = -1

    # Iterate over the shoe_list
    for i, shoe in enumerate(shoe_list):
        if shoe.quantity > max_quantity:
            max_quantity = shoe.quantity
            shoe_index = i

    if shoe_index != -1:
        print(f"This Shoe is on sale,sale: {shoe_list[shoe_index].product}")
    else:
        print("No shoes found in the inventory")


# Main Menu
# Create a menu that executes each function above.
# This menu should be inside the while loop. Be creative!
# The menu will have the following options
# data which will contain all information about the shoe.
# view option were the user will be able to view shoes that are in stock
# Restock option for shoes that have been sold.
# find shoe is for looking for shoes that are in stock
# Price option for calculating total value for shoes.
# Sale option is for shoes on sale
# defining user choice

user_choice = ""
while user_choice != "end of stock taking":
    user_choice = input("""
                        Please select the following options
                        1 = Capture data about the shoes
                        2 = view all shoes available
                        3 = restock shoes that are sold out
                        4 = search for a shoe
                        5 = calculate the total value
                        6 = shoes on sale
                        7 = exit
                        \n""").lower()

    if user_choice == "1":
        capture_shoes()
    elif user_choice == "2":
        view_all()
    elif user_choice == "3":
        update()
        re_stock()
    elif user_choice == "4":
        s_code = input("Please enter the shoe code you are looking for: ")
        print(f"{search_shoe(s_code)}")
    elif user_choice == "5":
        value_per_item()
    elif user_choice == "6":
        highest_qty()
    elif user_choice == "7":
        exit()
    else:
        print("Please select an option from the menu!!")
