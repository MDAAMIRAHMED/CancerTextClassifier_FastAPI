# ClassiCancer

## Description

This project performs **text classification** on medical text data to predict types of **cancer** using **Natural Language Processing (NLP)** techniques. A simple **TensorFlow** deep learning model is trained on labeled data to identify patterns and classify cancer types. The model is deployed using a **FastAPI**-based REST service, enabling real-time predictions via API calls.


dataset: [link](https://www.kaggle.com/datasets/falgunipatel19/biomedical-text-publication-classification/data)

## Folder Structure
1. app/
    1. main.py
    2. tokenizer.pkl
    3. label_encoder.pkl
    4. text_rnn_model.h5      # (Model saved from CancerTextClassifier.ipynb)
    5. templates/
       1. index.html
       2. result.html
3. venv/
4. requirements.txt
