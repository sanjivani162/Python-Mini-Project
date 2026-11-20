#define the menu of restaurant
menu = {
    'tea':20,
    'coffee':40,
    'burger':50,
    'salad':60,
    'pasta':100,
    'pizza':120
}
#greet
print("Welcome to Mauli Restaurant")
print("pizza:100\n pasta:120\n burger:60\n salad:50\n coffee:90\n tea:20\n ")

order_total =0
#80 + 70 =150
item_1 =input('enter the name of item you want to order =')
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item{item_1} has been add to your order")
else:
    print(f"order item {item_1} is not avaialable yet!")

    another_order =input("DO you want to add another item? (yes/no)")
    if another_order == "yes":
        item_2 = input('enter the name of second item =')
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"item {item_2} has been add to order")
        else:
            print(f"order item {item_2} is not avaialable!")
print(f"the total amount of items is {order_total}" )
