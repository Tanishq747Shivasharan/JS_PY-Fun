from core.service import Service

def test_service_creation():
    service = Service(80, "TCP")
    assert service.port_number == 80 and service.protocol == "TCP"

def test_service_str():
    service = Service(80)
    assert str(service) == "80/TCP"

if __name__ == "__main__":
    test_service_creation()
    test_service_str()
    print("All service tests passed.")
