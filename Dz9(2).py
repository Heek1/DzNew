import random

def who():
 x=(input('Who is first? if computer,print "computer",if human,print "human"\t'))
 if x=="computer":
    com=random.choice(["камінь","ножиці","папір"])
    print(f"Computer select {com}")
    hum = input("Enter what you want to choose: камінь,ножиці,папір\t")
    if hum.strip()!="камінь"and hum.strip()!="ножиці"and hum.strip()!="папір":
        print("try again")
        return who()
 if x=="human":
    hum=input("Enter what you want to choose: камінь,ножиці,папір\t")
    if hum.strip()!="камінь"and hum.strip()!="ножиці"and hum.strip()!="папір":
        print("try again")
        return who()
    com = random.choice(["камінь", "ножиці", "папір"])
    print(f"Computer select {com}")
 else:
     print("try again")
     return who()

 if hum=="камінь" and com=="ножиці":
     print("You win!")
 if hum=="папір" and com=="камінь":
     print("You win!")
 if hum=="ножиці" and com=="папір":
     print("You win!")

 if hum=="камінь" and com=="камінь":
     print("Nobody win")
 if hum=="ножиці" and com=="ножиці":
     print("Nobody win")
 if hum=="папір" and com=="папір":
     print("Nobody win")

 if com=="камінь" and hum=="ножиці":
     print("Computer win!")
 if com=="папір" and hum=="камінь":
     print("Computer win!")
 if com=="ножиці" and hum=="папір":
     print("Computer win!")

who()




