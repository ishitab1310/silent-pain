from collections import Counter

def group_clusters(texts, labels):
    clusters = {}

    for text, label in zip(texts, labels):
        if label not in clusters:
            clusters[label] = []

        clusters[label].append(text)

    return clusters


def summarize_cluster(cluster_texts):
    return cluster_texts[:5]


def opportunity_score(cluster):
    return len(cluster)