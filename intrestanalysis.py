#------------Interest Rate-----------#
# General formula for compounding interest: A = P(1+i)^n

typeofinterest = input("Enter whether you are doing compounding or simple interest: ").lower()
term = float(input("How long is your current plan (in years): "))
investment = float(input("How much money have you invested: "))
section = input("Enter your type of timeline for interest rate (annual only for simple): ").lower()
interestrate = float(input("Enter your percentage interest rate here (don't add %): "))

# interest rate conversions
interest_semiannually = (interestrate / 100) / 2
interest_quarterly = (interestrate / 100) / 4
interest_daily = (interestrate / 100) / 365
interest_biweekly = (interestrate / 100) / 26
interest_annually = (interestrate / 100)

if typeofinterest == "compounding":

    #------ Semi Annual Calculations------#
    if section == "semi annually":
        amount_of_terms = 2
        nvalue = term * amount_of_terms

        total_amount = investment * ((1 + interest_semiannually) ** nvalue)
        print(f"\nThe total amount of interest is: ${total_amount:.2f}")

        gain = total_amount - investment
        print(f"The amount of money gained is: ${gain:.2f}")

        if 0 <= gain <= 900:
            print("Rerun the code and try again to see which type benefits you.")
        else:
            print("Thank you for running the code, if you want to check other terms, re-run!")

    #------ Quarterly Calculations------#
    elif section == "quarterly":
        print("\nA quarterly term indicates interest is applied 4 times per year.")

        amount_of_terms = 4
        nvalue = term * amount_of_terms

        total_amount = investment * ((1 + interest_quarterly) ** nvalue)
        print(f"\nThe total amount of interest for {term} years is: ${total_amount:.2f}")

        gain = total_amount - investment

        if 0 <= gain <= 900:
            print("This does not seem to be a beneficial plan for compounding interest.")
            checkup = input("\nWhat are you calculating compound interest for: ").lower()

            if checkup.lower() == "rrsp" or checkup.lower() == "resp":
                print("Compounding interest is very beneficial for RRSP/RESP.")
            elif checkup == "loans" or checkup == "mortgage":
                print("Compounding interest is very bad for loans — it becomes expensive.")
        else:
            print(f"This is a beneficial compounding program with a gain of ${gain:.2f}")

    #------ Daily Calculations------#
    elif section == "daily":
        print("\nDaily compounding applies interest every day.")

        amount_of_terms = 365
        nvalue = term * amount_of_terms

        total_amount = investment * ((1 + interest_daily) ** nvalue)
        print(f"\nThe total amount of interest is: ${total_amount:.2f}")

        gain = total_amount - investment

        if 0 <= gain <= 900:
            print("This seems like a low-benefit plan.")
        else:
            print(f"This is a beneficial program with a gain of ${gain:.2f}")
    #------Annual Calculations----#
    elif section == "annually" or "Annual":
        print("\Annual compounding applies interest every day.")

        amount_of_terms = 1
        nvalue = term * amount_of_terms

        total_amount = investment * ((1 + interest_daily) ** nvalue)
        print(f"\nThe total amount of interest is: ${total_amount:.2f}")

        gain = total_amount - investment

        if 0 <= gain <= 900:
            print("This seems like a low-benefit plan.")
        else:
            print(f"This is a beneficial program with a gain of ${gain:.2f}")

    #------ Bi-weekly Calculations------#
    elif section == "bi-weekly" or section == "biweekly":
        print("\nBi-weekly compounding applies interest 26 times per year.")

        amount_of_terms = 26
        nvalue = term * amount_of_terms

        total_amount = investment * ((1 + interest_biweekly) ** nvalue)
        print(f"\nThe total amount of interest is: ${total_amount:.2f}")

        gain = total_amount - investment

        if 0 <= gain <= 900:
            print("This seems like a low-benefit plan.")
        else:
            print(f"This is a beneficial program with a gain of ${gain:.2f}")

    else:
        print("Invalid compounding timeline entered.")

#-------Simple Interest Calculations------#
if typeofinterest == "simple":
    print("\nIn simple interest, there is a linear increase in the amount every year")
    print("Simple intrest is calculated based on an annual rate, in per year")
   
    interestprice = investment * (interestrate / 100)

    print(f"\nTotal interest earned: ${interestprice:.2f}")
    print(f"Final amount after {term} years: ${interestprice:.2f}")

#Hope you enjoyed the code! More types of such calculators and other programs are coming soon #
#Please do give me any feedback and send me feedback to my email: pavan00909@gmail.com #
# Do give me ideas for the next one if you have any other ideas on what you want me to create# 




