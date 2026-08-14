import os
import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

load_dotenv()

app=FastAPI(
    title="Divyashree Voice Agent",
    description="Outbound AI Voice Agent for lead qualification",
    version="1.0.0"
)

VAPI_API_KEY = os.getenv("VAPI_API_KEY")
VAPI_ASSISTANT_ID = os.getenv("VAPI_ASSISTANT_ID")
VAPI_PHONE_NUMBER_ID = os.getenv("VAPI_PHONE_NUMBER_ID")

VAPI_CALL_URL="https://api.vapi.ai/call"


class Lead(BaseModel):
    phone_number: str
    name: str = "there"


@app.get("/")
async def root():
    return {
        "status": "online",
        "agent": "Divyashree Voice Agent",
        "version": "1.0.0"
    }

@app.post("/call")
async def make_call(lead: Lead):

    if not VAPI_API_KEY:
        raise HTTPException(
            status_code=500, 
            detail="VAPI_API_KEY is missing in .env."
            )
    if not VAPI_ASSISTANT_ID:
        raise HTTPException(
            status_code=500,
            detail="VAPI_ASSISTANT_ID is missing in .env"
        )

    if not VAPI_PHONE_NUMBER_ID:
        raise HTTPException(
            status_code=500,
            detail="VAPI_PHONE_NUMBER_ID is missing in .env"
        )

    payload = {
        "assistantId": VAPI_ASSISTANT_ID,

        "phoneNumberId": VAPI_PHONE_NUMBER_ID,

        "customer": {
            "number": lead.phone_number,
            "name": lead.name
        }
    }

    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }

    try:

        response = requests.post(
            VAPI_CALL_URL,
            json=payload,
            headers=headers,
            timeout=30
        )

    except requests.RequestException as error:

        raise HTTPException(
            status_code=500,
            detail=f"Failed to connect to Vapi: {str(error)}"
        )

    
    if response.status_code >= 400:
       print("VAPI STATUS:", response.status_code)
       print("VAPI RESPONSE:", response.text)

       raise HTTPException(
            status_code=response.status_code,
            detail=response.text
    )
    
    return {
        "success": True,
        "message": "Outbound call started",
        "vapi_response": response.json()
    }