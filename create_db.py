from database import Base, db

def create_db():
    return Base.metadata.create_all(db)

if __name__ == "__main__":
    create_db()