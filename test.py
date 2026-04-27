# 초기 데이터
accounts = {
    "1001": {"name": "김철수", "balance": 50000},
    "1002": {"name": "이영희", "balance": 120000},
}

history = []  # 거래 내역 저장


def deposit(account_no, amount):    # 계좌번호 , 입금액
    """입금"""
    if account_no in accounts:
        if amount > 0:
            accounts[account_no]["balance"]+=amount
            history.append({"type":"입금","account":account_no,"amount":amount})
        else:
            print("잘못된 금액입니다")
    else:
        print("존재하지 않는 계좌 번호입니다.")
 


def withdraw(account_no, amount):
    """출금"""
    if account_no in accounts:
        if amount > 0:
            if accounts[account_no]["balance"]>=amount:
                accounts[account_no]["balance"]-=amount
                history.append({"type":"출금","account":account_no,"amount":amount})
            else:
                print("현재 잔고 량 보다 많은 금액을 출금 할 수 없습니다")
        else:
            print("잘못된 금액입니다")
    else:
        print("존재하지 않는 계좌 번호입니다.")
 


def transfer(from_no, to_no, amount):
    """이체"""
    if from_no in accounts and to_no in accounts:
        if amount > 0:
            if accounts[from_no]["balance"]>=amount:
                accounts[from_no]["balance"]-=amount
                accounts[to_no]["balance"]+=amount
                history.append({"type":"이체","from":from_no,"to":to_no,"amount":amount})
            else:
                print("현재 잔고 량 보다 많은 금액을 출금 할 수 없습니다")
        else:
            print("잘못된 금액입니다")
    else:
        print("존재하지 않는 계좌 번호입니다.")
  


def show_history(account_no):
    """특정 계좌의 거래 내역 보기"""
    if account_no in accounts:
        rs = [x for x in history if x.get("from") == account_no or x.get("to") == account_no or x.get("account") == account_no]
        if not rs:
            return print("거래 내역이 없습니다")
        else:
            return print(rs)
    else:
        return print("계좌번호를 다시 확인 해 주세요")
    
   


def show_account(account_no):
    """잔액 + 거래 내역"""
    if account_no in accounts:
        balance = accounts[account_no]["balance"]
        show_history(account_no)
        print(f"현재 잔액 : {balance}")
    else:
        print("잘못된 계좌 번호 입니다")    
    
    


# 메인 루프
while True:
    print("\n==== ATM ====")
    print("1. 입금")
    print("2. 출금")
    print("3. 이체")
    print("4. 계좌 조회")
    print("0. 종료")

    menu = input("선택: ").strip()
    # ... 메뉴 분기 작성
    if menu == "1":
        account_no = input("입금 계좌를 입력해 주세요 : ").strip()
        amount = int(input("입금할 금액을 입력해 주세요 : ").strip())
        deposit(account_no,amount)
    elif menu =="2":
        account_no = input("출금 계좌를 입력해 주세요 : ").strip()
        amount = int(input("출금할 금액을 입력해 주세요 : ").strip())
        withdraw(account_no,amount)
    elif menu =="3":
        from_no = input("(이체)출금 계좌를 입력해 주세요 : ").strip()
        to_no = input("(이체)입금 계좌를 입력해 주세요 : ").strip()
        amount = int(input("이체할 금액을 입력해 주세요 : ").strip())
        transfer(from_no,to_no,amount)
    elif menu =="4":
        account_no = input("조회할 계좌 번호를 입력하세요").strip()
        show_account(account_no)
    elif menu =="0":
        break
    else:
        print("잘못된 입력 입니다")

     