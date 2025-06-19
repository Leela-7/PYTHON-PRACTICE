player={'virat':1000,
         'rohit':900,
         'dhoni':800}
runs=player['virat']  # Accessing the value associated with the key 'virat'
runs2=player['rohit']  # Accessing the value associated with the key 'rohit'
print("Runs scored by Virat:", runs)
print("Runs scored by Rohit:", runs2)
if 'dhoni' in player:  # Checking if 'dhoni' is a key in the dictionary
    runs3=player['dhoni']  # Accessing the value associated with the key
    print("Runs scored by Dhoni:", runs3)
else:
    print("Enter a valid key")
