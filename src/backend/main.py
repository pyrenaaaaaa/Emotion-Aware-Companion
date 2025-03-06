from fastapi import FastAPI, UploadFile, File
import librosa
import numpy as np
import os
import shutil
import logging

# Initialize FastAPI app
app = FastAPI()

# Create temp directory if it doesn't exist
os.makedirs("temp", exist_ok=True)

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Placeholder function for loading your trained model
def load_model():
    # Replace with your actual model loading code
    logger.info("Loading emotion detection model...")
    return None  # Replace with your trained model (e.g., a TensorFlow/PyTorch model)

# Placeholder function for predicting emotion using the model
def predict_emotion(features):
    # Replace with actual ML model prediction
    emotions = ["happy", "sad", "angry", "neutral", "stressed"]
    logger.info("Predicting emotion...")
    return np.random.choice(emotions)  # Replace with model.predict(features)

# Feature extraction for audio files
def extract_features(file_path):
    logger.info(f"Extracting features from: {file_path}")
    y, sr = librosa.load(file_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return np.mean(mfccs.T, axis=0)

@app.get("/")
def read_root():
    return {"message": "Emotion detection backend is running"}

@app.post("/detect_emotion")
async def detect_emotion(file: UploadFile = File(...)):
    temp_dir = "temp"
    try:
        # Save the uploaded file
        file_path = os.path.join(temp_dir, file.filename)
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
        logger.info(f"File saved: {file_path}")

        # Extract features and predict emotion
        features = extract_features(file_path)
        emotion = predict_emotion(features)

        logger.info(f"Detected emotion: {emotion}")
        return {"emotion": emotion}
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return {"error": str(e)}
    finally:
        # Cleanup the temporary file
        if os.path.exists(file_path):
            os.remove(file_path)
            logger.info(f"Temporary file deleted: {file_path}")