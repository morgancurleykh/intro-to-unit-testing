FROM python

ENV PYTHONPATH=/src

# Install testing tools
RUN pip install pytest pytest-testmon pytest-watch tdda factory_boy

VOLUME ["/src"]
WORKDIR /src

CMD pip install -r requirements.txt && ptw -- --testmon ./tests/
