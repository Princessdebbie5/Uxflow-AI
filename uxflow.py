import streamlit as st
import openai

# Use secret key stored in Streamlit Cloud
openai.api_key = st.secrets["OPENAI_API_KEY"]

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

User Flow:
"""

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful UX design assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            user_flow = response['choices'][0]['message']['content']
            st.success("✅ User flow generated!")
            st.markdown(user_flow)

 
