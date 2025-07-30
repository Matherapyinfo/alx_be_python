class BankAccount:
    """Represents a bank account with basic operations."""
    
    def __init__(self, initial_balance=0.0):
        """
        Initialize bank account with optional starting balance.
        
        Args:
            initial_balance (float): Starting balance (default 0.0)
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Deposit funds into account.
        
        Args:
            amount (float): Amount to deposit
        """
        if amount > 0:
            self.account_balance += amount
    
    def withdraw(self, amount):
        """
        Withdraw funds from account if sufficient balance exists.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            bool: True if withdrawal successful, False otherwise
        """
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Display current balance in user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")
