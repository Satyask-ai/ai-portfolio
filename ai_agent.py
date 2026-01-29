import streamlit as st
import time
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="SafeGuard AI | HIPAA Watcher Agent",
    page_icon="🛡️",
    layout="wide"
)

# --- SIDEBAR INFO ---
with st.sidebar:
    st.header("System Architecture")
    st.info("This demo simulates the **Agentic Orchestration** workflow used in my enterprise clinical systems.")
    st.markdown("""
    **Active Nodes:**
    - **Orchestrator:** Routes queries.
    - **Researcher:** RAG retrieval (simulated).
    - **Watcher Agent:** Intercepts & validates.
    """)
    st.divider()
    st.write("Current Status: **Online** ")
    st.write("Compliance Mode: **Strict (HIPAA)**")

# --- MAIN UI ---
st.title(" Enterprise AI Orchestration Lab")
st.markdown("""
> **System Notification:** "Watcher Agent" is active. All outputs are being monitored for **Hallucinations** and **PHI (Protected Health Information)** leakage.
""")

# Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- THE AGENT LOGIC ---
prompt = st.chat_input("Ask a clinical or financial question...")

if prompt:
    # 1. User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Agent Processing (The "Live" Experience)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # --- PHASE 1: ORCHESTRATION ---
        with st.status("Orchestrator: Analyzing intent...", expanded=True) as status:
            time.sleep(1)
            st.write("↳ Intent detected: **Clinical Query**")
            st.write("↳ Routing to: **Medical RAG Node**")
            
            # --- PHASE 2: RETRIEVAL ---
            time.sleep(1.2)
            status.update(label="Researcher: Retrieving context...", state="running")
            st.write("↳ Querying Vector DB (Pinecone)...")
            st.write("↳ Retrieved 3 chunks from 'FDA_21_CFR_Part_820.pdf'")
            
            # --- PHASE 3: GENERATION ---
            time.sleep(1.5)
            status.update(label="LLM: Generating response...", state="running")
            
            # --- PHASE 4: WATCHER AGENT (YOUR KEY SKILL) ---
            time.sleep(1)
            status.update(label="Watcher Agent: Validating safety...", state="running")
            st.write("↳ **Check 1:** PII/PHI Scanning... [PASSED]")
            st.write("↳ **Check 2:** Hallucination Score (Ragas)... [0.98 - HIGH ACCURACY]")
            st.write("↳ **Check 3:** Tone Analysis... [PROFESSIONAL]")
            
            status.update(label="Response Verified & Delivered", state="complete", expanded=False)

        # --- SIMULATED RESPONSE GENERATION ---
        # This simulates a smart response based on keywords in your prompt
        response_text = ""
        if "patient" in prompt.lower() or "medical" in prompt.lower():
            response_text = "Based on the retrieved clinical protocols, the patient data has been processed securely. The **Watcher Agent** confirmed that no PHI was exposed in this output. Refer to ISO 13485 Section 7 for further validation guidelines."
        elif "finance" in prompt.lower() or "cost" in prompt.lower():
            response_text = "Financial analysis complete. The 'Accounting Gatekeeper' node has verified these figures against the latest SEC filings. Note: Optimizing this workflow saved approximately **$40,000 annually** in token costs."
        else:
            response_text = "I have processed your request through the **Multi-Agent Ecosystem**. The internal logic graph confirmed the query is safe to answer. How else can I assist with your orchestration needs?"

        # Stream the response like ChatGPT
        full_response = ""
        for chunk in response_text.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})