#문제1
# def station(a,b,c):
#     print("{} 행 열차가 들어오고 있습니다.".format(a))
#     print("{} 행 열차가 들어오고 있습니다.".format(b))
#     print("{} 행 열차가 들어오고 있습니다.".format(c))
#
# station("사당", "신도림", "인천공항")

#문제2
# from random import *
#
# rand = random.randint(4,28)
#
# print("오프라인 스터디 모임 날짜는 매월 {}일로 선정되었습니다.".format(rand))

#문제3
# def password(link):
#     if link[0:7] == "http://":
#         new_link = link[7:]
#     else:
#         new_link = link
#
#     dot = new_link.find(".")
#
#     word = new_link[:dot]
#
#     print(word[:3]+str(len(word))+str(word.count("e"))+"!")
#
# password("http://naver.com")

#문제4
# from random import *
# lst = []
# for x in range(1,21):
#     if x not in lst:
#         lst.append(x)
#
# shuffle(lst)
# chicken_winner = sample(lst,1)
# str1 = ""
# for y in chicken_winner:
#     str1 = str1 + str(y)
#
# lst.remove(int(str1))
# shuffle(lst)
# coffee_winner = sample(lst,3)
#
# print("""-- 당첨자 발표 --
# 치킨 당첨자 : {}
# 커피 당첨자 : {}
# -- 축하합니다 --
# """.format(chicken_winner, coffee_winner))

# 문제5
# from random import *
# count = 0
# for x in range(1,51):
#     time = randint(5, 50)
#     if time <= 15:
#         print("[O] {}번째 손님 (소요시간: {}분)".format(x,time))
#         count = count + 1
#     else:
#         print("[ ] {}번째 손님 (소요시간: {}분)".format(x, time))
#
# print("총 탑승 승객 : {} 분".format(count))

# 문제6
#
# def std_weight(height, gender):
#     if gender == "male":
#         weight = (height * height * 22)/10000
#         print("키 {}cm 남자의 표준 체중은 {}kg 입니다".format(height, str(round(weight, 2))))
#     else:
#         weight = (height * height * 21)/10000
#         print("키 {}cm 여자의 표준 체중은 {}kg 입니다".format(height, str(round(weight, 2))))
#
# std_weight(168,"female")

# 문제7
# week = 1
# while week < 5:
#     file = open("{}주차.txt".format(week), "w", encoding="utf8")
#     print("""- {} 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :
#     """.format(week), file=file)
#     file.close()
#     week = week + 1

#문제8

# class House:
#     def __init__(self, location, build_type, deal_type, price, reg_year):
#         self.location = location
#         self.build_type = build_type
#         self.deal_type = deal_type
#         self.price = price
#         self.reg_year = reg_year
#
#     def show_detail(self):
#         print("| 지역: {} | 매물종류: {} | 매매종류2: {} | 가격: {} | 등록년도: {} |".format(self.location, self.build_type, self.deal_type, self.price, self.reg_year))
#
# house1 = House("강남","빌딩", "전세", "1억원", 2020)
# house2 = House("서울","아파트", "월세", "250만원", 2018)
# house3 = House("부산","주택", "매매", "20억원", 2020)
#
# lst = [house1, house2, house3]
#
# print("제이슨의 부동산에 오신걸 환영합니다.")
# if len(lst) <= 1:
#     print("총 {}대의 매물이 있습니다.".format(len(lst)))
#     for x in lst:
#         x.show_detail()
# else:
#     print("총 {}대의 매물들이 있습니다.".format(len(lst)))
#     for x in lst:
#         x.show_detail()

#문제9
# class ZeroError(Exception):
#     pass
#
# chicken = 10
# count = 1
# while chicken > 0:
#     try:
#         str_order = input("How many chicken would you like to order?")
#         order = int(str_order)
#         if order == 0:
#             raise ZeroError
#         if order <= chicken:
#             chicken = chicken - order
#             print("Order#: {}".format(count))
#             print("You've ordered {} order of chicken".format(order))
#             print("Available chicken: [{}]".format(chicken))
#             count+=1
#             if chicken == 0:
#                 print("We are out of chicken. Please come back next time, good bye.")
#         else:
#             print("You can only order up to {}".format(chicken))
#     except ValueError:
#         print("Wrong value. Please try again.")
#     except ZeroError:
#         print("Can't order 0 amount.")

