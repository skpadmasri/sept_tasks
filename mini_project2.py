import datetime

# Customer details
name = input("Enter your Name: ").strip()

# Product catalog (Dictionary of items and prices per unit)
items = {
    'rice': 10,
    'sugar': 8,
    'oil': 30,
    'salt': 25,
    'paneer': 40,
    'maggie': 12,
    'boost': 200
}

# Declarations
cart = []
totalprice = 0

while True:
    option = input("\nPress 1 for list or 2 to exit: ").strip()
    
    if option == '2':
        print("\nThank you for shopping!")
        break
        
    elif option == '1':
        print("\n" + "=" * 35)
        print(f"{'Item':<15} {'Price per unit':<15}")
        print("-" * 35)
        for item_name, unit_price in items.items():
            print(f"{item_name.capitalize():<15} Rs {unit_price}")
        print("=" * 35)
        
        while True:
            inp1 = input("\nTo buy press 1 or press 2 to exit: ").strip()
            
            if inp1 == '2':
                break
                
            elif inp1 == '1':
                item = input("Choose your item: ").strip().lower()
                
                if item in items:
                    while True:
                        quantity_input = input("Enter quantity: ").strip()
                        if quantity_input.isdigit() and int(quantity_input) > 0:
                            quantity = int(quantity_input)
                            break
                        else:
                            print("Please enter a valid quantity (positive integer).")
                    
                    unit_price = items[item]
                    item_total = quantity * unit_price
                    totalprice += item_total
                    
                    # Store purchased details
                    cart.append({
                        'name': item.capitalize(),
                        'quantity': quantity,
                        'unit_price': unit_price,
                        'total': item_total
                    })
                    print(f"Added {quantity} x {item.capitalize()} to cart.")
                else:
                    print("Selected item is not available. Sorry for the inconvenience.")
            else:
                print("Invalid option! Please enter 1 or 2.")
        
        # Billing details and receipt display
        if totalprice > 0:
            tax = (totalprice * 12) / 100  # 12% tax calculation
            finalamount = totalprice + tax
            current_date = datetime.datetime.now().strftime("%b %d %Y")
            
            print("\n" + "=" * 65)
            print(f"{'Pythonlife Supermarket':^65}")
            print(f"{'Hyderabad':^65}")
            print("=" * 65)
            print(f"Customer Name: {name:<25} Date: {current_date}")
            print("-" * 65)
            print(f"{'S.No':<6}{'Item':<16}{'Quantity':<12}{'Price/Unit':<15}{'Total (Rs)':<12}")
            print("-" * 65)
            
            for index, entry in enumerate(cart, start=1):
                print(f"{index:<6}{entry['name']:<16}{entry['quantity']:<12}Rs {entry['unit_price']:<12}Rs {entry['total']:<12}")
                
            print("-" * 65)
            print(f"{'Total Amount before tax:':<49} Rs {totalprice:.2f}")
            print(f"{'Tax Amount (12%):':<49} Rs {tax:.2f}")
            print(f"{'Final Amount after tax:':<49} Rs {finalamount:.2f}")
            print("-" * 65)
            print(f"{'Thank you & Visit again!':^65}")
            print("=" * 65)
        else:
            print("\nNo items were purchased.")
            
        print("Thank you for shopping!")
        break
        
    else:
        print("Invalid choice! Please press 1 or 2.")