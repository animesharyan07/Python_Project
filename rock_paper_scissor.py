import random

def play():
    user=input("Enter your choice 'R' , 'P' , 'S': ")
    computer=random.choice(['R','S','P'])

    if(user==computer):
        return "Tie"
    if(is_won(user,computer)):
        return "User Won"
    
    return f"Computer Won becoz computer choice is {computer}"
# r>s , s>p , p>r
def is_won(player1,player2):
    if(player1=='R' and player2=='S') or (player1=='S' and player2=='P') or(player1=='P' and player2=='R'):
        return True
    
    return False

print(play())