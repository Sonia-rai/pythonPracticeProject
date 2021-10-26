#  Health management system

# 3 clients-Harry,Rohan,Hammad

# total 6 user defined files

# write a function that when executed takes as input client name

# order of print :[]"chicken butter"

#define one more function to retrieve exercise or food for any client



def gettime():
    import datetime
    return datetime.datetime.now()



def enter(k):
    if k==1:
        c=int(input("Press 1 for Exercise\nPress 2 for food\n"))
        if c==1:
            value=input("Type here \n")
            with open('Harry_Exercise.txt','a') as f:
                f.write("["+str(gettime)+']'+ value+'\n')
                print("Written Successfully ")
        elif c==2:
            value = input("Type here \n")
            with open('Harry_food.txt', 'a') as f:
                f.write("[" + str(gettime) + ']' + value + '\n')
                print("Written Successfully ")


    elif k==2:
        c = int(input("Press 1 for Exercise\nPress 2 for food\n"))
        if c == 1:
            value = input("Type here \n")
            with open('Rohan_Exercise.txt', 'a') as f:
                f.write("[" + str(gettime) + ']' + value + '\n')
                print("Written Successfully ")
        elif c == 2:
            value = input("Type here \n")
            with open('Rohan_food.txt', 'a') as f:
                f.write("[" + str(gettime) + ']' + value + '\n')
                print("Written Successfully ")


    elif k==3:
        c = int(input("Press 1 for Exercise\nPress 2 for food\n"))
        if c == 1:
            value = input("Type here \n")
            with open('Hammad_Exercise.txt', 'a') as f:
                f.write("[" + str(gettime) + ']' + value + '\n')
                print("Written Successfully ")
        elif c == 2:
            value = input("Type here \n")
            with open('Hammad_food.txt', 'a') as f:
                f.write("[" + str(gettime) + ']' + value + '\n')
                print("Written Successfully ")


    else:
        print("INVALID INPUT")


def retrieve(z):

    if z==1:
        w=int(input("Press 1 for Exercise\nPress 2 for Food\n"))
        if w==1:
            with open("Harry_Exercise.txt") as f:
                for i in f:
                    print(i,end=' ')
        if w==2:
            with open("Harry_food.txt") as f:
                for i in f:
                    print(i,end=" ")


    elif z==2:
        w = int(input("Press 1 for Exercise\nPress 2 for Food\n"))
        if w == 1:
            with open("Rohan_Exercise.txt") as f:
                for i in f:
                    print(i, end=' ')
        if w == 2:
            with open("Rohan_food.txt") as f:
                for i in f:
                    print(i, end=" ")


    elif z==3:
        w = int(input("Press 1 for Exercise\nPress 2 for Food\n"))
        if w == 1:
            with open("Hammad_Exercise.txt") as f:
                for i in f:
                    print(i, end=' ')
        if w == 2:
            with open("Hammad_food.txt") as f:
                for i in f:
                    print(i, end=" ")


    else:
        print("INVALID INPUT")


x=int(input("Press 1 to Log the info\nPress 2 to Retrieve\n"))

if x==1:

    y=int(input(" Press the following key \n 1--Harry\n 2--Rohan\n 3--Hammad\n"))

    enter(y)
elif x==2:

    y=int(input(" Press the following key \n 1--Harry\n 2--Rohan\n 3--Hammad"))

    retrieve(y)

else:
   print("INVALID INPUT")