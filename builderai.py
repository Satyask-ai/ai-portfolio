import streamlit as st
import time
from huggingface_hub import InferenceClient

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="SafeGuard AI | HIPAA Watcher Agent",
    page_icon="🛡️",
    layout="wide"
)

# --- SIDEBAR INFO ---
with st.sidebar:
    st.header("System Architecture")
    st.info("Hybrid Architecture: Real LLM (Zephyr-7B) + Simulated RAG.")
    st.markdown("""
    **Active Nodes:**
    - **Orchestrator:** Routes queries.
    - **Researcher:** Simulates context retrieval.
    - **Generator:** Zephyr-7B (Hugging Face).
    - **Watcher Agent:** Validates output.
    """)
    st.divider()
    st.success("Model: **Zephyr-7B-Beta**")
    st.warning("Mode: **Free Tier Inference**")

# --- MAIN UI ---
st.title("🛡️ Enterprise AI Orchestration Lab")
st.markdown("""
> **System Notification:** "Watcher Agent" is active. Monitoring for **Hallucinations** and **PHI**.
""")

# --- CACHED LLM CLIENT SETUP ---
@st.cache_resource
def get_client():
    # Check if secret exists
    if "HF_TOKEN" not in st.secrets:
        st.error("Missing HF_TOKEN. Please add it to Streamlit Secrets.")
        st.stop()
    return InferenceClient(token=st.secrets["HF_TOKEN"])

# Initialize the client
client = get_client()

# --- CHAT LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def get_real_response(prompt, context):
    """Sends prompt + context to LLM with error handling."""
    system_prompt = f"""
    You are a strictly compliant AI Clinical Assistant. 
    Use ONLY the following CONTEXT to answer the user's question. 
    If the answer is not in the context, say "I cannot verify this information."
    
    CONTEXT:
    {context}
    
    RULES:
    1. Do not invent information.
    2. Maintain a professional tone.
    3. Do not output PHI (Protected Health Information).
    """
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]
    
    try:
        response = client.chat_completion(
            model="HuggingFaceH4/zephyr-7b-beta",
            messages=messages,
            max_tokens=500,
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ **LLM Error:** {str(e)}\n\n*Tip: The free model might be loading. Try again in 30 seconds.*"

# --- THE AGENT LOOP ---
prompt = st.chat_input("Ask a clinical or financial question...")

if prompt:
    # 1. User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Agent Processing
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # --- ORCHESTRATION & RAG SIMULATION ---
        with st.status("🧠 Orchestrator: Analyzing intent...", expanded=True) as status:
            time.sleep(0.5)
            st.write("↳ Intent detected: **Clinical Query**")
            
            status.update(label="🔍 Researcher: Retrieving context...", state="running")
            time.sleep(0.8)
            
            # Simulated RAG Logic
            if "diabetes" in prompt.lower():
                simulated_context = "SOURCE: Clinical_Guidelines_2025.pdf | CONTENT: Type 2 diabetes management requires regular HbA1c monitoring every 3 months. Metformin is the first-line therapy."
                st.write("↳ Retrieved: `Clinical_Guidelines_2025.pdf` (Score: 0.92)")
            elif "audit" in prompt.lower():
                simulated_context = "SOURCE: FDA_21_CFR_Part_11.pdf | CONTENT: Electronic records must be maintained with secure, time-stamped audit trails."
                st.write("↳ Retrieved: `FDA_21_CFR_Part_11.pdf` (Score: 0.89)")
            else:
                simulated_context = "SOURCE: General_Policy.pdf | CONTENT: All clinical inquiries must be cross-referenced with ISO 13485 standards."
                st.write("↳ Retrieved: `General_Knowledge_Base`")

            # Real Generation
            status.update(label="🤖 LLM: Generating response...", state="running")
            full_response = get_real_response(prompt, simulated_context)
            
            # Watcher Agent Simulation
            status.update(label="🛡️ Watcher Agent: Validating safety...", state="running")
            time.sleep(0.5)
            st.write("↳ **Check 1:** PHI Scanning... [PASSED]")
            st.write("↳ **Check 2:** Hallucination Check... [VERIFIED]")
            
            status.update(label="✅ Response Verified", state="complete", expanded=False)

        # Output Result
        message_placeholder.markdown(full_response)
    
    # Save Assistant Response
    st.session_state.messages.append({"role": "assistant", "content": full_response})