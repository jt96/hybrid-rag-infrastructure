#!/bin/bash

# 1. Check for a special Environment Variable
if [ "$RUN_INGEST" = "true" ]; then
    echo "RUN_INGEST is set to true. Starting ingestion..."
    python ingest.py
    if [ $? -ne 0 ]; then
        echo "Ingestion failed."
        exit 1
    fi
    echo "Ingestion complete."
fi

# 2. Always start the Chatbot afterwards
echo "Starting Streamlit UI..."
echo "--------------------------------------------------"
echo "APP RUNNING! Click here -> http://localhost:8501"
echo "--------------------------------------------------"
streamlit run app.py --server.port=8501 --server.address=0.0.0.0