# Transfer-Learning-Based-Classification-of-Poultry-Diseases-for-Enhanced-Health-Management
This project uses **Transfer Learning (VGG16)** to classify poultry diseases based on image data. It categorizes poultry into four classes:
- **Salmonella**
- **New Castle Disease**
- **Coccidiosis**
- **Healthy**

A **Flask-based web application** is developed to allow farmers, students, and commercial poultry businesses to upload images and receive real-time disease predictions to support early intervention and health management.


##  Project Structure

Project Files/
└── poultry_disease_detection/
├── app.py
├── templates/
│ ├── index.html
│ ├── predict.html
│ ├── about.html
│ ├── contact.html
│ └── developer.html
├── static/
│ └── uploads/images(to predict the diasease)
└── healthy_vs_rotten.h5 (trained model in  Google Drive)



##  Model Details

- **Architecture**: VGG16 (pre-trained)
- **Framework**: TensorFlow/Keras
- **Training Data**: Poultry disease dataset (Kaggle)
- **Preprocessing**: Image resizing, augmentation
- **Evaluation**: Accuracy, loss, confusion matrix



## 🔗 Model Files (Hosted on Google Drive)

Due to GitHub's file size and bandwidth restrictions, model files are hosted externally:

- [Download healthy_vs_rotten.h5](https://drive.google.com/file/d/13jzly1NEZrYors9ogzTQwUhytAVh6wmt/view?usp=sharing)

## 🚀 How to Run the Application

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ChanduCharanSample/Transfer-Learning-Based-Classification-of-Poultry-Diseases-for-Enhanced-Health-Management.git
Install dependencies:

pip install -r requirements.txt
Download model files from the links above and place them in:

Project Files/poultry_disease_detection/
Run the Flask app:

cd "Project Files/poultry_disease_detection"
python app.py
Access the app in your browser:

http://127.0.0.1:5000/
📷 Features
Real-time disease prediction from poultry images

Confidence scores displayed

Multi-page interface (About, Contact, Developer)

Simple and user-friendly interface

Works offline once model is downloaded

📽️ Project Demo
Watch Demo Video on LinkedIn(https://www.linkedin.com/in/chandrikaranipothina/)





