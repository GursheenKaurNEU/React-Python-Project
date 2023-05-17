
FROM  python:3.11
WORKDIR /app
EXPOSE 5050


COPY Pipfile Pipfile.lock ./
RUN pip install pipenv
# RUN pipenv lock --requirements > requirements.txt
RUN pipenv requirements --dev > requirements.txt

RUN pip install -r requirements.txt

COPY . ./

CMD ["python","main.py"]