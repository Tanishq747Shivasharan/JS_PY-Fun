from config import RISK_WEIGHTS

class TargetSystem:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.discovered_services = []
        self.risk_score = 0

    def add_service(self, service):
        self.discovered_services.append(service)

    def calculate_risk(self):
        self.risk_score = 0
        for service in self.discovered_services:
            self.risk_score += RISK_WEIGHTS.get(service.port_number, 0)
        return self.risk_score

    def generate_report(self):
        score = self.calculate_risk()
        service_list = ", ".join(str(s) for s in self.discovered_services)
        return f"Audit Complete for {self.ip_address}. Risk Level: {score}. Exposed Services: {service_list}"