FROM owasp/zap2docker-stable

WORKDIR /zap
COPY . /usr/src/app/

CMD ["/bin/sh", "-c", "python -u /usr/src/app/run.py"]
