from database import SessionLocal
from models import SystemMetric

db = SessionLocal() # db is the instance
all_session = db.query(SystemMetric).all() # here we query the class not the table name and we use instance name here for querying.
print(f"{'ID':<20} {'CPU%':>20} {'RAM%':>20} {'TIMESTAMP':>20}")
for session in all_session:
    print(f"{session.id:<20} {session.cpu_percentage:>20} {session.ram_percentage:>20} {str(session.time_stamp):>20}")
db.close()