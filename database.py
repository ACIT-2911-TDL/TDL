from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:password@localhost/TDL')

# engine = create_engine('mysql+mysqlconnector://root:password@localhost/test_tdl')
