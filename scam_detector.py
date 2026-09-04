from link_detector import detect_suspicious_link

# Suspicious scam words
suspicious_words = [
    "urgent",
    "free money",
    "lottery",
    "winner",
    "prize",
    "bank details",
    "password",
    "click here",
    "limited offer"
]

message = input("Enter a social media message or link: ")

message_lower = message.lower()

found_words = []

# Check suspicious words
for word in suspicious_words:
    if word in message_lower:
        found_words.append(word)

# Calculate message risk score
message_score = len(found_words) * 10

# Detect suspicious links
link_score, link_risk, link_patterns = detect_suspicious_link(message)

# Calculate total score
total_score = message_score + link_score

# Determine total risk
if total_score == 0:
    risk_level = "LOW"
elif total_score <= 30:
    risk_level = "MEDIUM"
else:
    risk_level = "HIGH"

print("\n----- SCAM DETECTION RESULT -----")

print("Risk Score:", total_score)
print("Risk Level:", risk_level)

if found_words:
    print("\n⚠️ Suspicious Words Found:")
    for word in found_words:
        print("-", word)

if link_patterns:
    print("\n⚠️ Suspicious Link Patterns Found:")
    for pattern in link_patterns:
        print("-", pattern)

if not found_words and not link_patterns:
    print("\n✅ No suspicious patterns detected.")