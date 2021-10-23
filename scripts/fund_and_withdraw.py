from brownie import FundMe

from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    print(f"fund_me: {fund_me}")
    account = get_account()
    print(f"account: {account}")
    entrance_fee = fund_me.getEntranceFee()
    print(f"entrance_fee: {entrance_fee}")
    print("funding...")
    fund_me.fund({"from": account, "value": entrance_fee})


def withraw():
    fund_me = FundMe[-1]
    print(f"fund_me in withdraw func: {fund_me}")
    account = get_account()
    print(f"account in withdraw func: {account}")
    withraw_fee = fund_me.getEntranceFee()
    print(f"withraw_fee: {withraw_fee}")
    print("withrawing...")
    fund_me.withdraw({"from": account, "value": withraw_fee})


# 0.0250000000000000
def main():
    fund()
    withraw()
