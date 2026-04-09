# PROJECT 01 — Network Auditor

A modular, object-oriented network auditing tool built in Python. It loads a configurable set of commonly exposed ports, represents each as a typed service, evaluates the risk level of the target system, and produces a structured audit report.

This is the first project in the Python learning path, focused on applying object-oriented design, separation of concerns, configuration management, and unit testing in a security-relevant context.

---

## What This Project Does

The auditor simulates the core workflow of a basic network reconnaissance tool:

1. A scanner loads a list of known ports and randomizes their order to mimic real-world scan behavior
2. Each port is wrapped in a Service object that carries its protocol information
3. A TargetSystem collects all discovered services and computes a cumulative risk score
4. A final report is generated summarizing the audit findings

No live network calls are made. The project is a structural and logical exercise in Python class design.

---

## Project Structure

```
PROJECT_01_network_auditor/
├── main.py                       # Entry point — orchestrates the full audit pipeline
├── config.py                     # Central configuration: ports, risk weights, protocol default
├── core/
│   ├── scanner.py                # Scanner class — loads and shuffles target ports
│   ├── service.py                # Service class — represents a single open port
│   └── target_system.py          # TargetSystem class — aggregates services, scores risk
├── tests/
│   ├── test_scanner.py           # Unit tests for Scanner
│   ├── test_service.py           # Unit tests for Service
│   └── test_target_system.py     # Unit tests for TargetSystem
└── README.md
```

---

## Configuration

All configurable values are centralized in `config.py`. Modify this file to adjust scan targets and risk thresholds without touching core logic.

```python
COMMON_PORTS = [21, 22, 80, 443]
```
The ports the scanner will load on initialization. These correspond to FTP (21), SSH (22), HTTP (80), and HTTPS (443).

```python
RISK_WEIGHTS = {
    21: 10,
    22: 10,
    80: 5,
    443: 5
}
```
Maps each port to a risk score. Ports not listed here default to 0. FTP and SSH are weighted higher due to their direct system access potential.

```python
DEFAULT_PROTOCOL = "TCP"
```
The fallback protocol assigned to a service when none is explicitly provided at instantiation.

---

## Core Modules

### Scanner — `core/scanner.py`

Manages the list of ports to be audited and simulates non-sequential scanning behavior.

| Method | Description |
|---|---|
| `__init__()` | Copies all ports from `COMMON_PORTS` into `self.target_ports` |
| `shuffle_targets()` | Randomly reorders `target_ports` in place using `random.shuffle` |
| `__str__()` | Returns a readable summary: port count and current order |

---

### Service — `core/service.py`

Represents a single discovered open port on the target machine.

| Attribute | Type | Description |
|---|---|---|
| `port_number` | int | The port number, e.g. `80` |
| `protocol` | str | Transport protocol, defaults to `"TCP"` |

String representation via `str(service)` returns `port/protocol` format — for example, `80/TCP`.

---

### TargetSystem — `core/target_system.py`

Represents the machine under audit. Collects service objects and computes an overall risk score.

| Method | Description |
|---|---|
| `add_service(service)` | Appends a Service object to `discovered_services` |
| `calculate_risk()` | Iterates services, sums their risk weights, stores result in `risk_score` |
| `generate_report()` | Calls `calculate_risk()` and returns a formatted audit summary string |

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

The port order will vary on each run due to shuffling.

---

## Running the Tests

Using pytest from the project root:

```bash
python -m pytest tests/
```

Or run individual test files directly:

```bash
python tests/test_scanner.py
python tests/test_service.py
python tests/test_target_system.py
```

### Test Coverage

| Test File | What It Covers |
|---|---|
| `test_scanner.py` | Port list loading, shuffle preserves count |
| `test_service.py` | Object creation, attribute values, string format |
| `test_target_system.py` | Service registration, risk score calculation |

---

## Requirements

- Python 3.7 or higher
- No third-party dependencies — standard library only (`random`, built-ins)
- `pytest` recommended for the test suite

```bash
pip install pytest
```

---

## Concepts Demonstrated

| Concept | Where Applied |
|---|---|
| Object-Oriented Design | `Scanner`, `Service`, `TargetSystem` classes |
| Separation of Concerns | Each class has a single, well-defined responsibility |
| Configuration Management | All constants isolated in `config.py` |
| Default Parameters | `Service.__init__` uses `DEFAULT_PROTOCOL` as fallback |
| Dictionary Lookup with Fallback | `RISK_WEIGHTS.get(port, 0)` in `calculate_risk` |
| String Representation | `__str__` methods on Scanner and Service |
| Unit Testing | Full test suite across all three core modules |

---

## Extending the Project

This project is intentionally minimal to keep the focus on structure and design. Possible extensions:

- Add real socket-based port scanning to `Scanner` using Python's `socket` module
- Replace the static `COMMON_PORTS` list with a dynamic range input from the user
- Add severity labels (Low / Medium / High / Critical) based on risk score thresholds
- Export the audit report to a `.txt` or `.json` file
- Add a `--target` CLI argument using `argparse` to specify the IP at runtime

---

*Part of the Python PHASE 01 learning path — focused on OOP fundamentals and security tooling.*
