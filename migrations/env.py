"""Configurazione ambiente Alembic e runner delle migrazioni."""
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Questo è l'oggetto di configurazione di Alembic, che fornisce
# i valori della sezione [alembic] del file
# .ini in uso.
config = context.config

# Interpreta il file di configurazione per il logging di Python.
# Questa riga configura i logger fondamentalmente.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Aggiungi l'oggetto MetaData del tuo modello qui
# per il supporto dell'autogenerazione
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from app import db
target_metadata = db.metadata


def run_migrations_offline() -> None:
    """Esegui le migrazioni in modalità 'offline'.

    Questo configura il contesto con solo un URL
    e non un Engine, anche se un Engine è accettabile
    qui pure. Saltando la creazione dell'Engine
    non abbiamo nemmeno bisogno di un DBAPI disponibile.

    Le chiamate a context.execute() qui emettono la stringa data all'output
    dello script.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Esegui le migrazioni in modalità 'online'.

    In questo scenario abbiamo bisogno di creare un Engine
    e associare una connessione al contesto.

    """
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = "sqlite:///carsharing.db"
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.StaticPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
