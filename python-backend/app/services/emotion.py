from transformers import pipeline

classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

def analyze_emotion(text: str):
    results = classifier(text)[0]
    top_emotion = max(results, key=lambda r: r["score"])
    return {
        "text": text,
        "emotion": top_emotion["label"],
        "confidence": round(top_emotion["score"], 4)
    }
 