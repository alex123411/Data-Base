import psycopg2
import os
import controller

def MENU():
    connection = psycopg2.connect(host="localhost", port = 5432, database="Lab1", user="postgres", password="1234")
    cursor = connection.cursor()

    while True:       
        i = input("u have this commands:\n 1 - add\n 2 - delete\n 3 - edit\n 4 - exit \n 5 - generate random data\n 6 - filtrationsn\nselect a command u wanna use\n")
        i = int(i)
        os.system('cls||clear')
        if i == 1:
            l = input("u can add smthing in this tables:\n 1 - faculties\n 2 - groups\n 3 - students\n 4 - cancel \nchoose the table\n ") 
            os.system('cls||clear')
            l = int(l)
            if l == 1:
                x = input("input faculty`s name ")                 
                y = input("input its foundation year ")
                z = input("input its dean name ")
                controller.addfaculty(x,y,z)
                
            if l == 2:
                print("u work in table of groups\nu already have this\n")
                print("\n")
                x = input("input group`s name ")                 
                y = input("input its faculty name ")
                z = input("input its head name ")
                f = input("input count of students in this group ")
                controller.addgroup(x,y,z,f)

            if l == 3:
                print("u work in table of students\nAdd new student")
                x = input("input student`s id  ")                
                y = input("input grou where this student is ")
                z = input("input his name and surname ")
                f = input("input his birthdate ")
                vv = controller.addstudent(x,y,z,f)
                if vv == 0:
                    print("Sorry, you couldn`t add this student. Student with such id already exists or there is no such group\n")
            if l == 4:
                break
        if i == 2:
            v = input("u can delete smthing in this tables:\n 1 - faculties\n 2 - groups\n 3 - students \n 4 - cancel\n")
            os.system('cls||clear')
            v = int(v)
            if v == 1:
                print("delete hear")
                k = input("Input name of faculty ot delete\n")
                controller.deletefaculty(k)
            if v == 2:
                print("delete hear")
                k = input("Input goup name to delete group\n")
                controller.deletegroup(k)
            if v == 3:
                print("delete hear")
                k = input("Input student`s id to delete student\n")
                count = controller.deletestudent(k)
                if count == 0:
                    print ("Student with such ID doesn`t exist")
            if v == 4:
                break
            

        if i == 3:
            
            b = input("\nu can edit smthing in this tables:\n 1 - faculties\n 2 - groups\n 3 - students \n 4 - cancel\n")
            os.system('cls||clear')
            b = int(b)
            if b == 1:
                k = input("Choose name of faculty ot edit\n")
                new_fac_name = input("INput new name for this faculty\n")
                foundationyear = input("input new foundation year\n")
                foundationyear= int(foundationyear)
                dean = input("input new dean`s name\n")
                controller.editfaculty(k, new_fac_name, foundationyear, dean)
            if b == 2:
                k = input("Choose group name to edit group\n")              
                new_group_name = input("Choose new group name\n")               
                fac_name = input("input new faculty for this group\n")               
                head_of_group = input("Input new head of this group\n")
                student_count = input("Input new count of students\n")
                student_count = int(student_count)
                controller.editgroup(k, new_group_name, fac_name, head_of_group, student_count)
            if b == 3:               
                id_ = input("Choose student`s id to edit student\n")
                id_ = int(id_)
                gr_name = input("input new group name for this student\n")
                gr_name = str(gr_name)
                name_surname = input("input new name and surname student\n")
                name_surname = str(name_surname)
                birthdate = input("input new birthdate for this student\n")
                birthdate = str(birthdate)
                controller.editstudent(id_, gr_name, name_surname, birthdate)
            if b == 4:
                break

        if i == 4:
            return 0

        if i == 5:
            dd = input("Choose in which table u wanna generate\n 1 - faculty\n 2 - group\n")
            dd = int(dd)
            
            if dd == 1:
                lp = input("input number of random rows\n")
                controller.generate_in_faculty(lp)
            if dd == 2:
                lp = input("input number of random rows\n")
                controller.generate_in_group(lp)
        if i == 6:
            cc = input("Choose which filtrarion u wanna use\n 1 - find all students on this faculty\n 2 - find all students whoose group count is more then\n 3 - find a dean for this group\n")
            cc = int(cc)
            os.system('cls||clear')
            if cc == 1:
                x = input("INput a faculty u are interested in ")
                records = controller.find_all_students_on_faculty(x)
                for row in records:
                    print("---------------")               
                    print("Id = ", row[0], )
                    print("Name = ", row[1])
                    print("birthdate  = ", row[2])
            if cc == 2:
                x = input("INput a number of students ")
                records = controller.find_all_students_whoose_group_count_is_more_then(x)
                for row in records: 
                    print("---------------")              
                    print("Id = ", row[0], )
                    print("Name = ", row[1])
                    print("birthdate  = ", row[2])
                    print("numb of students in this group  = ", row[3])
            if cc == 3:
                x = input("INput a group name to find its dean ")
                records = controller.who_is_a_dean_4_yhis_group(x)
                  
                    
                print("dean  = ", records[0])
    cursor.close()
    connection.close()

    return 1
