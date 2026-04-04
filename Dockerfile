FROM python:3.12-slim-bookworm

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
COPY constraints.txt ./

RUN python -m pip install -c constraints.txt -r requirements.txt

COPY ./src/ /src
COPY ./series_settings /series_settings/
WORKDIR /src
CMD ["python", "-m", "main"]
