import random

# Class labels
CLASSES = [
    "Melanoma",
    "Benign Keratosis",
    "Nevus",
    "Basal Cell Carcinoma"
]

def predict_image(image):
    """
    Simulated prediction logic (replace with real model later)
    """

    # Simulate different confidence ranges per class
    prediction = random.choice(CLASSES)

    if prediction == "Melanoma":
        confidence = round(random.uniform(70, 90), 2)
    elif prediction == "Basal Cell Carcinoma":
        confidence = round(random.uniform(75, 92), 2)
    else:
        confidence = round(random.uniform(85, 99), 2)

    return prediction, confidence