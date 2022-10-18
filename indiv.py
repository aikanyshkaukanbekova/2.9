#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fum(m, n):
    if m == 0 or m == n:
        return 1
    if 0 <= m <= n:
        return fum(m, n - 1) + fum(m - 1, n - 1)

if __name__ == '__main__':
    m = int(input())
    n = int(input())
    print(fum(m, n))
