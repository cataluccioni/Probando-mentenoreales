import streamlit as st
from groq import Groq


st.set_page_config(
    page_title="Chat de Cata 🌸", 
    layout="centered"
)

st.title("Mi Chatbot🌸")
st.title("Responde")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])



if "messages" not in st.session_state:
    st.session_state.messages = [] 
    

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Escribí tu mensaje:")


if user_input:
   
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    print(f"*** MENSAJE DEL USUARIO: {user_input} ***")

    try:
        full_history = st.session_state.messages
        modelo = "llama-3.1-8b-instant"
        
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                chat_completion = client.chat.completions.create(
                    messages=full_history, 
                    model=modelo,
                )

            
                ai_response = chat_completion.choices[0].message.content
                st.markdown(ai_response)
        
    
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        
    except Exception as e:
        st.error(f"Error: {e}")
