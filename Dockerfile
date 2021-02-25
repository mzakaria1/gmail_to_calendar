FROM python:3.8.3

RUN apt-get update -y && apt-get -y install cron vim

WORKDIR /opt/application

RUN pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib && \
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# COPY crontab /etc/cron.d/crontab

COPY . /opt/application

RUN echo "* * * * * root /usr/local/bin/python3 /opt/application/app.py >> /var/log/cron.log 2>&1" >> /etc/cron.d/crontab

RUN chmod 0644 /etc/cron.d/crontab && touch /var/log/cron.log

RUN /usr/bin/crontab /etc/cron.d/crontab

CMD cron && tail -f /var/log/cron.log

# CMD [ "cron", "-f" ]
