// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BankAccount {

    address public owner;
    uint256 private balance;

    // Constructor
    constructor() {
        owner = msg.sender;
    }

    // Modifier to allow only account owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this operation");
        _;
    }

    // 1. Deposit Money
    function deposit() public payable onlyOwner {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balance += msg.value;
    }

    // 2. Withdraw Money
    function withdraw(uint256 amount) public onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(amount <= balance, "Insufficient balance");

        balance -= amount;

        (bool success, ) = payable(owner).call{value: amount}("");
        require(success, "Withdrawal failed");
    }

    // 3. Show Balance
    function showBalance() public view returns (uint256) {
        return balance;
    }
}