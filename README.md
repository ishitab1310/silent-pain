# Silent Pain — Product Opportunity Discovery Tool

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![NLP](https://img.shields.io/badge/NLP-SentenceTransformers-green)
![Machine Learning](https://img.shields.io/badge/MachineLearning-Clustering-orange)
![Reddit API](https://img.shields.io/badge/API-Reddit-orange)

Silent Pain is a product discovery tool that analyzes large volumes of online user complaints to identify unmet needs and potential product opportunities.

Instead of starting with solutions, product teams should begin by understanding real user pain points. Silent Pain collects complaints from online discussions and clusters them to reveal recurring problems that may represent gaps in existing products.

This project demonstrates product thinking by focusing on problem discovery, user research at scale, and data-driven opportunity identification.

---

## Problem Statement

Many products fail because they are built without a deep understanding of user problems.

Online platforms contain thousands of complaints and frustrations expressed by users every day. However, this information is scattered and difficult to analyze manually.

Silent Pain addresses this by automatically extracting and organizing these complaints so that product teams can quickly identify:

- recurring user frustrations
- underserved problem areas
- potential product opportunities

---

## Key Features

- Collects user complaints from Reddit discussions
- Cleans and processes text data
- Uses sentence embeddings to represent semantic meaning
- Groups similar complaints using clustering
- Displays pain clusters with example complaints
- Highlights areas where new product ideas may emerge

---

## Product Thinking Behind the Project

This tool is designed from a product management perspective rather than a purely engineering perspective.

The focus is on answering the following questions:

- What problems are users repeatedly complaining about?
- Which areas have the highest concentration of frustration?
- Where might a new product or feature solve these problems?

The goal is to simulate the early stages of product discovery used by product teams.

---

## Tech Stack

- Python
- Streamlit (interactive dashboard)
- PRAW (Reddit API)
- Sentence Transformers
- Scikit-learn
- Pandas / NumPy

---

## Project Structure

<pre>
silent_pain/
│
├── app.py             
├── scraper.py          
├── clustering.py       
├── insights.py         
├── requirements.txt    
             
</pre>

---

## Installation

Clone the repository.

<pre>
git clone https://github.com/yourusername/silent_pain.git
cd silent_pain
</pre>

Create a virtual environment.

<pre>
python -m venv venv
</pre>

Activate the virtual environment.

Windows:

<pre>
venv\Scripts\activate
</pre>

Mac / Linux:

<pre>
source venv/bin/activate
</pre>

Install dependencies.

<pre>
pip install -r requirements.txt
</pre>

---

## Reddit API Setup

This project requires Reddit API credentials.

Create an application here:

https://www.reddit.com/prefs/apps

Choose **script** as the application type.

After creating the app, copy the credentials into `scraper.py`.

Example configuration:

<pre>
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
USER_AGENT = "silent_pain_app"
</pre>

---

## Running the Application

Start the Streamlit server.

<pre>
python -m streamlit run app.py
</pre>

Open the browser at:

<pre>
http://localhost:8501
</pre>

Enter a domain such as:

<pre>
productivity apps
AI tools
note taking apps
</pre>

The system will collect complaints and display clusters of user pain points.

---

## Example Workflow

1. User enters a product domain
2. The system collects complaints from Reddit discussions
3. Text is cleaned and converted into embeddings
4. Similar complaints are grouped using clustering
5. Pain clusters are displayed with example user complaints

This allows quick discovery of areas where existing products may not be meeting user needs.

---

## Example Output

<pre>
Pain Cluster: Productivity Tool Fragmentation

Mentions: 120

Example complaints:
- I hate switching between Notion and Todoist
- Wish notes and tasks were connected
- Too many apps for productivity
</pre>

Potential product insight:

A unified productivity workspace that combines notes, tasks, and scheduling.

---

## Future Improvements

Possible extensions include:

- sentiment analysis of complaints
- trend detection over time
- integration with additional platforms such as product reviews
- automatic generation of product opportunity summaries
- visualization dashboards for product teams

---

## Why This Project Matters

This project demonstrates an approach to product discovery grounded in real user feedback.
- Many product fail because they are not able to identify the needs of users. 
- Instead of guessing product ideas, Silent Pain identifies opportunities by analyzing large volumes of user complaints. 
- This approach helps teams prioritize problems that are widely experienced by users.

