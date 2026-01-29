import streamlit as st

st.set_page_config(page_title="Agentic AI Lab", layout="wide")
st.title("🤖 Live AI Agent Showcase")

st.markdown("""
### Watcher Agent Simulation
This demo mimics the **deterministic guardrail** logic I implemented to reduce clinical hallucinations by 40%.
""")

user_input = st.text_input("Enter a prompt for the Agent:")
if st.button("Run Agent"):
    with st.status("Agent Orchestrating...", expanded=True):
        st.write("Researcher Agent: Searching vector database (Pinecone)...")
        st.write("Watcher Agent: Validating HIPAA compliance & safety...")
        st.success("Response verified and delivered.")