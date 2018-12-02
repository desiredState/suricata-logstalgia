# suricata-logstalgia
# Streams Suricata EVE logs to Logstalgia Custom Log Format.
# See README.md for documentation.

FROM python:alpine

ENV APK_PACKAGES \
    alpine-sdk \
    libffi-dev \
    tzdata

ENV PIP_PACKAGES \
    termcolor \
    python-dateutil \
    tailer

RUN apk --no-cache add $APK_PACKAGES && \
    pip --no-cache-dir install $PIP_PACKAGES && \
    cp /usr/share/zoneinfo/Europe/London /etc/localtime && \
    echo "Europe/London" > /etc/timezone && \
    apk del tzdata && \
    mkdir -p /opt/project

WORKDIR /opt/project

COPY src .

RUN python -m compileall -b .; \
    find . -name "*.py" -type f -print -delete

ENTRYPOINT ["python","-u", "main.pyc"]
