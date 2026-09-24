# -------------------- EMERGENCY MODULE --------------------

def emergency_simulation(telemetry, log_event):
    print("\n--- EMERGENCY SIMULATION ---")
    print("1. Fuel Leak")
    print("2. Oxygen Loss")
    print("3. Overheating")
    print("4. Battery Failure")
    print("5. Cancel")

    choice = input("Select emergency: ")

    if choice == "1":
        telemetry["fuel"] -= 25
        if telemetry["fuel"] < 0:
            telemetry["fuel"] = 0
        log_event("Emergency simulated: fuel leak")
        print("Fuel leak simulated.")

    elif choice == "2":
        telemetry["oxygen"] -= 30
        if telemetry["oxygen"] < 0:
            telemetry["oxygen"] = 0
        log_event("Emergency simulated: oxygen loss")
        print("Oxygen loss simulated.")

    elif choice == "3":
        telemetry["temperature"] += 40
        log_event("Emergency simulated: overheating")
        print("Overheating simulated.")

    elif choice == "4":
        telemetry["battery"] = 10
        log_event("Emergency simulated: battery failure")
        print("Battery failure simulated.")

    elif choice == "5":
        print("Emergency simulation cancelled.")

    else:
        print("Invalid choice.")