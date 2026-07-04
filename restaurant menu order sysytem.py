#we used dictionary datatype
#conditional statement and dictionary based project
menu={
    "pizza":80,
    "pasta":80,
    "pavbhaji":120,
    "misalpav":70,
    "Burger":60,
    "hot coffee":50,
    "coldcoffee":80,
    "french fries":90,
    "manchurian":100,
    "sandwich":60,
    "paneer chilli":120,
    "alo paratha":60,
    "paneer paratha":80,
    "masala chai":20,
    "dosa":70,
    "salad":70,
}
print("WELCOME TO RESTAURANT")
print("pizza: Rs80\npasta: Rs80\npavbhaji: Rs120\nmisalpav: Rs70\nBurger:Rs60\nhot coffee:Rs50\ncoldcoffee:Rs80\nfrench fries:Rs90\nmanchurian:Rs100\nsandwich:Rs60\npaneer chill:Rs120\nalo paratha:Rs60\npaneer paratha:Rs80\nmasala chai:Rs20\ndosa:RRs70\nsalad:Rs50")

total_order = 0
item_1= input("Enter the name of item you want to order = ")
if item_1 in menu:
    total_order += menu[item_1]
    print(f"your item {item_1} has been added")
else:
    print(f"SORRY but order item {item_1} is not available yet")

another_order = input("do you want to add any onther item?? (yes/no) ")
if another_order ==  "yes":
    item_2=input("Enter the name of second item = ")
    if item_2 in menu:
        total_order += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"Sorry ordered item {item_2} is not availble ")

print(f"the total amount of item to pay {total_order}")
