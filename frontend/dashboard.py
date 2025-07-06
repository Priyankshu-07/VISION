import streamlit as st
import pymongo
import os
def show():
    st.title("📊 Dashboard – History of Summaries")
    try:
        MONGO_URL = os.getenv("MONGO_URL")
        client = pymongo.MongoClient(MONGO_URL)
        db = client["VISION"]
        collection = db["results"]
        entries = list(collection.find().sort("timestamp", -1).limit(10))
        if not entries:
            st.info("No history yet. Start summarizing something first.")
            return
        for entry in entries:
            with st.expander(f"📌 {entry.get('input_type')} | {entry.get('timestamp')}"):
                st.markdown(f"**Input:** `{entry.get('input_value', '')}`")

                if entry.get("summary"):
                    st.markdown("#### 📃 Summary")
                    st.success(entry["summary"])

                if entry.get("questions"):
                    st.markdown("#### ❓ Questions")
                    for i, q in enumerate(entry["questions"], 1):
                        st.write(f"**Q{i}.** {q}")
    except Exception as e:
        st.error(f"Failed to load data: {e}")
