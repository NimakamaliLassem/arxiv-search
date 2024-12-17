# arXiv Semantic Search App

This repository provides a **semantic search application** for arXiv articles, allowing users to search and analyze a vast collection of scientific research efficiently. The application leverages **PGVector** (PostgreSQL vector extension) and **ChromaDB** for high-performance vector similarity search and benchmarking.

![image](https://github.com/user-attachments/assets/a4a4ef46-0ceb-4af2-ab8d-392bac67d4f2)

The app enables users to:
- Perform **single query searches** across the arXiv dataset.
- **Benchmark query latencies** using either manually entered queries or an uploaded query file.  
- Visualize performance results through **plots**.
- Compare query performance (latency) between **ChromaDB** and **PGVector**.


---

## Prerequisites

Before running the application, ensure the following dependencies and tools are set up:

1. **PostgreSQL** with the **pgvector** extension installed.
   - Follow [pgvector installation guide](https://github.com/pgvector/pgvector) to set up `pgvector`.
2. Python environment with all required libraries (details below).
3. Kaggle credentials for downloading the arXiv dataset.

---

## Features

### 1. **Single Query Search**
   - Input any query, and the app will search through the arXiv dataset using **ChromaDB** or **PGVector**.
   - Results include titles, abstracts, and the latency for the query.

  ![image](https://github.com/user-attachments/assets/9272eae3-47b0-480f-acc7-13a421f49b9c)

### 2. **Benchmarking Mode**
   - Run performance benchmarks to compare **ChromaDB** and **PGVector** latencies.
   - Two modes are supported:
     - **Manual Queries**: Enter multiple queries manually.
     - **Upload Query File**: Upload a `.txt` file containing multiple queries.
   - Visualize latency results through **box plots**, **distributions**, and **latency-over-time charts**.

  ![image](https://github.com/user-attachments/assets/50fc809b-cebd-45b6-b704-5e3f16e07401)

### 3. **Performance Visualization**
   - After running benchmarks, the app generates insightful visualizations:
     - **Latency Distribution**: Density plots showing latency for both ChromaDB and PGVector.
     ![image](https://github.com/user-attachments/assets/c811246c-7aa4-4268-bfac-a505eccce3db)

     - **Latency Comparison**: Box plots comparing query response times.
     ![image](https://github.com/user-attachments/assets/f9fce11a-e858-4dc2-bd03-2d193392743a)

     - **Latency Over Queries**: Line charts illustrating how latencies evolve across queries.
     ![image](https://github.com/user-attachments/assets/c54ffba7-874c-4129-93a0-1743301dcf17)

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

## Notes

- **pgvector setup is required** for the PostgreSQL part of the app.
- The notebook (`arxiv-app.ipynb`) must be executed **step by step** before running `app.py`.
- Both **ChromaDB** and **PGVector** databases will store the embeddings for the arXiv articles.

---

## License

This project is licensed under the MIT License.
