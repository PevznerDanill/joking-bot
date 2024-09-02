#!/bin/bash
# Load environment variables from .env file
export $(cat .env | xargs)

# Set environment variables on Heroku
heroku config:set BOT_TOKEN=$BOT_TOKEN
heroku config:set CHAT_ID=$CHAT_ID
heroku config:set JOKES_API=$JOKES_API
heroku config:set FREQUENCY=$FREQUENCY