#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def mul(a):
    def helper(b):
        return a * b
    return helper


if __name__ == "__main__":
    print(mul(5)(8))