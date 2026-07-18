@echo off
title RAG Search API
echo Запускаем FastAPI сервер...
uvicorn server:app --host 127.0.0.1 --port 8000 --reload
pause