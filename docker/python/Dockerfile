FROM python:3.7
RUN mkdir /app
COPY ./app /app
WORKDIR /app
RUN ls -la
RUN pip install --upgrade pip \
 && pip install pipenv \
 && pipenv install --deploy --system --ignore-pipfile --skip-lock
CMD python run.py