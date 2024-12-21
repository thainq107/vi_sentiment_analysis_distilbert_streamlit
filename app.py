import streamlit as st
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="thainq107/ntc-scv-distilbert-base-uncased"
)

def main():
  st.title('Sentiment Analysis')
  st.title('Model: DistilBERT. Dataset: NTC-SCV')
  text_input = st.text_input("Sentence: ", "Đồ ăn ở quán này quá tệ luôn!")
  result = classifier(text_input)[0]
  label = result['label']
  score = result['score']
  st.success(f'Sentiment: {label} with {score:.2f} % probability.') 

if __name__ == '__main__':
     main() 