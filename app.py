import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Smart Bug Analyzer",
    page_icon="🐞",
    layout="centered"
)

# Title
st.title("🐞 AI Smart Bug Analyzer & Fix Advisor")

st.markdown("### Submit a Bug Report")

# Input Fields
bug_title = st.text_input("Bug Title")

bug_description = st.text_area(
    "Bug Description",
    height=150
)

stack_trace = st.text_area(
    "Stack Trace / Error Log",
    height=150
)

uploaded_file = st.file_uploader(
    "Upload Bug Report / Log File",
    type=["txt", "log", "pdf"]
)

# Analyze Button
if st.button("Analyze Bug"):

    if bug_title == "" and bug_description == "":
        st.error("Please enter the Bug Title and Description.")
    else:
        st.success("Bug Submitted Successfully!")

        st.subheader("Submitted Bug Information")

        st.write("### Bug Title")
        st.write(bug_title)

        st.write("### Bug Description")
        st.write(bug_description)

        st.write("### Stack Trace")
        st.write(stack_trace)

        if uploaded_file is not None:
            st.write("### Uploaded File")
            st.write(uploaded_file.name)