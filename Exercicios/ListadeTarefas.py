'''
Cada tarefa será um item do dicionario com:

-> chave - título da tarefa
-> valor - o status ex("pendente" ou "concluído")
'''

tasks = {}

def add_task():
    task = input('Enter the task: ')
    tasks[task] = 'pending'
    print('📝Task successfully added ✅')

def complete_task():
    task = input('Enter the task to mark as completed: ')

    if task in tasks:
        tasks[task] = 'completed'
        print('Task completed ✔')
    else:
        print('❌ Task not found!')

def remove_task():
    task = input('Enter the task to remove: ')

    if task in tasks:
        del tasks[task]
        print('🗑 Task removed!')
    else:
        print('❌ Task not found!')

def list_tasks():
    print('🧾 Tasks List')

    for task, status in tasks.items():
        if status == 'completed':
            print(f'-> {task} - {status}✔')
        else:
            print(f'-> {task} - {status}')

#############################################

while True:
    print('Welcome to the Task List')
    print('Choose the desired option: ')
    print('1 - ✍ Add Task')
    print('2 - ✅ Mark as completed')
    print('3 - 🗑 Remove Task')
    print('4 - 🧾 List Tasks')
    print('5 - 🙋‍♂️ Sair')
    print()

    option = input()

    if option == '1':
        add_task()
    elif option == '2':
        complete_task()
    elif option == '3':
        remove_task()
    elif option == '4':
        list_tasks()
    elif option == '5':
        print('Bye! You left')
    else:
        print('Option not found! Try again')
    


