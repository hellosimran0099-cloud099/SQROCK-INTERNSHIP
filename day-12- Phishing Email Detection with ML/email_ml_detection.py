import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from datetime import datetime
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

# Load the training dataset
data = pd.read_csv("dataset.csv")


# Display the dataset
emails = data["text"]
# Convert email text into numerical features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(emails)
# Display the shape of the feature matrix
print("\nFeature matrix shape:", X.shape)

# Display number of emails
print("\nTotal emails:", len(data))
# Get the labels
y = data["label"]
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Create the ML model
model = MultinomialNB()

# Train the model using training data
model.fit(X_train, y_train)

# Test the model
test_predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, test_predictions)

print("\nModel Accuracy:", accuracy * 100, "%")


# New email for testing
new_email = input("\nEnter email text: ")

# Convert the new email using the same TF-IDF vectorizer
new_features = vectorizer.transform([new_email])

# Make prediction
prediction = model.predict(new_features)
# Create confusion matrix
cm = confusion_matrix(y_test, test_predictions)

print("\nConfusion Matrix:")
print(cm)

# Display confusion matrix as a graph
plt.figure()
plt.imshow(cm)
plt.title("Phishing Email Detection - Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")

plt.xticks([0, 1], ["Legitimate", "Phishing"])
plt.yticks([0, 1], ["Legitimate", "Phishing"])

# Write values inside the matrix
for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i, j], ha="center", va="center")

plt.savefig("confusion_matrix.png")
plt.show()
# Display result
# Convert prediction into readable result
if prediction[0] == 1:
    result = "PHISHING EMAIL"
else:
    result = "LEGITIMATE EMAIL"

print("\nPrediction:", result)

# Save detection result
with open("detection_report.txt", "w") as file:
    file.write("=== PHISHING EMAIL DETECTION REPORT ===\n")
    file.write(f"Date & Time: {datetime.now()}\n")
    file.write(f"Input Email: {new_email}\n")
    file.write(f"Prediction: {result}\n")
    file.write(f"Model Accuracy: {accuracy * 100}%\n")

print("\nDetection report saved to detection_report.txt")
