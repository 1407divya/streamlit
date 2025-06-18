import streamlit as st
import requests
import json

# Page config
st.set_page_config(page_title="👋 Self Introduction & Chat App", layout="wide")

# Sidebar for self-introduction
with st.sidebar:
    st.title("👋 About Me")
    st.subheader("🚫 NAME")
    st.text("Divya Peddi")

    st.subheader("🎓 College")
    st.text("Matrusri Engineering College, Hyderabad")

    st.subheader("📍 Location")
    st.text("Kothapet, Hyderabad")

    st.subheader("💡 Interests")
    st.text("Web Development\nData Science\nCreative Design\nAI & Emerging Tech")

    st.subheader("🛠 Skills")
    st.markdown("""
    - Python, C, Java  
    - SQL, Data Analysis (Excel)  
    - Problem Solving  
    - Teamwork & Communication  
    - Fast Learner & Adaptive
    """)

    with st.expander("📜 More About Me"):
        st.markdown("""
        I'm a curious and driven CSE student who loves solving real-world problems.

        I enjoy exploring AI, web development, and data science.

        I thrive in collaborative environments, especially during hackathons and group projects.

        📌 Outside tech, I enjoy storytelling, design, and brainstorming innovative ideas.

        📚 I've also completed certifications in:

        - Scaler's Coding Essentials  
        - PHP & MySQL  
        - PostgreSQL RDBMS  
        - Spoken Tutorial Python 3.4.3
        """)

# Main chat interface
st.title("💬 Chat with AI Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare API request
    API_URL = "https://api-inference.huggingface.co/models/684bfeda7486403e677a9ef7"
    headers = {
        "Authorization": f"Bearer {st.secrets['HUGGINGFACE_API_KEY']}",
        "Content-Type": "application/json"
    }
    
    try:
        # Make API request
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        response.raise_for_status()
        
        # Extract and display assistant's response
        assistant_response = response.json()[0]["generated_text"]
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info("Please make sure you have set up your Hugging Face API key in the secrets.toml file.")
