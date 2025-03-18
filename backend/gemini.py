from google import genai
import os

def ask_gemini(question: str, context: str) -> str:
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Give me the short and crisp answer for the question with given context only, if the context do not have answer reply with not sufficient information. Context: {context}\n\nQuestion: {question}",
        )

        return (response.text)
    except Exception as e:
        raise Exception(f"Error asking Gemini: {str(e)}")

def summarise_gemini(context: str) -> str:
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"I will provide you the context, remove the redundant information/text from it, so that I can use the relevant context for questions and answers. Context: {context}\n",
        )

        return (response.text)
    except Exception as e:
        raise Exception(f"Error asking Gemini: {str(e)}")