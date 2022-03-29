# FROM --platform=linux/amd64 x11docker/mate
# EXPOSE 8000:8000
# RUN apt-get update
# RUN apt-get install -y firefox-esr

# *** OLD *** #

ARG CONDA_VER=latest
ARG OS_TYPE=x86_64
ARG PY_VER=3.8.11
ARG TF_VER=2.5.0

FROM dorowu/ubuntu-desktop-lxde-vnc:focal
VOLUME /dev/shm:/dev/shm
EXPOSE 8080:8080

# System packages 
RUN apt-get update && apt-get install -yq curl wget jq vim
# tz_data
RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone
RUN apt-get install -y tzdata

# Use the above args during building https://docs.docker.com/engine/reference/builder/#understand-how-arg-and-from-interact
ARG CONDA_VER
ARG OS_TYPE

# Install miniconda to /miniconda
RUN curl -LO "http://repo.continuum.io/miniconda/Miniconda3-${CONDA_VER}-Linux-${OS_TYPE}.sh"
RUN bash Miniconda3-${CONDA_VER}-Linux-${OS_TYPE}.sh -p /miniconda -b
RUN rm Miniconda3-${CONDA_VER}-Linux-${OS_TYPE}.sh
ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda

RUN mkdir -p /code
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt

# chrome
RUN curl -LO https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb 
RUN rm google-chrome-stable_current_amd64.deb 

