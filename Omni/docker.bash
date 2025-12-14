# Build the container
docker build -t slizzai-unified .

# Run the container
docker run -p 8000:8000 slizzai-unified