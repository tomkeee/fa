from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv
load_dotenv()

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
NAME = os.getenv('NAME')

engine = create_engine(f'mysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{NAME}')
Base = declarative_base()


Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()