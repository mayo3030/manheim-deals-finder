# Manheim Deals Finder

A full-stack webapp to find the best car deals from Manheim auctions and other sources.

## Project Structure

```
manheim-deals-finder/
âââ app.jsx                    # React frontend (standalone with sample data)
âââ ManheimDealsFinder.jsx     # Alternative React component
âââ index.html                 # HTML shell with dark theme CSS
âââ backend/
â   âââ main.py               # FastAPI server with all API endpoints
â   âââ config.py             # Configuration (DB, ports, intervals)
â   âââ models.py             # SQLAlchemy models + Pydantic schemas
â   âââ requirements.txt      # Python dependencies
â   âââ .env.example          # Environment variables template
â   âââ scrapers/
â       âââ __init__.py
â       âââ base_scraper.py   # Abstract base scraper class
â       âââ manheim_scraper.py # Manheim.com scraper (requires login)
â       âââ copart_scraper.py  # Copart auction scraper
â       âââ carscom_scraper.py # Cars.com scraper
```

## Quick Start

### Frontend Only (Preview with Sample Data)

Open `app.jsx` in any React environment or use the standalone `index.html`.

### Full Stack Setup

1. Install Python dependencies:
```bash
cd backend
pip install -r requirements.txt
```

2. Copy and configure environment:
```bash
cp .env.example .env
# Edit .env with your Manheim credentials
```

3. Start the backend:
```bash
python main.py
```

The API runs at `http://localhost:8000` with auto-docs at `/docs`.

## Features

- Search & filter by make, model, year, price, mileage, fuel type, transmission
- Deal Score algorithm (compares price vs MMR value + condition + mileage)
- Side-by-side vehicle comparison (up to 3 cars)
- Price distribution & top makes charts
- Dark/Light mode toggle
- DealShield & Buy Now filters
- Pagination with smart page navigation

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/cars` | Search cars with filters |
| GET | `/api/cars/{id}` | Get car details |
| GET | `/api/dashboard` | Dashboard statistics |
| GET | `/api/filters` | Available filter options |
| POST | `/api/scrape/{source}` | Trigger manual scrape |
| POST | `/api/alerts` | Create price alert |

## Tech Stack

- **Backend**: Python, FastAPI, SQLAlchemy, APScheduler
- **Frontend**: React, Recharts, Lucide Icons
- **Database**: SQLite (default) / PostgreSQL
- **Scrapers**: Playwright/aiohttp-based
