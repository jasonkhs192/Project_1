import pandas as pd
import xlsxwriter as xls

# df = pd.read_excel("test.xlsx", sheet_name=0)
# x = df["First Name"].tolist()
# print(x)

# workbook = xls.Workbook('C:/Users/jasonkim/Documents/TN/mirror spec/mes_on')

#Source
item1 = "Book2"
#Copy
item2 = "RCG30006"

x = 'PN'
y = "Part Number"

df = pd.read_excel('C:/Users/jasonkim/Documents/TN/mirror spec/test/{}.xlsx'.format(item1), sheet_name=0) # can also index sheet by name or fetch all sheets
mylist = df[x].tolist()

df2 = pd.read_excel('C:/Users/jasonkim/Documents/TN/mirror spec/test/{}.xlsx'.format(item2), sheet_name=0) # can also index sheet by name or fetch all sheets
mylist2 = df2[y].tolist()

mylist3 = []
mylist4 = []
count = 0
pos = []
for x in mylist2:
    if x in mylist:
        mylist3.append(x)
    else:
        mylist4.append(x)
        pos.append(count+2)

    count+=1

print(mylist3)
print(len(mylist3))
print(mylist4)
print(len(mylist4))
print(pos)


# if mylist == mylist2:
#     print("Same")
# else:
#     print("Not Same")
#     print("{}: {}".format(item1, len(mylist)))
#     print("{}: {}".format(item2, len(mylist2)))
#
#
# for x in mylist2:
#     if x not in mylist:
#         mylist3.append(x)
#
# print(mylist3)
# #
# count = 0
# added = []
# row_num = []
# for x in mylist:
#     if x != mylist2[count]:
#         added.append(x)
#         row_num.append(count+1)
#
#     count += 1
#
# print(row_num)

#
# cnt_lst = []
# cnt2_lst = []
# for x in mylist2:
#     cnt = mylist2.count(x)
#     cnt_lst.append(cnt)
#
# for x in mylist:
#     cnt2 = mylist.count(x)
#     cnt2_lst.append(cnt2)
#
# print(cnt_lst)
# print(cnt2_lst)
#
# count = 0
# for x in cnt_lst:
#     if x == cnt2_lst[count]:
#         pass
#     else:
#         print(count)
#     count += 1


# worksheet1 = workbook.add_worksheet("Sheet1")
# worksheet1.write_column('A1', mylist3)
# workbook.close()