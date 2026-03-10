FROM docker:20.10.7 

RUN apk add --no-cache docker-compose
WORKDIR /app

COPY . .

CMD ["docker-compose", "up"]
