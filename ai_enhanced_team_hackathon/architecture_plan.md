# Architecture Plan

## Overview
A web application where users submit code, an AI model analyzes it, and the result is shown with an explanation and a fixed version.

## Components
- **Frontend:** Web interface with a code input box, language selector and result view.
- **Backend API:** REST API that receives submissions, calls the AI service and stores results.
- **AI Service:** External LLM API that returns the bug explanation and fixed code.
- **Database:** Stores users, submissions, reviews and votes.

## Data Flow
1. The user pastes code in the frontend and selects a language.
2. The frontend sends the code to the backend API.
3. The backend builds a prompt and sends it to the AI service.
4. The AI service returns an explanation and a fixed version.
5. The backend saves the result in the database.
6. The frontend displays the result to the user.

## API Endpoints
- POST /api/submissions - submit code for review
- GET /api/reviews/{id} - get a review
- GET /api/reviews - list the user's past reviews
- POST /api/reviews/{id}/vote - vote on a review

## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- Database: SQLite
- AI: LLM API

## Risks
- AI may give incorrect fixes, so we show a confidence level and ask for user votes.
- API cost and rate limits, so we limit requests per user.
