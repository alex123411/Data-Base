import time
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, session
from sqlalchemy.ext.declarative import declarative_base
import data_generation
from data_generation import create_tables , create_csvs , import_csvs
import matplotlib
import matplotlib.pyplot as plt
import warnings
import numpy as np

Base = declarative_base()

class Dataset(Base):
        __tablename__ = '1_dataset'
        id = Column(Integer, primary_key = True , autoincrement = True)
        title = Column(String)
        pub_date = Column(String)
        views = Column(Integer)
        city = Column(String)
        region= Column(String)
        mark= Column(String)
        model= Column(String)
        year= Column(String)
        mileage= Column(String)
        body_type= Column(String)
        color= Column(String)
        engine_vol= Column(String)
        fuel= Column(String)
        gearbox= Column(String)
        cleared= Column(String)
        condition= Column(String)
        add_opt= Column(String)
        multimedia= Column(String)
        security= Column(String)
        other= Column(String)
        owner_note= Column(String)
        price= Column(Integer)

class Pub_info(Base):
    __tablename__ = '2_publication_info'
    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String)
    pub_date = Column(String)
    views = Column(Integer)
    city = Column(String)
    region= Column(String)
    mark= Column(String)
    price= Column(Integer)

class Car_main_info(Base):
    __tablename__ = '3_car_main_info'
    id = Column(Integer, primary_key = True )
    mark= Column(String)
    model= Column(String)
    year= Column(Integer)
    mileage= Column(Integer)
    body_type= Column(String)
    color= Column(String)
    engine_vol= Column(Integer)
    fuel= Column(String)
    gearbox= Column(String)
    cleared= Column(String)
    price= Column(Integer)

class Car_addit_info(Base):
    __tablename__ = '4_car_additional_info'
    id = Column(Integer, primary_key = True )
    condition= Column(String)
    add_opt= Column(String)
    multimedia= Column(String)
    security= Column(String)
    other= Column(String)
    owner_note= Column(String)

class PostgreSQL_base():
    
    def __init__ (self , url_):
        self.engine = create_engine( url_ , echo = False)
        
        self.Session = sessionmaker(bind = self.engine)
        self.session_ = self.Session()  

    def add_publication(self , title_,   pub_date_,   views_,     city_,     region_ ,   mark_  ,  price_):
        try:
            pub = self.session_.query(Pub_info).order_by(Pub_info.id.desc()).first()
            id_ = int(pub.id)
            id_ = id_ + 1
            publication_ = Pub_info(id = id_, title = title_,   pub_date = pub_date_,   views = views_,     city = city_,     region  = region_,   mark  =mark_,  price = price_)
            self.session_.add(publication_)
            self.session_.commit()
            
            return id_
        except (Exception, psycopg2.Error) as er :
            print(er)

    def add_car_info(self , id_, mark_,  model_, year_, mileage_, body_type_,  color_,  engine_vol_,   fuel_,  gearbox_,  cleared_,price_):
        try:   
            publication_ = Car_main_info(id = id_, mark=mark_,  model=model_, year=year_, mileage=mileage_, body_type=body_type_,  color=color_,  engine_vol=engine_vol_,   fuel=fuel_,  gearbox=gearbox_,  cleared=cleared_,price=price_)
            self.session_.add(publication_)
            self.session_.commit()
        except (Exception, psycopg2.Error) as er :
            print(er)

    def add_caradditional_info(self ,id,  add_opt,  multimedia,  security,  other,  owner_note):
        try:
            pass
        except (Exception, psycopg2.Error) as er :
            print(er)

    def edit_publication(self , id , title,   pub_date,   views,     city,     region ,   mark  ,  price):
        try:
            pass
        except (Exception, psycopg2.Error) as er :
            print(er)

    def  edit_car_info(self , id, mark,  model, year, mileage, body_type,  color,  engine_vol,   fuel,  gearbox,  cleared,price ):
        try:
            pass
        except (Exception, psycopg2.Error) as er :
            print(er)

    def update_publication(self, id, fac_name, foundation_year, dean):
        try:
            faculty_ = self.session_.query(faculty).filter(faculty.fac_name == faculty).first()
            faculty_.fac_name = fac_name
            faculty_.foundation_year = foundation_year
            faculty_.dean = dean
            self.session_.commit()
        except (Exception, psycopg2.Error) as er :
            print(er)

    def show_publication(self, id):
        try:
            print("----------------------")
            publication = self.session_.query(Pub_info).filter(Pub_info.id == id).first()
            print("Заголовок: "+ str(publication.title) +  "\n"
            "Дата публікації: " +  str(publication.pub_date) +  "\n"
            "Переглядів цієї публікації: "+  str(publication.views) +  "\n"
            "Місто: "+  str(publication.city) +  "\n"
            "Регіон: "+  str(publication.region) +  "\n"
            "Марка авто: "+  str(publication.mark) +   "\n"
            "Ціна: "+ str(publication.price) + "\n")
            print("----------------------")
        except (Exception, psycopg2.Error) as er :
            print(er)
    def show_car_info(self, id):
        try:
            print("----------------------")
            publication = self.session_.query(Car_main_info).filter(Car_main_info.id == id).first()
            print("Марка авто: "+ str(publication.mark) +  "\n"
            "Модель авто: " +  str(publication.model) +  "\n"
            "Рік випуску авто: "+  str(publication.year) +  "\n"
            "Пробіг в км.: "+  str(publication.mileage) +  "\n"
            "Тип корпуса: "+  str(publication.body_type) +  "\n"
            "Колір: "+  str(publication.color) +   "\n"
            "Вмістимість двигуна: "+ str(publication.engine_vol) + "\n"
            "Тип бензину: " + str(publication.fuel)+ "\n"
            "Коробка передач: " + str(publication.gearbox))
            if publication.cleared == '1.0' :
                print("Розтаможка: розтаможений")
            else:
                print("Розтаможка: нерозтаможений")
            print("Ціна: " + str(publication.price)+ "\n")
            print("----------------------")
        except (Exception, psycopg2.Error) as er :
            print(er)
    def show_additional_info(self, id):
        try:
            print("----------------------")
            publication = self.session_.query(Car_addit_info).filter(Car_addit_info.id == id).first()
            print("Стан: "+ str(publication.condition) +  "\n"
            "Додаткові опції: " +  str(publication.add_opt) +  "\n"
            "Мудьтимедія: "+  str(publication.multimedia) +  "\n"
            "Захист: "+  str(publication.security) +  "\n"
            "Інше: "+  str(publication.other) +  "\n"
            "Коментар власника: "+  str(publication.owner_note) +   "\n")
            print("----------------------")
        except (Exception, psycopg2.Error) as er :
            print(er)
    
    def delete(self, id_):
        try:
            publication = self.session_.query(Pub_info).filter(Pub_info.id == id_).first()
            self.session_.delete(publication)
            self.session_.commit()

            maininfo = self.session_.query(Car_main_info).filter(Car_main_info.id == id_).first()
            self.session_.delete(maininfo)
            self.session_.commit()

            add_info = self.session_.query(Car_addit_info).filter(Car_addit_info.id == id_).first()
            self.session_.delete(add_info)
            self.session_.commit()
        except (Exception, psycopg2.Error) as er :
            print('Oops')

def most_popular_mark():
    connection = psycopg2.connect(host="localhost", port = 5432, database="course_work", user="postgres", password="1234")
    cursor = connection.cursor()
    try:      
        query = """select mark, count(*)
                from public."2_publication_info"  
                group by mark
                order by count(*) DESC LIMIT 10""" 
        cursor.execute(query)
        connection.commit()  
        records = cursor.fetchall()
        x =  0
        length = len(records)
        print(length)
        records_x = []
        records_y = []
        PLOT_LABEL_FONT_SIZE = 14
        PLOT_MEANING_FONT_SIZE = 6
        for record in records:
            records_x.append(record[0])
            records_y.append(record[1])
            print(str(record[0]) + " - " + str(record[1]) )
            x = x + 1
        plt.title('10 найпопулярніших марок на ринку', fontsize=PLOT_LABEL_FONT_SIZE)
        plt.bar(records_x, records_y, color=getColors(len(records_x)))
        plt.ylabel('Кількість публікацій', fontsize=PLOT_LABEL_FONT_SIZE)
        plt.xticks(fontsize=PLOT_MEANING_FONT_SIZE)
        plt.show()

    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
    input("press smthing to get back...")


def getColors(n):
    COLORS = []
    cm = plt.cm.get_cmap('hsv', n)
    for i in np.arange(n):
        COLORS.append(cm(i))
    return COLORS


def most_popular_types():
    connection = psycopg2.connect(host="localhost", port = 5432, database="course_work", user="postgres", password="1234")
    cursor = connection.cursor()
    try:      
        query = """select body_type , count(*) from public."3_car_main_info" group by body_type order by count(*) DESC LIMIT 10""" 
        cursor.execute(query)
        connection.commit()  
        records = cursor.fetchall()
        x =  0
        length = len(records)
        print(length)
        records_x = []
        records_y = []
        PLOT_LABEL_FONT_SIZE = 14
        PLOT_MEANING_FONT_SIZE = 6
        for record in records:
            records_x.append(record[0])
            records_y.append(record[1])
            print(str(record[0]) + " - " + str(record[1]) )
            x = x + 1
        plt.title('10 найпопулярніших типів кузова на ринку', fontsize=PLOT_LABEL_FONT_SIZE)
        plt.bar(records_x, records_y, color=getColors(len(records_x)))
        plt.ylabel('Кількість таких авто', fontsize=PLOT_LABEL_FONT_SIZE)
        plt.xticks(rotation = 90,fontsize=PLOT_MEANING_FONT_SIZE)
        plt.show()

    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
    input("press smthing to get back...")


def show_in_diapason( lower, upper):
    connection = psycopg2.connect(host="localhost", port = 5432, database="course_work", user="postgres", password="1234")
    cursor = connection.cursor()
    try:      
        query = """
        select mark, price , model
        from public."3_car_main_info"  
        where price > %s and price < %s  order by price ASC limit 50;""" 
        cc = (lower, upper)
        cursor.execute(query , cc)
        connection.commit()  
        records = cursor.fetchall()
        x =  0
        records_x = []
        records_y = []
        PLOT_LABEL_FONT_SIZE = 14
        PLOT_MEANING_FONT_SIZE = 6
        for record in records:
            records_x.append(str(record[0])+str(record[2]))
            records_y.append(str(record[1]))
            print(str(record[0]) + " - " + str(record[1]) )
            x = x + 1

        plt.title('Перші 50 авто в вашому діапазоні', fontsize=PLOT_LABEL_FONT_SIZE)
        plt.bar(records_x, records_y, color=getColors(len(records_x)))
        plt.ylabel('Ціна', fontsize=PLOT_LABEL_FONT_SIZE)
        plt.xticks(rotation=90 , fontsize=PLOT_MEANING_FONT_SIZE)
        plt.show()

    except (Exception, psycopg2.Error) as error:
        print(error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
    input("press smthing to get back...")
