#!/usr/bin/env python
# coding=utf-8

def binarysearch(items, v):
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if (items[mid] == v):
            return mid
        elif (items[mid] < v):
            low = mid + 1
        else:
            high = mid - 1
    return None


items = [1, 2, 3, 4, 5]
binarysearch(items, 3)
print(binarysearch(items, 3))
print(binarysearch(items, 6))
