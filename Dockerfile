FROM debian:bookworm-slim

WORKDIR /flask_app

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONPATH=/flask_app
RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "web_app/app.py", "--host=0.0.0.0", "port=5000"]