import os
print(f"Choose a option\n")
print("1: Create\n")
print("2: Update\n")
print("3: Delete\n")
print("4: View/Track\n")
option=int(input())
if option == 1:
    todolist=[]
    n=int(input("Enter number of task to be performed within the day"))
    file=open('todolist.txt','w')
    for i in range(0,n):
        task=input()
        todolist.append(task)
    file.write(print(todolist))
    file.close()
elif option == 2:
    file=open('todolist.txt','a')
    n=int(input("Enter number of task to be added"))
    for i in range(0,n):
        task=input()
        file.write(task)
    file.close()
elif option==3:
    if os.path.exists("todolist.txt"):
        os.remove("todolist.txt")
        print("File deleted successfully")
    else:
        print("File doesnot exist or is already deleted")
    file.close()
elif option == 4:
    file=open('todolist','r')
    print(file.read())