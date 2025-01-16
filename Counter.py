import time

counter = 0
purchased = True

while True:
    print(counter, end='\r')
    counter += 1
    time.sleep(0.1)
    
    if counter == 20:
        coin = input("Would you like to buy 20 coins with 20 coins? (Y/N): ")
        
        if coin.upper() == "N":
            purchased = False
            for x in range(1,5):
                finalDecision = input("Are you sure? It's a big deal! (Y/N)")
                purchased = finalDecision.upper() == "Y"
                if purchased:
                    break
        break

if purchased:
    print("Thank you!")
else:
    print("You missed out!")
