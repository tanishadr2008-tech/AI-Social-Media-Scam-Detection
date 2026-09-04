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


def analyze_message():

    message = input("\nEnter a social media message or link: ")

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

    # Scam classification
    if total_score == 0:
        classification = "SAFE"
    elif total_score <= 30:
        classification = "SUSPICIOUS"
    else:
        classification = "HIGH RISK"

    print("\n----- AI SCAM DETECTION RESULT -----")

    print("Risk Score:", total_score)
    print("Classification:", classification)

    if found_words:
        print("\nSuspicious Words Found:")

        for word in found_words:
            print("-", word)

    if link_patterns:
        print("\nSuspicious Link Patterns Found:")

        for pattern in link_patterns:
            print("-", pattern)

    if not found_words and not link_patterns:
        print("\nNo suspicious patterns detected.")


# Main menu
while True:

    print("\n====================================")
    print(" AI SOCIAL MEDIA AND ONLINE SCAM DETECTION")
    print("====================================")

    print("1. Analyze Message or Link")
    print("2. Exit")

    choice = input("\nEnter your choice (1 or 2): ")

    if choice == "1":
        analyze_message()

    elif choice == "2":
        print("\nThank you for using AI Scam Detection!")
        break

    else:
        print("\nInvalid choice! Please enter 1 or 2.")