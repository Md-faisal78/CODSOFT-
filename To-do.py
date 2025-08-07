tasks=[]
def view():
    if not tasks:
        print("No tasks")
    else:
        print("\nYour Tasks")
        for i ,task in enumerate(tasks):
            status = "✅" if task["done"] else "❌"
            print(f"{i + 1}. {task['title']} [{status}]")

def Add():
    name=input("Enter the task name: ")
    tasks.append({"title":name,"done":False})
    print("Task added!")
    
def mark():
    view()
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        tasks[task_num - 1]["done"] = True
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete():
    view()
    try:
        task_num = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_num - 1)
        print(f"Task '{removed['title']}' deleted!")
    except (IndexError, ValueError):
        print("Invalid task number.")

while True:
    print("\n")
    print("======To-do:====\n1.View tasks\n2.Add tasks\n3.Mark as completed\n4.Delete task\n5.Exit")
    n=int(input("Enter your choice(1-5):  "))
    match n:
        case 1:
            view()
        case 2:
            Add()
        case 3:
            mark()
        case 4:
            delete()
        case 5:
            print("Goodbye! 👋 and Thnk u")
            break
        case _:
            print("Invalid selection")