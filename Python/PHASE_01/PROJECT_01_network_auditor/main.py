from core.scanner import Scanner
from core.target_system import TargetSystem
from core.service import Service

if __name__ == "__main__":
    scanner = Scanner()
    scanner.shuffle_targets()
    print(scanner)

    system = TargetSystem("127.0.0.1")
    for port in scanner.target_ports:
        system.add_service(Service(port))
    report = system.generate_report()
    print(report)