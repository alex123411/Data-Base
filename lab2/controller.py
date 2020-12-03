
import view
import model

def start():
    print("START!")
    x = view.MENU()
    if x == 0:
        print("Goodbye!")

def addfaculty(x,y,z):
    y = int(y)
    model.add_faculty(x,y,z)

def addgroup(x,y,z,f):
    f = int(f)
    model.add_group(x,y,z,f)

def addstudent(x,y,z,f):
    try:
        int(x)
    except ValueError:
        print("Please make sure that student`s id is a number and try again\n")
        return

    y = model.add_student(x,y,z,f)
    return y

def deletefaculty(fac_name):
    model.deletefaculty(fac_name)
    

def deletegroup(group_name):
    model.deletegroup(group_name)

def deletestudent(student_name):
    count  = model.deletestudent(student_name)
    return count

def editfaculty(k, new_fac_name, foundationyear, dean):
    model.editfaculty(k, new_fac_name, foundationyear, dean)

def editgroup(k, new_group_name, fac_name, head_of_group, student_count):
    model.editgroup(k, new_group_name, fac_name, head_of_group, student_count)

def editstudent(id_, gr_name, name_surname, birthdate):
    model.editstudent(id_, gr_name, name_surname, birthdate)

def generate_in_faculty(num):
    model.generate_in_faculty(num)

def generate_in_group(num):
    model.generate_in_group(num)

def find_all_students_on_faculty(fac_name):
    records = model.find_all_students_on_faculty(fac_name)
    return records

def find_all_students_whoose_group_count_is_more_then(num):
    records = model.find_all_students_whoose_group_count_is_more_then(num)
    return records

def who_is_a_dean_4_yhis_group(group_name):
    records = model.who_is_a_dean_4_yhis_group(group_name)
    return records