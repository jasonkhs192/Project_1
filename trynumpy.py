import numpy as np

a = np.array([1,2,3])
b = np.array([[4,5,6,7,8],[1,2,3,4,5]])
num = [1,2,3,4,5]
x = min(num)


def centered_average(nums):
  x = int(len(nums)/2 + 0.5)
  if len(nums)%2 == 0:
    print((nums[x] + nums[x-1])/2)
  else:
    print((nums[x-1]))


centered_average([5,3,4,6,2])


