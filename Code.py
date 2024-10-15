def mortgage_table(header, data, principal, interest):
    spacing = 20

    print("".join([f"{h:<{spacing}}" for h in header]))
    print("-" * spacing * len(header))

    # Print rows of data
    for row in data:
        print("".join([f"{str(item):<{spacing}}" for item in row]))

    print("")
    print(f"{'Total Principal Paid: MYR':<{spacing}} {round(principal, 2)}")
    print(f"{'Total Interest Paid: MYR':<{spacing}} {round(interest, 2)}")

def monthly_payment(loan_amount: int, interest_rate: float, years):
    monthly_interest_rate = interest_rate / 12
    total_payments = years * 12

    # loan amortization formula
    monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)

    return round(monthly_payment, 2)


def calculation(loan_amount: int, interest_rate: float, years: int, lump_sums=None):
    loan_data = []
    principal_paid = 0
    interest_paid = 0

    total_principal = loan_amount
    payment = monthly_payment(loan_amount, interest_rate, years)

    if lump_sums is None:
        lump_sums = {}

    for months in range(1, (years*12)+1):
        # immediately knock off principal from lump sum payment
        lump_sum = lump_sums.get(months, 0)
        total_principal -= lump_sum

        interest_portion = total_principal * (interest_rate/12)

        # check if monthly payment exceeds remaining amounts, then adjust accordingly
        if payment > (total_principal + interest_portion):
            payment = total_principal + interest_portion

        principal_portion = payment - interest_portion

        #append data to yearly data
        yearly_data = [
            months,
            round(total_principal, 2),
            round(payment, 2),
            round(principal_portion, 2),
            round(interest_portion, 2),
            round(lump_sum, 2)
        ]

        # minus off for next cycle calculation
        total_principal -= principal_portion

        # keep track of paid amounts
        principal_paid += principal_portion + lump_sum
        interest_paid += interest_portion

        #append yearly total to overall data
        loan_data.append(yearly_data)

        if total_principal <= 0:
            break

    return loan_data, principal_paid, interest_paid


def gen_lump_sum(years:int, amount:int):
    lump_sum = {}
    for years in range(5, years+1,5):
        lump_sum[years*12] = amount

    print(lump_sum)
    return lump_sum

# run it:
header = ["Month #", "O/S Principal", "Monthly Payment", "= Principal", "+ Interest", "Principal payoff"]
lump_sums = gen_lump_sum(years=5, amount=10000)
loan_data, total_principal, total_interest = calculation(loan_amount=660000, interest_rate=.03, years=35, lump_sums=lump_sums)
mortgage_table(header, loan_data, total_principal, total_interest)