# C10K in Python

## Introduction

Demonstrates scalable techniques for handling 10,000 concurrent requests in Python.

## Install dependencies

```bash
make install_dependencies
```

## Run Async Server

This implementation uses asyncio and uvloop to handle the requests.

```bash
make run_async_server
```

## Run Flask Gevent  

This implementation uses gevent to handle the requests.

```bash
make run_flask_gevent
```

## Run FastAPI

This implementation uses FastAPI to handle the requests.

```bash
make run_fastapi
```