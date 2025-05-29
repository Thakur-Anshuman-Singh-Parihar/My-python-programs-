print("")
print("*" * 120)
print("                            📋 WELCOME TO THE TASK MANAGER 📋")
print("                         🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟\n")

alltask = []
rtask = []
ctask = []

for i in range(1, 1000):
    print("💡 You have 7 powerful functions. Choose wisely! 😎")
    print("     1️ . Add a task               2️ . View all tasks            3️.  View completed tasks")
    print("     4️ . View pending tasks       5️ . Update the task status")
    print("     6️ . Delete a task            7️ . 🚪 Exit")
    print("-" * 120)
    
    option = int(input("🎯 Enter the choice number ➡️  "))

    if option == 1:
        task = input("📝 Enter the task to add ➡️  ")
        alltask.append(task)
        rtask.append(task)
        print("✅ Task added successfully! 🥳")
        print("=" * 120)

    elif option == 2:
        print("📚  ALL TASKS")
        print("=================")
        if len(alltask) == 0:
            print("⚠️  There are no tasks to show!")
        for i in range(1, len(alltask)+1):
            print(i, ".", "📌", alltask[i-1])
        print("=" * 120)

    elif option == 3:
        print("🏁  COMPLETED TASKS")
        print("=========================")
        if len(ctask) == 0:
            print("⚠️  There are no completed tasks to show!")
        for i in range(1, len(ctask)+1):
            print(i, ".", "✅", ctask[i-1])
        print("=" * 120)

    elif option == 4:
        print("🕒  REMAINING TASKS")
        print("========================")
        if len(rtask) == 0:
            print("⚠️  There are no remaining tasks to show!")
        for i in range(1, len(rtask)+1):
            print(i, ".", "🕗", rtask[i-1])
        print("=" * 120)

    elif option == 5:
        print("🔄 Updating Task Status... 🔄")
        print("Here are your remaining tasks:")
        for i in range(1, len(rtask)+1):
            print(i, ".", "📌", rtask[i-1])
        com = int(input("✅ Enter the number of the task to mark as completed ➡️  "))
        ctask.append(rtask[com-1])
        rtask.pop(com-1)
        print("🎉 Task updated successfully!")
        print("🏁 Completed Tasks:")
        for i in range(1, len(ctask)+1):
            print(i, ".", "✅", ctask[i-1])
        print("🕒 Remaining Tasks:")
        for i in range(1, len(rtask)+1):
            print(i, ".", "🕗", rtask[i-1])
        print("=" * 120)

    elif option == 6:
        print("🗑️  DELETE OPTIONS:")
        print("1️. Delete from remaining tasks")
        print("2️. Delete from completed tasks")
        print("3️. Delete from all tasks")
        deltask = int(input("🔍 Enter the number (1, 2, or 3) ➡️  "))
        
        if deltask == 1:
            for i in range(1, len(rtask)+1):
                print(i, ".", "🕗", rtask[i-1])
            d = int(input("🗑️ Enter the task number to delete ➡️  "))
            rtask.pop(d-1)
            print("🗑️ here updated remaining tasks list")
            for i in range(1, len(rtask)+1):
                print(i, ".", "🕗", rtask[i-1])

        elif deltask == 2:
            for i in range(1, len(ctask)+1):
                print(i, ".", "✅", ctask[i-1])
            d = int(input("🗑️ Enter the task number to delete ➡️  "))
            ctask.pop(d-1)
            print("🗑️ here updated completed tasks list")
            for i in range(1, len(ctask)+1):
                print(i, ".", "✅", ctask[i-1])

        elif deltask == 3:
            for i in range(1, len(alltask)+1):
                print(i, ".", "📌", alltask[i-1])
            d = int(input("🗑️ Enter the task number to delete ➡️  "))
            alltask.pop(d-1)
            print("🗑️ here updated all tasks list")
            for i in range(1, len(alltask)+1):
                print(i, ".", "📌", alltask[i-1])

        print("=" * 120)

    elif option == 7:
        print("👋 Exiting Task Manager. Stay organized! 🧠🗂️")
        break

    else:
        print("🚨 Invalid option! Please choose between 1 - 7 only.")



            
        
