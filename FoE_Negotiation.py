import random


class Negotiate:
    def __init__(self, selection=5):
        self.selection = selection
        goodkey = {
            1: "Coin",
            2: "Supply",
            3: "Wine",
            4: "Lumber"
        }
        selection = 5
        goods = [goodkey[1], goodkey[2], goodkey[3], goodkey[4]]
        choice_list = random.choices(goods, k=selection)
        print(goodkey)

    def options(self):
        print("Please select {} goods.".format(self.selection))
        choice1 = input("Choice 1: ")
        choice2 = input("Choice 2: ")
        choice3 = input("Choice 3: ")
        choice4 = input("Choice 4: ")
        choice5 = input("Choice 5: ")

        if choice1 in

Negotiate().options()
#
# attempt_count = 3
# goods = ["Coin", "Supply", "Lumber", "Wine"]
# player_lst = random.choices(goods, k=5)
# choice = []
# correct1 = 0
# correct2 = 0
# correct3 = 0
# correct4 = 0
# correct5 = 0
# choice_save = []
#
# while attempt_count > 0:
#     print("Attempt Left: {}".format(attempt_count))
#     if correct1 == 0:
#         print(goods)
#         x1 = input("Player1:")
#         choice.append(x1)
#     else:
#         choice.append(choice_save[0])
#     if correct2 == 0:
#         print(goods)
#         x2 = input("Player2:")
#         choice.append(x2)
#     else:
#         choice.append(choice_save[1])
#     if correct3 == 0:
#         print(goods)
#         x3 = input("Player3:")
#         choice.append(x3)
#     else:
#         choice.append(choice_save[2])
#     if correct4 == 0:
#         print(goods)
#         x4 = input("Player4:")
#         choice.append(x4)
#     else:
#         choice.append(choice_save[3])
#     if correct5 == 0:
#         print(goods)
#         x5 = input("Player5:")
#         choice.append(x5)
#     else:
#         choice.append(choice_save[4])
#
#     #player1
#     if choice[0] == player_lst[0]:
#         print("Player1: correct | Resource: {}".format(choice[0]))
#         correct1 = 1
#     elif choice[0] != player_lst[0] and choice[0] == player_lst[1] or choice[0] == player_lst[2] or choice[0] == player_lst[3] or choice[0] == player_lst[4]:
#         print("Player1: Yellow | Resource: {}".format(choice[0]))
#     else:
#         print("Player1: Red | Resource: {}".format(choice[0]))
#         if choice[0] in goods:
#             goods.remove(choice[0])
#
#     #player2
#     if choice[1] == player_lst[1]:
#         print("Player2: correct | Resource: {}".format(choice[1]))
#         correct2 = 1
#     elif choice[1] != player_lst[1] and choice[1] == player_lst[0] or choice[1] == player_lst[2] or choice[1] == player_lst[3] or choice[1] == player_lst[4]:
#         print("Player2: yellow | Resource: {}".format(choice[1]))
#     else:
#         print("Player2: Red | Resource: {}".format(choice[1]))
#         if choice[1] in goods:
#             goods.remove(choice[1])
#
#     #player3
#     if choice[2] == player_lst[2]:
#         print("Player3: correct | Resource: {}".format(choice[2]))
#         correct3 = 1
#     elif choice[2] != player_lst[2] and choice[2] == player_lst[1] or choice[2] == player_lst[0] or choice[2] == player_lst[3] or choice[2] == player_lst[4]:
#         print("Player3: yellow | Resource: {}".format(choice[2]))
#     else:
#         print("Player3: Red | Resource: {}".format(choice[2]))
#         if choice[2] in goods:
#             goods.remove(choice[2])
#
#     #player4
#     if choice[3] == player_lst[3]:
#         print("Player4: correct | Resource: {}".format(choice[3]))
#         correct4 = 1
#     elif choice[3] != player_lst[3] and choice[3] == player_lst[1] or choice[3] == player_lst[2] or choice[3] == player_lst[0] or choice[3] == player_lst[4]:
#         print("Player4: yellow | Resource: {}".format(choice[3]))
#     else:
#         print("Player4: Red | Resource: {}".format(choice[3]))
#         if choice[3] in goods:
#             goods.remove(choice[3])
#
#     #player5
#     if choice[4] == player_lst[4]:
#         print("Player5: correct | Resource: {}".format(choice[4]))
#         correct5 = 1
#     elif choice[4] != player_lst[4] and choice[4] == player_lst[1] or choice[4] == player_lst[2] or choice[4] == player_lst[3] or choice[4] == player_lst[0]:
#         print("Player5: yellow | Resource: {}".format(choice[4]))
#     else:
#         print("Player5: Red | Resource: {}".format(choice[4]))
#         if choice[4] in goods:
#             goods.remove(choice[4])
#
#     if choice == player_lst:
#         print("Pass")
#         exit()
#
#     print(choice)
#     choice_save = choice.copy()
#     choice.clear()
#     attempt_count = attempt_count - 1
# if choice == player_lst:
#     print("Pass")
# else:
#     print("Fail")
#
#
#
#
#
#
#
#
