FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /k_telekom
WORKDIR /k_telekom
COPY requirements.txt /k_telekom/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /k_telekom/