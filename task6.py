import csv

def write_into_csv(info_list):
    with open ('student_info.csv', 'a', newline = '') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Class", "DOB", "Contact"])
        writer.writerow(info_list)

if _name_ == '_main_':
    student_num = 1
    condition = True
while(condition):
    student_info = input("Please enter information for student #{} in the given format (Name Class DOB Contact): ".format(student_num))
    student_info_list = student_info.split(' ')
    print("Entered information is-\nName: {}\nClass: {}\nDOB: {}\nContact: {}".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
    check1 = input("Is the entered information correct?(yes/no): ")
    if check1 == "yes":
        write_into_csv(student_info_list)
        check2 = input("Do you want to continue?(yes/no): ")
        if check2 == "yes":
            condition = True
            student_num += 1
        else:
                condition = False
    elif check1 == "no":
        print("Please re-enter values")
