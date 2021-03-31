FROM owasp/zap2docker-stable

COPY . /usr/src/app/

CMD ["/bin/sh", "/usr/src/app/run.sh"]
