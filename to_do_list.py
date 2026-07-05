# To Do List Project
mytasks=[]
def show_tasks():
   if(mytasks): 
        print("\nYour To-Do List:")
        for index, task in enumerate(mytasks, 1):
            print(f"{index}. {task}")
   else:
       print("\nYour To-Do List is empty.")             


def to_do_list():
  
    while(True):
        print("-------------To Do List-----------------")
        print("\n1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Quit")
        print("-----------------------------------------")
        choice=int(input("Enter your choice(1-4):"))
        if(choice==1):
            task = input("Enter the task you want to add: ")
            mytasks.append(task)
        elif(choice==2):
            show_tasks()
        elif(choice==3):
           show_tasks()
           try:
                task_num = int(input("Enter the task number to remove: "))
                if  task_num <= len(mytasks):
                    removed_task = mytasks.pop(task_num - 1)
                    print(f"Removed task: {removed_task}")
                else:
                    print("Invalid task number.")
           except ValueError:
                print("Invalid input!")   
        else:
            print("Bye Bye ")    
            break

# Main Calling 
to_do_list()