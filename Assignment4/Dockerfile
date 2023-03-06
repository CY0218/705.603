FROM python:3.8
COPY . ./
ENV SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True
RUN pip3 install -r requirements.txt
CMD ["Amazon_Musical_Instrument_Review.py"]
ENTRYPOINT ["python"]
