def main():
    fruits = [
        ('apple', 130), ('avocado', 50), ('banana', 110),
        ('Cantaloupe', 50),('Grapefruit', 60), ('Grapes', 90),
        ('Honeydew Melon', 50),('Kiwifruit', 90),('Lemon', 15),
        ('Lime', 20),('Nectarine', 60),('Orange', 60),
        ('Peach',60),('Pear',100),('Pineapple', 50),('Plums', 70),
        ('Strawberries', 50),('Sweet Cherries', 100),
        ('Tangerine', 50), ('Watermelon', 80)
        
        
        ]
    
    ask = input("Fruit: ")
    for fruit, calories in fruits:
        if ask.title() == fruit.title():
            print(calories)
            break
    else:
        print("Fruit not found")

main()
