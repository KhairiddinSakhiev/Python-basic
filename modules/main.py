from datetime import datetime
list_of_tasks = []
cnt=0
def add():
    global cnt
    cnt+=1
    task = {
        "id": cnt,
        "user": input("username: "),
        "task": input("task name: "),
        "due_date": input("due date: "),
        "is_completed": False,
        "created_at": datetime.now(),
    }
    list_of_tasks.append(task)

def get():
    for task in list_of_tasks:
        for key,value in task.items():
            print(key,value)
        print("__________________")

def get_by_id(id):
    for task in list_of_tasks:
        if task["id"]==id:
            print(task)


while True:
    print("""
    1. add
    2. get
    3. edit
    4. delete
    5. get by id
    6. exit
""")
    choice = input()
    match choice:
        case '1':
            add()
        case '2':
            get()
        case '5':
            get_by_id(int(input()))
        case '6':
            break
        case _:
            print("Command not found")


nums = [{"a":1, "b":2, "c":3},2,3,4,5,6,7]
nums.pop(4)

# HOME WORK
def delete(id):
    pass

def edit(id):
    pass

def todays_tasks():
    pass

def filter_by_user():
    pass



