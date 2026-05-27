# =========================================================
# FastBox Mystery Delivery System
# =========================================================
# This version supports:
# ✔ Multiple test cases
# ✔ Dictionary JSON format
# ✔ Large combined JSON files
# ✔ Unlimited packages
# ✔ Unlimited agents
# ✔ Unlimited warehouses
# ✔ Random delivery delay
# ✔ Report generation
# ✔ report.json export
# =========================================================

import json
import math
import random


# =========================================================
# Calculate Euclidean Distance
# =========================================================
def calculate_distance(point1, point2):

    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2
    )


# =========================================================
# Load JSON File
# =========================================================
def load_json_file(filename):

    try:

        with open(filename, "r") as file:

            data = json.load(file)

        print("\nJSON file loaded successfully!")

        return data

    except FileNotFoundError:

        print("\nERROR: File not found!")
        return None

    except json.JSONDecodeError:

        print("\nERROR: Invalid JSON format!")
        return None


# =========================================================
# Convert Warehouse Data
#
# Handles:
# "W1": [34,29]
# OR
# "W1": [34,29,11,35,...]
#
# Keeps first 2 values only
# =========================================================
def process_warehouses(raw_warehouses):

    warehouses = {}

    for warehouse_id, coordinates in raw_warehouses.items():

        x = coordinates[0]
        y = coordinates[1]

        warehouses[warehouse_id] = [x, y]

    return warehouses


# =========================================================
# Convert Agent Data
#
# Handles:
# "A1": [5,5]
# OR
# "A1": [5,5,10,20,...]
#
# Keeps first 2 values only
# =========================================================
def process_agents(raw_agents):

    agents = {}

    for agent_id, coordinates in raw_agents.items():

        x = coordinates[0]
        y = coordinates[1]

        agents[agent_id] = [x, y]

    return agents


# =========================================================
# Find Nearest Agent
# =========================================================
def find_nearest_agent(warehouse_location, agents):

    nearest_agent = None

    minimum_distance = float("inf")

    for agent_id, agent_location in agents.items():

        distance = calculate_distance(
            warehouse_location,
            agent_location
        )

        if distance < minimum_distance:

            minimum_distance = distance
            nearest_agent = agent_id

    return nearest_agent, minimum_distance


# =========================================================
# Simulate Deliveries
# =========================================================
def simulate_delivery(data):

    warehouses = process_warehouses(
        data["warehouses"]
    )

    agents = process_agents(
        data["agents"]
    )

    packages = data["packages"]

    # =====================================================
    # Report Structure
    # =====================================================
    report = {}

    for agent_id in agents:

        report[agent_id] = {
            "packages_delivered": 0,
            "total_distance": 0,
            "efficiency": 0
        }

    delivered_packages = 0

    # =====================================================
    # Process Packages
    # =====================================================
    for package in packages:

        package_id = package["id"]

        warehouse_id = package["warehouse"]

        destination = package["destination"]

        # Skip invalid warehouse
        if warehouse_id not in warehouses:

            print(f"\nInvalid warehouse: {warehouse_id}")
            continue

        warehouse_location = warehouses[
            warehouse_id
        ]

        # =================================================
        # Find nearest agent
        # =================================================
        assigned_agent, distance_to_warehouse = (
            find_nearest_agent(
                warehouse_location,
                agents
            )
        )

        # =================================================
        # Warehouse -> Destination Distance
        # =================================================
        delivery_distance = calculate_distance(
            warehouse_location,
            destination
        )

        # =================================================
        # Total Trip Distance
        # =================================================
        total_trip_distance = (
            distance_to_warehouse +
            delivery_distance
        )

        # =================================================
        # Random Delay
        # =================================================
        random_delay = random.randint(1, 10)

        # =================================================
        # Update Report
        # =================================================
        report[assigned_agent][
            "packages_delivered"
        ] += 1

        report[assigned_agent][
            "total_distance"
        ] += total_trip_distance

        delivered_packages += 1

        # =================================================
        # Print Delivery Info
        # =================================================
        print("\n=================================")

        print(f"Package ID      : {package_id}")

        print(f"Warehouse       : {warehouse_id}")

        print(f"Assigned Agent  : {assigned_agent}")

        print(f"Destination     : {destination}")

        print(
            f"Trip Distance   : "
            f"{round(total_trip_distance, 2)}"
        )

        print(
            f"Random Delay    : "
            f"{random_delay} minutes"
        )

        print(
            f"Route           : "
            f"{assigned_agent} -> "
            f"{warehouse_id} -> "
            f"{destination}"
        )

        print("=================================")

    # =====================================================
    # Calculate Efficiency
    # =====================================================
    best_agent = None

    best_efficiency = float("inf")

    for agent_id in report:

        delivered = report[agent_id][
            "packages_delivered"
        ]

        total_distance = report[agent_id][
            "total_distance"
        ]

        if delivered > 0:

            efficiency = (
                total_distance / delivered
            )

        else:

            efficiency = 0

        report[agent_id][
            "total_distance"
        ] = round(total_distance, 2)

        report[agent_id][
            "efficiency"
        ] = round(efficiency, 2)

        # Lower efficiency = Better
        if (
            delivered > 0 and
            efficiency < best_efficiency
        ):

            best_efficiency = efficiency
            best_agent = agent_id

    # =====================================================
    # Final Summary
    # =====================================================
    report["best_agent"] = best_agent

    report["total_packages"] = len(packages)

    report["delivered_packages"] = delivered_packages

    return report


# =========================================================
# Save Report
# =========================================================
def save_report(report, filename="report.json"):

    with open(filename, "w") as file:

        json.dump(report, file, indent=4)

    print("\nReport saved successfully!")
    print(f"Saved File: {filename}")


# =========================================================
# Main Function
# =========================================================
def main():

    print("\n======================================")
    print(" FastBox Mystery Delivery System ")
    print("======================================")

    filename = input(
        "\nEnter JSON filename: "
    )

    # =====================================================
    # Load JSON Data
    # =====================================================
    data = load_json_file(filename)

    if data is None:
        return

    # =====================================================
    # Run Simulation
    # =====================================================
    report = simulate_delivery(data)

    # =====================================================
    # Print Final Report
    # =====================================================
    print("\n\n=========== FINAL REPORT ===========\n")

    print(json.dumps(report, indent=4))

    # =====================================================
    # Save Report
    # =====================================================
    save_report(report)


# =========================================================
# Program Entry Point
# =========================================================
if __name__ == "__main__":

    main()