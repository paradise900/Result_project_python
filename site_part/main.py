#!/usr/bin/env python3
"""! @brief Result Python Project"""
##
# @mainpage The main page of this project


from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import koef_function as kf


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)


class Car(db.Model):
    ''' Создаем класс машины с информацией, которая будет храниться в БД '''
    id = db.Column(db.Integer, primary_key=True)
    symboling = db.Column(db.Integer)
    company_name = db.Column(db.String(50))
    horsepower = db.Column(db.Integer)
    city_mpg = db.Column(db.Float)
    fuel_type = db.Column(db.String(10))
    aspiration = db.Column(db.String(10))
    door_number = db.Column(db.String(10))
    drive_wheel = db.Column(db.String(10))
    engine_location = db.Column(db.String(10))
    engine_type = db.Column(db.String(10))
    cylinder_number = db.Column(db.String(10))
    wheel_base = db.Column(db.Float)
    car_body = db.Column(db.String(10))
    car_price = db.Column(db.Integer)


@app.route('/all_cars')
def all_cars():
    ''' Функция выводит историю запросов. 
        @return render history page    
    '''

    cars = Car.query.all()
    return render_template('data_base.html', cars=cars)


@app.route('/')
def main_page():
    ''' Функция рендерит главную страницу 
        @return render main page
    '''
    
    return render_template('main_page.html')


@app.route('/filter', methods=['GET', 'POST'])
def add_information():
    ''' 
    Функция рендерит форму воода информации и обрабатывает введеные данные 
    @return render form page
    '''

    if request.method == 'POST':
        symboling = request.form['symboling']
        company_name = request.form['company_name']
        horsepower = request.form['horsepower']
        city_mpg = request.form['city_mpg']
        fuel_type = request.form['fuel_type']
        aspiration = request.form['aspiration']
        door_number = request.form['door_number']
        drive_wheel = request.form['drive_wheel']
        engine_location = request.form['engine_location']
        engine_type = request.form['engine_type']
        cylinder_number = request.form['cylinder_number']
        wheel_base = request.form['wheel_base']
        car_body = request.form['car_body']

        car = Car(symboling=symboling, company_name=company_name,
                  horsepower=horsepower, city_mpg=city_mpg, fuel_type=fuel_type,
                  aspiration=aspiration, door_number=door_number, 
                  drive_wheel=drive_wheel, engine_location=engine_location, 
                  engine_type=engine_type, cylinder_number=cylinder_number, 
                  wheel_base=wheel_base, car_body=car_body, car_price=0)
        try:
            db.session.add(car)
            db.session.commit()
            car = Car.query.all()[-1]
            return redirect(f'/all_cars/{car.id}')
        except:
            return "При добавлении машины произошла ошибка"
    else:
        return render_template('information.html')


@app.route('/all_cars/<int:id>')
def price_car(id):
    '''
    @param id  id записи, которую хотим обработать
    @return    render car infomarion page

    Функция на вход получает id записи, которую необходимо обработать. 
    С помощью функции koef_function.py получает соответсвующие коэффициенты 
    и делает прогноз целевой стоимости желаемого автомобиля. В результате 
    рендерит странцу с результатами рассчетов '''

    car = Car.query.get(id)
    coef_symboling = kf.func_symboling(car.symboling)
    coef_company = kf.func_company(car.company_name)
    coef_fuel = kf.func_fuel(car.fuel_type)
    coef_aspiration = kf.func_aspiration(car.aspiration)
    coef_door = kf.func_door(car.door_number)
    coef_body = kf.func_body(car.car_body)
    coef_wheel = kf.func_wheel(car.drive_wheel)
    coef_engine = kf.func_engine(car.engine_location)
    coef_etype = kf.func_etype(car.engine_type)
    coef_cylinder = kf.func_cylinder(car.cylinder_number)

    price_1 = (coef_symboling + car.horsepower * 4335.025162 +
             car.city_mpg * 2865.776391 + car.wheel_base * 9934.397110 + 
             coef_company + coef_fuel + coef_aspiration + coef_door + coef_body + 
             coef_wheel + coef_engine + coef_etype + coef_cylinder)
    not_formatted_price = round(price_1)
    price_new = "{:,}".format(not_formatted_price)
    i = db.session.query(Car).get(id)
    i.car_price = price_new
    db.session.add(i)
    db.session.commit()
    return render_template("car_detail.html", car=car)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True) # запуск приложения с включенным режимом отладки