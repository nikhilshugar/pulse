#We create the session and hand it over to the FastAPI endpoint and close the session.
from database import SessionLocal

def session_provider():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()