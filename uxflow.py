import streamlit as st
import openai

# Optional: Use dotenv or hardcode your key
openai.api_key = st.secrets["OPENAI_API_KEY"]  # You’ll set this in Streamlit Cloud secrets later

st.set_page_config(page_title="UXFlow AI", layout="centered")

st.title("🎯 UXFlow AI")
st.subheader("Instant User Flow Generator for Designers")

app_idea = st.text_area("Describe your app idea (1–2 sentences)", placeholder="E.g. A fintech app for managing savings and loans.")

if st.button("Generate Flow"):
    if not app_idea.strip():
        st.warning("Please enter an app idea to continue.")
    else:
        with st.spinner("Generating your user flow..."):
            prompt = f"""
            You are a UX design assistant. Based on the following app idea, generate a simple, clear user flow in numbered format.

            App Idea: {app_idea}

            from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[...],
    temperature=0.7,
)


