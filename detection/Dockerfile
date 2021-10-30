FROM nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04
MAINTAINER Ammar Ali

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Installing dependencies for linux installation of opencv
RUN apt-get update && \
        apt-get install -y -q \
        build-essential \
        cmake \
        git \
        wget \
        unzip \
        yasm \
        pkg-config \
        libswscale-dev \
        libtbb2 \
        libtbb-dev \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        libavformat-dev \
        libpq-dev \
	python3.6 \
	python3-pip

COPY requirements.txt ./
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
#RUN useradd myuser  && chown -R myuser /chart
#USER myuser
WORKDIR /srv/app
ENTRYPOINT ["python3", "run.py"]
CMD python run.py
