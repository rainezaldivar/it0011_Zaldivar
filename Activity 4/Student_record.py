def save_rec(data, file_path):
    with open(file_path, 'a') as f:
        f.write(data + '\n')
    print(f"Record added to {file_path}.")

def display_recs(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            print(content if content else "No records available.")
    except FileNotFoundError:
        print("No records found.")

def create_record(file_path):
    student_id = input("Enter Student ID: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    standing = input("Enter Class Standing: ")
    exam_score = input("Enter Major Exam Grade: ")
    rec_entry = f"ID: {student_id}\nName: {last_name}, {first_name}\nStanding: {standing}\nExam Grade: {exam_score}\n"
    save_rec(rec_entry, file_path)

data_file = "student_records.txt"

while True:
    print("====================================")
    print("  Student Record Management System  ")
    print("====================================")
    print("1. View Records")
    print("2. New Record")
    print("3. Quit")
    print()
    user_choice = input("Select an option: ")
    print()

    if user_choice == "1":
        display_recs(data_file)
        print()
    elif user_choice == "2":
        create_record(data_file)
        print()
    elif user_choice == "3":
        print("Exiting program.")
        print()
        break
    else:
        print("Invalid selection, please try again.")
        print()
