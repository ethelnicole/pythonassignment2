class BankAccount:

  def __init__(self, initial_balance=0.0):
    # Private attribute using double underscore
    self.__balance = initial_balance

  def deposit(self, amount):
    """Deposit money if the amount is positive."""
    if amount > 0:
      self.__balance += amount
      print(f"Successfully deposited: ${amount:.2f}")
    else:
      print("Deposit amount must be greater than zero.")

  def withdraw(self, amount):
    """Withdraw money if funds are sufficient and amount is positive."""
    if 0 < amount <= self.__balance:
      self.__balance -= amount
      print(f"Successfully withdrew: ${amount:.2f}")
    else:
      print("Invalid withdrawal amount or insufficient funds.")

  def display_balance(self):
    """Display the current account balance."""
    print(f"Current Balance: ${self.__balance:.2f}")


# Demonstration of Encapsulation
if __name__ == "__main__":
  # Create an account with an initial balance
  my_account = BankAccount(100.0)

  # Display initial balance using the public method
  my_account.display_balance()

  # Perform valid transactions
  my_account.deposit(50.0)
  my_account.withdraw(30.0)

  # Display updated balance
  my_account.display_balance()

  # Attempting to modify or access __balance directly from outside will fail
  try:
    print(my_account.__balance)
  except AttributeError as e:
    print(
        "\nDirect access blocked! Python raises an AttributeError for"
        " '__balance'."
    )
