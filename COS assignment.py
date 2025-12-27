print("Tax filing status: ")
print("0= Single")
print("1= Married(joint)/Widow(er)")
print("2= Married(separate)")
print("3= Head of household")

status= int(input("Enter filing status: "))
income= float(input("Enter taxable income: "))
rate_brackets= {0: [(8350, 0.10),(33950, 0.15),
                    (82250, 0.25), (171550, 0.28),
                    (372950, 0.33), (float('inf'), 0.35),],
                1: [(16700, 0.10), (67900, 0.15),
                    (137050, 0.25), (208850, 0.28),
                    (372950, 0.33), (float('inf'), 0.35),],
                2: [(8350, 0.10), (33950, 0.15),
                    (68525, 0.25), (104425, 0.28),
                    (186475, 0.33), (float('inf'), 0.35),],
                3: [(11950, 0.10), (45500, 0.15),
                    (117450, 0.25), (190200, 0.28),
                    (372950, 0.33), (float('inf'), 0.35),]
}
def calculate_tax (taxable_income, bracket_list):
    tax = 0
    previous_limit = 0
    for limit, rate in bracket_list:
        if taxable_income > limit:
            tax += (limit-previous_limit) * rate
            previous_limit=limit
        else:
            tax += (taxable_income - previous_limit) * rate
            break
    return tax

if status in rate_brackets:
    tax = calculate_tax(income, rate_brackets[status])
    print(f"Your income tax is: ${tax:.2f}")
else:
    print("Status invalid")