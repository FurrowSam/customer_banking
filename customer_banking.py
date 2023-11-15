# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account

from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Please enter your Savings Balance:"))
    savings_interest = float(input("Please enter your interest rate:"))
    savings_maturity = int(input("Please select the term in months:"))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest = create_savings_account(savings_balance, savings_interest, savings_maturity)
    
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Savings Account Balance and Interest Earned")
    print(f"Interest Earned: {savings_interest:.2f}")
    print(f"Updated Balance: {updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("Please enter your CD Balance:"))
    cd_interest = float(input("Please enter your interest rate:"))
    cd_maturity = int(input("Please select the term in months:"))


    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest = create_cd_account(cd_balance, cd_interest, cd_maturity)
    
    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"CD Account Balance and Interest Earned")
    print(f"Interest Earned: {cd_interest:.2f}")
    print(f"Updated Balance: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()