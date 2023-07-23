def payment_schedule(loan_amount, annual_interest_rate, monthly_payment):
    # Calculate monthly interest rate
    monthly_interest_rate = annual_interest_rate / 1200

    # Initialize variables
    month = 1
    starting_balance = loan_amount
    payment = monthly_payment
    middle_balance = loan_amount - payment
    interest = middle_balance * monthly_interest_rate
    ending_balance = middle_balance + interest

    # Print table header
    print("Month\tStarting Balance\tPayment\tMiddle Balance\tInterest\tEnding Balance")

    # Print table rows
    while starting_balance > 0:
        # Print row
        print("{0}\t{1:.2f}\t\t{2:.2f}\t{3:.2f}\t\t{4:.2f}\t{5:.2f}".format(month, starting_balance, payment, middle_balance, interest, ending_balance))

        # Update balance, payment, and middle interest
        month += 1
        starting_balance = ending_balance
        payment = min(monthly_payment, ending_balance)
        middle_balance = starting_balance - payment
        interest = middle_balance * monthly_interest_rate
        ending_balance = middle_balance + interest

    # Check if loan is paid off or terminated early
    if starting_balance <= 0:
        print("Loan paid off in {0} months".format(month - 1))
    else:
        print("Loan terminated after {0} months".format(month - 1))


# Input validation
while True:
    try:
        loan_amount = float(input("Enter the loan amount (between $1000 and $100000): "))
        if loan_amount < 1000 or loan_amount > 100000:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid loan amount between $1000 and $100000")

while True:
    try:
        annual_interest_rate = float(input("Enter the annual interest rate (between 0.1% and 100%): "))
        if annual_interest_rate < 0.1 or annual_interest_rate > 100:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid annual interest rate between 0.1% and 100%")

while True:
    try:
        monthly_payment = float(input("Enter the monthly payment (less than $100): "))
        if monthly_payment > 100:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid monthly payment less than $100")

# Call payment_schedule function with validated input
payment_schedule(loan_amount, annual_interest_rate, monthly_payment)