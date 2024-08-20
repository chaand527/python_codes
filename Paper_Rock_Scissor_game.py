import random,sys
print('Rock,Paper,Scissor')
wins = 0
losses = 0
ties = 0
 
while True:
    print(f'{wins}-wins {losses}-losses {ties}-ties ')
    while True:
        print('Enter your move -- (r)ock (p)aper (s)cissor (q)uit   ')
        playe_move = input(': ')

        if playe_move == 'q':
            sys.exit()
        elif playe_move in ('r','p','s') :
            break
        else:
            print('Invalid input...Enter either of r,p,s') 
    if playe_move == 'r':
        print('Rock versus......')      
    elif playe_move == 'p':
        print('Paper versus.....')
    elif playe_move == 's':
        print('Scissor versus.....')   


    random_number = random.randint(1,3)
    if random_number == 1 :
        computer_move = 'r'
        print('Rock....')
    elif random_number == 2 :
        computer_move = 's'
        print('Scissors...')
    else:
        computer_move = 'p'
        print('Paper...')  

    if playe_move == computer_move:
        print('Its a tie..') 
        ties +=1
    elif playe_move == 'r' and computer_move == 's' :
        print('You win..')   
        wins += 1  
    elif playe_move == 's' and computer_move == 'p' :
        print('You win..')   
        wins += 1      
    elif playe_move == 'p' and computer_move == 'r' :
        print('You win..')   
        wins += 1  

    elif playe_move == 'r' and computer_move == 'p' :
        print('You loose..')   
        losses += 1  
    elif playe_move == 'p' and computer_move == 's' :
        print('You loose..')   
        losses += 1 
    elif playe_move == 's' and computer_move == 'r' :
        print('You loose..')   
        losses += 1             
