## Intro to unit testing

Unit testing is a development practice used to verify the functioning of a given codebase

This repo provides a ready to go testing environment

## Pre requisites

1. Signup for Dockerhub
2. Download & Install Docker
3. Link account to Komodo Hub via request to access from IT *(optional)*

### Build Docker Image

```
docker build -t intro-to-unit-testing ./
```

### Start test watcher

```
docker run --name itut -v $(pwd)/src:/src -t intro-to-unit-testing
```

### Connect to the Container to run commands

```
docker exec -it itut /bin/bash
```

#### Create records file

```
python computations.py 200
```
