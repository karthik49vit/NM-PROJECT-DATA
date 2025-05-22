import random
from cryptography.fernet import Fernet

medical_data = {
    "fever": {
        "diagnosis": "Common Cold",
        "treatment": "Rest, stay hydrated, and use over-the-counter medicines like paracetamol."
    },
    "cough": {
        "diagnosis": "Respiratory Infection",
        "treatment": "Cough suppressants, warm fluids, and humidified air."
    },
    "headache": {
        "diagnosis": "Migraine",
        "treatment": "Pain relievers, caffeine, and avoiding trigger factors."
    },
    "sore throat": {
        "diagnosis": "Pharyngitis",
        "treatment": "Warm saltwater gargles and throat lozenges. Antibiotics if bacterial."
    },
    "sneezing": {
        "diagnosis": "Allergic Rhinitis",
        "treatment": "Antihistamines and avoiding allergens."
    },
    "fatigue": {
        "diagnosis": "Anemia",
        "treatment": "Iron supplements and increased iron-rich food intake."
    },
    "chest pain": {
        "diagnosis": "Angina",
        "treatment": "Medical evaluation needed. May require nitroglycerin or ECG testing."
    },
    "shortness of breath": {
        "diagnosis": "Asthma",
        "treatment": "Inhalers (bronchodilators) and avoiding triggers."
    },
    "diarrhea": {
        "diagnosis": "Gastroenteritis",
        "treatment": "Oral rehydration salts, fluids, and rest."
    },
    "vomiting": {
        "diagnosis": "Food Poisoning",
        "treatment": "Hydration, antiemetics, and medical evaluation if persistent."
    }
}

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_data(text):
    return cipher_suite.encrypt(text.encode()).decode()

def decrypt_data(token):
    return cipher_suite.decrypt(token.encode()).decode()

def chatbot():
    print("Welcome to the AI Healthcare Assistant!")
    print("Type your main symptom (e.g. fever, cough, headache): ")
    symptom = input().strip().lower()

    if symptom in medical_data:
        diagnosis = medical_data[symptom]["diagnosis"]
        treatment = medical_data[symptom]["treatment"]
        print(f"AI Diagnosis: {diagnosis}")
        print(f"Recommended Treatment: {treatment}")
        encrypted_diagnosis = encrypt_data(diagnosis)
        print(f"Encrypted Diagnosis for storage: {encrypted_diagnosis}")
        decrypted_diagnosis = decrypt_data(encrypted_diagnosis)
        print(f"Decrypted for verification: {decrypted_diagnosis}")
    else:
        print("Sorry, I couldn't diagnose that symptom. Please consult a healthcare provider.")

def get_iot_data():
    heart_rate = random.randint(58, 100)
    temperature = round(random.uniform(36.5, 38.0), 1)
    print(f"IoT Input: Heart Rate = {heart_rate} bpm, Temperature = {temperature}°C")

def collect_feedback():
    print("\nPlease rate your experience (1-5):")
    while True:
        rating = input("Rating: ")
        if rating.isdigit() and 1 <= int(rating) <= 5:
            break
        print("Please enter a valid rating between 1 and 5.")
    comment = input("Any comments?: ")
    print("Thank you for your feedback!")

if __name__ == "__main__":
    get_iot_data()
    chatbot()
    collect_feedback()