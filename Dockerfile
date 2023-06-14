from python:3.10
EXPOSE 5000
WORKDIR /app
COPY requirment.txt .
RUN pip install -r requirment.txt
COPY . .
CMD ["flask" , "run" , "--host" , "0.0.0"]
