FROM ubuntu:latest

ENV TZ=America/Toronto
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install python3 python3-dev python3-pip chromium-browser firefox -y
RUN python3 -m pip install -r ./src/requirements.txt

CMD ["/bin/sh", "-c", "python3 ./src/test_all.py > ./results/test_results.txt 2>&1"]