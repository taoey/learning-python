#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float("+inf")
        res = 0
        for price in prices:
            low = min(low, price)
            res = max(res, price-low)
        return res
