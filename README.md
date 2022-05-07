# FastAPI NuxtJS Template

A template repo to jump-start development with:

+ A FastAPI backend
+ A NuxtJs frontend
+ A PostgreSQL database

## Running the project

1. Use the repo as a template on GitHub
2. Copy the contents of `.env.example` to a (gitignored) file named `.env`
3. Run `docker-compose up --build`
4. Profit

This will spin up the following:

+ [localhost:8000](localhost:8000) - Fast API Backend
+ [localhost:8000/docs](localhost:8000/docs) - API Documentation
+ [localhost:3000](localhost:3000) - NuxtJs Frontend
+ [localhost:5432](localhost:5432) - PostgreSQL Database

## What else is included?

+ GitHub Action CI for the frontend project
+ The ORM used is TortoiseORM
+ Aerich is used for managing database migrations

## Initializing the database

**NOTE: You should not really need to do this.**

```sh
# First, start the docker containers:
docker-compose up -d --build

# Then initialize the database:
docker-compose exec backend aerich init -t app.database.config.TORTOISE_ORM
    #Success create migrate location ./migrations
    #Success write config to pyproject.toml

docker-compose exec backend aerich init-db
    #Success create app migrate location migrations/models
    #Success generate schema for app "models"
```

## Running database migrations

```sh
docker-compose exec backend aerich migrate
docker-compose exec backend aerich upgrade
```

## License

Copyright 2022 Bradley Marques

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## References

1. [https://testdriven.io/blog/developing-a-single-page-app-with-fastapi-and-vuejs/](https://testdriven.io/blog/developing-a-single-page-app-with-fastapi-and-vuejs/)
2. [https://testdriven.io/blog/fastapi-docker-traefik/](https://testdriven.io/blog/fastapi-docker-traefik/)
