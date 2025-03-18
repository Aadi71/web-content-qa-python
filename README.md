# **Web Content Q&A Tool (Python Edition)**

A web-based tool that allows users to input one or more URLs, ingest their content, and ask questions based on the information from those pages. The tool uses **Gemini** for question answering and has a user-friendly interface built with **Streamlit** (frontend) and **FastAPI** (backend).

---

## **Demo Video**

Watch the demo on YouTube to see the Web Content Q&A Tool in action:

<a href="https://youtu.be/your-demo-video-id" target="_blank">
  <img src="https://img.youtube.com/vi/your-demo-video-id/0.jpg" alt="Web Content Q&A Tool Demo">
</a>

---

## **Features**

- **URL Ingestion**: Input one or more URLs to scrape and ingest their content.
- **Question Answering**: Ask questions based on the ingested content.
- **Gemini Integration**: Uses **Gemini** for accurate and context-aware question answering.
- **Minimal UI**: Clean and intuitive user interface for seamless interaction.

---

## **Tech Stack**

### **Frontend**
- **Framework**: Streamlit (Python)
- **Styling**: Streamlit components
- **Hosting**: Streamlit Cloud

### **Backend**
- **Framework**: FastAPI (Python)
- **Web Scraping**: `requests` + `BeautifulSoup`
- **Question Answering**: Gemini API
- **Hosting**: Render

---

## **Hosted Links**

- **Frontend**: [https://web-content-app-python-aadi71.streamlit.app/](https://web-content-app-python-aadi71.streamlit.app/)
- **Backend**: [https://web-content-qa-python.onrender.com](https://web-content-qa-python.onrender.com)

---

## **How to Run Locally**

Follow these steps to set up and run the project on your local machine.

### **Prerequisites**

- **Python**: Ensure you have Python installed (v3.8 or higher).
- **pip**: Python package manager.
- **Gemini API Key**: Get your API key from [Google AI Studio](https://makersuite.google.com/).

---

### **Step 1: Clone the Repository**

Clone the repository to your local machine:

```bash
git clone https://github.com/Aadi71/web-content-qa-tool-python.git
cd web-content-qa-tool-python
```

---

### **Step 2: Set Up the Backend**

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the `backend` directory and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your-gemini-api-key
   ```

4. Start the backend server:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

   The backend will run on `http://localhost:8000`.

---

### **Step 3: Set Up the Frontend**

1. Navigate to the `frontend` directory:
   ```bash
   cd ../frontend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the `frontend` directory and add the backend URL:
   ```env
   BACKEND_URL=http://localhost:8000
   ```

4. Start the frontend development server:
   ```bash
   streamlit run app.py
   ```

   The frontend will run on `http://localhost:8501`.

---

### **Step 4: Access the Application**

Open your browser and navigate to `http://localhost:8501` to use the Web Content Q&A Tool.

---

## **Project Structure**

```
web-content-qa-tool-python/
├── backend/                  # FastAPI backend
│   ├── main.py               # FastAPI application
│   ├── scraper.py            # Web scraping logic
│   ├── gemini.py             # Gemini integration
│   ├── requirements.txt      # Backend dependencies
│   └── .env                  # Environment variables
├── frontend/                 # Streamlit frontend
│   ├── app.py                # Streamlit application
│   ├── requirements.txt      # Frontend dependencies
│   └── .env                  # Environment variables
├── README.md                 # Project documentation
└── .gitignore                # Git ignore file
```

---

## **Environment Variables**

### **Backend**
- `GEMINI_API_KEY`: Your Gemini API key.

### **Frontend**
- `BACKEND_URL`: The URL of the backend server (e.g., `http://localhost:8000`).

---

## **How It Works**

1. **URL Ingestion**:
   - The user inputs one or more URLs.
   - The backend scrapes the content of the URLs using `requests` and `BeautifulSoup`.

2. **Question Answering**:
   - The user asks a question based on the ingested content.
   - The backend sends the question and context to the **Gemini API**.
   - Gemini generates an answer based on the provided context.

3. **Response Display**:
   - The frontend displays the answer to the user.

---

## **Dependencies**

### **Backend**
- `fastapi`: Backend framework.
- `uvicorn`: ASGI server to run FastAPI.
- `requests`: HTTP client for web scraping.
- `beautifulsoup4`: HTML parsing library.
- `google-generativeai`: Gemini API client.
- `python-dotenv`: Environment variable management.

### **Frontend**
- `streamlit`: Frontend framework.
- `requests`: HTTP client for API calls.

---
