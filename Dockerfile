FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV APP_DIR=/app

RUN apt-get update && apt-get install -y --no-install-recommends \
    fonts-dejavu-core \
 && rm -rf /var/lib/apt/lists/*

WORKDIR $APP_DIR

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY app/ $APP_DIR/

RUN chmod -R 775 $APP_DIR

USER 1000:1000   # fallback

EXPOSE 8503

CMD ["streamlit", "run", "app.py", "--server.port=8503", "--server.address=0.0.0.0"]
