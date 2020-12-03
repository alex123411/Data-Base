import psycopg2
import os
import controller

def MENU():

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
                controller.deletestudent(k)
                #if count == 0:
                #    print ("Student with such ID doesn`t exist")
            if v == 4:
                break
            

        if i == 3:
            
            b = input("\nu can edit smthing in this tables:\n 1 - faculties\n 2 - groups\n 3 - students \n 4 - cancel\n")
            os.system('cls||clear')
            b = int(b)
            if b == 1:
                k = input("Choose name of faculty ot edit\n")
                
                foundationyear = input("input new foundation year\n")
                foundationyear= int(foundationyear)
                dean = input("input new dean`s name\n")
                controller.editfaculty(k, foundationyear, dean)
            if b == 2:
                k = input("Choose group name to edit group\n")              
                             
                fac_name = input("input new faculty for this group\n")               
                head_of_group = input("Input new head of this group\n")
                student_count = input("Input new count of students\n")
                student_count = int(student_count)
                controller.editgroup(k, fac_name, head_of_group, student_count)
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


    return 1
