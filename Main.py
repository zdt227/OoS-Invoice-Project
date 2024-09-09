#Importing the Invoice class from the Invoice method
from Invoice import Invoice

#Inmporting excel interface
import xlwt
from xlwt import Workbook 

# Workbook is created 
wb = Workbook() 

# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Invoice data') 

#Creating an array of invoice objects
invoices = []

#Creating instances of invoice objects in the list
invoices.append(Invoice("Cheese Cheddar Sharp Prin", "Dairy Products", "8222312", "BRLMP", "SYSCO", 45.92))
invoices.append(Invoice("Cheese Swiss/Amer 120 Sli", "Dairy Products", "5148453", "", "SYSCO", 21.79))

for y, Invoice in enumerate(invoices):
    for x in range(6):
        if x == 0: 
            sheet1.write(y,x, invoices[y].vendor)
        elif x == 1: 
            sheet1.write(y,x, invoices[y].category)
        elif x == 2: 
            sheet1.write(y,x, invoices[y].brand)
        elif x == 3: 
            sheet1.write(y,x, invoices[y].description)
        elif x == 4: 
            sheet1.write(y,x, invoices[y].product_code)
        elif x == 5: 
            sheet1.write(y,x, invoices[y].price)

wb.save('Invoice_data.xls') 