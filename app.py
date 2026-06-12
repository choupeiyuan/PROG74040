import gradio as gr 
from transformers import pipeline

MODEL_ID = "choupeiyuan/imdb-sentiment"

classifier = pipeline(
    "sentiment-analysis",
    model=MODEL_ID
)

def predict_sentiment(text):
    if not text.strip():
        return "Please enter a movie review."

    result = classifier(text)[0]

    label = result["label"]
    score = result["score"]

    return {
        label: float(score)
    }

demo = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(
        lines=5,
        placeholder="Enter a movie review here..."
    ),
    outputs=gr.Label(num_top_classes=2),
    title="IMDb Sentiment Analysis Demo",
    description="This app uses a DistilBERT model fine-tuned on the IMDb movie review dataset."
)

demo.launch()