from database import SessionLocal,engine,Base
from models import User

#this line creates the tables that dont exist.
Base.metadata.create_all(bind=engine)
# db = SessionLocal()
# new_user = User(email="quant_dev@example.com", hashed_password="securepassword123")
# db.add(new_user)
# db.commit()
# print(f"Success! User {new_user.email} added to the database")
# db.close()