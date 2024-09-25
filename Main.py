#Importing the Invoice class from the Invoice method
from Invoice import Invoice
#Importing necessary libaries for invoice parsing
from typing import Optional
from google.api_core.client_options import ClientOptions
from google.cloud import documentai  # type: ignore
from google.protobuf.field_mask_pb2 import FieldMask  # Import FieldMask
from google.protobuf.json_format import MessageToJson  # Import MessageToJson
#Inmporting excel interface
import xlwt
from xlwt import Workbook
#Importing InvoiceParsing.py
import InvoiceParsing
#Importing regex
import re

#Parse the invoice
InvoiceParsing.parseInvoice()

# Excel Workbook is created
wb = Workbook()

# add_sheet is used to create spreadsheet
sheet1 = wb.add_sheet('Invoice data')

#Creating an array of invoice objects
invoices = []

#Reformat the text file
with open("invoice_output.txt", 'r') as file:
    content = file.read()  # Read the entire file content
    modified_content = content.replace("Item:", "|")
    with open("invoice_output.txt", 'w') as file:
        file.write(modified_content)

#Get the invoice vendor from the text file
invoiceData = open("invoice_output.txt", "r")
vendor = invoiceData.readline().split(":")[1].strip()

items_array = modified_content.split("|")
items_array = [item.strip() for item in items_array]
items_array = [item.replace('\n', ' ') for item in items_array]

regex = r'^(.*?)\s+(.*?)\s+(\d{7})\s+([\d.]+)\s+([\d.]+)$'
for x in items_array[1:]:
    match = re.search(regex, x)
    if match:
        brand = match.group(1)
        description = match.group(2)
        category = ""
        productCode = match.group(3)
        price = match.group(5)
        invoices.append(Invoice(vendor, brand, description, category, productCode, price))

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
invoiceData.close()