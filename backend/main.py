from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scraper import scrape_url
from gemini import ask_gemini, summarise_gemini
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

app = FastAPI()

class URLInput(BaseModel):
    urls: list[str]

class QuestionInput(BaseModel):
    question: str
    context: str

@app.post("/ingest")
async def ingest_urls(data: URLInput):
    try:
        scraped_content = []
        for url in data.urls:
            content = scrape_url(url)
            scraped_content.append(content)
            relevant_content = summarise_gemini(" ".join(scraped_content))
        return {"content": " ".join(relevant_content)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask")
async def ask_question(data: QuestionInput):
    try:
        answer = ask_gemini(data.question, data.context)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3001)
