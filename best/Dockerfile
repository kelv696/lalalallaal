FROM rasa/rasa:3.6.2-full

COPY . /app

WORKDIR /app

USER root

RUN if [ -z "$(ls -A)" ]; then \
      echo "No files found in the project directory. Running rasa init..."; \
      rasa init; \
    else \
      echo "Files found in the project directory. Skipping rasa init."; \
    fi

EXPOSE 5005

CMD ["run", "--enable-api", "--cors", "*"]

