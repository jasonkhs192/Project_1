import pandas as pd
import xlsxwriter as xls

write = "Reverse"
workbook = xls.Workbook('C:/Users/jasonkim/Documents/TN/mirror spec/test/{}.xlsx'.format(write))
item1 = "tma_lh_al"

x = "Spec Signal"

df = pd.read_excel('C:/Users/jasonkim/Documents/TN/mirror spec/test/{}.xlsx'.format(item1), sheet_name=0, converters={'Spec Signal':str}) # can also index sheet by name or fetch all sheets
mylist = df[x].tolist()

reverse = []

for item in mylist:
    x = item[::-1]
    reverse.append(x)

worksheet1 = workbook.add_worksheet("Sheet1")
worksheet1.write_column('A1', reverse)
workbook.close()