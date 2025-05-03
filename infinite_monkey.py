# Infinite monkey theorem
import string
import random
import time


# Variables needed for the theorem 
SHAKESPEARE = 'methinks it is like a weasel'
ALPHABET = string.ascii_lowercase + ' '


# Function that generates a string of random 28 characters
def monkey(n=28):
    monkey_string = list()
    
    for each_letter in range(n):
        monkey_string.append(random.choice(ALPHABET))
    return ''.join(monkey_string) #str
    


# A second function that compares the monkey generated text with Shakespeare,
# and gives it a score from 0 to 28 (perfect score)
def comparison(monkey_text):
    score = 0
    
    for shakespeare_letter, monkey_letter in zip(SHAKESPEARE, monkey_text):
        if shakespeare_letter == monkey_letter:
            score += 1
    return score #int


# Loop function for infinite monkey text and comparison with Shakespeare    
def infinite_monkey_theorem():
    
    monkey_press = monkey()
    iteration = 1
    
    BEST_TEXT = monkey_press
    
    try:
        while comparison(monkey_press) < 28:
        
            print(f"Monkey text: {monkey_press} Score: {comparison(monkey_press)} Iteration: {iteration}")
            time.sleep(0.2)
            iteration += 1
            
            if iteration % 1000 == 0:
                print('BEST SO FAR:', BEST_TEXT, 'Score: ', comparison(BEST_TEXT))
        
            monkey_press = monkey()
        
            if comparison(BEST_TEXT) < comparison(monkey_press):
                BEST_TEXT = monkey_press
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        print(f"BEST SO FAR: {BEST_TEXT}  Score: {comparison(BEST_TEXT)}")
        

        

if __name__=='__main__':
    infinite_monkey_theorem()


















