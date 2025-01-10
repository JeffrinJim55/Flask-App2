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
        return "I'm sorry you're feeling unwell. To manage fever: Stay hydrated, Rest, Apply a cool compress to your forehead, \nCommon tablets for fever: Paracetamol (e.g., Crocin, Calpol, Tylenol): For fever reduction and pain relief.\nIf the fever lasts more than 1-2 days, Consult a Doctor"
    elif any(x in user_input for x in ['Increased body temperature', 'chills', 'sweating', 'headache', 'muscle aches', 'fatigue', 'loss of appetite', 'dehydration', 'flushed skin']):
        return "Fever" 
    elif any(x in user_input for x in ['flu', 'influenza', 'cold', 'runny nose', 'fever', 'sore throat']):
        return "You might have the flu. Symptoms include fever, chills, body aches, and sore throat.\nRest, hydrate, and use paracetamol.\nIf symptoms last more than 3 days, consult a doctor."
    elif any(x in user_input for x in ['headache', 'migraine', 'pain in head', 'pain behind eyes']):
        return "Headaches can be caused by stress or dehydration.\nDrink water, rest, and use pain relievers like ibuprofen or paracetamol.\nConsult a doctor if it persists."
    elif any(x in user_input for x in ['cough', 'i have a cough', 'dry cough', 'wet cough']):
        return "Coughs can be caused by cold or flu.\nDrink warm liquids, rest, and consider over-the-counter medicine.\nSee a doctor if it lasts more than 3 weeks."
    elif any(x in user_input for x in ['stomach ache', 'pain in stomach', 'upset stomach']):
        return "Stomach aches can be caused by indigestion or food poisoning.\nRest, stay hydrated, and avoid heavy food.\nConsult a doctor if the pain persists."
    elif any(x in user_input for x in ['diabetes', 'i have diabetes', 'high blood sugar']):
        return "Diabetes symptoms include frequent urination, thirst, fatigue.\nMaintain a healthy diet, exercise, and monitor blood sugar.\nConsult your doctor for treatment."
    elif any(x in user_input for x in ['asthma', 'shortness of breath', 'wheezing']):
        return "Asthma can cause shortness of breath and wheezing.\nUse inhalers as prescribed, avoid triggers, and consult a doctor for an action plan."
    elif any(x in user_input for x in ['back pain', 'lower back pain', 'sore back']):
        return "Back pain may be from poor posture or strain.\nRest, apply heat or cold, and use pain relievers.\nConsult a doctor if the pain is severe or lasts."
    elif any(x in user_input for x in ['high blood pressure', 'hypertension', 'blood pressure']):
        return "High blood pressure can cause headaches and dizziness.\nMaintain a healthy diet, reduce salt intake, and monitor regularly.\nConsult a doctor for medication."
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
    # app.run(debug=True, host='0.0.0.0', port=5000)
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
