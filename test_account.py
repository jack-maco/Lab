import pytest
from account import *

class test_account():
    def setup_method(self):
        self.a1 = Account('Jane')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'Jane'
        assert self.a1.get_balance() == 0


    def test_deposit(self):
        #Testing Negative Input
        assert self.a1.deposit(-26.34) == False
        assert self.a1.get_balance() == pytest.approx(0, abs=0.001)

        #Testing Zero Input
        assert self.a1.deposit(0) == False
        assert self.a1.get_balance() == pytest.approx(0, abs=0.001)

        #Testing Positive Input
        assert self.a1.deposit(26.34) == True
        assert self.a1.get_balance() == pytest.approx(26.34, abs=0.001)

    def test_withdraw(self):
        #Testing Negative Input
        assert self.a1.withdraw(-26.34) == False
        assert self.a1.get_balance() == pytest.approx(0, abs=0.001)

        #Testing Zero Input
        assert self.a1.withdraw(0) == False
        assert self.a1.get_balance() == pytest.approx(0, abs=0.001)

        #Testing Positive Input
        self.a1.deposit(26.34)
        assert self.a1.withdraw(25) == True
        assert self.a1.get_balance() == pytest.approx(1.34, abs=0.001)

        #Testing Greater Than Input
        assert self.a1.withdraw(self.a1.get_balance() + 1) == False
        assert self.a1.get_balance() == pytest.approx(1.34, abs=0.001)