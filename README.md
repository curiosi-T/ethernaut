# ethernaut
[Ethernaut](https://ethernaut.openzeppelin.com/) is a fun game to learn blockchain development in Solidity. It consists of 25 challenges that need to be solved. I used [Brownie](https://eth-brownie.readthedocs.io/en/stable/) for local testing and deploying the contracts to the Rinkeby network. Other Solidity development frameworks one can use are [Truffle](https://trufflesuite.com/) or [Hardhat](https://hardhat.org/). 

Here are my solutions:
### 1. Fallback
- Call *contribute()* function with ether value > 0.001
- Call *receive()* function with ether value > 0: e.g. *await contract.send(toWei("0.1", "ether"))*
- Call *withdraw()*
### 2. Fallout
- There is a typo in the constructor. Just call the *Fal1out()* functions to become the owner
### 3. Coin Flip
- A [2nd contract (attacking contract)](solutions/contracts/CoinFlipAttack.sol) is used to run the logic from the actual flipping contract to predict the result and then calls the actual contract with the calculated result. 
### 4. Telephone
- Know the difference between tx.origin and msg.sender: *tx.origin* refers to the address the transaction was initiated from while *msg.sender* is the address that invoked the function. 
- Solution: Call *changeOwner()* from [another contract](solutions/contracts/TelephoneAttack.sol).
### 5. Token
- The require statement in the transfer function is useless, as the left side (*balances[msg.sender] - _value*) of the operand is rendered as uint, which is always greater than 0.
- Solution: Call *transfer* with a value greater than 20.