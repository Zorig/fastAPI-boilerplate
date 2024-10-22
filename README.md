To create the venv: `python3 -m venv .venv`

To run: ` docker-compose up --build`

To stop: `docker-compose stop`

# Migration

To run the migration:

```sh
docker-compose exec web alembic revision --autogenerate -m "<MigrationNAME>"
```

To apply the migration:

```sh
docker-compose exec web alembic upgrade head
```
