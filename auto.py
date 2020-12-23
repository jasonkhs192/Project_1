import random

lst = ["apple", "banana", "tttbb"]

rnd = random.choice(lst)

length = len(rnd)

rnd_lst = []

masked = []

masked_str = ""

for x in rnd:
    rnd_lst.append(x)

for x in rnd_lst:
    masked.append("-")

attempts = length + 4

status = False

while attempts > 0 and status is False:
    print(rnd)
    print(masked)
    print("You have {} attempts.".format(attempts))
    choice = input("Select: ")

    if choice in rnd_lst:
        print("Correct")

    else:
        print("Wrong")
        attempts -= 1

    for x in range(length):
        if choice in rnd_lst:
            p = rnd_lst.index(choice)
            rnd_lst[p] = "-"
            masked[p] = choice

# length = len(rnd)
#
# attempt = length + 3
#
# dash_str = ""
#
# dash_lst = []
#
# lst_rnd = []
#
# for x in rnd:
#     lst_rnd.append(x)
#
# # Create dash string
# for x in range(1, length+1):
#     dash_str = dash_str + "-"
# print(dash_str)
# print(rnd)
#
# # Create dash list
# for x in dash_str:
#     dash_lst.append(x)
#
# # Create Loop
# status = False
# while attempt > 0 and status == False:
#     choice = input("You have {} attempts.".format(attempt))
#     p = lst_rnd.index(choice)
#
#     for x in lst_rnd:
#         if x == choice and lst_rnd[p] != "#":
#             lst_rnd[p] = "#"
#     print(lst_rnd)


# idx = []
# for i in dash:
#     idx.append(i)
#
# while attempt > 0:
#     choice = input("You have {} attempts.".format(attempt))
#     p = rnd.find(choice)
#
#     if choice in rnd:
#         new = ""
#         for x in rnd:
#             if x == choice:
#                 if idx[p] == "-":
#                     idx[p] = x
#                     for i in idx:
#                         new = new + i
#     else:
#         print("Wrong")
#         attempt -= 1