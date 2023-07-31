import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from PIL import Image, ImageDraw

# Set your Azure Custom Vision endpoint, prediction key, and project ID
ENDPOINT = "https://customvisionfreetiertom-prediction.cognitiveservices.azure.com/"
PREDICTION_KEY = "<PREDICTION_KEY>"
PROJECT_ID = "<PROJECT_ID>"

# Create a prediction client
credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
predictor = CustomVisionPredictionClient(ENDPOINT, credentials)

# Load the image to be processed
image_path = "test-file.jpg"
image = Image.open(image_path)

# Perform prediction on the image using
with open(image_path, "rb") as image_file:
    prediction = predictor.detect_image(PROJECT_ID, "Iteration6", image_file)

# Create a new image with buildings marked
draw = ImageDraw.Draw(image)
for prediction in prediction.predictions:
#Enter tag and prediction probability
    if prediction.tag_name == "Buildings" and prediction.probability > 0.001:
        left = prediction.bounding_box.left * image.width
        top = prediction.bounding_box.top * image.height
        width = prediction.bounding_box.width * image.width
        height = prediction.bounding_box.height * image.height
        draw.rectangle([left, top, left + width, top + height], outline="red", width=2)

# Save the marked image
marked_image_path = "test-file-marked.jpg"
image.save(marked_image_path)

print("Marked image saved successfully.")
