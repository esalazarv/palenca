FROM python:3.9-slim as base
WORKDIR /var/www/html
ADD ./requirements.txt /var/www/html
RUN pip3 install -r requirements.txt
ADD . /var/www/html

# For development stage
FROM python:3.9-slim as development
COPY --from=base /root/.cache /root/.cache
COPY --from=base /var/www/html/requirements.txt /var/www/html/
WORKDIR /var/www/html
RUN pip3 install -r requirements.txt && rm -rf /root/.cache
EXPOSE 5000
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]

# For production stage
FROM python:3.9-alpine as production
COPY --from=base /root/.cache /root/.cache
COPY --from=base /var/www/html/requirements.txt /var/www/html/
RUN pip3 install -r /var/www/html/requirements.txt && rm -rf /root/.cache
WORKDIR /var/www/html
EXPOSE 5000
CMD ["gunicorn", "--config", "./gunicorn_config.py", "server:app"]
