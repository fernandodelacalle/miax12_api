FROM python:3.11-alpine

# set the working directory in the container
WORKDIR /code
# copy the dependencies file to the working directory
COPY ../src/requirements.txt .
# install dependencies
RUN pip install -r requirements.txt

# Expose the API Port
EXPOSE 8080

# Run the server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]