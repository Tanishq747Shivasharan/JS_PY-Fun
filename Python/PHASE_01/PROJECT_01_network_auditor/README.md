# Network Auditor

A lightweight, modular network auditing tool written in Python. It scans a set of commonly exposed ports on a target system, evaluates the risk level of each discovered service, and produces a structured audit report.

---

## Overview

Network Auditor simulates the process of identifying open ports on a target machine and assessing the potential security risk they introduce. Each port is represented as a service with an associated protocol, and the target system aggregates those services to compute an overall risk score based on configurable weights.

This project is structured around three core concepts:

- **Scanning** — loading and randomizing a list of target ports to simulate real-world scan behavior
- **Service identification** — representing each open port as a typed service object
- **Risk assessment** — scoring the target system based on which services are exposed

---

## Project Structure

```
PROJECT_01_network_auditor/
├── main.py                  # Entry point — runs the full audit pipeline
├── config.py                # Central configuration: ports, risk weights, defaults
├── core/
│   ├── scanner.py           # Scanner class — manages and shuffles target ports
│   ├── service.py           # Service class — represents a single open port
│   └── target_system.py     # TargetSystem class — aggregates services and scores risk
├── tests/
│   ├── test_scanner.py      # Unit tests for Scanner
│   ├── test_service.py      # Unit tests for Service
│   └── test_target_system.py# Unit tests for TargetSystem
└── README.md
```

---

## Configuration

All configurable values live in `config.py`.

```python
COMMON_PORTS = [21, 22, 80, 443]
```
The list of ports the scanner will load. These represent FTP, SSH, HTTP, and HTTPS respectively.

```python
RISK_WEIGHTS = {
    21: 10,
    22: 10,
    80: 5,
    443: 5
}
```
A mapping of port numbers to their assigned risk scores. Ports not present in this dictionary default to a score of 0. Adjust these values to reflect your own threat model.

```python
DEFAULT_PROTOCOL = "TCP"
```
The default protocol assigned to a service when none is explicitly provided.

---

## Core Modules

### Scanner — `core/scanner.py`

Responsible for loading the target port list and optionally randomizing scan order.

| Method | Description |
|---|---|
| `__init__()` | Loads ports from `COMMON_PORTS` into `target_ports` |
| `shuffle_targets()` | Randomly reorders `target_ports` to simulate non-sequential scanning |
| `__str__()` | Returns a human-readable summary of the loaded scanner state |

---

### Service — `core/service.py`

Represents a single open port on a target machine.

| Attribute | Description |
|---|---|
| `port_number` | The port number (e.g. 80) |
| `protocol` | The transport protocol, defaults to `TCP` |

`str(service)` returns the format `port/protocol`, for example `80/TCP`.

---

### TargetSystem — `core/target_system.py`

Represents the machine being audited. Collects discovered services and computes a risk score.

| Method | Description |
|---|---|
| `add_service(service)` | Registers a Service object against this system |
| `calculate_risk()` | Sums risk weights for all discovered services |
| `generate_report()` | Returns a formatted audit summary string |

---

## Running the Auditor

From the project root directory:

```bash
python main.py
```

Sample output:

```
Scanner loaded with 4 ([443, 21, 80, 22])
Audit Complete for 127.0.0.1. Risk Level: 30. Exposed Services: 443/TCP, 21/TCP, 80/TCP, 22/TCP
```

---

## Running the Tests

From the project root directory:

```bash
python -m pytest tests/
```

Or run individual test files directly:

```bash
python tests/test_scanner.py
python tests/test_service.py
python tests/test_target_system.py
```

The test suite covers:

- Scanner port loading and shuffle behavior
- Service object creation and string representation
- TargetSystem service registration and risk calculation

---

## Requirements

- Python 3.7 or higher
- No external dependencies — uses only the Python standard library
- `pytest` is recommended for running the test suite (`pip install pytest`)

---

## Design Notes

The project intentionally avoids live network calls. It is designed as a structural and logical exercise in object-oriented Python, demonstrating class design, separation of concerns, configuration management, and unit testing. Extending it to perform real socket-based port scanning would require adding socket logic to the `Scanner` class and replacing the static port list with dynamic scan results.
