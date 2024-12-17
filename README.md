# arXiv Semantic Search App

This repository provides a semantic search application for arXiv articles, leveraging **PGVector** and **ChromaDB** for efficient vector search. The app allows users to compare query performance across the two databases and includes benchmarking capabilities.

---

## Prerequisites

Before running the application, ensure the following dependencies and tools are set up:

1. **PostgreSQL** with the **pgvector** extension installed.
   - Follow [pgvector installation guide](https://github.com/pgvector/pgvector) to set up `pgvector`.
2. Python environment with all required libraries (details below).
3. Kaggle credentials for downloading the arXiv dataset.

---

## Setup Instructions

### 1. Install Dependencies

Clone the repository and install the required Python packages:

```bash
pip install tensorflow tensorflow-hub chromadb psycopg psycopg2-binary pgvector kagglehub streamlit numpy pandas matplotlib seaborn
pip install --upgrade ipywidgets
```

---

### 2. Run Project Setup Notebook

Follow the step-by-step instructions in the `arxiv-app.ipynb` notebook:

1. **Setup PostgreSQL and PGVector**: 
   - Ensure you have PostgreSQL running.
   - Configure connection settings in the notebook:
     ```python
     PG_USER = "postgres"
     PG_PASSWORD = "password"  # Replace with your password
     PG_HOST = "localhost"
     PG_PORT = 5434  # Replace with your PostgreSQL port
     PG_DBNAME = "arxivdb"
     ```
2. **Download and Prepare the Dataset**:
   - Use the KaggleHub library to download the latest arXiv dataset.
   - Process and embed the dataset using **TensorFlow Hub's Universal Sentence Encoder**.

3. **Populate Databases**:
   - Insert processed embeddings into **ChromaDB** and **PGVector**.

4. **Indexing**:
   - Create vector similarity indexes (HNSW) in PostgreSQL for efficient search.

Run each cell sequentially in the notebook until the data preparation is complete.

---

### 3. Run the Streamlit App

Once the notebook setup is complete:

1. Go to the directory where `app.py` is located.
2. Run the Streamlit app with the following command:

```bash
streamlit run app.py
```

The app will launch in your default web browser.

---

## Optional: Generate Query File

The repository includes `query_generation.py` for generating a `queries.txt` file with 1000 semantic search queries. This file can be used for benchmarking.

- To generate or modify the query file:
  ```bash
  python query_generation.py
  ```
- The default `queries.txt` file is already provided in the repository.

---

## Using the App

1. **Single Query Search**:
   - Enter a query in the text box.
   - Choose between **ChromaDB** and **PGVector**.
   - The app will display the top results along with query performance metrics.

2. **Benchmarking**:
   - Select "Benchmarking" in the app.
   - Choose to run queries manually or upload a `queries.txt` file.
   - The app will measure and compare latencies for ChromaDB and PGVector.

3. **Performance Metrics**:
   - View latency distributions, average query times, and detailed visualizations.

---

## Example

1. **Setup PostgreSQL with pgvector**:
   ```bash
   CREATE EXTENSION IF NOT EXISTS vector;
   ```
2. **Run the notebook**:
   - Prepare the arXiv data and store embeddings.

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

4. **Generate queries**:
   ```bash
   python query_generation.py
   ```

---

## Notes

- **pgvector setup is required** for the PostgreSQL part of the app.
- The notebook (`arxiv-app.ipynb`) must be executed **step by step** before running `app.py`.
- Both **ChromaDB** and **PGVector** databases will store the embeddings for the arXiv articles.

---

## License

This project is licensed under the MIT License.
