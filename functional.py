import gspread
import os
from google.oauth2.service_account import Credentials

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'client_secret.json') #google api secret json
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file(file_path, scopes=scope)
client = gspread.authorize(creds)
sheet = client.open("your sheet").sheet1

def get_status(id):
    all_ids = sheet.col_values(1)  
    if str(id) in all_ids:
        row = all_ids.index(str(id)) + 1  
        estado = sheet.cell(row, 2).value.strip().lower()
        return estado
    else:
        return None
