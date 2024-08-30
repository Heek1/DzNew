import os.path
while True:
 print("Hello,please choose what you want to do:")
 print("1 - Create a new file")
 print("2 - Add smth to file")
 print("3 - Read file")
 print("4 - Remove file")
 print("5 - Exit")
 userChoise=input("Enter what you want to do:\t")
 task="tasks.txt"
 if userChoise=="1":
    with open(task,"w")as file1:
        file1.write("Hello ")
        file1.close()
 elif userChoise=="2":
    entChoise=input("Enter what do you want to add:\t")
    with open(task,"a")as file1:
        file1.write(entChoise)
        file1.close()
 elif userChoise=="3":
     if os.path.exists(task):
      with open(task, "r") as file1:
        print(file1.read())
        file1.close()
     else:
         print("you don't have a file")
 elif userChoise=="4":
    if os.path.exists(task):
        os.remove(task)
        again=input("Do you want to create a file:\t")
        if again=="yes":
            with open(task, "w") as file1:
                file1.write("Hello")
                file1.close()
        elif again=="no":
            print("Ok")
        else:
            print("bye")
            break
    else:
        print("you don't have a file")
 elif userChoise=="5":
     print("bye")
     break
 else:
    print("Error,try again")
