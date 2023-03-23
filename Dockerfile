FROM python:3.8
MAINTAINER OCP TEAM 

# List packages here
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        file        \
        gcc         \
        libwww-perl && \
    apt-get autoremove -y && \
    apt-get clean

# Upgrade pip
RUN pip install --upgrade pip

WORKDIR /src

ADD requirements requirements/
RUN pip install -r requirements/requirements.txt

ADD . /src


RUN chown -R 1001 /src
USER 1001

ENTRYPOINT ["entrypoint"]