from brownie import FundMe, config, network, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    print(account)
    # if we are on a persistent network like rinkeby, use the assosiated address
    # otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        dataFeedAdd = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        dataFeedAdd = deploy_mocks()
    fund_me = FundMe.deploy(
        dataFeedAdd,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(f"Contract deployed to ", {fund_me.address})
    return fund_me


def main():
    deploy_fund_me()
