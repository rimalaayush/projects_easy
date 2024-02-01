print("Welcome to Quiz Game")

interest=input("Do you want to play? ").upper()
if interest !="YES":
    print("So sad you lack knowledge")
    quit()

print("Okay let's play:) ")

score=0

ques1=input("Who is known as father of Computer ").lower()
if ques1 == "charles babbage":
   print("Wow correct")
   score +=1
else:
    print("Dhatteri wrong bhayo ni")

ques1=input("What does GPU stand for ").lower()
if ques1 == "graphics processing unit":
   print("Wow correct")
   score +=1
else:
    print("Dhatteri wrong bhayo ni")

ques1=input("What does CPU stand for ").lower()
if ques1== "central processing unit":
   print("Wow correct")
   score +=1
else:
    print("Dhatteri wrong bhayo ni")



print(score)
print((score/3)*100,"%")