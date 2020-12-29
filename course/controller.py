
import view
import model

url = 'postgresql://postgres:1234@localhost:5433/course_work'
#Base.metadata.create_all(engine)

db = model.PostgreSQL_base(url)

def start():
    print("START!")
    x = view.MENU()
    if x == 0:
        print("Goodbye!")
        
def show_in_diapason(lower, upper):
    model.show_in_diapason(lower, upper)

def most_popular_mark():
    model.most_popular_mark()

def most_popular_types():
    model.most_popular_types()

def add_publication(title,   pub_date,   views,     city,     region ,   mark  ,  price):
    id_ = db.add_publication(title,   pub_date,   views,     city,     region ,   mark  ,  price)
    return id_

def add_car_info(id, mark,  model, year, mileage, body_type,  color,  engine_vol,   fuel,  gearbox,  cleared,price):
    db.add_car_info(id, mark,  model, year, mileage, body_type,  color,  engine_vol,   fuel,  gearbox,  cleared,price)

def add_caradditional_info(id,  add_opt,  multimedia,  security,  other,  owner_note):
    db.add_caradditional_info(id,  add_opt,  multimedia,  security,  other,  owner_note)


def edit_publication(id , title,   pub_date,   views,     city,     region ,   mark  ,  price):
    db.edit_publication(id , title,   pub_date,   views,     city,     region ,   mark  ,  price)

def edit_car(id, mark,  model, year, mileage, body_type,  color,  engine_vol,   fuel,  gearbox,  cleared,price):
    db.edit_car_info(id, mark,  model, year, mileage, body_type,  color,  engine_vol,   fuel,  gearbox,  cleared,price )

def show_publication(id):
    db.show_publication(id)

def show_car_info(id):
    db.show_car_info(id)

def show_car_add_info(id):
    db.show_additional_info(id)

def delete(id):
    db.delete(id)