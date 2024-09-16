from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://db_215076784_sit722_part33_user:yu1lqg8MWJM5nemg92tb93USysqkSLxh@dpg-crjs4plds78s73edlen0-a.oregon-postgres.render.com/db_215076784_sit722_part33" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
