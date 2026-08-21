import streamlit as st
import numpy as np
import faiss
import PyPDF2
import io
import time
import json
import os
from datetime import datetime
from sentence_transformers import SentenceTransformer
from orchestrator import orchestrate_bug_analysis
from defect_pattern_analytics import get_defect_patterns
# -------------------------------
# LOAD AI MODEL
# -------------------------------

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()


# -------------------------------
# LOAD FAISS INDEX
# -------------------------------

@st.cache_resource
def load_faiss():
    return faiss.read_index("bug_index.faiss")

index = load_faiss()
# ---------------------------------
# PAGE CONFIGURATION
# ---------------------------------

st.set_page_config(
    page_title="AI Smart Bug Analyzer",
    page_icon="🐞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------
# CUSTOM CSS
# ---------------------------------

st.markdown("""
<style>

.main-title{
font-size:42px;
font-weight:bold;
color:#4F8BF9;
}

.sub-title{
font-size:18px;
color:gray;
}

.card{
padding:20px;
border-radius:15px;
background:#262730;
border:1px solid #4F8BF9;
margin-bottom:15px;
}

.small-card{
padding:15px;
border-radius:12px;
background:#1F2028;
text-align:center;
}

.metric{
font-size:25px;
font-weight:bold;
color:#00E676;
}

.footer{
text-align:center;
color:gray;
padding-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------
# SIDEBAR
# ---------------------------------

with st.sidebar:

    st.title("🐞 AI Smart Bug Analyzer")

    st.markdown("---")

    st.subheader("Project")

    st.write("""
**AI Smart Bug Analyzer & Fix Advisor**

Infosys Springboard Internship Project
""")

    st.markdown("---")

    st.subheader("Pipeline")

    st.success("✔ Bug Submission")

    st.success("✔ Preprocessing")

    st.success("✔ Chunking")

    st.success("✔ Embedding Generation")

    st.success("✔ FAISS Index")

    st.success("✔ Similarity Search")

    st.info("LLM Fix Advisor (Coming Soon)")

    st.markdown("---")

    st.subheader("Statistics")

    col1,col2=st.columns(2)

    with col1:
        st.metric("Historical Bugs","267")

    with col2:
        st.metric("Embeddings","267")

    st.metric("Database","Ready")

    st.markdown("---")

    st.subheader("Workflow")

    st.write("""
1️⃣ Submit Bug

2️⃣ Generate Embedding

3️⃣ Search FAISS

4️⃣ Retrieve Similar Bugs

5️⃣ Suggest Fix
""")

# ---------------------------------
# HEADER
# ---------------------------------

st.markdown(
"""
<div class="main-title">
🐞 AI Smart Bug Analyzer & Fix Advisor
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="sub-title">
AI-powered semantic bug analysis using RAG, Sentence Transformers and FAISS.
Upload your bug report or describe your issue below.
</div>
""",
unsafe_allow_html=True
)

st.divider()

# ---------------------------------
# FEATURE CARDS
# ---------------------------------

c1,c2,c3,c4=st.columns(4)

with c1:
    st.info("📄 Bug Upload")

with c2:
    st.info("🧠 AI Analysis")

with c3:
    st.info("🔍 Similarity Search")

with c4:
    st.info("💡 Fix Suggestions")

st.divider()
# ==========================================
# BUG SUBMISSION FORM
# ==========================================

st.subheader("📥 Submit a Bug Report")

left, right = st.columns([2, 1])

with left:

    bug_title = st.text_input(
        "🐞 Bug Title",
        placeholder="Example: NullPointerException while logging into the application"
    )

    bug_description = st.text_area(
        "📝 Bug Description",
        height=180,
        placeholder="""Describe the issue...

Example:

Application crashes after clicking Login.
The issue occurs when invalid user data is returned from the database.
"""
    )

    stack_trace = st.text_area(
        "⚠ Stack Trace / Error Log",
        height=180,
        placeholder="""Example:

java.lang.NullPointerException
    at LoginService.java:45
    at LoginController.java:20
"""
    )

with right:

    st.markdown("### 📂 Upload File")

    uploaded_file = st.file_uploader(
        "Choose Bug Report",
        type=["txt", "log", "pdf"]
    )

    st.info("""
Supported Files

• TXT

• LOG

• PDF
""")

    st.warning("""
Maximum Size

200 MB
""")

st.divider()
# ==========================================
# ANALYZE BUTTON
# ==========================================

# ==========================================
# ANALYZE BUTTON
# ==========================================

analyze = st.button(
    "🚀 Analyze Bug",
    use_container_width=True
)

# ==========================================
# FILE READING & ANALYSIS
# ==========================================

file_text = ""

if analyze:

    st.divider()

    # ----------------------------
    # INPUT VALIDATION
    # ----------------------------

    if bug_title.strip() == "":
        st.error("⚠ Please enter Bug Title.")
        st.stop()

    if bug_description.strip() == "":
        st.error("⚠ Please enter Bug Description.")
        st.stop()

    # ----------------------------
    # LOADING
    # ----------------------------

    with st.spinner("🔍 Analyzing Bug... Please wait..."):
        time.sleep(2)

    st.success("✅ Bug Submitted Successfully!")
    # ------------------------------
# TRIAGE AGENT
# ------------------------------

    analysis_result = orchestrate_bug_analysis(
    bug_title,
    bug_description,
    stack_trace
    )

    triage = analysis_result["triage"]
    log_analysis = analysis_result["log_analysis"]
    root_cause = analysis_result["root_cause"]
    duplicate = analysis_result["duplicate_detection"]
    remediation = analysis_result["remediation"]
    # ------------------------------------
# SAVE COMBINED OUTPUT
# ------------------------------------

    with open("analysis_output.json", "w") as file:

        json.dump(
        analysis_result,
        file,
        indent=4
    )
    # =====================================
# SAVE HISTORY OF ALL ANALYSES
# =====================================


    history_file = "analysis_history.json"

    history = []

    if os.path.exists(history_file):

        with open(history_file, "r") as file:

            try:
                history = json.load(file)

            except:

                history = []

    # Store additional details
    history.append({

        "bug_title": bug_title,

        "bug_description": bug_description,

        "stack_trace": stack_trace,

        "analysis": analysis_result

    })

    with open(history_file, "w") as file:

        json.dump(
            history,
            file,
            indent=4
        )
    st.success("✅ Analysis saved successfully!")
    # ----------------------------
    # BUG SUMMARY
    # ----------------------------

    st.subheader("📋 Bug Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Title Length", len(bug_title))

    with col2:
        st.metric("Description Length", len(bug_description))

    with col3:
        st.metric("Stack Trace Length", len(stack_trace))

    st.info(f"📅 Analysis Time : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")

    # ----------------------------
    # DISPLAY USER INPUT
    # ----------------------------

    st.markdown("## 🐞 Submitted Bug")

    st.markdown(f"### 📝 Bug Title\n{bug_title}")

    st.markdown(f"### 📄 Bug Description\n{bug_description}")

    st.markdown(f"### ⚠ Stack Trace\n{stack_trace}")
    st.divider()

    st.header("🧠 Triage Agent Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Severity", triage["severity"])

    with col2:
        st.metric("Priority", triage["priority"])

    col3, col4 = st.columns(2)

    with col3:
        st.metric("Component", triage["component"])

    with col4:
        st.metric("Confidence", f"{triage['confidence']}%")

    st.subheader("📌 Reasoning")
    st.info(triage["reasoning"])

    st.subheader("🔑 Matched Keywords")
    st.write(", ".join(triage["matched_keywords"]))
    st.divider()

    st.header("📄 Log Analysis Agent")

    st.metric("Exception Type", log_analysis["exception_type"])

    st.metric("Failure Point", log_analysis["failure_point"])

    st.subheader("🛤 Affected Code Path")

    if log_analysis["code_path"]:

        for path in log_analysis["code_path"]:
            st.code(path)

    else:
        st.info("No stack trace available.")
    st.divider()

    st.header("🧠 Root Cause Analysis")

    st.markdown(root_cause)
    st.divider()

    st.header("🔄 Duplicate Detection")

    if duplicate["duplicate"]:
        st.success("✅ This bug appears to be a duplicate.")
    else:
        st.warning("🆕 This appears to be a new bug.")

    st.metric("Similarity", f"{duplicate['similarity_percentage']}%")

    st.subheader("📄 Matched Historical Bug")

    st.text(duplicate["matched_bug"])

    st.divider()

    st.header("💡 Remediation Agent")

    st.markdown(remediation)
    # ----------------------------
    # FILE UPLOAD
    # ----------------------------

    if uploaded_file is not None:

        st.divider()

        st.subheader("📂 Uploaded File Information")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("📄 File Name", uploaded_file.name)

        with col2:
            st.metric("📦 File Size", f"{uploaded_file.size/1024:.2f} KB")

        with col3:
            st.metric("📁 File Type", uploaded_file.type)

        try:

            # TXT & LOG
            if uploaded_file.type == "text/plain":

                file_text = uploaded_file.read().decode("utf-8")

            # PDF
            elif uploaded_file.type == "application/pdf":

                pdf_reader = PyPDF2.PdfReader(uploaded_file)

                for page in pdf_reader.pages:

                    text = page.extract_text()

                    if text:
                        file_text += text

            # EMPTY FILE
            if file_text.strip() == "":

                st.warning("""
⚠ No readable text found.

Possible Reasons:

• Uploaded file is empty

• PDF contains scanned images

• Unsupported encoding
""")

            else:

                st.success("✅ File Read Successfully!")

                c1, c2 = st.columns(2)

                with c1:
                    st.metric("Characters", len(file_text))

                with c2:
                    st.metric("Lines", len(file_text.splitlines()))

                with st.expander("📖 View Extracted File Content"):

                    st.text_area(
                        "",
                        value=file_text,
                        height=250
                    )

        except Exception as e:

            st.error(f"Error while reading file:\n{e}")

    else:

        st.info("📂 No file uploaded. Analysis will use the manually entered bug description.")
        # ==========================================
# AI ANALYSIS
# ==========================================

if analyze:

    st.divider()

    st.header("🧠 AI Analysis")

    # Combine all available text
    complete_text = (
        bug_title +
        " " +
        bug_description +
        " " +
        stack_trace +
        " " +
        file_text
    ).lower()

    # --------------------------------------
    # Severity Prediction
    # --------------------------------------

    severity = "🟢 Low"

    if any(word in complete_text for word in [
        "crash",
        "fatal",
        "outofmemory",
        "segmentation fault",
        "exception",
        "nullpointerexception"
    ]):
        severity = "🔴 Critical"

    elif any(word in complete_text for word in [
        "error",
        "failed",
        "timeout",
        "unable",
        "database"
    ]):
        severity = "🟠 High"

    elif any(word in complete_text for word in [
        "warning",
        "slow",
        "delay",
        "performance"
    ]):
        severity = "🟡 Medium"

    # --------------------------------------
    # Category Prediction
    # --------------------------------------

    category = "General"

    if any(word in complete_text for word in [
        "database",
        "sql",
        "mysql",
        "oracle"
    ]):
        category = "🗄 Database"

    elif any(word in complete_text for word in [
        "login",
        "button",
        "page",
        "ui",
        "screen"
    ]):
        category = "🖥 Frontend"

    elif any(word in complete_text for word in [
        "api",
        "server",
        "backend"
    ]):
        category = "⚙ Backend"

    elif any(word in complete_text for word in [
        "memory",
        "cpu",
        "performance"
    ]):
        category = "🚀 Performance"

    # --------------------------------------
    # Metrics
    # --------------------------------------

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Severity", severity)

    with c2:
        st.metric("Category", category)

    with c3:
        st.metric("Analysis Status", "Completed")

    st.divider()

    # --------------------------------------
    # Root Cause
    # --------------------------------------

    st.subheader("🔍 Possible Root Cause")

    if severity == "🔴 Critical":

        st.error("""
Possible Reasons

• Null Object Access

• Invalid Memory Reference

• Application Crash

• Missing Exception Handling
""")

    elif severity == "🟠 High":

        st.warning("""
Possible Reasons

• Database Failure

• API Timeout

• Invalid Request

• Connection Failure
""")

    else:

        st.success("""
Possible Reasons

• Minor Validation Issue

• UI Rendering Problem

• Configuration Error
""")

    # --------------------------------------
    # Suggested Fix
    # --------------------------------------

    st.subheader("💡 Suggested Fix")

    st.info("""
✔ Check stack trace carefully.

✔ Validate user input.

✔ Add proper exception handling.

✔ Verify database/API connection.

✔ Review application logs.
""")
# ==========================================
# SIMILARITY SEARCH
# ==========================================

st.divider()

st.header("🔍 Similar Historical Bug Reports")

# Read bug report chunks
with open("chunks.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunks = text.split("========== Bug Report")
chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

# Create query
query = (
    bug_title
    + " "
    + bug_description
    + " "
    + stack_trace
    + " "
    + file_text
)

# Generate embedding
query_embedding = model.encode([query]).astype("float32")

# Search FAISS
k = 5

distances, indices = index.search(query_embedding, k)

for i, idx in enumerate(indices[0]):
    if idx < 0 or idx >= len(chunks):
        continue
    similarity = max(0, 100 - distances[0][i])

    with st.expander(f"🐞 Similar Bug {i+1}   ({similarity:.2f}% Match)"):

        st.write(chunks[idx][:1000])

        st.progress(min(int(similarity),100))
# ==========================================
# DEFECT PATTERN ANALYTICS
# ==========================================

st.header("📊 Defect Pattern Analytics")

try:
    patterns = get_defect_patterns()

    # -------------------------------
    # Severity
    # -------------------------------
    st.subheader("Severity Distribution")

    st.bar_chart(patterns["severity"])

    # -------------------------------
    # Priority
    # -------------------------------
    st.subheader("Priority Distribution")

    st.bar_chart(patterns["priority"])

    # -------------------------------
    # Affected Components
    # -------------------------------
    st.subheader("Frequently Affected Components")

    st.bar_chart(patterns["component"])

    # -------------------------------
    # Exception Types
    # -------------------------------
    st.subheader("Frequent Exception Types")

    st.bar_chart(patterns["exception"])

    # -------------------------------
    # Root Cause Themes
    # -------------------------------
    st.subheader("Recurring Root Cause Themes")

    st.bar_chart(patterns["root_cause"])

except Exception as e:
    st.error(f"Unable to load defect analytics: {e}")