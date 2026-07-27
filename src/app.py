import streamlit as st
from predict import predict_news

st.title("📰 Fake News Detection")

news = st.text_area("Enter News Article")

if st.button("Predict"):
    result = predict_news(news)

    if result == "FAKE":
        st.error("Fake News")
    else:
        st.success("Real News")
