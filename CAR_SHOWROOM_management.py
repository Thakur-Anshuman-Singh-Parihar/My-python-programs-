def separator():
    print("\n" + "-" * 50 + "\n")

def welcome_message():
    print("🚗 Welcome to SDEEDY Showroom 🚗")
    print("Your one-stop destination for premium cars! 🏎️")

def main_menu():
    print("📋 Main Menu:")
    print("1️⃣ Owner/Staff Access")
    print("2️⃣ Customer Access")
    print("0️⃣ Exit")

def owner_menu():
    print("🔧 Owner/Staff Menu:")
    print("1️⃣ Add New Car")
    print("2️⃣ Update Car Price")
    print("3️⃣ Delete Car")
    print("4️⃣ Change Password")
    print("0️⃣ Return to Main Menu")

def customer_menu():
    print("🛍️ Customer Menu:")
    print("1️⃣ View All Cars")
    print("2️⃣ Search Car")
    print("3️⃣ Purchase Car")
    print("4️⃣ Test Drive")
    print("0️⃣ Return to Main Menu")

def add_new_car():
    print("✏️ Enter the car details:")
    new_car = {
        "name": input("Enter the name of the new car: ").strip().upper(),
        "type": input("Type (e.g., SUV, Hatchback, Sedan, Jeep): ").strip().lower(),
        "engine_type": input("Engine type (e.g., Diesel, Petrol, Hybrid, Electric): ").strip().lower(),
        "mileage": input("Enter the mileage of the car: "),
        "manufacture_year": input("Enter the manufacturing year of the car: "),
        "special_features": input("Enter the special features of the car: ").strip().lower(),
        "price": input("Enter the price of the car: "),
        "seats": input("Enter the seating capacity of the car: "),
        "color": input("Enter the number of available colors for the car: ")
    }
    car_list.append(new_car)
    print("✅ Car added successfully!")

def display_car_details(index):
    car = car_list[index]
    print("🚘 Model Name: " + car["name"])
    print("🛻 Type of Vehicle: " + car["type"])
    print("⚙️ Engine Type: " + car["engine_type"])
    print("⛽ Mileage: " + str(car["mileage"]))
    print("🏭 Manufacturing Year: " + str(car["manufacture_year"]))
    print("✨ Special Features: " + car["special_features"])
    print("💰 Price: " + str(car["price"]))
    print("🪑 Seats: " + car["seats"])
    print("🎨 Available Colors: " + car["color"])
    separator()

# Sample car list
car_list = [
    {
        "type": "suv",
        "engine_type": "hybrid",
        "name": "SCORPIO",
        "mileage": 22,
        "manufacture_year": 2022,
        "special_features": "3 air bags, sunroof, 4X4",
        "price": 2100000,
        "seats": "7 seater",
        "color": "5 colors available"
    },
    {
        "type": "sedan",
        "engine_type": "petrol",
        "name": "VERNA",
        "mileage": 28,
        "manufacture_year": 2023,
        "special_features": "2 air bags, sunroof",
        "price": 1500000,
        "seats": "5 seater",
        "color": "2 colors available"
    },
    {
        "type": "hatchback",
        "engine_type": "electric",
        "name": "SWIFT",
        "mileage": 32,
        "manufacture_year": 2021,
        "special_features": "3 air bags, sunroof, compact design",
        "price": 1100000,
        "seats": "5 seater",
        "color": "4 colors available"
    }
]

password = "4444"

# Main program loop
while True:
    welcome_message()
    separator()
    main_menu()
    choice = input("Enter your choice: ")
    separator()

    if choice == "1":
        entered_password = input("Enter your password: ")
        if entered_password == password:
            print("🔓 Access granted.")
            while True:
                owner_menu()
                owner_choice = input("Enter your choice: ")
                separator()

                if owner_choice == "1":
                    add_new_car()
                elif owner_choice == "2":
                    car_name = input("Enter the name of the car to update the price: ").strip().upper()
                    found = False
                    for car in car_list:
                        if car["name"] == car_name:
                            new_price = input("Enter the new price for " + car_name + ": ")
                            car["price"] = new_price
                            print("✅ Price updated for " + car_name + ".")
                            found = True
                            break
                    if not found:
                        print("❌ Car not found.")
                elif owner_choice == "3":
                    car_name = input("Enter the name of the car to delete: ").strip().upper()
                    car_list = [car for car in car_list if car["name"] != car_name]
                    print("🗑️ " + car_name + " has been deleted.")
                elif owner_choice == "4":
                    password = input("Enter your new password: ")
                    print("🔐 Password changed successfully.")
                elif owner_choice == "0":
                    break
                else:
                    print("❌ Invalid choice.")
                separator()
        else:
            print("❌ Incorrect password.")
    elif choice == "2":
        while True:
            customer_menu()
            customer_choice = input("Enter your choice: ")
            separator()

            if customer_choice == "1":
                for i in range(len(car_list)):
                    display_car_details(i)
            elif customer_choice == "2":
                print("🔍 Search by:")
                print("1️⃣ Name")
                print("2️⃣ Type of Vehicle")
                print("3️⃣ Engine Type")
                print("4️⃣ Price")
                print("5️⃣ Seats")
                search_choice = input("Enter your choice: ")

                if search_choice == "1":
                    name = input("Enter the car name: ").strip().upper()
                    found = False
                    for i in range(len(car_list)):
                        if car_list[i]["name"] == name:
                            display_car_details(i)
                            found = True
                    if not found:
                        print("❌ Car not found.")
                elif search_choice == "2":
                    vehicle_type = input("Enter the type of vehicle: ").strip().lower()
                    found = False
                    for i in range(len(car_list)):
                        if car_list[i]["type"] == vehicle_type:
                            display_car_details(i)
                            found = True
                    if not found:
                        print("❌ No cars found for the specified type.")
                elif search_choice == "3":
                    engine_type = input("Enter the engine type: ").strip().lower()
                    found = False
                    for i in range(len(car_list)):
                        if car_list[i]["engine_type"] == engine_type:
                            display_car_details(i)
                            found = True
                    if not found:
                        print("❌ No cars found for the specified engine type.")
                elif search_choice == "4":
                    max_price = int(input("Enter your maximum budget: "))
                    found = False
                    for i in range(len(car_list)):
                        if int(car_list[i]["price"]) <= max_price:
                            display_car_details(i)
                            found = True
                    if not found:
                        print("❌ No cars found within the specified budget.")
                elif search_choice == "5":
                    seats = input("Enter the seating capacity (e.g., 5 seater): ").strip().lower()
                    found = False
                    for i in range(len(car_list)):
                        if car_list[i]["seats"] == seats:
                            display_car_details(i)
                            found = True
                    if not found:
                        print("❌ No cars found with the specified seating capacity.")
                else:
                    print("❌ Invalid choice.")
            elif customer_choice == "3":
                car_name = input("Enter the name of the car you want to purchase: ").strip().upper()
                found = False
                for car in car_list:
                    if car["name"] == car_name:
                        print("💰 The price of " + car_name + " is " + str(car['price']))
                        print("Choose a payment option:")
                        print("1️⃣ EMI")
                        print("2️⃣ Cheque")
                        print("3️⃣ Cash")
                        payment_option = input("Enter your choice: ")

                        if payment_option == "1":
                            down_payment = int(car["price"]) * 0.3
                            emi = (int(car["price"]) - down_payment) / 24
                            print("💰 Down Payment: " + str(down_payment))
                            print("💳 Monthly EMI: " + str(emi) + " for 24 months")
                        elif payment_option == "2":
                            print("📝 Please submit your cheque at the counter.")
                        elif payment_option == "3":
                            print("💵 Please pay the amount in cash at the counter.")
                        else:
                            print("❌ Invalid payment option.")
                        found = True
                        break
                if not found:
                    print("❌ Car not found.")
            elif customer_choice == "4":
                car_name = input("Enter the name of the car for a test drive: ").strip().upper()
                found = False
                for car in car_list:
                    if car["name"] == car_name:
                        security_deposit = int(car["price"]) * 0.1
                        print("🔑 " + car_name + " is available for a test drive.")
                        print("💰 Security Deposit: " + str(security_deposit))
                        print("📝 Please sign the necessary documents.")
                        print("⏳ Test drive duration: 48 hours")

