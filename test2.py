class Account:

    def __init__(self,account_no,name,balance=0):
        self.account_no=account_no
        self.name=name
        self.balance=balance
        self.history=[]
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"{amount}원 이 입금 되었습니다")
            self.history.append({"type":"입금","amount":amount})
        else:
            print("잘못된 금액 입니다")
    
    def withdraw(self,amount):
        if amount>0:
            if self.balance>=amount:
                self.balance-=amount
                print(f"{amount}원 이 출금 되었습니다")
                self.history.append({"type":"출금" , "amount":amount})
            else:
                print("금액이 부족합니다. 잔액을 확인 해 주세요")
        else:
            print("잘못된 금액 입니다")
    
    def show(self):
        print("이름 : ",self.name," / 잔액 : ",self.balance)
        for record in self.history:
           print(f"{record['type']}: {record['amount']:,}원")

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def add_account(self, account):
        # account.account_no를 키로 self.accounts에 저장
        self.accounts[account.account_no] = account
        
    
    def find(self, account_no):
        ...
    
    def transfer(self, from_no, to_no, amount):
        # 1. 두 계좌 모두 존재하는지 확인
        # 2. amount > 0 인지
        # 3. from 계좌 잔액 충분한지 (← 이걸 미리 체크해야 마법 방지!)
        # 4. 다 통과하면 withdraw + deposit
        ...
    
    def show_all(self):
        # self.accounts.values()로 모든 Account를 순회하며 .show() 호출
        ...

acc1 = Account("1001", "김철수", 50000)

print(acc1)              # 객체 자체 — <__main__.Account object at 0x...>
print(acc1.account_no)   # "1001"
print(acc1.name)         # "김철수"
print(acc1.balance)      # 50000
print(type(acc1))        # <class '__main__.Account'>