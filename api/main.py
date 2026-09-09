from fastapi import FastAPI, Depends, HTTPException
from api.dependencies import session_provider
from models import SystemMetric
from api.schemas import MetricOut

pulse_api = FastAPI()

@pulse_api.get("/health")
def health_check():
    return({"status":"running"})

@pulse_api.get('/health/database')
def database_health(db = Depends(session_provider)):
    all_count = db.query(SystemMetric).count()
    return {'status': 'connected', 'metric_count':all_count}

@pulse_api.get('/metrics/latest',response_model=MetricOut)
def latest_metric(db = Depends(session_provider)):
    latest = db.query(SystemMetric).order_by(SystemMetric.time_stamp.desc(),SystemMetric.id.desc()).first()
    if latest is None:
        raise HTTPException(status_code=404,detail='The DB is empty.')
    return latest