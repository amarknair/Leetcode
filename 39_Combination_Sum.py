#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:49:34 2020

@author: amar.kelunair
"""
class Solution(object):
    def combinationSum(self, array, N):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        
        def backtrack(combination=[], i=0):
            if sum(combination)==N:
                ans.append(combination)
                return
            while(i<len(array)):
                if sum(combination)+array[i]<=N:
                    backtrack(combination+[array[i]],i)
                i+=1
        backtrack()
        return ans
