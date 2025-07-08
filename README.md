# 📰 Fake News Detection Web App

A simple and interactive **Streamlit-based web application** that detects whether a given news article or headline is likely **Fake** or **Real** using machine learning.

---

## Features

- Detects fake vs real news using logistic regression
- Clean and modern UI built using Streamlit
- Accepts any custom text input
- Outputs live prediction (Fake or Real)
- Lightweight and runs locally

---

## Project Structure

fake-news-detection/
├── app.py # Streamlit app script
├── fake_news_detector.ipynb # Jupyter Notebook - training & evaluation
├── Fake_news.jpg # Banner image used in app

yaml
Copy code

 **Note:** Dataset files (`Fake.csv`, `True.csv`) are not uploaded due to GitHub's 25MB file limit.

---

## Dataset Used

- [Kaggle: Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

Download both `Fake.csv` and `True.csv` and place them in the same directory.

---

##  How to Run

### Run in Jupyter Notebook (for training)
1. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn matplotlib
Open fake_news_detector.ipynb in Jupyter and run all cells.

Run the Web App (Streamlit)
Install Streamlit:

bash
Copy code
pip install streamlit
Run the app:

bash
Copy code
streamlit run app.py
The app will open in your browser at http://localhost:8501

🖼️ Sample

💡 Author
Aklesh D Shetty
B.E AI-ML | 6th Semester
Sir M Visvesvaraya Institute of Technology

⭐️ Feel free to fork, star, or suggest improvements!
