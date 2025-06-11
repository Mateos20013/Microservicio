from database import Base, engine
from models import User

# Create all tables in the database
if __name__ == "__main__":
    print("Initializing database...")
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully.")
