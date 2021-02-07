import pygsheets

def validate_age(age):

    if (age.isnumeric() == True):

        if (int(age) > 18 and int(age) < 80): return True

        else : return False

    else: return False

def validate_weight(weight):

    if (weight.isnumeric() == True):

        if (int(weight) > 30 and int(weight) < 180): return True

        else : return False

    else: return False

def validate_height(height):

    if (height.isnumeric() == True):

        if (int(height) > 130 and int(height) < 230): return True

        else : return False

    else: return False

def validate_sex(sex):

    if (sex.isnumeric() == True):

        if (int(sex) == 1 or int(sex) == 2): return True

        else : return False

    else: return False

def auth_gsheets():

    service_file = r'pmvcalculator-304117-16a25badba46.json'

    gc = pygsheets.authorize (service_file=service_file)

    sheetname = 'PMV_Calculator'

    sh = gc.open(sheetname)

    wks = sh.worksheet_by_title('Sheet1')

    return wks

def append_gsheets():

    new_row = ['firstname', 'lastname', 'Email', 'Number']

    cells = wks.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')

    last_row = len(cells)

    worksheet = wks.insert_rows(last_row, number=1, values= new_row)

    return None

while True :

    age = input ("Please enter your age:")

    valid = validate_age(age)

    if valid == True : break

    else : print ("INVALID")

while True :

    weight = input ("Please enter your weight [kg]:")

    valid = validate_weight(weight)

    if valid == True : break

    else : print ("INVALID")

while True :

    height = input ("Please enter your height [cm]:")

    valid = validate_height(height)

    if valid == True : break

    else : print ("INVALID")

while True :

    sex = input ("Please enter your sex [1: Male, 2: Female]:")

    valid = validate_sex(sex)

    if valid == True : break

    else : print ("INVALID")

wks = auth_gsheets()

#append_gsheets()
