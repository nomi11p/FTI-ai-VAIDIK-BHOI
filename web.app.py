import streamlit as st
import os

# Try multiple import styles to be compatible with different google-genai versions
GenAIClient = None
try:
    from google_genai import Client as GenAIClient
except Exception:
    try:
        from google import genai
        GenAIClient = genai.Client
    except Exception:
        GenAIClient = None

st.title("Google GenAI — Streamlit demo")

st.markdown(
    "Enter a text prompt below and click Generate. "
    "Make sure GOOGLE_API_KEY or GOOGLE_APPLICATION_CREDENTIALS is set in the environment, or paste an API key in the field below."
)

api_key = st.text_input("Google API key (optional — prefer env var)", type="password")

model = st.selectbox("Model", ["models/text-bison-001"], index=0)
prompt = st.text_area("Prompt", height=200)

def get_client(api_key_input):
    if GenAIClient is None:
        return None
    # Some client constructors accept api_key kwarg, others rely on ADC. Try both.
    if api_key_input:
        try:
            return GenAIClient(api_key=api_key_input)
        except TypeError:
            # Fallback to no-arg constructor and rely on environment
            return GenAIClient()
    return GenAIClient()

if st.button("Generate") and prompt.strip():
    client = get_client(api_key)
    if client is None:
        st.error("google-genai client not available. Install the package 'google-genai' in your environment.")
        st.stop()
    with st.spinner("Generating..."): 
        try:
            # Try common generate_text signature; adapt if your client library differs
            resp = client.generate_text(model=model, prompt=prompt)
            # Try some common response shapes
            text = getattr(resp, "text", None)
            if not text:
                try:
                    text = resp.output[0].content[0].text
                except Exception:
                    text = str(resp)
            st.subheader("Response")
            st.write(text)
        except Exception as e:
            st.error(f"Request failed: {e}")
