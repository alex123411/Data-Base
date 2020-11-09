
import psycopg2

def add_faculty(x,y,z):
    connection = psycopg2.connect(host="localhost", port = 5432, database="Lab1", user="postgres", password="1234")
    cursor = connection.cursor()
    postgres_insert_query = """ INSERT INTO faculty (fac_name, foundation_year, dean) VALUES (%s,%s,%s)"""
    try:
        record_to_insert = (x, y, z)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into faculties table\n")
    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into faculties table, this faculty already exists")

    cursor.close()
    connection.close()

def add_group(x,y,z,f):
    connection = psycopg2.connect(host="localhost", port = 5432, database="Lab1", user="postgres", password="1234")
    cursor = connection.cursor()
    try:
        postgres_insert_query = """ INSERT INTO public.group (group_name, fac_name, head_of_group, student_count) VALUES (%s,%s,%s,%s)"""
        record_to_insert = (x, y, z, f)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into groups table\n")
    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into groupss table, group with such name already exists or there is no such faculty" , error)
    cursor.close()
    connection.close()

def add_student(x,y,z,f):
    connection = psycopg2.connect(host="localhost", port = 5432, database="Lab1", user="postgres", password="1234")
    cursor = connection.cursor()
    postgres_insert_query = """ INSERT INTO public.student (student_id, group_name, name_surname, birthdate) VALUES (%s,%s,%s,%s)"""
    try:
        record_to_insert = (x, y, z, f)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into students table\n")
    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into student table, student with such id already exists or there is no such group", error)  
    cursor.close()
    connection.close()  

def show_faculties():
    connection = psycopg2.connect(host="localhost", port = 5432, database="Lab1", user="postgres", password="1234")
    cur = connection.cursor()
    cur.execute("SELECT fac_name, foundation_year, dean FROM public.faculty")
    rows = cur.fetchall()
    print("faculty name    foundation year    Dean ")
    for row in rows:  
        print(row[0] +' '+ str(row[1])+ ' ' + row[2])              
    cur.close()
    connection.close()   

def show_students():
    connection = psycopg2.connect(host="localhost", port = 5432, database="Lab1", user="postgres", password="1234")
    cur = connection.cursor()
    cur.execute("SELECT student_id, group_name, name_surname, birthdate FROM public.student")
    rows = cur.fetchall()
    print("student_id    group_name  name_surname   birthdate ")
    for row in rows:  
        print( str(row[0]) +' '+ str(row[1])+ ' ' + row[2]+ ' ' + str(row[3]))       
    cur.close()
    connection.close()  

def show_groups():
    connection = psycopg2.connect(host="localhost", port = 5432, database="Lab1", user="postgres", password="1234")
    cur = connection.cursor()
    cur.execute("SELECT group_name, fac_name, head_of_group, student_count FROM public.group")
    rows = cur.fetchall()
    print("group_name   its faculty    head_of_group     student_count ")
    for row in rows:  
        print(row[0] +' '+ str(row[1])+ ' ' + row[2]+ ' ' +  str(row[3]))
                 
    cur.close()
    connection.close()   

def deletefaculty(fac_name):
    try:
        connection = psycopg2.connect(host="localhost", port = 5432, database="Lab1", user="postgres", password="1234")

        cursor = connection.cursor()

        #deleting students
        sql_sel_query = """SELECT DISTINCT group_name FROM public.group WHERE fac_name = %s"""
        cursor.execute(sql_sel_query, (fac_name, ))
        rows = cursor.fetchall()
        
        for row in rows: 
            sql_delete_query = """Delete from student where group_name = %s"""
            cursor.execute(sql_delete_query, (row[0], ))
            connection.commit()
            count = cursor.rowcount
            print(count, "Records were deleted ")

        #deleting groups
        sql_delete_query = """Delete from public.group where fac_name = %s"""
        cursor.execute(sql_delete_query, (fac_name, ))
        connection.commit()
        count = cursor.rowcount
        print(count, "Records were deleted ")

        # Update single record now
        sql_delete_query = """Delete from public.faculty where fac_name = %s"""
        cursor.execute(sql_delete_query, (fac_name, ))
        connection.commit()
        count = cursor.rowcount
        print(count, "Records were deleted ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

def deletestudent(student_name):
    try:
        connection = psycopg2.connect(host="localhost", port = 5432, database="Lab1", user="postgres", password="1234")

        cursor = connection.cursor()

        # Update single record now
        sql_delete_query = """Delete from public.student where student_id = %s"""
        cursor.execute(sql_delete_query, (student_name, ))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

def deletegroup(group_name):
    try:
        connection = psycopg2.connect(host="localhost", port = 5432, database="Lab1", user="postgres", password="1234")

        cursor = connection.cursor()
        sql_delete_query = """Delete from public.student where group_name = %s"""
        cursor.execute(sql_delete_query, (group_name, ))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")
        # Update single record now
        sql_delete_query = """Delete from public.group where group_name = %s"""
        cursor.execute(sql_delete_query, (group_name, ))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")

    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            



def editstudent(id_, gr_name, name_surname, birthdate):
    try:
        connection = psycopg2.connect(host="localhost", port = 5432, database="Lab1", user="postgres", password="1234")

        cursor = connection.cursor()
        # Update multiple records
        sql_update_query = """Update public.student set group_name = %s, name_surname = %s, birthdate = %s where student_id = %s"""
        cursor.execute(sql_update_query, (gr_name, name_surname, birthdate, id_))
        connection.commit()

        row_count = cursor.rowcount
        print(row_count, "Records Updated")

    except (Exception, psycopg2.Error) as error:
        print("Error while updating PostgreSQL table", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            

def editgroup(group_name, new_group_name, fac_name, head_of_group, student_count):
    try:
        connection = psycopg2.connect(host="localhost", port = 5432, database="Lab1", user="postgres", password="1234")

        cursor = connection.cursor()
        
        #create new group with new_group_name
        postgres_insert_query = """ INSERT INTO public.group (group_name, fac_name, head_of_group, student_count) VALUES (%s,%s,%s,%s)"""
        record_to_insert = (new_group_name, fac_name, head_of_group, student_count)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()

        #update all students where this grop is
        sql_update_query = """ Update public.student set group_name = %s WHERE group_name = %s"""
        cursor.execute(sql_update_query, (new_group_name, group_name))
        connection.commit()

        #delete created group
        sql_delete_query = """Delete from public.group where group_name = %s"""
        cursor.execute(sql_delete_query, (group_name, ))
        connection.commit()     

    except (Exception, psycopg2.Error) as error:
        print("Error while updating PostgreSQL table", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            

def editfaculty(faculty_name, new_fac_name, foundationyear, dean):
    try:
        connection = psycopg2.connect(host="localhost", port = 5432, database="Lab1", user="postgres", password="1234")

        cursor = connection.cursor()
        
        #create new faculty with new_fac_name
        postgres_insert_query = """ INSERT INTO public.faculty (fac_name, foundation_year, dean) VALUES (%s,%s,%s)"""
        record_to_insert = (new_fac_name, foundationyear, dean)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()

        #update all groups where this faculty is
        sql_update_query = """ Update public.group set fac_name = %s WHERE fac_name = %s"""
        cursor.execute(sql_update_query, (new_fac_name, faculty_name))
        connection.commit()

        #delete faculty
        sql_delete_query = """Delete from public.faculty where fac_name = %s"""
        cursor.execute(sql_delete_query, (faculty_name, ))
        connection.commit()     

    except (Exception, psycopg2.Error) as error:
        print("Error while updating PostgreSQL table", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()




def generate_in_faculty(number):
    try:
        connection = psycopg2.connect(host="localhost", port = 5432, database="Lab1", user="postgres", password="1234")

        cursor = connection.cursor()

        postgres_insert_query = """
        INSERT INTO public.faculty  (fac_name, foundation_year, dean) SELECT MD5(random()::text), trunc(random()*%s)::int, MD5(random()::text) FROM generate_series(1,%s)"""
        cursor.execute(postgres_insert_query, (number,number))
        connection.commit() 
    except (Exception, psycopg2.Error) as error:
        print("Error while updating PostgreSQL table", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


def generate_in_group(number):
    try:
        connection = psycopg2.connect(host="localhost", port = 5432, database="Lab1", user="postgres", password="1234")

        cursor = connection.cursor()

        postgres_insert_query = """
        INSERT INTO public.group  (group_name, fac_name, head_of_group, student_count) 
        SELECT MD5(random()::text), (SELECT fac_name  FROM public.faculty ORDER BY random() LIMIT 1) , MD5(random()::text), trunc(random()*%s)::int FROM generate_series(1,%s)"""
        cursor.execute(postgres_insert_query, (number,number))
        connection.commit() 
    except (Exception, psycopg2.Error) as error:
        print("Error while updating PostgreSQL table", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

def find_all_students_on_faculty(s):
    try:
        print(" ")
        connection = psycopg2.connect(host="localhost", port = 5432, database="Lab1", user="postgres", password="1234")

        cursor = connection.cursor()
        query = """with x as(SELECT group_name from public.group WHERE fac_name = %s)
        select student_id , name_surname, birthdate from public.student h inner join(select* from x) m on h.group_name = m.group_name"""
        cursor.execute(query, (s, ))
        connection.commit() 
        recoreds = cursor.fetchall()
        return recoreds
    except (Exception, psycopg2.Error) as error:
        print("Error while updating PostgreSQL table", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            
def find_all_students_whoose_group_count_is_more_then(і):
    try:      
        print(" ")
        connection = psycopg2.connect(host="localhost", port = 5432, database="Lab1", user="postgres", password="1234")
        cursor = connection.cursor()
        query = """with x as(SELECT group_name, student_count from public.group WHERE student_count > %s)
        select student_id , name_surname, birthdate , student_count from public.student h inner join(select* from x) m on h.group_name = m.group_name"""
        cursor.execute(query, (і, ))
        connection.commit() 
        recoreds = cursor.fetchall()
        return recoreds
    except (Exception, psycopg2.Error) as error:
        print("Error while updating PostgreSQL table", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

def who_is_a_dean_4_yhis_group(name):
    try:      
        print(" ")
        connection = psycopg2.connect(host="localhost", port = 5432, database="Lab1", user="postgres", password="1234")
        cursor = connection.cursor()
        query = """with x as(SELECT fac_name,dean from public.faculty WHERE dean = %s)
        select group_name , student_count, dean from public.group h inner join(select* from x) m on h.fac_name = m.fac_name"""
        cursor.execute(query, (name, ))
        connection.commit() 
        recoreds = cursor.fetchall()
        return recoreds
    except (Exception, psycopg2.Error) as error:
        print("Error while updating PostgreSQL table", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()