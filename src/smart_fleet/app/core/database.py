from sqlmodel import SQLModel, create_engine

def app_engine(db_name):
    url = f"sqlite:///{db_name}.db"
    return create_engine(url, echo=True)

def create_db_and_tables(db_name: str):
    engine = app_engine(db_name=db_name)
    SQLModel.metadata.create_all(engine)
