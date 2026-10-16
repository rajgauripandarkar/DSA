
from collections import deque

queue = deque()

while True:
    print("\n--- Event Processing System ---")
    print("1. Add Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel Event")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Add Event
    if choice == 1:
        event = input("Enter event: ")
        queue.append(event)
        print("Event added:", event)

    # Process Next Event
    elif choice == 2:
        if queue:
            event = queue.popleft()
            print("Event processed:", event)
        else:
            print("Queue is empty.")

    # Display Pending Events
    elif choice == 3:
        if queue:
            print("Pending Events:", list(queue))
        else:
            print("No pending events.")

    # Cancel Event
    elif choice == 4:
        event = input("Enter event to cancel: ")
        if event in queue:
            queue.remove(event)
            print("Event cancelled:", event)
        else:
            print("Event not found.")

    # Exit
    elif choice == 5:
        print("Exiting Event Processing System.")
        break

    else:
        print("Invalid choice!")
