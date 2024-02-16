import gspread

from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


print ("something")

CREDS = Credentials.from_service_account_file('cred.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

""" sales = SHEET.worksheet('sales')
data = sales.get_all_values()
print(data)
 """
#fct get sales data from the user

def get_sales_data():
    print("please input sales data")
    print("expected format 6 numbers separated by commas")
    print("Example: 1,11,22,24,1,21\n")  
    data_str = input("enter your numbers here: ")
    print(f"you gave the following numbers {data_str}")
#call fct
get_sales_data()
    