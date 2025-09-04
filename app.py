import streamlit as st
import json
import random
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="DigiSkills.PK FAQ Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #f0f2f6;
    }
    .bot-message {
        background-color: #e6f7ff;
    }
    .title-text {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subheader-text {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# DigiSkills.PK FAQ data
faq_data = {
    "general": [
        {
            "question": "What is DigiSkills.PK?",
            "answer": "DigiSkills.PK is a initiative of the Government of Pakistan to equip the youth with essential digital skills. It offers free online courses in various digital domains to help Pakistanis become financially independent through freelancing."
        },
        {
            "question": "Who can join DigiSkills.PK?",
            "answer": "Any Pakistani citizen with basic education and access to the internet can join DigiSkills.PK. There are no age restrictions or specific educational requirements."
        },
        {
            "question": "Are the courses really free?",
            "answer": "Yes, all courses on DigiSkills.PK are completely free of cost for all Pakistani citizens."
        }
    ],
    "registration": [
        {
            "question": "How do I register for DigiSkills.PK?",
            "answer": "You can register by visiting the DigiSkills.PK website, clicking on the 'Register' button, and filling out the registration form with your personal details, educational background, and course preferences."
        },
        {
            "question": "What documents do I need for registration?",
            "answer": "You need a valid CNIC (Computerized National Identity Card) and a recent photograph for registration. For some advanced courses, educational certificates might be required."
        },
        {
            "question": "Can I change my selected courses after registration?",
            "answer": "Course selection can be changed during the add/drop period at the beginning of each batch. After that period, changes may not be possible."
        }
    ],
    "courses": [
        {
            "question": "What courses are offered on DigiSkills.PK?",
            "answer": "DigiSkills.PK offers courses in various domains including Freelancing, Digital Marketing, WordPress, Graphic Design, QuickBooks, AutoCAD, and many more digital skills."
        },
        {
            "question": "How long are the courses?",
            "answer": "Most courses are 3 months long, with a structured curriculum that includes video lectures, quizzes, and assignments."
        },
        {
            "question": "Will I get a certificate after completing a course?",
            "answer": "Yes, you will receive a certificate upon successful completion of a course, which requires passing all quizzes and assignments with the minimum required score."
        }
    ],
    "technical": [
        {
            "question": "What are the technical requirements for taking courses?",
            "answer": "You need a computer or smartphone with internet connection. Some courses may require specific software, but most use freely available tools."
        },
        {
            "question": "How do I access course materials?",
            "answer": "Once registered and enrolled, you can access course materials through the Learning Management System (LMS) on the DigiSkills.PK website."
        }
    ]
}

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Initialize session state for user info
if "user_info" not in st.session_state:
    st.session_state.user_info = {}

# Function to get answer from FAQ data
def get_answer(user_input):
    user_input = user_input.lower()
    
    # Check each category and question
    for category, questions in faq_data.items():
        for qa in questions:
            if any(keyword in user_input for keyword in qa["question"].lower().split()):
                return qa["answer"]
    
    # If no direct match, check for similar intents
    if any(word in user_input for word in ["hello", "hi", "hey", "greetings"]):
        return "Hello! Welcome to DigiSkills.PK FAQ chatbot. How can I help you today?"
    
    elif any(word in user_input for word in ["thank", "thanks", "appreciate"]):
        return "You're welcome! Is there anything else you'd like to know about DigiSkills.PK?"
    
    elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
        return "Thank you for chatting with me. Goodbye and best of luck with your DigiSkills journey!"
    
    elif any(word in user_input for word in ["course", "courses", "learn"]):
        return "DigiSkills.PK offers various digital skills courses. Would you like to know about specific courses like Freelancing, Digital Marketing, or WordPress?"
    
    elif any(word in user_input for word in ["register", "sign up", "join"]):
        return "You can register at the DigiSkills.PK website. Do you need help with the registration process?"
    
    # Default response if no match found
    return "I'm sorry, I don't have information about that. Could you please ask about DigiSkills.PK courses, registration process, or certificates? For more specific queries, please visit the official DigiSkills.PK website."

# App title and description
st.markdown('<p class="title-text">DigiSkills.PK FAQ Chatbot</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader-text">Get answers to your questions about DigiSkills.PK courses and registration process</p>', unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask about DigiSkills.PK..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get bot response
    response = get_answer(prompt)
    
    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar with additional information
with st.sidebar:
    st.header("About DigiSkills.PK")
    st.info("""
    DigiSkills.PK is a initiative of the Government of Pakistan to train 1 million people in digital skills.
    
    **Key Features:**
    - Free online courses
    - Self-paced learning
    - Certificates upon completion
    - Freelancing guidance
    """)
    
    st.header("Popular Questions")
    popular_questions = [
        "How do I register?",
        "What courses are available?",
        "Are certificates provided?",
        "What are the technical requirements?"
    ]
    
    for question in popular_questions:
        if st.button(question):
            # Add to chat when clicked
            st.session_state.messages.append({"role": "user", "content": question})
            response = get_answer(question)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    st.header("Need more help?")
    st.write("Visit the official [DigiSkills.PK website](https://digiskills.pk) for detailed information and support.")
