from core.scanner import Scanner

def test_scanner_load_ports():
    scanner = Scanner()
    assert len(scanner.target_ports) == 4

def test_shuffle_runs():
    scanner = Scanner()
    original_order = list(scanner.target_ports)
    scanner.shuffle_targets()
    assert len(scanner.target_ports) == 4

if __name__ == "__main__":
    test_scanner_load_ports()
    test_shuffle_runs()
    print("All scanner tests passed.")