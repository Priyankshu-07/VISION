import streamlit as st
import home
import main
import dashboard
st.set_page_config(page_title="AI Summarizer", layout="wide")
st.sidebar.title("📚 AI Summarizer")
page = st.sidebar.radio("Navigate", ["🏠 Home", "📝 Summarizer", "📊 Dashboard"])
if st.sidebar.button("🔄 Reset All"):
    st.session_state.clear()
    st.success("Session reset! All inputs and outputs cleared.")
    st.experimental_rerun()
if page == "🏠 Home":
    home.show()
elif page == "📝 Summarizer":
    main.show()
elif page == "📊 Dashboard":
    dashboard.show()
st.markdown("<hr><center>Keep UP the Hustle</center>", unsafe_allow_html=True)
