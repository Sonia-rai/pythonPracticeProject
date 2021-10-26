# HEALTHY PROGRAMMER

# Time duration-9am to 5pm

# Water-water.mp3(audio name)-3.5 l/day i.e.200ml-Every 30 min-Drank(input by user)

# Eyes-eyes.mp3(audio name)-Every 40 min-Eydone(user input)

# Physical exercise-physical.mp3(audio name)-Every 45 min-Exdone(user input)

# log the activity with time in a file to retrieve later


print("\t\t\t\t\t\t\t\t\t\t\t HEALTHY PROGRAMMER")

import time

from pygame import mixer

# importing specific function from pygame module


def datetime():

    import datetime

    return datetime.datetime.now()

def water():

    time.sleep(30*60)

    """This function contains use of pygame module to play a mp3 song
    
    things and storing all with time in a file"""


    while True:

        # the iterative loop while

        mixer.init()           # starting mixer

        mixer.music.load("water.mp3")   # Loading the song

        mixer.music.play()    # Playing the song

        print("Type codeword DRANK to stop:")

        query=input().upper()

        if query =='DRANK':

            mixer.music.stop()

            # Stopping the song

        else:

            print("Please enter right code word")

        with open("waterlog.txt",'a') as f:

            # writing in a file

            f.write(f"You have drank the water at"
                    +":"+str([str(datetime())])+"\n")

            break
            # using jump statement break here to go out of loop


def eyes():

    # defining a function

    time.sleep(10*60)

    # one of time function to rest the system for specified seconds
    # i.e. literally sleeping

    while True:

         mixer.init()

         mixer.music.load("eyes.mp3")

         mixer.music.play()

         print("Type codeword EYDONE to stop:")

         query = input()

         if query == 'EYDONE':

             # checking condition via if statement

             mixer.music.stop()

         else:

             print("Please enter right code word")

         with open("Eyexceriselog.txt", 'a') as f:

             f.write( f"You have done eyes exercise at"+":"+str([str(datetime())])+"\n")

             break


def physical():

    time.sleep(5*60)

    while True:

        mixer.init()

        mixer.music.load("physical.mp3")

        mixer.music.play()

        print("Type codeword EXERCISE DONE to stop:")

        query = input()

        if query == 'EXERCISE DONE':

            mixer.music.stop()

        else:

            print("Please enter right code word")

        with open("Exceriselog.txt", 'a') as f:

            f.write( f"You have done exercise at"+":"+str([str(datetime())])+"\n" )

            break


def retrieve():

    z=int(input("Press 1 to retrieve water drank data\nPress 2 to retrieve eyes exercise data"
    
                "\nPress 3 to retrieve physical exercise data  "))

    if z==1:

        print("The record of water drank is: ")

        with open ("waterlog.txt") as f:

            for i in f:

                print(i)

    elif z==2:

        print("The record of Eyes exercise done is: ")

        with open("Eyexerciselog.txt") as f:

            for i in f:

                print(i)

    if z==3:

        print("The record of Physical Exercise done is: ")

        with open ("Exerciselog.txt") as f:

            for i in f:

                print(i)

if __name__=="__main__":

    while True:

       water()
       eyes()
       physical()

       print("Do you want  to retrieve the data??")

       ch=input()

       if ch=="y":

          retrieve()

       elif ch=='n':

         continue

       else:

          print("Enter correct input!!")


# 1 loop hole is there in program: time is not managed according to office hours(9am to 5pm)

# erase when resolved