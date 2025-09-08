FROM python:3.11-slim
WORKDIR /work
COPY . /work
RUN pip install --no-cache-dir .
ENTRYPOINT ["dir2md"]
CMD ["."]