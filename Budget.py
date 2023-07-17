class Budget:
    food = int(input("Enter the Budget you want to allocate to your food expenses: "))
    entertainment = int(input("Enter the Budget you want to allocate to your movies and other entertainment expenses: "))
    clothing = int(input("Enter your Budget you want to allocate to your Clothing and lifestyle expenses: "))
    others = int(input("Enter your Budget for miscellenous expenses: "))
    bal_food = food
    bal_ent = entertainment
    bal_cloth = clothing
    bal_oth = others
    
a = Budget()
b = Budget()
c = Budget()
d = Budget()

x = input("Have you made any spends(type yes if you had or no if you didn't): ")

if x == 'yes' or 'YES' or 'Yes':
    q = input("What was your spending on(food/entertainment/clothing/others): ")
    if q == 'food' or 'FOOD' or 'Food':
        f = int(input("How much did you spend for the food: "))
        fb = a.bal_food-f
        print("The balance of the food budget is",fb)
    elif q == 'entertainment' or 'ENTERTAINMENT' or 'Entertainment':
        e = int(input('How much did you spend for the tickets: '))
        eb = a.bal_ent-e
        print("The balance of the entertainment budget is",eb)
    elif q == 'clothing' or 'CLOTHING' or 'Clothing':
        l = int(input('How much did you spend for the cloths: '))
        lb = a.bal_cloth-l
        print("The balance of the clothing budget is",lb)
    elif q == 'others' or 'OTHERS' or 'Others':
        o = int(input("How much did you spend miscellenously: "))
        ob = a.bal_oth-o
        print("The balance of your miscellenous budget is",ob)
    else:
        print("Sorry,try to type the categories mentioned above!!!")
else:
    print("Great!!! spend your money wisely.")