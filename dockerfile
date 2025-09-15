# 1. Base image: Python 3.12,
FROM python:3.12-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy over all the goodies we need
COPY requirements.txt .
COPY . .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5.  Expose port 8000 so the world can meet our FastAPI app
EXPOSE 8000

# 6. Start the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
