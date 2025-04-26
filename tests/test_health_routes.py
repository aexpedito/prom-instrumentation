def test_health_check():
    # Simulate a health check endpoint response
    response = {"status": "ok"}
    assert response["status"] == "ok"

def test_health_status():
    # Simulate a health status endpoint response
    response = {"status": "healthy", "uptime": 12345}
    assert response["status"] == "healthy"
    assert response["uptime"] > 0

def test_health_check_failure():
    # Simulate a failed health check
    response = {"status": "erro"}
    assert response["status"] == "error"

def test_health_status_downtime():
    # Simulate a health status with downtime
    response = {"status": "unhealthy", "uptime": 0}
    assert response["status"] == "unhealthy"
    assert response["uptime"] == 0