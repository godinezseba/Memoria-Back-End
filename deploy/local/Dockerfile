FROM python:3.6

RUN pip install --upgrade pip

WORKDIR /app
RUN useradd -m worker
RUN chown worker:worker .
USER worker

RUN pip install --upgrade --user pipenv
ENV PATH=/home/worker/.local/bin:$PATH

COPY --chown=worker:worker ./code /app

RUN pipenv lock -r > requirements.txt
RUN python -m pip install -r requirements.txt

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080"]
