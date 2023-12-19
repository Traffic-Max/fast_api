from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DARABASE_URL = "postgresql://postgres:2517@localhost/db"

engine = create_engine(
    SQLALCHEMY_DARABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




# Depency
