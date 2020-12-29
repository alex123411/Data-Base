import time
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, session
from sqlalchemy.ext.declarative import declarative_base
import csv

def create_csvs():
    print("creation of publication info")
    with open("C:/Users/alext/Desktop/BD/course/dataset/2_publication_info.csv",'w', newline='', encoding="utf8") as csvfile:
        writer = csv.writer(csvfile, delimiter = ",")
        writer.writerow(["id","title","pub_date","views","city","region","mark","price"])
        with open("C:/Users/alext/Desktop/BD/course/dataset/cars_dataset.csv", newline='', encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter =",")
            for row in reader:
                writer.writerow([row['id'],row['title'],row['pub_date'],row['views'],row['city'],row['region'],row['mark'],row['price']])


    print("creation of car main info")
    with open("C:/Users/alext/Desktop/BD/course/dataset/3_car_main_info.csv",'w', newline='', encoding="utf8") as csvfile:
        writer = csv.writer(csvfile, delimiter = ",")
        writer.writerow(["id","mark","model","year","mileage","body_type","color","engine_vol","fuel","gearbox","cleared","price"])
        with open("C:/Users/alext/Desktop/BD/course/dataset/cars_dataset.csv", newline='', encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter =",")
            for row in reader:
                writer.writerow([row['id'],row['mark'],row['model'],row['year'],row['mileage'],row['body_type'],row['color'],row['engine_vol'],row['fuel'],row['gearbox'],row['cleared'],row['price']])

    
    print("creation of car additional info")
    with open("C:/Users/alext/Desktop/BD/course/dataset/4_car_additional_info.csv",'w', newline='', encoding="utf8") as csvfile:
        writer = csv.writer(csvfile, delimiter = ",")
        writer.writerow(["id","condition","add_opt","multimedia","security","other","owner_note"])
        with open("C:/Users/alext/Desktop/BD/course/dataset/cars_dataset.csv", newline='', encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter =",")
            for row in reader:
                writer.writerow([row['id'],row['condition'],row['add_opt'],row['multimedia'],row['security'],row['other'],row['owner_note']])

def create_tables(dburl):
    engine = create_engine(dburl, echo = False)
    Session = sessionmaker(bind = engine)
    session = Session()
    Base = declarative_base()
    class Dataset(Base):
        __tablename__ = '1_dataset'
        id = Column(Integer, primary_key = True)
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
        id = Column(Integer, primary_key = True)
        title = Column(String)
        pub_date = Column(String)
        views = Column(Integer)
        city = Column(String)
        region= Column(String)
        mark= Column(String)
        price= Column(Integer)

    class Car_main_info(Base):
        __tablename__ = '3_car_main_info'
        id = Column(Integer, primary_key = True)
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
        id = Column(Integer, primary_key = True)
        condition= Column(String)
        add_opt= Column(String)
        multimedia= Column(String)
        security= Column(String)
        other= Column(String)
        owner_note= Column(String)

    Base.metadata.create_all(engine)

def import_csvs():
    try:
        all_value = []
        conn = psycopg2.connect("host=localhost dbname=course_work user=postgres password=1234")
        cur = conn.cursor()
        with open("C:/Users/alext/Desktop/BD/course/dataset/cars_dataset.csv", newline='', encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter =",")
            for row in reader:
                value = ([row['id'],row['title'],row['pub_date'],row['views'],row['city'],row['region'],row['mark'],row['price']])
                all_value.append(value)

        
    except Exception as e:
        print(e)