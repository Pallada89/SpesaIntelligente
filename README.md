# RisparmioSmart Backend (Heroku Ready)

FastAPI + Tesseract (ITA) su Heroku, con endpoint:
- `GET /health`
- `GET /offers`
- `POST /ocr`

## Deploy con bottone

Aggiungi nel README del tuo repo:
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=<URL_REPO>)

## Deploy manuale (CLI)
heroku create risparmiosmart-backend
heroku buildpacks:add heroku-community/apt
heroku buildpacks:add heroku/python
git push heroku main

## Frontend Vercel
Configura `REACT_APP_API_BASE` = URL della tua app Heroku.
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Pallada89/SpesaIntelligente)


