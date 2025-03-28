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
            content = scrape_url(url)  # Scrape content from each URL
            scraped_content.append(content)  # Add scraped content to the list

        # Combine all scraped content into a single string
        combined_content = " ".join(scraped_content)

        # Summarize and clean the combined content using Gemini
        # relevant_content = summarise_gemini(combined_content)

        return {"content": combined_content}  # Return the cleaned content
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
