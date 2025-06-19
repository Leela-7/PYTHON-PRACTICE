# Shopping Cart
cart = {}

while True:
    print("1. Add Item")
    print("2. Update Item")
    print("3. Remove Item")
    print("4. View Items")
    print("5. Exit")
    
    opt = int(input("Enter Your Option: "))
    
    if opt == 1:
        name = input("Item Name: ")
        if name not in cart:
            qty = int(input("Qty: "))
            cart[name] = qty
            print("Item Added to Cart")
        else:
            print("This item exists in Cart")
    
    elif opt == 2:
        name = input("Item Name: ")
        if name in cart:
            qty = int(input("Updated Qty: "))
            cart[name] = qty
            print("Item Updated in Cart")
        else:
            print("Item not Exists")
    
    elif opt == 3:
        name = input("Item Name: ")
        if name in cart:
            del cart[name]
            print("Item Removed from Cart")
        else:
            print("Item not Exists")
    
    elif opt == 4:
        if len(cart) == 0:
            print("Cart is empty")
        else:
            print("Items in Cart:")
            for name, qty in cart.items():
                print(f'{name}\t{qty}')
    
    elif opt == 5:
        break
    
    else:
        print("Invalid Option. Please try again.")
