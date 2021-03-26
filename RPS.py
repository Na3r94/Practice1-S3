import random


items = ['Rock' , 'Paper' , 'Scissor']

# index = random.randint(0,2)

# computer_choice = items[index]

computer_score = 0
user_score = 0
while True:
    computer_choice = random.choice(items)

    print('0-Rock')

    print('1-Paper')

    print('2-Scissor')

    print('3- Exit')

# dastore digit ru peyda knm vas einke age str dadim betune errror bede

    print(computer_choice)
    
    user_choice_index = int(input())
    if user_choice_index == 3:
        if computer_score > user_score:
            print('Computer Wiinnns')

        elif user_score == computer_score:
            print('Mosaviiii')

        else:
            print('Useeer Wiiins')
        
        break
    user_choice = items[user_choice_index]
    print(user_choice)

    if computer_choice == 'Rock':
        if user_choice == 'Rock':
            print('Mosavi')

        elif user_choice == 'Scissor':
            print('Computer wins')
            computer_score += 1
        else:
            print('User wins')
            user_score += 1


    if computer_choice == 'Paper':
        if user_choice == 'Paper':
            print('Mosavi')

        elif user_choice == 'Rock':
            print('Computer wins')
            computer_score += 1
        else:
            print('User wins')
            user_score += 1


    if computer_choice == 'Scissor':
        if user_choice == 'Scissor':
            print('Mosavi')
        elif user_choice == 'Paper':
            print('Computer wins')
            computer_score += 1
        else:
            print('User wins')
            user_score += 1



    print  "User = " ,user_score
    print 'Com =' , computer_score

    