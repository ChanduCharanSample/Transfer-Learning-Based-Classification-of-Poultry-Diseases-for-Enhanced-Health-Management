# Transfer-Learning-Based-Classification-of-Poultry-Diseases-for-Enhanced-Health-Management
This project uses **Transfer Learning (VGG16)** to classify poultry diseases based on image data. It categorizes poultry into four classes:
- **Salmonella**
- **New Castle Disease**
- **Coccidiosis**
- **Healthy**

A **Flask-based web application** is developed to allow farmers, students, and commercial poultry businesses to upload images and receive real-time disease predictions to support early intervention and health management.

```text
Project Files/
└── poultry_disease_detection/
    ├── app.py
    ├── templates/
    │   ├── index.html
    │   ├── predict.html
    │   ├── about.html
    │   ├── contact.html
    │   └── developer.html
    ├── static/
    │   └── uploads/
    │       └── images (to predict the disease)
    └── healthy_vs_rotten.h5 (trained model stored in Google Drive)
```
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
Access the app in your browser:http://127.0.0.1:5000/

Features
Real-time disease prediction from poultry images

Confidence scores displayed

Multi-page interface (About, Contact, Developer)

Simple and user-friendly interface

Works offline once model is downloaded

Project Demo
Watch Demo Video on LinkedIn(https://www.linkedin.com/in/chandrikaranipothina/)

Output Screenshots:

![Image](https://github.com/user-attachments/assets/fa7889ae-8de7-441b-9aa7-6d690b13399a)

![Image](https://github.com/user-attachments/assets/f5e98ca7-e48f-4b37-aafb-0b94997d73f3)

![Image](https://github.com/user-attachments/assets/f5b02fd7-c453-4d88-a603-4038862808b1)

![Image](https://github.com/user-attachments/assets/d3bf407d-0512-4e88-b80e-4bfd3d198abd)

![Image](https://github.com/user-attachments/assets/ae612817-7ae8-4a68-bd35-1863022af2c4)

![Image](https://github.com/user-attachments/assets/115415cd-96bd-4754-ba2c-fa474e37fd4a)





