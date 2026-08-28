# Digital Payment Fraud Detection

A beginner-friendly Python project that analyzes digital payment transactions and identifies potentially suspicious activity using rule-based risk scoring.

## Features

- Analyzes transaction amount
- Checks the number of transactions in a day
- Detects unusual transaction times
- Calculates a risk score
- Classifies transactions as:
  - NORMAL
  - NEEDS REVIEW
  - SUSPICIOUS
- Displays reasons for suspicious activity

## Technologies Used

- Python
- Conditional Statements
- Lists
- Loops
- User Input

## How It Works

The program collects three transaction details:

1. Transaction amount
2. Number of transactions today
3. Transaction hour

It then assigns risk points based on predefined rules and calculates a total risk score.

## Example

**Input:**

- Transaction amount: ₹4500
- Transactions today: 2
- Transaction hour: 2

**Output:**

```text
Risk Score: 25 / 80
Status: NEEDS REVIEW
Reason: Unusual transaction time
