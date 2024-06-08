# -*- coding: utf-8 -*-
"""Cities_More_PSD.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AGzo0qyRNaNaz9TGAX0nMRaiRa0DSCcm
"""


import os
import ultralytics
from ultralytics import YOLO
import matplotlib.pyplot as plt
import numpy as np
import os
from IPython.display import display, Image
import gradio as gr
from PIL import Image
import onnxruntime as ort



# Load the ONNX model
onnx_model_path = "best.onnx"
# onnx_model_path = f"{HOME}/runs/classify/train/weights/best.onnx"

session = ort.InferenceSession(onnx_model_path)

# Define class names
class_names = ["Boston", "Chicago", "LosAngeles", "Phoenix", "WashingtonDC"]

# Prediction function
def predict_image(img):
    # Resize image to (224, 224) as expected by the model
    img = Image.fromarray(img).resize((224, 224))
    img_array = np.array(img).astype(np.float32) / 255.0  # Normalize the image
    img_array = img_array.transpose(2, 0, 1)  # Convert to (C, H, W)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Run inference
    input_name = session.get_inputs()[0].name
    outputs = session.run(None, {input_name: img_array})
    prediction = outputs[0][0]

    return {class_names[i]: float(prediction[i]) for i in range(len(class_names))}

# Create Gradio interface
image = gr.Image()
label = gr.Label(num_top_classes=5)

demo = gr.Interface(fn=predict_image, inputs=image, outputs=label).launch(debug=True)
demo.launch()