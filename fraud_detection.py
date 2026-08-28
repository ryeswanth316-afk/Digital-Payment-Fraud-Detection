print("========================================")
print("   DIGITAL PAYMENT FRAUD DETECTION")
print("========================================")

print("\nEnter the transaction details")

amount = float(input("Transaction amount (₹): "))
transactions = int(input("Number of transactions today: "))
hour = int(input("Transaction hour (0-23): "))

risk_score = 0
reasons = []

if amount > 30000:
    risk_score += 30
    reasons.append("High transaction amount")

if transactions > 10:
    risk_score += 25
    reasons.append("Unusually high number of transactions")

if hour < 6 or hour > 23:
    risk_score += 25
    reasons.append("Unusual transaction time")

print("\n========== FRAUD ANALYSIS ==========")
print("Risk Score:", risk_score, "/ 80")

if risk_score >= 50:
    print("Status: SUSPICIOUS")
elif risk_score >= 25:
    print("Status: NEEDS REVIEW")
else:
    print("Status: NORMAL")

if reasons:
    print("\nReasons:")
    for reason in reasons:
        print("-", reason)
else:
    print("\nNo suspicious activity detected.")

print("====================================")