
# Student Record Management System using Singly Linked List

# Node class
class Node:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.next = None


# Linked List class
class StudentLinkedList:
    def __init__(self):
        self.head = None

    # Add student
    def add(self, roll_no, name, marks):
        new_node = Node(roll_no, name, marks)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

        print("Student record added successfully.")

    # Display students
    def display(self):
        if self.head is None:
            print("No student records available.")
            return

        print("\n----- STUDENT RECORDS -----")
        temp = self.head

        while temp is not None:
            print("Roll No:", temp.roll_no)
            print("Name:", temp.name)
            print("Marks:", temp.marks)
            print("-----------------------")
            temp = temp.next

    # Search student
    def search(self, roll_no):
        temp = self.head

        while temp is not None:
            if temp.roll_no == roll_no:
                print("\nStudent Found")
                print("Roll No:", temp.roll_no)
                print("Name:", temp.name)
                print("Marks:", temp.marks)
                return
            temp = temp.next

        print("Student record not found.")

    # Sort records
    def sort(self, choice, order):
        if self.head is None:
            print("List is empty.")
            return

        if choice not in (1, 2) or order not in (1, 2):
            print("Invalid sorting choice.")
            return

        current = self.head

        while current is not None:
            next_node = current.next

            while next_node is not None:
                if choice == 1:
                    value1 = current.roll_no
                    value2 = next_node.roll_no
                else:
                    value1 = current.marks
                    value2 = next_node.marks

                # Ascending order
                if order == 1 and value1 > value2:
                    self.swap_data(current, next_node)

                # Descending order
                elif order == 2 and value1 < value2:
                    self.swap_data(current, next_node)

                next_node = next_node.next

            current = current.next

        print("Records sorted successfully.")

    # Swap student data
    def swap_data(self, node1, node2):
        node1.roll_no, node2.roll_no = node2.roll_no, node1.roll_no
        node1.name, node2.name = node2.name, node1.name
        node1.marks, node2.marks = node2.marks, node1.marks

    # Delete student
    def delete(self, roll_no):
        if self.head is None:
            print("List is empty.")
            return

        # Delete first node
        if self.head.roll_no == roll_no:
            self.head = self.head.next
            print("Student record deleted successfully.")
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.roll_no == roll_no:
                temp.next = temp.next.next
                print("Student record deleted successfully.")
                return
            temp = temp.next

        print("Student record not found.")

    # Update student
    def update(self, roll_no):
        temp = self.head

        while temp is not None:
            if temp.roll_no == roll_no:
                print("Current Name:", temp.name)
                print("Current Marks:", temp.marks)

                temp.name = input("Enter new name: ")
                temp.marks = float(input("Enter new marks: "))

                print("Student record updated successfully.")
                return

            temp = temp.next

        print("Student record not found.")


# Main program
student_list = StudentLinkedList()

while True:
    print("\n====== STUDENT RECORD MANAGEMENT ======")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Display Students")
    print("6. Sort Records")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        student_list.add(roll_no, name, marks)

    elif choice == 2:
        roll_no = int(input("Enter Roll No to delete: "))
        student_list.delete(roll_no)

    elif choice == 3:
        roll_no = int(input("Enter Roll No to update: "))
        student_list.update(roll_no)

    elif choice == 4:
        roll_no = int(input("Enter Roll No to search: "))
        student_list.search(roll_no)

    elif choice == 5:
        student_list.display()

    elif choice == 6:
        print("\nSort By:")
        print("1. Roll Number")
        print("2. Marks")

        sort_choice = int(input("Enter choice: "))

        print("\nOrder:")
        print("1. Ascending")
        print("2. Descending")

        order = int(input("Enter order: "))

        student_list.sort(sort_choice, order)
        student_list.display()

    elif choice == 7:
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")
