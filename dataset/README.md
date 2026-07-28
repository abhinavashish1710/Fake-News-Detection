# 📰 Fake News Detection using Machine Learning

A Machine Learning project that classifies news articles as **Real** or **Fake** using Natural Language Processing (NLP).

---

## 🚀 Features

- Detects fake and real news articles
- Text preprocessing and cleaning
- TF-IDF Vectorization
- Machine Learning classification
- Streamlit Web Application
- Easy-to-use interface

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit

---

## 📂 Project Structure

```
Fake-News-Detection/
│
├── dataset/
│   └── README.md
│
├── models/
│
├── notebooks/
│
├── src/
│   ├── app.py
│   ├── train.py
│   ├── predict.py
│   └── preprocess.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

The dataset is not included because of GitHub file size limits.

Download it from Kaggle:

https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

After downloading, place

```
Fake.csv
True.csv
```

inside the **dataset** folder.

---

## ▶️ Installation

```bash
git clone https://github.com/abhinavashish1710/Fake-News-Detection.git

cd Fake-News-Detection

pip install -r requirements.txt
```

---

## ▶️ Run

Train the model

```bash
python src/train.py
```

Run the application

```bash
streamlit run src/app.py
```

---

## 📌 Future Improvements

- Deep Learning Models
- BERT-based classifier
- News URL prediction
- Cloud deployment

---

## 👨‍💻 Author

**Abhinav Ashish**

GitHub:
https://github.com/abhinavashish1710
