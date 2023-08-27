# -*- coding: utf-8 -*-
"""Exercise 12: Calculate income tax for the given income
by adhering to the below rules

Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20

Expected Output:
For example, suppose the taxable income is 45000 the income tax payable is
10000*0% + 10000*10%  + 25000*20% = $6000.
"""


def solution(income):
    ten_grand = 10_000
    twenty_grand = 20_000

    if income <= ten_grand:
        tax = 0
    elif ten_grand < income <= twenty_grand:
        tax = (income - ten_grand) * 0.1
    elif income > twenty_grand:
        tax = ten_grand * 0.1 + (income - twenty_grand) * 0.2

    return tax
