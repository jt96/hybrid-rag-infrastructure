#!/bin/bash

# Add /app/src to the python path so modules can find each other
export PYTHONPATH="${PYTHONPATH}:/app/src"

# Check for a special Environment Variable
if [ "$RUN_INGEST" = "true" ]; then
    echo "RUN_INGEST is set to true. Starting ingestion..."
    python src/ingest.py
    if [ $? -ne 0 ]; then
        echo "Ingestion failed."
        exit 1
    fi
    echo "Ingestion complete."
fi

# Launch the Streamlit application with clickable link
echo "Starting Streamlit UI..."
echo "--------------------------------------------------"
echo "Server Ready: http://localhost:8501"
echo "--------------------------------------------------"

streamlit run src/app.py --server.port=8501 --server.address=0.0.0.0