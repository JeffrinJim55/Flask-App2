from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

def get_chatbot_response(user_input):
    # Logic from the Python chatbot
    user_input = user_input.lower()
    
    # Fixed conditionals for multiple options
# General Disease Responses
    if any(x in user_input for x in ['bi', 'bye', 'goodbye', 'good bi', 'good bye']):
        return 'Goodbye! Have a great day! 😊'
    elif any(x in user_input for x in ['hello', 'hi', 'hai']):
        return 'Hi there! How can I help you?'
    elif any(x in user_input for x in ['how are you', 'how about you', 'how its going', 'whats up']):
        return "I'm just a bot, but I'm doing great!"
    elif any(x in user_input for x in ['your name', 'name', 'what is your name', 'whats your name', 'whats ur name']):
        return "I'm your Ai Doctor Bot 😊"
    elif any(x in user_input for x in ['help', 'need help', 'can you help me', 'can u hlp me', 'can you hlp me']):
        return "Sure! I'm here to help. What do you need assistance with?"
    elif any(x in user_input for x in ['how old are you', 'how old r u', 'how old r you']):
        return "Sorry! I'm a Bot so I have no age limit."
    elif any(x in user_input for x in ['jeffrin', 'jeffrin j', 'jeffy']):
        return "Jeffy is my Owner who creates me 😊"
    elif any(x in user_input for x in ['do you have crush', 'do you have girlfriend','do you have love','do you have lover','do you have any crush','do you have any girlfriend','do you have any girl friend','do you have any girlfruend' 'do you have girl friend','do you have any crush',]):
        return "Hahaha 😊. As an AI, I don't experience emotions like humans do, so I don't have a crush."
    elif any(x in user_input for x in ['ok', 'good', 'tq','great','excellet','thank a lot','thank you so much','thank you soo much' 'thankyou', 'thank you', 'thanks']):
        return "You're welcome! 😊"
    elif any(x in user_input for x in ['who is jeffy', 'who is jeffrin', 'who is Jeffrin']):
        return "Jeffy is my Owner who creates me 😊"
    elif any(x in user_input for x in ['tell me about jeffy', 'tell me about jeffrin', 'tell me abt jeffrin', 'tell me about Jeffrin J']):
        return "Jeffy is my Owner who creates me 😊"
    elif any(x in user_input for x in ['tell me abt yourself', 'tell me about yourself', 'yourself']):
        return "I'm your Ai Doctor Bot. I can assist you!"
    elif any(x in user_input for x in ['fever', 'my body is hot', 'temperature is high','i feel hot', 'i feel hot','i feel heat' ,'im suffering from fever', 'I m suffering from fever', 'i am suffering from fever']):
        return "I'm sorry you're feeling unwell 🥺. To manage fever: Stay hydrated, Rest, Apply a cool compress to your forehead, \nCommon tablets for fever: Paracetamol (e.g., Crocin, Calpol, Tylenol): For fever reduction and pain relief.\nIf the fever lasts more than 1-2 days, Consult a Doctor"
    elif any(x in user_input for x in ['Increased body temperature', 'chills', 'sweating', 'headache', 'muscle aches', 'fatigue', 'loss of appetite', 'dehydration', 'flushed skin']):
        return "Fever" 
    elif any(x in user_input for x in ['flu', 'influenza', 'cold', 'runny nose', 'fever', 'sore throat']):
        return "You might have the flu. Symptoms include fever, chills, body aches, and sore throat.\nRest, hydrate, and use paracetamol.\nIf symptoms last more than 3 days, consult a doctor."
    elif any(x in user_input for x in ['headache', 'migraine', 'pain in head', 'pain behind eyes']):
        return "Headaches can be caused by stress or dehydration.\nDrink water, rest, and use pain relievers like ibuprofen or paracetamol.\nConsult a doctor if it persists."
    elif any(x in user_input for x in ['cough', 'i have a cough', 'dry cough', 'wet cough']):
        return "Coughs can be caused by cold or flu.\nDrink warm liquids, rest, and consider over-the-counter medicine.\nSee a doctor if it lasts more than 3 weeks."
    elif any(x in user_input for x in ['head pain', 'pain in my head', 'pain on my head', 'headache', 'severe headache', 'pressure in head', 'tension headache', 'cluster headache', 'migraine', 'Suffring from head pain', 'suffering from headpain', 'suffering from severe head pain','suffering from severe headpain','im suffering from severe headpain','Im suffering from severe headpain','Im suffering from severe headpain can you help me']):
        return "Head pain or headaches can be caused by several factors such as stress, dehydration, lack of sleep, or migraines. Here are some general remedies:\n\n- Drink plenty of water to stay hydrated.\n- Rest in a quiet, dark room if the pain is severe.\n- Use over-the-counter pain relievers such as ibuprofen or paracetamol.\n- Apply a cold or warm compress to your head or neck.\n\nIf the headache persists for more than a few days, consult a doctor."
    elif any(x in user_input for x in ['fever', 'high temperature', 'body is hot', 'suffering from fever']):
        return "I'm sorry you're feeling unwell 🥺. To manage fever:\n- Stay hydrated by drinking plenty of fluids.\n- Rest as much as possible.\n- Use a cool compress on your forehead.\n- Common medications include Paracetamol (e.g., Crocin, Calpol, Tylenol) for reducing fever and relieving pain.\nIf the fever lasts more than 1-2 days, consult a doctor."
    elif any(x in user_input for x in ['flu', 'cold', 'runny nose', 'sore throat', 'influenza']):
        return "You might have the flu or a common cold. Symptoms include fever, chills, body aches, and a sore throat.\n- Rest and drink warm fluids like herbal teas or soups.\n- Use over-the-counter medicines like paracetamol or ibuprofen to relieve symptoms.\n- Gargle with salt water to soothe a sore throat.\nIf symptoms persist for more than 3 days, consult a doctor."
    elif any(x in user_input for x in ['headache', 'migraine', 'pain in head', 'head pain', 'pain behind eyes']):
        return "Headaches can be caused by stress, dehydration, or other factors.\n- Drink plenty of water to stay hydrated.\n- Rest in a quiet, dark room to relieve migraines or severe headaches.\n- Use pain relievers like ibuprofen or paracetamol.\n- Apply a cold or warm compress to your head or neck.\nIf the headache persists or is unusually severe, consult a doctor."
    elif any(x in user_input for x in ['cough', 'dry cough', 'wet cough', 'persistent cough']):
        return "Coughs can result from cold, flu, or allergies.\n- Stay hydrated with warm liquids like tea or honey water.\n- Rest and use throat lozenges to ease irritation.\n- Over-the-counter cough suppressants or expectorants can help.\n- See a doctor if the cough lasts more than 3 weeks or if accompanied by fever."
    elif any(x in user_input for x in ['stomach ache', 'pain in stomach', 'upset stomach', 'abdominal pain']):
        return "Stomach aches can be caused by indigestion, gas, or food poisoning.\n- Rest and avoid heavy or spicy foods.\n- Drink warm water or ginger tea to ease digestion.\n- Use antacids for relief from indigestion.\nIf the pain is severe or persists, consult a doctor."
    elif any(x in user_input for x in ['diabetes', 'high blood sugar', 'sugar problem']):
        return "Diabetes symptoms include frequent urination, thirst, and fatigue.\n- Maintain a healthy diet with controlled sugar intake.\n- Exercise regularly to manage blood sugar levels.\n- Monitor your blood glucose levels frequently.\n- Consult your doctor for medications or insulin therapy."
    elif any(x in user_input for x in ['asthma', 'shortness of breath', 'wheezing', 'difficulty breathing']):
        return "Asthma causes symptoms like shortness of breath and wheezing.\n- Use your prescribed inhaler to relieve symptoms.\n- Avoid known triggers such as allergens or cold air.\n- Stay calm and practice deep breathing exercises.\n- Consult your doctor for a personalized asthma action plan."
    elif any(x in user_input for x in ['back pain', 'lower back pain', 'sore back', 'spinal pain']):
        return "Back pain can be caused by poor posture, strain, or injury.\n- Rest and avoid heavy lifting.\n- Apply heat or cold packs to the affected area.\n- Consider over-the-counter pain relievers like ibuprofen.\nIf the pain persists or is severe, consult a doctor."
    elif any(x in user_input for x in ['high blood pressure', 'hypertension', 'blood pressure issue']):
        return "High blood pressure may not have noticeable symptoms but can lead to complications.\n- Maintain a healthy diet, reducing salt and saturated fats.\n- Engage in regular exercise like walking or yoga.\n- Monitor your blood pressure regularly and consult your doctor for medications."
    elif any(x in user_input for x in ['heart attack', 'chest pain', 'tightness in chest', 'cardiac arrest']):
        return "A heart attack is a medical emergency. Symptoms include:\n- Severe chest pain or tightness, radiating to the arm or jaw.\n- Shortness of breath and sweating.\n- Nausea or lightheadedness.\nCall emergency services immediately if you or someone else experiences these symptoms."
    elif any(x in user_input for x in ['stroke', 'slurred speech', 'numbness', 'face drooping']):
        return "A stroke is a medical emergency. Symptoms include:\n- Sudden numbness or weakness in the face, arm, or leg (especially on one side of the body).\n- Confusion, trouble speaking, or understanding.\n- Trouble seeing or sudden severe headache.\nCall emergency services immediately if a stroke is suspected."
    elif any(x in user_input for x in ['allergy', 'rash', 'itching', 'hives']):
        return "Allergy symptoms include itching, rash, or swelling.\n- Avoid allergens or triggers causing the reaction.\n- Use antihistamines to relieve symptoms.\nIf you experience difficulty breathing or severe swelling, seek emergency medical help."
    elif any(x in user_input for x in ['food poisoning', 'vomiting', 'diarrhea', 'nausea']):
        return "Food poisoning symptoms include nausea, vomiting, and diarrhea.\n- Stay hydrated by drinking plenty of fluids with electrolytes.\n- Rest and avoid solid foods until your stomach settles.\n- Use anti-nausea medications if needed.\nIf symptoms persist or worsen, consult a doctor."
    elif any(x in user_input for x in ['skin infection', 'redness', 'swelling', 'pus']):
        return "Skin infections may cause redness, swelling, or pain.\n- Keep the area clean and dry.\n- Use over-the-counter antibiotic ointments.\n- If the infection spreads or worsens, consult a doctor."
    elif any(x in user_input for x in ['arthritis', 'joint pain', 'stiffness']):
        return "Arthritis causes joint pain and stiffness.\n- Use heat or cold packs to relieve pain.\n- Engage in gentle exercises or physical therapy.\n- Consult a doctor for medications or treatment options."
    elif any(x in user_input for x in ['depression', 'feeling sad', 'hopeless', 'mental health issue']):
        return "Depression can cause persistent sadness and loss of interest.\n- Talk to someone you trust about your feelings.\n- Engage in activities you enjoy and practice mindfulness or relaxation techniques.\n- Consult a mental health professional for therapy or medication."
    elif any(x in user_input for x in ['anxiety', 'panic attack', 'nervousness', 'stress']):
        return "Anxiety symptoms include restlessness, rapid heartbeat, and worry.\n- Practice deep breathing and relaxation exercises.\n- Engage in physical activity to reduce stress.\n- Consult a mental health professional for support and treatment options."
    elif any(x in user_input for x in ['fever', 'high temperature', 'body is hot', 'suffering from fever']):
        return "I'm sorry you're feeling unwell. To manage fever:\n- Stay hydrated by drinking plenty of fluids.\n- Rest as much as possible.\n- Use a cool compress on your forehead.\n- Common medications include Paracetamol (e.g., Crocin, Calpol, Tylenol) for reducing fever and relieving pain.\nIf the fever lasts more than 1-2 days, consult a doctor."
    elif any(x in user_input for x in ['flu', 'cold', 'runny nose', 'sore throat', 'influenza']):
        return "You might have the flu or a common cold. Symptoms include fever, chills, body aches, and a sore throat.\n- Rest and drink warm fluids like herbal teas or soups.\n- Use over-the-counter medicines like paracetamol or ibuprofen to relieve symptoms.\n- Gargle with salt water to soothe a sore throat.\nIf symptoms persist for more than 3 days, consult a doctor."
    elif any(x in user_input for x in ['headache', 'migraine', 'pain in head', 'head pain', 'pain behind eyes']):
        return "Headaches can be caused by stress, dehydration, or other factors.\n- Drink plenty of water to stay hydrated.\n- Rest in a quiet, dark room to relieve migraines or severe headaches.\n- Use pain relievers like ibuprofen or paracetamol.\n- Apply a cold or warm compress to your head or neck.\nIf the headache persists or is unusually severe, consult a doctor."
    elif any(x in user_input for x in ['cough', 'dry cough', 'wet cough', 'persistent cough']):
        return "Coughs can result from cold, flu, or allergies.\n- Stay hydrated with warm liquids like tea or honey water.\n- Rest and use throat lozenges to ease irritation.\n- Over-the-counter cough suppressants or expectorants can help.\n- See a doctor if the cough lasts more than 3 weeks or if accompanied by fever."
    elif any(x in user_input for x in ['stomach ache', 'pain in stomach', 'upset stomach', 'abdominal pain']):
        return "Stomach aches can be caused by indigestion, gas, or food poisoning.\n- Rest and avoid heavy or spicy foods.\n- Drink warm water or ginger tea to ease digestion.\n- Use antacids for relief from indigestion.\nIf the pain is severe or persists, consult a doctor."
    elif any(x in user_input for x in ['diabetes', 'high blood sugar', 'sugar problem']):
        return "Diabetes symptoms include frequent urination, thirst, and fatigue.\n- Maintain a healthy diet with controlled sugar intake.\n- Exercise regularly to manage blood sugar levels.\n- Monitor your blood glucose levels frequently.\n- Consult your doctor for medications or insulin therapy."
    elif any(x in user_input for x in ['asthma', 'shortness of breath', 'wheezing', 'difficulty breathing']):
        return "Asthma causes symptoms like shortness of breath and wheezing.\n- Use your prescribed inhaler to relieve symptoms.\n- Avoid known triggers such as allergens or cold air.\n- Stay calm and practice deep breathing exercises.\n- Consult your doctor for a personalized asthma action plan."
    elif any(x in user_input for x in ['back pain', 'lower back pain', 'sore back', 'spinal pain']):
        return "Back pain can be caused by poor posture, strain, or injury.\n- Rest and avoid heavy lifting.\n- Apply heat or cold packs to the affected area.\n- Consider over-the-counter pain relievers like ibuprofen.\nIf the pain persists or is severe, consult a doctor."
    elif any(x in user_input for x in ['high blood pressure', 'hypertension', 'blood pressure issue']):
        return "High blood pressure may not have noticeable symptoms but can lead to complications.\n- Maintain a healthy diet, reducing salt and saturated fats.\n- Engage in regular exercise like walking or yoga.\n- Monitor your blood pressure regularly and consult your doctor for medications."
    elif any(x in user_input for x in ['heart attack', 'chest pain', 'tightness in chest', 'cardiac arrest']):
        return "A heart attack is a medical emergency. Symptoms include:\n- Severe chest pain or tightness, radiating to the arm or jaw.\n- Shortness of breath and sweating.\n- Nausea or lightheadedness.\nCall emergency services immediately if you or someone else experiences these symptoms."
    elif any(x in user_input for x in ['stroke', 'slurred speech', 'numbness', 'face drooping']):
        return "A stroke is a medical emergency. Symptoms include:\n- Sudden numbness or weakness in the face, arm, or leg (especially on one side of the body).\n- Confusion, trouble speaking, or understanding.\n- Trouble seeing or sudden severe headache.\nCall emergency services immediately if a stroke is suspected."
    elif any(x in user_input for x in ['allergy', 'rash', 'itching', 'hives']):
        return "Allergy symptoms include itching, rash, or swelling.\n- Avoid allergens or triggers causing the reaction.\n- Use antihistamines to relieve symptoms.\nIf you experience difficulty breathing or severe swelling, seek emergency medical help."
    elif any(x in user_input for x in ['food poisoning', 'vomiting', 'diarrhea', 'nausea']):
        return "Food poisoning symptoms include nausea, vomiting, and diarrhea.\n- Stay hydrated by drinking plenty of fluids with electrolytes.\n- Rest and avoid solid foods until your stomach settles.\n- Use anti-nausea medications if needed.\nIf symptoms persist or worsen, consult a doctor."
    elif any(x in user_input for x in ['skin infection', 'redness', 'swelling', 'pus']):
        return "Skin infections may cause redness, swelling, or pain.\n- Keep the area clean and dry.\n- Use over-the-counter antibiotic ointments.\n- If the infection spreads or worsens, consult a doctor."
    elif any(x in user_input for x in ['arthritis', 'joint pain', 'stiffness']):
        return "Arthritis causes joint pain and stiffness.\n- Use heat or cold packs to relieve pain.\n- Engage in gentle exercises or physical therapy.\n- Consult a doctor for medications or treatment options."
    elif any(x in user_input for x in ['depression', 'feeling sad', 'hopeless', 'mental health issue']):
        return "Depression can cause persistent sadness and loss of interest.\n- Talk to someone you trust about your feelings.\n- Engage in activities you enjoy and practice mindfulness or relaxation techniques.\n- Consult a mental health professional for therapy or medication."
    elif any(x in user_input for x in ['anxiety', 'panic attack', 'nervousness', 'stress']):
        return "Anxiety symptoms include restlessness, rapid heartbeat, and worry.\n- Practice deep breathing and relaxation exercises.\n- Engage in physical activity to reduce stress.\n- Consult a mental health professional for support and treatment options."
    elif any(x in user_input for x in ['stomach ache', 'pain in stomach', 'upset stomach']):
        return "Stomach aches can be caused by indigestion or food poisoning.\nRest, stay hydrated, and avoid heavy food.\nConsult a doctor if the pain persists."
    elif any(x in user_input for x in ['diabetes', 'i have diabetes', 'high blood sugar']):
        return "Diabetes symptoms include frequent urination, thirst, fatigue.\nMaintain a healthy diet, exercise, and monitor blood sugar.\nConsult your doctor for treatment."
    elif any(x in user_input for x in ['asthma', 'shortness of breath', 'wheezing']):
        return "Asthma can cause shortness of breath and wheezing.\nUse inhalers as prescribed, avoid triggers, and consult a doctor for an action plan."
    elif any(x in user_input for x in ['back pain', 'lower back pain', 'sore back']):
        return "Back pain may be from poor posture or strain.\nRest, apply heat or cold, and use pain relievers.\nConsult a doctor if the pain is severe or lasts."
    elif any(x in user_input for x in ['pneumonia', 'difficulty breathing', 'chest pain', 'cough', 'fever', 'shortness of breath']):
        return "Pneumonia symptoms include cough, fever, chest pain, and difficulty breathing.\n- Rest, stay hydrated, and monitor symptoms.\n- Antibiotics may be needed if it's bacterial.\n- Seek immediate medical care if breathing worsens or fever persists."
    elif 'pneumonia' in user_input or 'difficulty breathing' in user_input or 'chest pain' in user_input or 'cough' in user_input:
        return "It sounds like you may be experiencing symptoms of pneumonia. This could include cough, fever, chest pain, and difficulty breathing. Rest, stay hydrated, and consult a doctor promptly. If it's bacterial, antibiotics may be necessary. Seek emergency care if symptoms worsen."
    elif 'flu' in user_input or 'influenza' in user_input or 'runny nose' in user_input or 'sore throat' in user_input:
        return "The flu typically causes symptoms like fever, chills, sore throat, runny nose, and body aches. Rest, stay hydrated, and take over-the-counter medicines like paracetamol for fever. Consult a doctor if symptoms last longer than 3 days."
    elif 'diabetes' in user_input or 'high blood sugar' in user_input:
        return "High blood sugar can cause symptoms like frequent urination, thirst, and fatigue. Maintain a healthy diet, monitor your blood sugar levels, and consult your doctor for appropriate medication and treatment plans."
    elif 'asthma' in user_input or 'shortness of breath' in user_input or 'wheezing' in user_input:
        return "Asthma may cause wheezing, shortness of breath, and chest tightness. Use prescribed inhalers, avoid known triggers, and consult your doctor to manage your symptoms effectively."
    elif 'high blood pressure' in user_input or 'hypertension' in user_input:
        return "High blood pressure often has no symptoms but can cause headaches or dizziness. Monitor your blood pressure regularly, reduce salt intake, and follow a healthy diet. Consult your doctor for medication if necessary."
    elif 'skin rash' in user_input or 'itchy skin' in user_input:
        return "Skin rashes can result from allergies, infections, or irritants. Keep the area clean, avoid scratching, and use antihistamines or topical creams. If the rash worsens or spreads, consult a doctor."
    elif 'allergy' in user_input or 'sneezing' in user_input or 'itchy eyes' in user_input:
        return "Allergies can cause sneezing, runny nose, and itchy eyes. Avoid known allergens, use antihistamines, and consult a doctor if symptoms persist."
    elif 'back pain' in user_input or 'lower back pain' in user_input:
        return "Lower back pain can be due to poor posture or strain. Rest, apply heat or cold, and avoid heavy lifting. If the pain persists or worsens, consult a doctor."
    elif 'toothache' in user_input:
        return "Toothache can be caused by cavities or gum issues. Rinse with warm salt water, use over-the-counter pain relief, and consult a dentist for further treatment."
    elif 'eye pain' in user_input or 'red eyes' in user_input:
        return "Eye pain or redness can result from dryness, infections, or strain. Use lubricating eye drops, rest your eyes, and avoid screen overuse. Consult an eye specialist if the pain persists or worsens."
    elif 'vomiting' in user_input or 'nausea' in user_input:
        return "Nausea and vomiting can be caused by food poisoning or stomach infections. Rest, stay hydrated with small sips of water or ORS, and avoid solid food until you feel better. Consult a doctor if symptoms persist or worsen."
    elif 'joint pain' in user_input or 'arthritis' in user_input:
        return "Joint pain can result from arthritis or overuse. Rest the affected area, use pain relievers, and apply hot or cold compresses. Consult a doctor if the pain is severe or lasts long."
    elif 'depression' in user_input or 'feeling sad' in user_input:
        return "Depression can cause feelings of sadness, fatigue, and loss of interest in activities. Talk to someone you trust, stay active, and consult a mental health professional for support."
    elif 'fever' in user_input:
        return "It sounds like you're experiencing a fever. Common symptoms include a high temperature, chills, and body aches. To manage it, rest well, stay hydrated, and consider taking paracetamol to reduce fever. If the fever lasts more than 1-2 days or is very high, consult a doctor."
    elif 'severe head pain' in user_input or 'headache' in user_input:
        return "Severe head pain or headaches can result from stress, dehydration, or migraines. Drink plenty of water, rest in a dark and quiet room, and take over-the-counter pain relievers like ibuprofen or paracetamol. If the pain persists or is accompanied by other symptoms like nausea or vision issues, seek medical attention."
    elif 'stomach ache' in user_input or 'pain in stomach' in user_input:
        return "Stomach ache can be due to indigestion, gas, or more serious conditions. Try drinking warm water, eating bland foods, and avoiding spicy or greasy meals. If the pain is severe, recurring, or accompanied by symptoms like vomiting or fever, consult a doctor."
    elif any(x in user_input for x in ['high blood pressure', 'hypertension', 'blood pressure']):
        return "High blood pressure can cause headaches and dizziness.\nMaintain a healthy diet, reduce salt intake, and monitor regularly.\nConsult a doctor for medication."
    elif any(x in user_input for x in ['im suffering from pneumonia', 'Causes of pneumonia', 'how to cure pneumonia', 'how to cure pneumonia disease?','how to cure pneumonia disease']):
        return "Pneumonia causes fever, cough, difficulty breathing, and chest pain, often due to bacteria, viruses, or fungi. Treatment includes antibiotics or antivirals, rest, hydration, and medical care for severe symptoms.."
    elif any(x in user_input for x in ['who is leena', 'who is leena mam', 'tell me something about leena watson',]):
        return "Dr. Leena Watson is a Lecturer in Noorul Islam Centre for Higer Education at Kumaracoil"
    elif 'good morning' in user_input:
        return "Good morning! 😊 I hope you have a fantastic start to your day. How can I assist you?"
    elif any(x in user_input for x in ['who is vigila', 'who is vigila mam', 'tell me something about vigila',]):
        return "Dr. vigila is a Lecturer in Noorul Islam Centre for Higer Education at Kumaracoil"
    elif 'good afternoon' in user_input:
        return "Good afternoon! 😊 I hope your day is going well. What can I help you with today?"  
    elif 'good evening' in user_input:
        return "Good evening! 😊 I hope you had a great day. Let me know if there's anything I can assist you with."
    elif 'good night' in user_input:
        return "Good night! 😊 Wishing you sweet dreams and a restful sleep. Take care!"
    elif 'happy birthday' in user_input:
        return "Happy Birthday! 🎉🎂 I hope your day is filled with joy, love, and wonderful memories!"
    elif 'happy anniversary' in user_input:
        return "Happy Anniversary! 🎉 Wishing you many more years of happiness and love ahead!"
    elif 'good day' in user_input:
        return "Good day! 😊 I hope everything is going smoothly for you. How can I assist you?"
    elif 'goodbye' in user_input or 'bye' in user_input:
        return "Goodbye! 😊 Take care and have a wonderful day ahead!"
    elif 'have a great day' in user_input:
        return "Thank you! 😊 Wishing you a fantastic day as well!"
    elif 'good to see you' in user_input:
        return "Good to see you too! 😊 How can I assist you today?"
    elif 'nice to meet you' in user_input:
        return "Nice to meet you too! 😊 Let me know how I can help."
    elif 'how are you' in user_input:
        return "I'm just a bot, but I'm doing great! 😊 How about you?"
    else:
        return 'I am sorry, I have no knowledge about this request! Ask me another request 😊'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_chatbot_response(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
