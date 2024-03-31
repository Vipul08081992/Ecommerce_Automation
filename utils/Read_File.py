# Read data from Excel:
import openpyxl
def read_row_from_excel(file_path,sheet_name):
    test_cred=[]
    workbook=openpyxl.load_workbook(file_path)
    sheet=workbook[sheet_name]
    for row in sheet.iter_rows(min_row=2,min_col=2,values_only=True):
        username,password=row
        test_cred.append({
            "username":username,
            "password":password
        })
    return test_cred
'''
test_cred=read_row_from_excel("C:\\Users\\vipul\\PycharmProjects\\Swag_Labs\\resources\\Data\\Valid Credentials.xlsx",sheet_name="login_cred")
print(test_cred)
'''