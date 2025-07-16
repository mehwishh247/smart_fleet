from sqlmodel import SQLModel, create_engine

def create_app_engine(db_name):
    url = f"sqlite:///{db_name}.db"
    global engine
    engine = create_engine(url, echo=True)
    return engine

def get_engine():
    return engine

def create_db_and_tables(db_name: str):
    engine = create_app_engine(db_name=db_name)
    SQLModel.metadata.create_all(engine)
