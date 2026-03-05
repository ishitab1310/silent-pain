import streamlit as st

from scraper import fetch_complaints
from clustering import clean_text, embed_text, cluster_texts
from insights import group_clusters, summarize_cluster, opportunity_score

st.title("Silent Pain")
st.subheader("Discover Unsolved User Problems")

query = st.text_input("Enter product domain (example: productivity apps)")

if st.button("Analyze Pain Points"):

    with st.spinner("Collecting complaints from Reddit..."):
        posts = fetch_complaints(query)

    if len(posts) == 0:
        st.write("No complaints found.")
        st.stop()

    cleaned = [clean_text(p) for p in posts if len(p) > 20]

    with st.spinner("Analyzing complaints..."):
        embeddings = embed_text(cleaned)

        labels = cluster_texts(embeddings)

        clusters = group_clusters(cleaned, labels)

    st.success("Pain points discovered!")

    for cluster_id, texts in clusters.items():

        st.markdown("---")

        score = opportunity_score(texts)

        st.subheader(f"Pain Cluster {cluster_id}")

        st.write(f"Mentions: {score}")

        examples = summarize_cluster(texts)

        st.write("Example complaints:")

        for e in examples:
            st.write("-", e)