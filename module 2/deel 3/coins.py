# name of student:
# number of student:
# purpose of program: Provide change with the minimum number of coins
# function of program: Calculate and return change using the least amount of coins
# structure of program: Input, calculation, output, loop, conditionals

# Request the amount to pay and the amount paid from the user
toPay = int(float(input('Amount to pay: ')) * 100)  # Convert the input to cents
paid = int(float(input('Paid amount: ')) * 100)  # Convert the input to cents
change = paid - toPay  # Calculate the change in cents

# Check if change is due
if change > 0:
    coinValues = [20, 100, 50, 20, 10, 5, 2, 1]  # Different coin values in cents

    # Initialize a dictionary to keep track of the number of each coin returned
    returnedCoins = {20: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    for coinValue in coinValues:
        while change >= coinValue:
            nrCoins = change // coinValue
            print('Return maximal', nrCoins, 'coins of', coinValue, 'cents!')
            nrCoinsReturned = int(input('How many coins of ' + str(coinValue) + ' cents did you return? '))
            change -= nrCoinsReturned * coinValue
            returnedCoins[coinValue] = nrCoinsReturned  # Update the dictionary

    # Print the returned coins
    print("\nReturned coins:")
    for coinValue, count in returnedCoins.items():
        if count > 0:
            print(f"{count} coin(s) of {coinValue} cents")

    # Check if all the required change is returned
    if change > 0:
        print('Change not returned:', str(change) + ' cents')
    else:
        print('Done')
else:
    print('No change due.')