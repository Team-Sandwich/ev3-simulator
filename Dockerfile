FROM debian:stretch
MAINTAINER Marc Rooding <admin@webresource.nl>

RUN apt-get update && apt-get -y install build-essential libreadline-dev libffi-dev pkg-config python-setuptools python-dev git dh-autoreconf python3

WORKDIR /

RUN git clone https://github.com/micropython/micropython.git

WORKDIR /micropython/mpy-cross

RUN make

WORKDIR /micropython/ports/unix

RUN make submodules

RUN make deplibs

RUN make

WORKDIR / 

RUN git clone https://github.com/micropython/micropython-lib.git

WORKDIR /micropython-lib

RUN make install

WORKDIR /micropython/ports/unix

ENTRYPOINT ["./micropython"]