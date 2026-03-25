# Functions & Scope

def generate_report(target, severity="Low"):
    print(f"Alert for {target} Severity {severity}")

generate_report("Server1", "Medium")
generate_report("UndergroundServer7", "High")
generate_report("MainServer")