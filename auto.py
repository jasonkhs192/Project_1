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


            
            
# import random

# lst = ["apple", "banana", "peace", "jason"]

# rnd = random.choice(lst)

# length = len(rnd)

# rnd_lst = []

# masked = []

# masked_str = ""

# for x in rnd:
#     rnd_lst.append(x)

# for x in rnd_lst:
#     masked.append("-")

# attempts = length + 4

# status = False


# while status is False:
#     for x in masked:
#         masked_str = masked_str + x

#     print(masked_str)

#     if attempts == 0:
#         print("You lost... Answer was [ {} ]".format(rnd))
#         exit()

#     while attempts > 0:
#         masked_str = ""
#         print("You have {} attempts.".format(attempts))
#         choice = input("Select a letter: ")

#         if choice in rnd_lst:
#             print("Your selection '{}' is correct".format(choice))
#             for x in rnd_lst:
#                 if choice in rnd_lst:
#                     p = rnd_lst.index(choice)
#                     rnd_lst[p] = "-"
#                     masked[p] = choice

#             for x in masked:
#                 masked_str += x

#             print(masked_str)

#             if masked_str == rnd:
#                 print("You got it all. You won!")
#                 exit()

#         else:
#             for x in masked:
#                 masked_str += x

#             print(masked_str)
#             print("Wrong,try again...")
#             attempts -= 1
