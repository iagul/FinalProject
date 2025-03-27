# ===========================================================================canculator=================================================================================================
# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     return x / y


# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")

# while True:
#     choice = input("Enter choice(1/2/3/4): ")

#     if choice in ('1', '2', '3', '4'):
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue

#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))

#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))

#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))

#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
        
#         TryAgain = input("Let's do next calculation? (yes/no): ")
#         if TryAgain == "no":
#           break
#     else:
#         print("Invalid Input")

# ==========================================================================guess number game=============================================================================================

# import random

# print("hi this is guess number game enter your number u have 7 chances(game will give you hints if your number is high game ill say thats its lower if ypur number is too low game will say its higher): ")

# GuessNumber = random.randrange(100)

# Chances = 7

# GuessCounter = 0

# while GuessCounter < Chances:

#     GuessCounter += 1
#     MyGuess = int(input("enter you number: "))

#     if MyGuess == GuessNumber:
#         print(f"the number is {GuessNumber} and you found it !! in the {GuessCounter} attempt")
#         break
#     elif GuessCounter >= Chances and MyGuess != GuessNumber:
#         print(f"opps sorry number is {GuessNumber} good luck next time")
#     elif MyGuess > GuessNumber:
#         print("number is higher")
#     elif MyGuess < GuessNumber:
#         print("number is lower")

# ==============================================================================hang man game=====================================================================================================

# import random
# from collections import Counter

# someWords = '''apple banana mango strawberry 
# orange grape pineapple apricot lemon coconut watermelon 
# cherry papaya berry peach lychee muskmelon'''

# someWords = someWords.split(' ')
# word = random.choice(someWords)

# if __name__ == '__main__':
#     print('Guess the word! HINT: word is a name of a fruit')

#     for i in word:
#         print('_', end=' ')
#     print()

#     playing = True
#     letterGuessed = ''
#     chances = len(word) + 2
#     correct = 0
#     flag = 0
#     try:
#         while (chances != 0) and flag == 0:  
#             print()
#             chances -= 1

#             try:
#                 guess = str(input('Enter a letter to guess: '))
#             except:
#                 print('Enter only a letter!')
#                 continue

#             if not guess.isalpha():
#                 print('Enter only a LETTER')
#                 continue
#             elif len(guess) > 1:
#                 print('Enter only a SINGLE letter')
#                 continue
#             elif guess in letterGuessed:
#                 print('You have already guessed that letter')
#                 continue

#             if guess in word:
#                 k = word.count(guess)
#                 for _ in range(k):
#                     letterGuessed += guess  

#             for char in word:
#                 if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
#                     print(char, end=' ')
#                     correct += 1
                
#                 elif (Counter(letterGuessed) == Counter(word)):
#                     print("The word is: ", end=' ')
#                     print(word)
#                     flag = 1
#                     print('Congratulations, You won!')
#                     break  
#                 else:
#                     print('_', end=' ')

#         if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
#             print('You lost! Try again..')
#             print('The word was {}'.format(word))

#     except KeyboardInterrupt:
#         print('Bye! Try again.')
#         exit()

# ===============================================================================Translator====================================================================================================

# from deep_translator import GoogleTranslator

# def translate_text(text, source_lang='auto', target_lang='fr'):
#     translator = GoogleTranslator(source=source_lang, target=target_lang)
#     return translator.translate(text)

# text = input("Enter the text to translate: ")

# target_lang = input("Enter target language (e.g., 'fr' for French, 'es' for Spanish, 'de' for German): ").lower()

# source_lang = 'auto'

# translated_text = translate_text(text, source_lang=source_lang, target_lang=target_lang)

# print(f"Translated Text ({target_lang}): {translated_text}")

# ============================================================ATM=======================================================================

# def show_balance(balance):
#     print(f"your balance is ${balance:.2f}")

# def deposit():
#     amount = float(input("enter a amount to deposit: "))

#     if amount < 0:
#         print("thats not a valid amount")
#         return 0 
#     else:
#         return amount

# def withdraw(balance):
#     amount = float(input("enter amount to be withdrawn: "))

#     if amount > balance:
#         print("u dont have enought money")
#         return 0 
#     elif amount < 0:
#         print("amount should bemore than 0")
#         return 0
#     else:
#         return amount
    
# def main():
#     balance = 0 
#     is_running = True

#     while is_running:
#         print("welcome to Banking program")


#         print("1.show balance")
#         print("2.deposit")
#         print("3.withdraw")
#         print("4.exit")

#         choice = input("enter your choice: ")

#         if choice == "1":
#             show_balance(balance)
#         elif choice == "2":
#             balance += deposit()
#         elif choice == "3":
#             balance -= withdraw(balance)
#         elif choice == "4":
#             is_running = False
#         else:
#             print("thats not valid choice")
            
        
#     print("thanks have a nice day")

# if __name__ == "__main__":
#     main()