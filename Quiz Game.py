print("Welcome the quiz game!")

name=input("Would you like to start? ")

if name.lower() != "yes":
    quit()

print("Okey let's start. ")
score=0

answer=input("What does CPU stand for? ")
if answer.lower() =="central processing unit":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")
   
answer=input("What does GPU stand for? ")
if answer.lower()=="graphics processing unit":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")
   
answer=input("What does RAM stand for? ")
if answer.lower()=="random access memory":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")
   
answer=input("What does PSU stand for? ")
if answer.lower()=="power supply":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")
   

print("You got "+str(score)+" questin(s) correct! ")
print("You got "+str((score/4)*100)+" %.")