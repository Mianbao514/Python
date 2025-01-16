import time

counter = 0
purchased = True

while True:
    if counter == 100:
        # Display 100 in bold and stop the program
        print(f"\033[1m{counter}\033[0m")
        break

    print(counter, end='\r')  
    counter += 1
    time.sleep(0.1)
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

if purchased:
    print("Thank you!")
else:
    print("Altomatic purchased!")
    print(f"Resuming from {counter}...")
