import streamlit as st
import requests
def show():
    st.title("📝 Generate Summary & Questions")
    if "summary" not in st.session_state:
        st.session_state["summary"] = None
    if "questions" not in st.session_state:
        st.session_state["questions"] = None
    if "input_data" not in st.session_state:
        st.session_state["input_data"] = ""
    input_type = st.radio("Select Input Type", ["YouTube URL", "PDF Upload", "Manual Text"])
    generate_summary = st.checkbox("Generate Summary", value=True)
    generate_questions = st.checkbox("Generate Questions", value=True)
    uploaded_file = None
    if input_type == "YouTube URL":
        st.session_state["input_data"] = st.text_input("Paste YouTube URL", value=st.session_state["input_data"])
    elif input_type == "Manual Text":
        st.session_state["input_data"] = st.text_area("Enter text here", height=200, value=st.session_state["input_data"])
    elif input_type == "PDF Upload":
        uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if st.button("🚀 Generate"):
        if not (generate_summary or generate_questions):
            st.warning("Please select at least one option (summary or questions).")
            return
        st.session_state["summary"] = None
        st.session_state["questions"] = None
        with st.spinner("⏳ Processing..."):
            try:
                if input_type == "Manual Text":
                    response = requests.post(
                        "http://localhost:8000/summarize-text/",
                        json={
                            "text": st.session_state["input_data"],
                            "generate_summary": generate_summary,
                            "generate_questions": generate_questions
                        }
                    )
                elif input_type == "YouTube URL":
                    response = requests.post(
                        "http://localhost:8000/summarize-youtube/",
                        data={
                            "url": st.session_state["input_data"],
                            "include": ",".join([
                                "summary" if generate_summary else "",
                                "questions" if generate_questions else ""
                            ])
                        }
                    )
                elif input_type == "PDF Upload":
                    if uploaded_file is None:
                        st.warning("Upload a PDF before clicking Generate.")
                        return
                    response = requests.post(
                        "http://localhost:8000/summarize-pdf/",
                        data={
                            "include": ",".join([
                                "summary" if generate_summary else "",
                                "questions" if generate_questions else ""
                            ])
                        },
                        files={"file": uploaded_file}
                    )
                if response.status_code == 200:
                    result = response.json()
                    st.session_state["summary"] = result.get("summary")
                    st.session_state["questions"] = result.get("questions")
                else:
                    st.error(f"❌ Backend Error: {response.status_code}")
                    return
            except Exception as e:
                st.error(f"⚠️ Request failed: {e}")
                return
    if st.session_state.get("summary"):
        st.subheader("📃 Summary")
        st.success(st.session_state["summary"])
    elif st.session_state.get("summary") == "":
        st.info("No summary generated.")
    if st.session_state.get("questions"):
        st.subheader("❓ Questions")
        for i, q in enumerate(st.session_state["questions"], 1):
            st.markdown(f"**Q{i}.** {q}")
    elif st.session_state.get("questions") == []:
        st.info("No questions generated.")
    if st.session_state.get("summary") or st.session_state.get("questions"):
        if st.button("🔄 Clear This Page"):
            st.session_state["summary"] = None
            st.session_state["questions"] = None
            st.session_state["input_data"] = ""
            st.experimental_rerun()
