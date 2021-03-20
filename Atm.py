import random
randomNumber = random.random()
class Atm:
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    def BalanceEnquiry(self):
        print(f"Here you go, Balance in Account {self.cardNumber} is {randomNumber}")
    def cashWithdrawl(self):
        print(f"{randomNumber} has been withdrawed succesfully")
hdfc = Atm(989784534123,3543)
hdfc.BalanceEnquiry()