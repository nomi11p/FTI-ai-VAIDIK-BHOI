import  streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyB2esPAWxN-E-PxWUogL9ID-AnJYLTA8H0")
model = genai.GenerativeModel('gemini-2.5-flash')



st.title(" FTI AI by Vaidik Bhoi")
st.markdown("** proud to india that have its first ai for daily life help**")

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask FTI AI..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("FTI soch raha hai..."):
            response = model.generate_content(prompt).text
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
        # TERA KEY

# TERA BRAND
CREATOR = "Vaidik Bhoi"

print("FTI AI LIVE HAI!\n")

while True:
        user = input(">>> ")
        if user.strip() == "":
            continue
        if user.lower() in ['bye', 'exit', 'quit', 'band']:
            print("Bye bhai! Vaidik Bhoi ka AI band! 🇮🇳\n")
            break

        # FINAL PROMPT — POLITE + BHAI STYLE
        prompt = f"""
        Tu FTI AI hai.
        Malik: {CREATOR}
        
        RULES:
        - Jawab **user ki language mein de**
        - Hamesha **polite**, **bhai wala pyar**, **respectful**
        - Koi bhi batamizi, slang, "yo", "bro" mat bolna
        - Short, helpful, natural
        - Malik → "{CREATOR}"
        - Tu kaun → "Main FTI AI hoon, {CREATOR} ne banaya hai."  

         User ne poocha ({lang}): {user}
        """

        reply = model.generate_content(prompt).text.strip()
        print(reply + "\n")

    