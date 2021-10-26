#creating a fun game snake,water,gun
# directions
#import random.choice module
#take user's input
#generate computer output
#check results and declare who wins
#No.of game --10(use while loop)
#No.of games win by computer and user
#then declare winner of whole game

print('\t\t\t\t\t\t\t\t\t\t WELCOME TO SNAKE,WATER,GUN GAME \t\t\t')

import random
chr=['Snake','Water','Gun']
user_wincount=comp_winercount=draw_count=0
n=1
e=int(input("How many rounds do you wanna play??"))
try:

    while n<=e:
      print("Press 1 for Snake\n2 for Water\n3 for Gun\n")
      user_input=int(input('Enter Here:'))
      comp_input=random.choice(chr)

      if user_input ==1:

        if comp_input =='Water':

            print(comp_input)
            print("COMPUTER WINS\n")
            comp_winercount+=1

        elif comp_input =='Snake':

            print("IT'S A DRAW ")
            draw_count += 1
            print(comp_input)

        elif comp_input =='Gun':

              print(comp_input)
              print("YOU WIN!!")
              user_wincount+=1

      elif user_input == 2:

        if comp_input =='Snake':

            print(comp_input)
            print("COMPUTER WINS\n")
            comp_winercount += 1

        elif comp_input =='Water':

            print(comp_input)
            draw_count +=1
            print("IT'S A DRAW ")

        elif comp_input =='Gun':

            print(comp_input)
            print("YOU WIN !!")
            user_wincount+=1

      elif user_input ==3:

        if comp_input =='Water':

           print(comp_input)
           print("COMPUTER WINS\n")
           comp_winercount += 1

        elif comp_input =='Snake':

            print(comp_input)
            print("YOU WIN")
            user_wincount += 1

        elif comp_input =='G':

            print(comp_input)
            draw_count += 1
            print("IT'S DRAW")

      else:

          print("Enter correct code")
          continue

      print(f"YOU HAVE NOW {e-n} ROUNDS LEFT")
      n+=1

    print("NO.OF ROUNDS WON BY COMPUTER",comp_winercount)
    print("NO.OF ROUNDS WON BY PLAYER",user_wincount)
    print("NO.OF ROUNDS DRAW ARE",draw_count)
    if comp_winercount>user_wincount:
       print("COMPUTER WINS BY",comp_winercount-user_wincount)
    elif comp_winercount==user_wincount:
       print("IT'S A TIE BETWEEN YOU AND COMPUTER")
       print('DRAW BY',draw_count)

    else:
        print("PLAYER WINS BY", user_wincount-comp_winercount)
except ValueError:
    print('its error in here \nType correct input')