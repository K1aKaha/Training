import random

print ("\n=================================")  
print ("Rock Paper Scissors Lizard Spock")
print ("=================================")
print ("\nA variation of the classic game:")
print("\n1 ) ✊ (Rock)")
print("2 ) ✋ (Paper)")
print("3 ) ✌ (Scissors)")
print("4 ) 🦎 (Lizard)")
print("5 ) 🧙‍♂️ (Spock)")


player = int(input('\nPick a number (1-5): '))

if player not in [1, 2, 3, 4, 5]:
    wrong_input = "\nWrong input, please try again with numbers by 1 to 5."
    print(wrong_input)
    print("\n===================")
else:
    computer = random.randint(1, 5)

choices = {
    1: "✊ Rock",
    2: "✋ Paper",
    3: "✌ Scissors",
    4: "🦎 Lizard",
    5: "🧙‍♂️ Spock"}

print(f"\nYou choose:{choices[player]}")   
print(f"Computer chose: {choices[computer]}")

if player == computer:
        print("\nIt's a tie!")
elif (player == 1 and computer == 3) or \
     (player == 2 and computer == 1) or \
     (player == 3 and computer == 2)or \
     (player == 4 and computer == 5) or \
     (player == 4 and computer == 2) or \
     (player == 5 and computer == 1) or \
     (player == 5 and computer == 3) :
     
    print("\nYou won!")       
else: 
    print("\nYou lost!")

print("\n=================================")
