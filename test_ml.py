from ml_model import predict_scam


message = input("Enter a message: ")

prediction, confidence = predict_scam(message)


print("\n----- ML SCAM PREDICTION -----")

print("Prediction:", prediction)

print("Confidence:", confidence, "%")