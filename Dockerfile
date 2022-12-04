 
FROM python:3.9

WORKDIR /app
 
#  Copy the pipfile and pipfile.lock for resolving dependencies
RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

# Install the dependencies
RUN pipenv install --system

# RUN echo uvicorn --version
# Copy the codebase
COPY . .

# Run the uvicorn server
# CMD ["fastapi", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
CMD [ "python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
EXPOSE 80