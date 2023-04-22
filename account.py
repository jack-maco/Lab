
class Account:
    def __init__(self, name:str) -> None:
        """
        Function to setup object
        :param name: string used as account name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount:float) -> bool:
        """
        Function to add deposit to bank total
        :param amount: Amount to deposit
        :return: Boolean to specify if the deposit was successful
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False
        
    def withdraw(self, amount:float) -> bool:
        """
        Function to withdray from bank total
        :param amount: Amount to withdraw
        :return: Boolean to specify if the withdrawal was successful
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Function to return the balance
        :return: Float that contains the amount of money in the account
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Function to return the name of the account
        :return: The name of the account
        """
        return self.__account_name
