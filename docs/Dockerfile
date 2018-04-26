FROM ubuntu:bionic

MAINTAINER Luis Melo <lhsm@cin.ufpe.br>

VOLUME /jsfuzz

RUN apt-get update
RUN apt-get install -y tox git build-essential python3.6

ADD dep.deb /

RUN dpkg -i /dep.deb && apt-get install -f -y

WORKDIR jsfuzz

ENTRYPOINT tox