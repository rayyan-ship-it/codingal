bill_amount=int(input("enter the bill amount"))
amount_paid=int(input("enter the amount paid"))
if amount_paid<bill_amount:
    due_payment=bill_amount-amount_paid
    print("due payment is ",due_payment)
elif amount_paid>bill_amount:
    change=amount_paid-bill_amount
    print("change to be returned is ",change)
else:
    print("no chenge or due amount")
