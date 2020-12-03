
import view
import model

url = 'postgresql://postgres:1234@localhost:5432/Lab1'
#Base.metadata.create_all(engine)

db = model.PostgreSQL_base(url)

def start():
    print("START!")
    x = view.MENU()
    if x == 0:
        print("Goodbye!")

def addfaculty(x,y,z):
    y = int(y)
    db.add_faculty(x,y,z)

def addgroup(x,y,z,f):
    f = int(f)
    db.add_group(x,y,z,f)

def addstudent(x,y,z,f):
    try:
        int(x)
    except ValueError:
        print("Please make sure that student`s id is a number and try again\n")
        return

    db.add_student(x,y,z,f)
    return y

def deletefaculty(fac_name):
    db.delete_faculty(fac_name)
    

def deletegroup(group_name):
    db.delete_group(group_name)

def deletestudent(student_name):
    db.delete_student(student_name)
    #return count

def editfaculty(k,  foundationyear, dean):
    db.update_faculty(k, foundationyear, dean)

def editgroup(k, fac_name, head_of_group, student_count):
    db.update_group(k, fac_name, head_of_group, student_count)

def editstudent(id_, gr_name, name_surname, birthdate):
    db.update_student(id_, gr_name, name_surname, birthdate)
