# FROM ubuntu

# COPY ./app /app

# WORKDIR /app

# RUN pip install flask_restful sklearn minio

# #CMD ["python3", "main.py"]

# ENTRYPOINT ["/bin/bash"]



FROM ubuntu

ENV DEBIAN_FRONTEND noninteractive

COPY ./app/requirements.txt /etc/requirements.txt
#WORKDIR /app

RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y \
    python3-setuptools \
    python3-pip \
    language-pack-en


# RUN pip3 install flask flask_restful minio sklearn
RUN pip3 install -r /etc/requirements.txt


#ENTRYPOINT ["/bin/bash"]