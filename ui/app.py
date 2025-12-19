import streamlit as st
import requests

st.title("SHL Assessment Recommendation System")

query = st.text_area("Enter Job Description or Query")

if st.button("Recommend"):
    res = requests.post(
        "http://localhost:8000/recommend",
        json={"query": query}
    ).json()

    for a in res["recommended_assessments"]:
        st.write(f"**{a['name']}**")
        st.write(a["url"])
        st.write("---")
