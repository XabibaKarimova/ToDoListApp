import datetime
from plyer import notification


def add_task(tasks):
    task = input("Enter the task: ")
    date_str = input("Enter the date in YYYY-MM-DD format: ")
    time_str = input("Enter the time in HH:MM format: ")

    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        time = datetime.datetime.strptime(time_str, "%H:%M")
        reminder_time = datetime.datetime.combine(date.date(), time.time())
        tasks.append((task, reminder_time))
        print("Task added successfully!")
    except ValueError:
        print("Invalid date or time format!")

def remove_task(tasks):
    task = input("Enter the task to remove: ")
    for item in tasks:
        if item[0] == task:
            tasks.remove(item)
            print("Task removed successfully!")
            return
    print("Task not found!")

def display_tasks(tasks):
    print("Tasks:")
    for item in tasks:
        print("Task:", item[0])
        print("Date:", item[1].date())
        print("Time:", item[1].time())
        print("----------------------")

def check_reminders(tasks):
    current_time = datetime.datetime.now()
    for task in tasks:
        if task[1] <= current_time:
            notification.notify(
                title="Todo List App",
                message=f"It's time for task: {task[0]}",
                timeout=10
            )

def main():
    tasks = []
    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            display_tasks(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice!")

        check_reminders(tasks)

if __name__ == '__main__':
    main()