import psycopg2
import os
import controller
from datetime import date

def MENU():

    while True:   
        os.system('cls||clear')
        print("----------------------")    
        i = input("u have this commands:\n 1 - add new publication\n 2 - operations by id\n 3 - show the most popular marks\n 4 - show mostpopular types of cars\n 5 - show cars in your price diapason \n 9 - exit \nselect a command u wanna use\n")
        i = int(i)
        os.system('cls||clear')
        if i == 1 :
            pub_add()
        if i == 2:
            x = input("Pls input publication`s id\n")
            x = int(x)
            controller.show_publication(x)

            l = input("u can:\n 1 - see information about car in this publication\n 2 - delete this publication\n 3 - edit this publication\n 4 - get back")
            l = int(l)

            if l == 1:
                Car_main_info_menu(x)
            if l == 2:
                controller.delete(x)
            if l == 3:
                pass
                #controller.edit_publication(id , title,   pub_date,   views,     city,     region ,   mark  ,  price)
            if l == 4:
                MENU()
        if i == 3:
            controller.most_popular_mark()
        if i == 4:
            controller.most_popular_types()
        if i == 5:   
            lower = input("input lower limit ")
            upper = input("upper limit ")
            controller.show_in_diapason(int(lower), int(upper))
        
        if i == 9:
            return 0

    return 1
def pub_add():
    title = input("input title ")
    pub_date = str(date.today())
    views = 123
    city = input("input city ")
    region= input("input region ")
    mark= input("input mark ")
    price= input("input price ")
    id = controller.add_publication(title,   pub_date,   views,     city,     region ,   mark  ,  price)
    print("id of your publication is "+ str(id))
    car_info_add(id ,mark , price)

def car_info_add(id_,mark_ , price_):
    print("----------------------")
    print("now give some information about your car")
    print("----------------------")
    id = id_
    mark = mark_
    model= input("input model ") 
    year= input("input year ") 
    mileage= input("input mileage ") 
    body_type= input("input body_type ")  
    color= input("input color ")  
    engine_vol= input("input engine volume ")
    fuel= input("input fuel type ")  
    gearbox= input("input gearbox ")  
    cleared= input("input if it is cleared(1.0 if yes, 0.0 if no) ")
    price= price_
    controller.add_car_info(id, mark,  model, year, mileage, body_type,  color,  engine_vol,   fuel,  gearbox,  cleared,price)
    print("----------------------")
    print("grats!! your publication is full and posted")
    print("----------------------")

def Car_main_info_menu(x):
    controller.show_car_info(x)

    l = input("u can:\n 1 - see car`s additional information\n 2 - edit this information\n 3 - get back")
    l = int(l)

    if l == 1:
        controller.show_car_add_info(x)
    if l == 2:
        mark = input("input mark")
        model= input("input model") 
        year= input("input year") 
        mileage= input("input mileage") 
        body_type= input("input body_type")  
        color= input("input color")  
        engine_vol= input("input engine_vol")
        fuel= input("input fuel")  
        gearbox= input("input gearbox")  
        cleared= input("input if it is cleared(1.0 if yes, 0.0 if no")
        price= input("input price")
        controller.edit_car(x, mark,  model, year, mileage, body_type,  color,  engine_vol,   fuel,  gearbox,  cleared,price)
    if l == 3: MENU()
