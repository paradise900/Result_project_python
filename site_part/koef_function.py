def func_symboling(symboling):
    ''' Заменяем категориальные переменные для значения symboling 
    на фиктивные переменные и задает соответсвующие коэффициенты '''

    coef_symboling = 0
    if symboling == -1:
        coef_symboling = -2335.889772
    if symboling == 0:
        coef_symboling = 49417.176360
    if symboling == 1:
        coef_symboling = 58158.693791
    if symboling == 2:
        coef_symboling = 14951.027648
    if symboling == 3:
        coef_symboling = 38623.141313
    return coef_symboling


def func_company(company_name):
    ''' Заменяем категориальные переменные для значения company_name 
    на фиктивные переменные и задает соответсвующие коэффициенты '''

    coef_company = 0
    if company_name == 'audi':
        coef_company = 150089.086473
    if company_name == 'bmw':
        coef_company = 174149.668150
    if company_name == 'buick':
        coef_company = 87589.619288
    if company_name == 'chevrolet':
        coef_company = 155824.141881
    if company_name == 'dodge':
        coef_company = 139403.603856
    if company_name == 'honda':
        coef_company = 93510.483888
    if company_name == 'isuzu':
        coef_company = 77061.798244
    if company_name == 'jaguar':
        coef_company = 258183.409597
    if company_name == 'mazda':
        coef_company = 75244.665537
    if company_name == 'mercury':
        coef_company = 245436.811950
    if company_name == 'mitsubishi':
        coef_company = 135838.239525
    if company_name == 'nissan':
        coef_company = 126907.374407
    if company_name == 'peugeot':
        coef_company = 178391.645681
    if company_name == 'plymouth':
        coef_company = 147454.964643
    if company_name == 'porsche':
        coef_company = 197384.390403
    if company_name == 'renault':
        coef_company = 59993.185897
    if company_name == 'saab':
        coef_company = 15094.024831
    if company_name == 'subaru':
        coef_company = 100340.167016
    if company_name == 'toyota':
        coef_company = 132675.499050
    if company_name == 'volkswagen':
        coef_company = 81368.152349
    if company_name == 'volvo':
        coef_company = 9991.657972
    return coef_company


def func_fuel(fuel_type):
    ''' Заменяем категориальные переменные для значения fuel_type 
    на фиктивные переменные и задает соответсвующие коэффициенты '''

    if fuel_type == 'gas':
        coef_fuel = -107861.008638
    else:
        coef_fuel = 0
    return coef_fuel


def func_aspiration(aspiration):
    ''' Заменяем категориальные переменные для значения aspiration
     на фиктивные переменные и задает соответсвующие коэффициенты '''

    if aspiration == 'turbo':
        coef_aspiration = -17497.211625
    else:
        coef_aspiration = 0
    return coef_aspiration


def func_door(door_number):
    ''' Заменяем категориальные переменные для значения door_number 
    на фиктивные переменные и задает соответсвующие коэффициенты '''

    if door_number == 'two':
        coef_door = -12811.633881
    else:
        coef_door = 0
    return coef_door


def func_body(car_body):
    ''' Заменяем категориальные переменные для значения car_body
     на фиктивные переменные и задает соответсвующие коэффициенты '''

    coef_body = 0
    if car_body == 'hardtop':
        coef_body = -46473.005124
    if car_body == 'hatchback':
        coef_body = -63873.062326
    if car_body == 'sedan':
        coef_body = -57975.750446
    if car_body == 'wagon':
        coef_body = -72847.781798
    return coef_body


def func_wheel(drive_wheel):
    ''' Заменяем категориальные переменные для значения drive_wheel
     на фиктивные переменные и задает соответсвующие коэффициенты '''

    coef_wheel = 0
    if drive_wheel == 'fwd':
        coef_wheel = -31387.576248
    if drive_wheel == 'rwd':
        coef_wheel = 1236.072683
    return coef_wheel


def func_engine(engine_location):
    ''' Заменяем категориальные переменные для значения engine_location
     на фиктивные переменные и задает соответсвующие коэффициенты '''

    if engine_location == 'rear':
        coef_engine = 162233.303267
    else:
        coef_engine = 0
    return coef_engine


def func_etype(engine_type):
    ''' Заменяем категориальные переменные для значения engine_type 
    на фиктивные переменные и задает соответсвующие коэффициенты '''

    coef_etype = 0
    if engine_type == 'dohcv':
        coef_etype = -990963.573083
    if engine_type == 'l':
        coef_etype = -189867.680850
    if engine_type == 'ohc':
        coef_etype = 95527.578428
    if engine_type == 'ohcf':
        coef_etype = 61893.136251
    if engine_type == 'ohcv':
        coef_etype = -14513.163784
    return coef_etype


def func_cylinder(cylinder_number):
    ''' Заменяем категориальные переменные для значения cylinder_number
     на фиктивные переменные и задает соответсвующие коэффициенты '''

    coef_cylinder = 0
    if cylinder_number == 'five':
        coef_cylinder = -399249.352574
    if cylinder_number == 'four':
        coef_cylinder = -780664.354546
    if cylinder_number == 'six':
        coef_cylinder = -681537.847456
    if cylinder_number == 'three':
        coef_cylinder = -368259.326531
    if cylinder_number == 'twelve':
        coef_cylinder = -762015.292756
    if cylinder_number == 'two':
        coef_cylinder = -312540.493988
    return coef_cylinder