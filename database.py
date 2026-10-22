from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DATABASE_URL ="mysql+pymysql://root:root@localhost:3306/fci_db"
DATABASE_URL = "postgresql+psycopg2://training_ufx5_user:SYW158K3tDrfhewcJyImsxs5aZ3GjoKJ@dpg-dbbfh7m1egvs73fsaovg-a.oregon-postgres.render.com/training_ufx5"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()