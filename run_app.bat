@echo off
echo Starting Hybrid RAG...

:: 1. Start Docker in detached mode (background)
docker compose up -d

:: 2. Wait 5 seconds for Streamlit to boot
timeout /t 5

:: 3. Open the browser
start http://localhost:8501

:: 4. Show logs (Optional - so you can see "Thinking...")
docker compose logs -f