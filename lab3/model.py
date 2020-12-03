import time
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class faculty(Base):
        __tablename__ = 'faculty'
        fac_name = Column(String(50), primary_key = True)
        foundation_year = Column(Integer)
        dean = Column(String(70))

class group(Base):
        __tablename__ = 'group'
        group_name = Column(String(111), primary_key = True)
        fac_name = Column(String(111), ForeignKey('faculty.fac_name'))
        head_of_group = Column(String(70))
        student_count = Column(Integer)

class student(Base):
        __tablename__ = 'student'
        student_id = Column(Integer, primary_key = True)
        group_name = Column(String(10), ForeignKey('group.group_name'))
        name_surname = Column(String(70))
        birthdate = Column(String(15))

class PostgreSQL_base():
    def __init__ (self , url_):
        self.engine = create_engine( url_ , echo = False)
        
        self.Session = sessionmaker(bind = self.engine)
        self.session_ = self.Session()  

    def delete_faculty(self, fac_name):
        try:
            groups = self.session_.query(group)
            for group_ in groups:
                if group_.fac_name == fac_name:
                    self.session_.query(student).filter(student.group_name == group_.group_name).\
                        delete()
                    self.session_.commit()

            self.session_.query(group).filter(group.fac_name == fac_name).\
                delete()
            self.session_.commit()

            faculty_ = self.session_.query(faculty).filter(faculty.fac_name == fac_name).first()
            self.session_.delete(faculty_)
            self.session_.commit()
        except (Exception, psycopg2.Error) as er :
            print(er)

    def delete_group(self, group_name):
        try:
            self.session_.query(student).filter(student.group_name == group_name).\
                delete()
            self.session_.commit()

            group_ = self.session_.query(group).filter(group.group_name == group_name).first()
            self.session_.delete(group_)
            self.session_.commit()
        except (Exception, psycopg2.Error) as er :
            print(er)

    def delete_student(self, student_id):
        try:
            student_ = self.session_.query(student).filter(student.student_id == student_id).first()
            self.session_.delete(student_)
            self.session_.commit()
        except (Exception, psycopg2.Error) as er :
            print('Oops')

    def add_faculty(self , x , y , z):
        try:
            faculty_1 = faculty(fac_name = x ,foundation_year = y ,dean = z)
            self.session_.add(faculty_1)
            self.session_.commit()
        except (Exception, psycopg2.Error) as er :
            print('Oops')

    def add_group(self , x , y , z , f):
        try:
            group_1 = group(group_name = x ,fac_name = y ,head_of_group = z, student_count = f)
            self.session_.add(group_1)
            self.session_.commit()
        except (Exception, psycopg2.Error) as er :
            print('Oops')

    def add_student(self , x , y , z , f):
        try:
            student_1 = student(student_id = x ,group_name = y ,name_surname = z, birthdate = f)
            self.session_.add(student_1)
            self.session_.commit()
        except (Exception, psycopg2.Error) as er :
            print('Oops')

    def update_faculty(self, fac_name, foundation_year, dean):
        try:
            faculty_ = self.session_.query(faculty).filter(faculty.fac_name == faculty).first()
            faculty_.fac_name = fac_name
            faculty_.foundation_year = foundation_year
            faculty_.dean = dean
            self.session_.commit()
        except (Exception, psycopg2.Error) as er :
            print(er)

    def update_group(self, group_name  , fac_name , head_of_group, student_count):
        try:
            group_ = self.session_.query(group).filter(group.group_name == group_name).first()
            group_.group_name = group_name
            group_.fac_name = fac_name
            group_.head_of_group = head_of_group
            group_.student_count = student_count
            self.session_.commit()
        except (Exception, psycopg2.Error) as er :
            print(er)

    def update_student(self, student_id, group_name, name_surname, birthdate):
        try:
            student_ = self.session_.query(student).filter(student.student_id == student_id).first()
            student_.group_name = group_name
            student_.name_surname = name_surname
            student_.birthdate = birthdate
            self.session_.commit()
        except (Exception, psycopg2.Error) as er :
            print('there is no such grop like '+group_name+' in database!')
