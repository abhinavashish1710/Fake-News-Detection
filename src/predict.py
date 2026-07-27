import joblib

model = joblib.load("models/fake_news_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_news(text):
    text = vectorizer.transform([text])
    prediction = model.predict(text)[0]
    return prediction
