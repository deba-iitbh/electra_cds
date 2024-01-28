FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=app.py

# Create the database
CMD ["python3", "create_db.py"]
# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
