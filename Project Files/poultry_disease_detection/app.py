from flask import Flask, render_template, request, redirect
from tensorflow.keras.models import load_model
import numpy as np
import os
import cv2

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load the trained model from root
model = load_model('healthy_vs_rotten.h5')

# Class labels
classes = ['Coccidiosis', 'Healthy', 'New Castle Disease', 'Salmonella']

# Prediction logic
def predict_disease(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (224, 224))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    class_index = np.argmax(pred)
    confidence = np.max(pred)

    explanation = {
        'Coccidiosis': 'Caused by protozoa, leads to bloody diarrhea and weakness.',
        'Healthy': 'No visible signs of disease.',
        'New Castle Disease': 'Highly contagious viral disease affecting the respiratory system.',
        'Salmonella': 'Causes diarrhea, dehydration, and reduced egg production.'
    }

    return classes[class_index], explanation[classes[class_index]], confidence

# Flask routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/developer')
def developer():
    return render_template('developer.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect('/predict')

        file = request.files['image']
        if file.filename == '':
            return redirect('/predict')

        if file:
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            prediction, explanation, confidence = predict_disease(filepath)
            image_path = f"/static/uploads/{filename}"

            return render_template('predict.html',
                                   prediction=f"{prediction} (Confidence: {confidence:.2f})",
                                   explanation=explanation,
                                   image_path=image_path)

    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
