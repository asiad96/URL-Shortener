# URL Shortener

A simple URL shortening service that turns long URLs into short, easy-to-share links. Built with FastAPI and PostgreSQL.

## How It Works

1. Enter a long URL
2. Get back a short link
3. Share the short link with anyone
4. When they open the short link, they'll be redirected to your original URL

## Quick Start

1. Install Python packages:
```bash
pip install -r requirements.txt
```

2. Set up your database:
- Create a free database at [Neon](https://neon.tech)
- Copy your database URL
- Create a `.env` file and add your database URL:
```
DATABASE_URL=your_database_url_here
```

3. Run the app:
```bash
uvicorn main:app --reload
```

4. Open http://localhost:8000 in your browser

## API Usage

Create a short URL:
```bash
curl -X POST "http://localhost:8000/shorten" \
     -H "Content-Type: application/json" \
     -d '{"original_url": "https://example.com/very/long/url"}'
```

## Deploy to Heroku

1. Create a Heroku account
2. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
3. Deploy:
```
heroku create your-app-name
heroku config:set DATABASE_URL=your_database_url
git push heroku main
```

## Built With

- FastAPI - Web framework
- PostgreSQL - Database (hosted on Neon)
- SQLAlchemy - Database ORM
- Heroku - Hosting
