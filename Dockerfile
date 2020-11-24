# Get ubuntu base image
FROM ubuntu:18.04

RUN apt-get update && apt-get install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && apt-get install -y python3.6 python3.6-dev python3-pip


# Get twirp and uvicorn

RUN pip3 install twirp==0.0.2
RUN pip3 install uvicorn==0.12.2

# Model related libraries
RUN pip3 install numpy==1.18.5
RUN pip3 install scipy==1.3
RUN pip3 install scikit-learn==0.21.3
RUN pip3 install tokenizers==0.8.1rc2


# Add folders and environment variables
ADD /twirpy_python /twirpy_python

WORKDIR /twirpy_python

ARG lang_var="C.UTF-8"
ENV LC_ALL=$lang_var
ENV LANG=$lang_var

EXPOSE 3000

CMD ["uvicorn", "server:app","--host","0.0.0.0","--port","3000"]

# docker run -p 3000:3000 twirpy_exps

