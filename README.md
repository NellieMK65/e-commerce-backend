# Setup

-   Install the necessary packages with `pipenv install "fastapi[standard]" sqlalchemy alembic`

# Migrations - version control for databases

-   Active shell with `pipenv shell`
-   To setup migrations, run `alembic init migrations` -> run this only once
-   Edit alembic.ini file and set `sqlalchemy.url = sqlite:///e-commerce.db`
-   Edit `env.py` in the migrations folder and import the Base class from the models file and update the `target_metadata`
-   To create a migration, run `alembic revision --autogenerate -m "message"`
-   To apply the generated migration, run `alembic upgrade head`
