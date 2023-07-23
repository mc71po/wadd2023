def payment_schedule(loan_amount, annual_interest_rate, monthly_payment):
    month = 1
    starting_balance = loan_amount
    payment = monthly_payment
    middle_balance = loan_amount - payment
    interest = middle_balance * annual_interest_rate / 12 / 100
    ending_balance = middle_balance + interest

    print("Month\tStarting Balance\t\tPayment\tMiddle Balance\tInterest\tEnding Balance")

    while starting_balance > 0:
        print("{0}\t{1:.2f}\t\t{2:.2f}\t{3:.2f}\t\t{4:.2f}\t{5:.2f}".format(month, starting_balance, payment, middle_balance, interest, ending_balance))

        month += 1
        starting_balance = ending_balance

        if ending_balance > monthly_payment:
            payment = monthly_payment
        else:
            payment = ending_balance

        middle_balance = starting_balance - payment
        interest = middle_balance * annual_interest_rate / 12 / 100
        ending_balance = middle_balance + interest


# Example Data 1
loan_amount = 300
annual_interest_rate = 12
monthly_payment = 100
payment_schedule(loan_amount, annual_interest_rate, monthly_payment)

# Example Data 2
loan_amount = 1000
annual_interest_rate = 15
monthly_payment = 350
payment_schedule(loan_amount, annual_interest_rate, monthly_payment)

# Example Data 3
loan_amount = 12345
annual_interest_rate = 33.25
monthly_payment = 3888.88
payment_schedule(loan_amount, annual_interest_rate, monthly_payment)