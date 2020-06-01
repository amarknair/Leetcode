#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 23:04:56 2019

@author: amar.kelunair
"""

points = [[1,1],[1,3],[2,1],[2,3],[2,2]]

def minAreaRect(points):
        S = set(map(tuple, points))
        ans = float('inf')
        for j, p2 in enumerate(points):
            for i in xrange(j):
                p1 = points[i]
                if (p1[0] != p2[0] and p1[1] != p2[1] and
                        [p1[0], p2[1]] in points and [p2[0], p1[1]] in points):
                    ans = min(ans, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))
        print ans if ans < float('inf') else 0

minAreaRect(points)