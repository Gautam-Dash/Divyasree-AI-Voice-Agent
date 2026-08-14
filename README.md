Divyasree AI Voice Agent

An outbound AI voice agent built for the Divyasree "Whispers of the Wind" (WOW) – Private Valley lead-qualification assignment.

The agent is designed to conduct a natural 2–3 minute conversation with a potential real-estate lead, qualify their requirements, and request a follow-up call from a Property Expert.

Features

Natural conversational voice interaction using Vapi

Permission-first introduction

Lead qualification across four checkpoints:

Intent: Self-use vs Investment

Geography: Nandi Hills / Devanahalli corridor

Budget: ₹92.4 lakh+ starting price

Timeline: Comfort with December 2029 possession / ongoing project

Short premium project pitch

Property Expert follow-up CTA

Avoids repeating questions when information is already provided

Natural acknowledgements such as "Understood", "Perfect", and "Absolutely"

Phonetic pronunciation guidance for:

Divyasree → Div-yaa-shree

Nandi → Nun-dhee

Lakh → Lakh

Crore → Crore

FastAPI endpoint for initiating outbound calls through Vapi

Project Context

Project: Whispers of the Wind (WOW) by Divyasree Developers
Product: Premium "Private Valley" villa plots
Location: Nandi Valley, near Nandi Hills, North Bengaluru
Plot Sizes: 1200–3199 sq.ft.
Pricing: Approximately ₹92.4 lakh – ₹2.46 crore, inclusive of taxes
USP: ~74% open space, 20,000 sq.ft. clubhouse, eco-parks, scenic hill views
Target Audience: HNIs, CXOs, NRIs, luxury weekend-home buyers, and high-value investors
Possession Timeline: December 2029

Architecture

Potential Lead
      |
      v
    Vapi
      |
      v
 AI Voice Assistant
      |
      +--> Intent
      |
      +--> Geography
      |
      +--> Budget
      |
      +--> Timeline
      |
      v
 Project Pitch
      |
      v
 Property Expert Follow-up

The Python backend provides a simple API layer for initiating outbound calls:

Client / Swagger
       |
       v
FastAPI  --->  Vapi API  --->  Lead Phone

Tech Stack

Python 3.x

FastAPI

Uvicorn

Vapi

Python Requests

python-dotenv

Project Structure

divyasree-voice-agent/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

Setup

1. Clone the repository

git clone <your-github-repository-url>
cd "Divyasree Voice Agent"

2. Create a virtual environment

Windows PowerShell:

python -m venv venv
venv\Scripts\activate

3. Install dependencies

python -m pip install --upgrade pip
pip install -r requirements.txt

4. Configure environment variables

Create a .env file in the project root:

VAPI_API_KEY=your_public_vapi_api_key
VAPI_ASSISTANT_ID=your_vapi_assistant_id
VAPI_PHONE_NUMBER_ID=your_vapi_phone_number_id

Never commit .env or your private API key to GitHub.

Vapi Assistant Setup

Create a Vapi account.

Create a new Assistant.

Configure the assistant with the Divyasree qualification system prompt.

Add the required voice and model configuration.

Test the assistant using Vapi's browser voice testing.

For actual outbound calls, configure a phone number supported for the destination country.

For Indian +91 outbound calls, a suitable international/custom phone setup may be required depending on the Vapi account and number configuration.

Run the Backend

Start FastAPI with:

python -m uvicorn main:app --reload

The API will be available at:

http://127.0.0.1:8000

Swagger API Documentation

Open:

http://127.0.0.1:8000/docs

You can test the API directly from Swagger UI.

Health Check

GET /

Example response:

{
  "status": "online",
  "agent": "Divyasree AI Voice Agent",
  "version": "1.0"
}

Start an Outbound Call

POST /call

Request body:

{
  "phone_number": "+91XXXXXXXXXX",
  "name": "Gautam"
}

The backend sends the configured assistant, phone number, and customer details to Vapi.

Conversation Flow

The agent follows this sequence:

Introduction

Introduces itself as a Divyasree consultant.

Mentions Whispers of the Wind / Private Valley.

Mentions Nandi Hills / North Bengaluru.

Asks for permission to speak.

Intent

Determines self-use, investment, or both.

Geography

Checks comfort with the Nandi Hills / Devanahalli corridor.

Budget

Checks fit with the approximately ₹92.4 lakh+ starting price.

Timeline

Checks comfort with the December 2029 possession timeline.

Pitch

Gives a concise premium lifestyle description focused on nature, space, clubhouse, eco-parks, scenic views, and community.

CTA

Requests a follow-up call with a Property Expert.

Conversation Intelligence

The agent is instructed not to repeat questions when the lead provides information early.

For example, if a lead says:

"I'm looking for an investment around Devanahalli and my budget is about ₹1.5 crore."

The agent should remember both the intent and budget, then continue with the next missing qualification point instead of asking the same questions again.

Example Qualification Result

A successful conversation may establish:

{
  "intent": "investment",
  "geography": "comfortable",
  "budget": "qualified",
  "timeline": "comfortable",
  "interest": "high",
  "follow_up": true
}

Testing Checklist

Before submitting the project, test these scenarios:

Lead gives permission to speak

Lead refuses to speak

Self-use lead

Investment lead

Lead already provides multiple qualification details

Lead is unsure about the location

Lead has a suitable budget

Lead cannot meet the starting budget

Lead needs immediate possession

Lead asks for project details

Lead asks an unknown question

Lead says they are not interested

Lead agrees to a Property Expert follow-up

Agent pronounces "Divyasree" correctly as "Div-yaa-shree"

Conversation stays around 2–3 minutes

Security

Do not commit secrets.

The .gitignore should include:

venv/
.env
__pycache__/
*.pyc

Never expose:

Vapi private API keys

Phone credentials

Other service secrets

Future Improvements

Possible future improvements, if required:

Structured call outcome extraction

Lead scoring

CRM integration

Call transcript storage

Follow-up scheduling

Web dashboard

Analytics for qualified vs unqualified leads

Automated lead summaries

These are intentionally outside the scope of the basic assignment implementation.

Author

Gautam Dash

Built as a practical AI Voice Agent project demonstrating:

Agentic AI

Voice AI

LLM-based conversation

Lead qualification

FastAPI

API integration
