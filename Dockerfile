FROM owasp/zap2docker-stable

COPY . /usr/src/app/

CMD ["/bin/sh", "-c", "python /usr/src/app/run.py"]
