from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


# ---------------- TRAINING DATA ----------------

messages = [

    "Hello everyone have a nice day",
    "Good morning friends",
    "Happy birthday",
    "See you tomorrow",
    "Thank you for your help",

    "Please verify your account",
    "Limited offer available now",
    "Click the link to update details",
    "Your account needs verification",

    "URGENT you won a lottery prize",
    "Click here to claim your prize",
    "Congratulations you are a winner",
    "Send your bank details immediately",
    "You have won free money"
]


# ---------------- LABELS ----------------

labels = [

    "SAFE",
    "SAFE",
    "SAFE",
    "SAFE",
    "SAFE",

    "SUSPICIOUS",
    "SUSPICIOUS",
    "SUSPICIOUS",
    "SUSPICIOUS",

    "HIGH RISK",
    "HIGH RISK",
    "HIGH RISK",
    "HIGH RISK",
    "HIGH RISK"
]


# ---------------- CREATE VECTORIZER ----------------

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(messages)


# ---------------- TRAIN MODEL ----------------

model = MultinomialNB()

model.fit(X, labels)


# ---------------- PREDICTION FUNCTION ----------------

def predict_scam(message):

    message_vector = vectorizer.transform([message])

    prediction = model.predict(message_vector)[0]

    probabilities = model.predict_proba(message_vector)[0]

    confidence = max(probabilities) * 100

    return prediction, round(confidence, 2)