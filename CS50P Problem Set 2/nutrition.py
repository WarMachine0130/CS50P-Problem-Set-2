while True:
    calorieReference = [['apple', 130], ['avacado', 50], ['banana', 110], ['cantaloupe', 50], ['grapefruit', 60], ['grapes', 90], 
                       ['honeydew', 50], ['kiwifruit', 90], ['lemon', 15], ['lime', 20], ['necterine', 60], ['orange', 80], 
                       ['peach', 60], ['pear', 100], ['pineapple', 50], ['plums', 70], ['strawberries', 50], ['sweet cherries', 100], 
                       ['tangerine', 50], ['watermelon', 80]]
    
    userInput = input('Item: ')
    userInput = userInput.lower()
    
    for x in range(len(calorieReference)):
        if userInput == calorieReference[x][0]:
            print(f'Calories: {calorieReference[x][1]}')
    
                        