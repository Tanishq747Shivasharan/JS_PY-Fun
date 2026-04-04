from core.target_system import TargetSystem
from core.service import Service

def test_add_service():
    system = TargetSystem("192.168.1.1")
    service = Service(80)
    system.add_service(service)
    assert len(system.discovered_services) == 1

def test_calculate_risk():
    system = TargetSystem("192.168.1.3")
    system.add_service(Service(21))  # High risk: 10
    system.add_service(Service(80))  # Medium risk: 5
    system.calculate_risk()
    assert system.risk_score == 15

if __name__ == "__main__":
    test_add_service()
    test_calculate_risk()
    print("All system tests passed.")
