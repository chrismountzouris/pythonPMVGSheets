import pygsheets

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

wks = auth_gsheets()

append_gsheets()
