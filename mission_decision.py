# -------------------- MISSION DECISION MODULE --------------------

def mission_decision(telemetry, log_event):
    print("\n--- MISSION DECISION ---")

    if telemetry["battery"] < 15:
        decision = "ABORT - critical battery"

    elif telemetry["fuel"] < 20:
        decision = "ABORT - critical fuel"

    elif telemetry["oxygen"] < 30:
        decision = "ABORT - critical oxygen"

    elif telemetry["temperature"] > 80:
        decision = "ABORT - critical temperature"

    elif (
        telemetry["fuel"] < 40
        or telemetry["oxygen"] < 60
        or telemetry["battery"] < 40
        or telemetry["temperature"] > 60
    ):
        decision = "CAUTION - monitor systems"

    else:
        decision = "GO - mission conditions nominal"

    print("Decision:", decision)

    log_event("Mission decision: " + decision)

    return decision