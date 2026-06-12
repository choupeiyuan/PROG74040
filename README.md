---
title: IMDb Sentiment Classifier
emoji: 🎬
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 5.0.0
app_file: app.py
pinned: false
---

# IMDb Sentiment Classifier

This is a simple sentiment analysis web app built with Hugging Face Spaces and Gradio.

The app uses a DistilBERT model fine-tuned on the IMDb movie review dataset. Users can enter a movie review, and the model predicts whether the review is positive or negative.

## Model

The model is loaded from Hugging Face Hub:

`your-username/imdb-distilbert-sentiment`

Please replace this model ID with your own uploaded model repository.

## How to Use

1. Type a movie review into the text box.
2. Click the submit button.
3. The app will return the predicted sentiment and confidence score.

## Example Inputs

Positive example:

`This movie was beautifully written and emotionally powerful.`

Negative example:

`The story was boring, the acting was weak, and I would not recommend it.`

## Files

- `app.py`: Main Gradio application.
- `requirements.txt`: Python packages required to run the app.
- `README.md`: Description and configuration for the Hugging Face Space.

## Notes

This project is designed as a teaching example for deploying a fine-tuned NLP model using Hugging Face Hub and Hugging Face Spaces.