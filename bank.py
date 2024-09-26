monthly_salary = float(input("Enter your Monthly Salary: "))
salary = float(30000.00)
if monthly_salary >= salary:
        print("You are eligible!")
        loan = float(input("Enter the amount of loan: "))
        if loan <= 10 * salary:
            payment = int(input("How many months to pay: "))
            interest = loan * 0.10
            total = loan + interest
            monthly = total / payment
            print(f"Loan Amount : {loan:.2f}")
            print(f"Interest (10%): {interest:.2f}")
            print(f"Amount to pay: {total:.2f}")
            print(f"Monthly Payment for {payment} months: {monthly:.2f}")
        else:
            print("You cannot avail loan, your request exceeded 10 times your monthly salary")
else:
        print("You are not eligible, Your Monthly Salary is too small to avail a loan")
