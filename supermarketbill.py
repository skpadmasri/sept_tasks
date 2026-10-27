name = input("Enter your Name: ")
lists = '''
Fortune Maida     Rs 45/kg
Toor Dal          Rs 140/kg
Sunflower Oil     Rs 130/liter
Basmati Rice      Rs 90/kg
Tata Salt         Rs 28/kg
Tea Powder        Rs 110/pack
Ghee              Rs 260/bottle
'''

# Declaration
price = 0
pricelist = []
totalprice = 0
Finalprice = 0
ilist = []
qlist = []
plist = []
# Rate for each item
items = {
    'maida': 45,
    'dal': 140,
    'oil': 130,
    'rice': 90,
    'salt': 28,
    'tea': 110,
    'ghee': 260
}
while True:
    option = input("Press 1 for list or 2 to exit: ")
    if option == '2':
        print("Thank you for shopping")
        break
    elif option == '1':
        print(lists)
        while True:
            inp1 = input("To buy press 1 or press 2 to exit: ")
            if inp1 == '2':
                print("Thank you for shopping")
                break
            elif inp1 == '1':
                item = input("Choose your items (maida, dal, oil, rice, salt, tea, ghee): ").lower()
                while True:
                    quantity_input = input("Enter quantity: ")
                    if quantity_input.isdigit():  # Check if input is a digit
                        quantity = int(quantity_input)
                        break
                    else:
                        print("Please enter a valid quantity.")
                if item in items:
                    price = quantity * items[item]
                    pricelist.append((item, quantity, items[item], price))
                    totalprice += price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                else:
                    print("Selected item is not available. Sorry for the inconvenience.")
        if totalprice > 0:
            tax = (totalprice * 12) / 100
            finalamount = tax + totalprice

            print(25 * "=", "Pythonlife Supermarket", 25 * "=")
            print(28 * " ", "Narasapur")
            print("Name:", name, 30 * " ", "OCT 07 2026")
            print(75 * "-")
            print("sno", 10 * " ", 'items', 8 * " ", 'quantity', 8 * " ", 'price')
            for i in range(len(pricelist)):
                print(i + 1, 13 * " ", ilist[i], 8 * " ", qlist[i], 8 * " ", plist[i])
            print(75 * "-")
            print(50 * " ", 'Total amount:', 'Rs', totalprice)
            print("Tax amount", 50 * " ", 'Rs', tax)
            print(75 * "-")
            print(50 * " ", 'Final amount:', 'Rs', finalamount)
            print(75 * "-")
            print(20 * " ", "Thank you & Visit again")
            print(75 * "-")
        break