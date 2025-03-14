from logging.config import fileConfig
import os
import sys
import psycopg2
from sqlalchemy import create_engine
from alembic import context
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from database import Base

# this is the Alembic Config object
config = context.config

# Interpret the config file for Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def get_connection_params():
    """Get database connection parameters."""
    return {
        "dbname": "neondb",
        "user": "neondb_owner",
        "password": "npg_jsb0a9gNwZAW",
        "host": "ep-old-mud-a56o7njn-pooler.us-east-2.aws.neon.tech",
        "sslmode": "require",
    }


def create_db_url():
    """Create database URL from parameters."""
    params = get_connection_params()
    return f"postgresql://{params['user']}:{params['password']}@{params['host']}/{params['dbname']}"


def test_connection():
    """Test database connection using psycopg2."""
    try:
        params = get_connection_params()
        print("Testing connection with parameters:", params)
        conn = psycopg2.connect(**params)
        print("Connection successful!")
        conn.close()
        return True
    except Exception as e:
        print(f"Connection failed: {str(e)}")
        return False


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    if not test_connection():
        raise Exception("Failed to connect to database")

    url = create_db_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    if not test_connection():
        raise Exception("Failed to connect to database")

    url = create_db_url()
    print(f"Using database URL: {url}")

    engine = create_engine(
        url,
        connect_args={
            "sslmode": "require",
        },
    )

    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
