# import numpy as np
#
# a = np.array([1,2,3])
# b = np.array([[4,5,6,7,8],[1,2,3,4,5]])
# num = [1,2,3,4,5]
# x = min(num)
#
#
# def centered_average(nums):
#   x = int(len(nums)/2 + 0.5)
#   if len(nums)%2 == 0:
#     print((nums[x] + nums[x-1])/2)
#   else:
#     print((nums[x-1]))
#
#
# centered_average([5,3,4,6,2])
#

# class Champion:
#   def __init__(self, name, attack_dmg, ability_dmg, attack_speed, movement_speed, attack_range, hp):
#     self.name = name
#     self.attack_dmg = attack_dmg
#     self.ability_dmg = ability_dmg
#     self.attack_speed = attack_speed
#     self.movement_speed = movement_speed
#     self.attack_range = attack_range
#     self.hp = hp
#
#   def stat(self):
#     print("{}: \n      Attack Damage [{}] \n      Ability Power [{}] \n      Attack Speed [{}] \n      Movement Speed [{}] \n      Attack Range [{}] \n      HP [{}]".format(self.name, self.attack_dmg, self.ability_dmg, self.attack_speed, self.movement_speed, self.attack_range, self.hp))
#
#   def attack(self, enemy):
#     self.enemy = enemy
#     print("{} attacked {}. {} took -{} damage".format(self.name, enemy, enemy, self.attack_dmg))
# c1 = Champion("Garen", 85, 0, 0.58, 350, 150, 485)
# c1.stat()
# c1.attack("Darius")

# def quick_sort(sequence):
#   length = len(sequence)
#   if length <= 1:
#     return sequence
#   else:
#     pivot = sequence.pop()
#   print(pivot)
#   items_greater = []
#   items_lower = []
#
#   for x in sequence:
#     if x > pivot:
#       items_greater.append(x)
#     else:
#       items_lower.append(x)
#
#   return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
#
# ans = quick_sort([5,4,3,2,1])
#
# print(ans)
#
class Solution:
  def romanToInt(self, s):
    symbol = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000
    }
    total = 0
    for x in s:
      total = total + symbol[x]

Solution().romanToInt("IXLCD")