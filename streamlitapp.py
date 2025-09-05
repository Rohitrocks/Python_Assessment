import streamlit as st
import requests


st.set_page_config(page_title="AI Document Agent", layout="wide")

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000" 


st.title("📝 AI Document Agent")
st.write("Upload .pdf/.docx document, and I'll check it against english guidelines. I can even fix it for you.")

uploaded_file = st.file_uploader(
    "Drag and drop your file here or click to browse files.",
    type=["pdf", "docx"]
)

# Using session_state to store data.
if "api_response" not in st.session_state:
    st.session_state.api_response = {}

if uploaded_file:
    if st.button("Analyze Document", type="primary"):
        with st.spinner("Analyzing document... this might take a second."):
            files = {'file': (uploaded_file.name, uploaded_file.getvalue())}
            
            try:
                response = requests.post(f"{API_URL}/upload-and-check-compliance/", files=files)
                response.raise_for_status()
                
                # API response
                st.session_state.api_response = response.json()

            except requests.RequestException as e:
                st.error(f"Couldn't reach the API. Is it running? Error: {e}")


if st.session_state.api_response:
    state = st.session_state.api_response
    
    report = state.get("report", {})
    
    st.divider()
    st.success("Analysis complete!")

    # CHANGE #2: Get metrics from the 'summary' object inside the report.
    summary = report.get("summary", {})
    col1, col2 = st.columns(2)
    col1.metric("Grammar/Style Issues", summary.get("issue_count", 0))
    col2.metric("Clarity Score (1-10)", summary.get("clarity_score", "N/A"))
    
    tab1, tab2 = st.tabs(["🤖 AI Analysis", "🧐 All Issues"])
    
    with tab1:
        st.subheader("AI's analysis on Clarity & Tone")
        st.info(report.get("ai_analysis", "No analysis available."))
        
    with tab2:
        st.subheader("Grammar and Style Details")
        details = report.get("details", [])
        if not details:
            st.write("Looks clean! No specific grammar issues found.")
        else:
            for issue in details:
                st.warning(f"**Issue:** {issue['message']}")
                st.caption(f"**In context:** ...{issue['context']}...")
                if issue['replacements']:
                    st.caption(f"**Suggestions:** {', '.join(issue['replacements'])}")

    st.divider()
    
    if st.button("Fix Document with an AI ✨"):
        with st.spinner("The AI agent is rewriting your document..."):
            try:
                payload = {"text": state.get("original_text")}
                response = requests.post(f"{API_URL}/modify-document/", json=payload)
                response.raise_for_status()
                
                st.download_button(
                    label="📥 Download Fixed Document",
                    data=response.content,
                    file_name=f"fixed_{uploaded_file.name}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
                
            except requests.RequestException as e:
                st.error(f"Couldn't get the fix from the API. Error: {e}")            