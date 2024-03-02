while True:
    totalCoins = 0
    
    while totalCoins < 50:
        print(f'Ammount Due: {50 - totalCoins}')
        insertCoin = int(input('Insert Coin: '))
        
        if insertCoin == 5 or insertCoin == 10 or insertCoin == 25:
            totalCoins += insertCoin
    
    print(f'Change Owed: {totalCoins - 50}')
    print('')