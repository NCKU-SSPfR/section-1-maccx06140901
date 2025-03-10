# TODO: Install the frontend dependency package into the app folder inside the container.
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the frontend port
EXPOSE 8088

# Run the FastAPI frontend application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]
