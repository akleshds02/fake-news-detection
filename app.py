import streamlit as st
import pandas as pd
import string
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from PIL import Image

# ---- 🔧 Load and prepare the data ---- #
@st.cache_data
def load_data():
    fake = pd.read_csv("Fake.csv/Fake.csv")
    true = pd.read_csv("True.csv/True.csv")
    
    # Balance dataset
    min_len = min(len(fake), len(true))
    fake = fake.sample(n=min_len, random_state=42)
    true = true.sample(n=min_len, random_state=42)
    
    fake['label'] = 0
    true['label'] = 1
    
    df = pd.concat([fake, true], ignore_index=True)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    return df

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

@st.cache_resource
def train_model(df):
    df['text'] = df['text'].apply(clean_text)

    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.8, min_df=5, ngram_range=(1, 2))
    X = vectorizer.fit_transform(df['text'])
    y = df['label']
    
    model = MultinomialNB()
    model.fit(X, y)
    
    return model, vectorizer

# ---- 🧠 App Interface ---- #
st.title("📰 𝔽𝕒𝕜𝕖 ℕ𝕖𝕨𝕤 𝔻𝕖𝕥𝕖𝕔𝕥𝕠𝕣")
image = Image.open("Fake-news.jpg") 
resized_image = image.resize((480, 520)) 
st.image(resized_image, caption="Fake? or Real?   You share it, WE SAY IT!", use_container_width=False)
st.write("​🇪​​🇳​​🇹​​🇪​​🇷​ ​🇦​​🇳​​🇾​ ​🇳​​🇪​​🇼​​🇸​ ​🇭​​🇪​​🇦​​🇩​​🇱​​🇮​​🇳​​🇪​ ​🇴​​🇷​ ​🇦​​🇷​​🇹​​🇮​​🇨​​🇱​​🇪​ ​🇹​​🇪​​🇽​​🇹​ ​🇹​​🇴​ ​🇨​​🇭​​🇪​​🇨​​🇰​ ​🇮​​🇫​ ​🇮​​🇹​'​🇸​ ​🇱​​🇮​​🇰​​🇪​​🇱​​🇾​ ​🇷​​🇪​​🇦​​🇱​ ​🇴​​🇷​ ​🇫​​🇦​​🇰​​🇪​.")

# Load and train model
df = load_data()
model, vectorizer = train_model(df)

# Input from user
user_input = st.text_area("Enter News Text Here:", height=150)

if st.button("Check"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        cleaned = clean_text(user_input)
        vec = vectorizer.transform([cleaned])
        pred = model.predict(vec)

        result = "🟢 Real News" if pred[0] == 1 else "🔴 Fake News"
        st.subheader("Prediction:")
        st.success(result)
st.markdown("---")
st.write("Made by Aklesh Shetty 🚀 | Powered by Streamlit❤️")

