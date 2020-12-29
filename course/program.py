# coding=utf-8
import controller
import model


url = 'postgresql://postgres:1234@localhost:5432/Lab1'
#Base.metadata.create_all(engine)

db = model.PostgreSQL_base(url)

#db.add_faculty('FPM14', 1994 , 'torgovskyh')

#db.add_group('KP-94', 'FPM14', 'Kozynets`', 28)

#db.add_student(2,'KP-94', 'Torgovskyh Olexandr', '2002-04-08')

#db.update_student(2, 'KP-93', 'Torgovskyh Olexandrrr', '2002-04-08')

#db.update_group('KP-93', 'FPM14' , 'Torgovskyh Olexandr', 2211)

#db.delete_student(1)

#db.delete_group('KP-95')

#db.delete_faculty('FPM')


#controller.start()

