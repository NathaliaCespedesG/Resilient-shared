FROM python:3.10.14 as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN mkdir -p /usr/share/fonts/truetype/msttcorefonts
COPY ./docker/database_backend/fonts/* /usr/share/fonts/truetype/msttcorefonts

COPY ./resilient_backend/api /app/api
COPY ./resilient_backend/reports /app/reports
COPY ./resilient_backend/utils /app/utils
COPY ./resilient_backend/config /app/config
COPY ./resilient_backend/manage.py /app/manage.py
COPY ./requirements.txt /app/requirements.txt
COPY ./python_withings_api /app/python_withings_api

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port on which the server will run
EXPOSE 8000
EXPOSE 5432

COPY ./docker/database_backend/entrypoint.sh /app

RUN ls && chmod +x ./entrypoint.sh

# Run entrypoint script
CMD ["/bin/bash", "./entrypoint.sh"]