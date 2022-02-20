import random

def get_guess ():
    return input ("What is your guess ?")

# Generate code
def generate_code():
    digits = [str(num) for num in range (10)]
    #Shuffle digits
    random.shuffle(digits)
    return digits[:3]


#Generate clues
def generate_clues(code, userguess):
    if userguess == code:
        return "Code Cracked !"
    
    clues = []

    for ind,num in enumerate (userguess):
        if num == code [ind]:
            clues.append ("Match")
        elif num in code:
            clues.append ("Close")

    if clues == []:
        return ["nope"]
    else:
         return clues

# Case Logic
print ("Welcome code breaker")

secretcode = generate_code()

cluereport = []

while cluereport != "Code Cracked !":
    guess = get_guess ()
    cluereport = generate_clues (guess,secretcode)
    print ("Here is the result of your guess: ")
    for clue in cluereport:
        print (clue)