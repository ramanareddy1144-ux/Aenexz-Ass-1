# Q3: Online Shopping Discount Eligibility

amount = float(input("Enter order amount (in Rs): "))
# strip() and lower() make the membership check case-insensitive
membership = input("Are you a member? (yes/no): ").strip().lower()

# Valid orders are from 0 to 1,00,000 inclusive
is_valid = amount >= 0 and amount <= 100000

if not is_valid:
    print("Invalid order amount. Must be between 0 and 1,00,000.")
else:
    if amount >= 5000:
        discount_percent = 15
        status = "Eligible: 15% discount"
    elif membership == "yes" and amount >= 2000:
        discount_percent = 10
        status = "Eligible: 10% member discount"
    else:
        discount_percent = 0
        status = "Not eligible for a discount"

    discount_amount = amount * discount_percent / 100
    final_amount = amount - discount_amount

    print("Original amount :", amount)
    print("Discount amount :", discount_amount)
    print("Final payable   :", final_amount)
    print("Status          :", status)

# Expected results:
# 6000, no       -> 15% off: discount 900, payable 5100
# 3000, yes      -> 10% off: discount 300, payable 2700
# 1500, no       -> no discount, payable 1500
# 100001, yes    -> invalid
