import random

def Guess(x):
    low=1
    high=x
    feedback=''
    while(feedback!='c'):
        if low!=high:
            num=random.randint(low,high)
        else:
            num=low
        feedback=input(f"{num} is the right one ? Enter the option in between (C)-correct, (H)-high, (L)-low").lower()
        if(feedback=='h'):
            high=num-1
        elif feedback=='l':
            low=num+1
        
    print(f"Correct Guess the number {num}")


Guess(20)

