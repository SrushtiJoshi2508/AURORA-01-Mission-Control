# -------------------- DIAGNOSTICS MODULE --------------------

def diagnostics(telemetry, log_event):
    print("\n--- SYSTEM DIAGNOSTICS ---")

    # Fuel check
    if telemetry["fuel"] < 20:
        print("Fuel       : CRITICAL")
    elif telemetry["fuel"] < 40:
        print("Fuel       : WARNING")
    else:
        print("Fuel       : OK")

    # Oxygen check
    if telemetry["oxygen"] < 30:
        print("Oxygen     : CRITICAL")
    elif telemetry["oxygen"] < 60:
        print("Oxygen     : WARNING")
    else:
        print("Oxygen     : OK")

    # Temperature check
    if telemetry["temperature"] > 80:
        print("Temperature: CRITICAL")
    elif telemetry["temperature"] > 60:
        print("Temperature: WARNING")
    else:
        print("Temperature: OK")

    # Battery check
    if telemetry["battery"] < 15:
        print("Battery    : CRITICAL")
    elif telemetry["battery"] < 40:
        print("Battery    : WARNING")
    else:
        print("Battery    : OK")

    print("Communication: ONLINE")

    log_event("Diagnostics completed")