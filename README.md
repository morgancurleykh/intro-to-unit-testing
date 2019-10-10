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
docker run --name iut -v $(pwd)/src:/src -t intro-to-unit-testing; docker rm $(docker ps -q -a)
```

### Connect to the Container to run commands

```
docker exec -it iut /bin/bash
```

#### Create records file

```
python computations.py 200
```
