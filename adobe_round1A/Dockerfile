# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY extract_outline.py .

# Install required Python packages
RUN pip install --no-cache-dir pymupdf

# Entry point when container runs
CMD ["python", "extract_outline.py"]
