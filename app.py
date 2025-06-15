# streamlit_app.py
import streamlit as st
import requests

st.set_page_config(page_title="Lead Generator", page_icon="📈")
st.title("📈 Lead Generation Assistant")
st.markdown("""
This tool helps you generate leads using Google search + Gemini AI.
Just type your query below (e.g., *"AI startups hiring in India"*) and we’ll do the rest.
""")

query = st.text_input("🔍 Enter your lead generation query")
submit = st.button("🚀 Generate Leads")

if submit and query:
    st.info("Sending request to AI pipeline...")

    # Replace with your actual deployed n8n webhook URL
    webhook_url = "https://f4f7-49-205-255-244.ngrok-free.app/webhook/4e2f5b34-6d1b-4311-968a-75eb75311f75"

    try:
        response = requests.post(webhook_url, json={"query": query})

        if response.status_code == 200:
            result = response.json()
            markdown = result.get("markdown")
            file_url = result.get("file_url")
            
            st.success("✅ Leads generated successfully!")
            
            if markdown:
                st.markdown(markdown, unsafe_allow_html=True)
            else:
                st.warning("No leads were returned.")

            if file_url:
                st.markdown(f"📥 [Download your leads file]({file_url})")
            else:
                st.warning("File URL not available. Check your n8n output.")

        else:
            st.error(f"❌ Request failed: {response.status_code}")

    except Exception as e:
        st.error(f"Exception occurred: {str(e)}")
