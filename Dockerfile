FROM postgres:alpine

COPY docker-compose.yml /docker-compose.yml

ENV POSTGRES_USER ${POSTGRES_USER}
ENV POSTGRES_PASSWORD ${POSTGRES_PASSWORD}

EXPOSE 5432


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
