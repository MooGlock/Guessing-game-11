import random
# setup 
num = random.randint(1,100)
guesses = [0]

print("WELCOME TO GUESS ME !")
print("I'M thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("if your guess is within 10 of my number, I'll tell you you're WARM")
print("if your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recemt guess, I'll say your getting WARMER")
print("LET'S PLAY!")

guesses = [0]
 
#while True:
guess_input = input("what is your guess? ")
guess = int(guess_input)

if guess <1 or guess > 100:

    #continue

 if guess == num:
   print(f'CORRECT! It took {len(guesses)} guesses.')
   print ('OUT OF BOUNDS!)'
    break
guesses.append (guess)
if guesses [-2]:
 if abs(num - guess) < abs(num-guesses'[-2])):
    (guesses[-2] will be >0)
  print('WARMER!')
#else:
  print('COLDER!')

#else:
  if abs (num-guess)  <= 10:
   print('WARM!')
  else:
   print"(COLD!")