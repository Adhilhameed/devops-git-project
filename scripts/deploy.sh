#!/bin/bash
# Build and run the app locally with Docker Compose
set -euo pipefail
echo "Building and starting containers..."
docker compose up -d --build
sleep 3
curl -fs http://localhost:5000/health && echo " <- healthy"
