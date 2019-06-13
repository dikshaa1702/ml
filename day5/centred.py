# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:25:53 2019

@author: DiPu
"""
nums=[int(x) for x in input().split()]
max_value = nums[0]
min_value = nums[0]
sum = 0
for x in nums:
    max_value = max(max_value, x)
    min_value = min(min_value, x)
    sum += x
b=len(nums)-2      
print((sum - max_value - min_value) /b)