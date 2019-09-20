#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:41:43 2019

@author: taka0
"""
       
def twoSum(nums, target):
    """ Given an array of integers, returns indices of the two numbers 
        such that they add up to a specific target.

        Assumptions: 
        - each input will have exactly one solution; 
        - the same element will not appear in the list twice."""
    
    for i in range(0, len(nums) - 1):
        print("nums[i]: " + str(nums[i]))
        for j in range(i + 1, len(nums)):
            print("nums[j]: " + str(nums[j]))
            print("nums[j] + nums[i]: " + str(nums[i] + nums[j]))
            if (nums[i] + nums[j] == target):
                return [i, j]
            
    print("error: no solution available")