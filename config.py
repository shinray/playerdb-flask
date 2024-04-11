import os

class Config:
    # Flask
    DEBUG = True

    # SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # csv path
    CSV_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lahman_1871-2023_csv', 'People.csv')
