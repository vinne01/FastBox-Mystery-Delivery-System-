# FastBox Mystery Delivery System

## Overview

FastBox Mystery Delivery System is a Python-based logistics simulation project that manages package deliveries between warehouses and destinations using delivery agents.

The system:
- Loads data from JSON files
- Assigns nearest delivery agents
- Calculates travel distances
- Simulates random delivery delays
- Generates delivery reports
- Exports results to `report.json`

---

# Features

✔ Multiple test case support  
✔ Dictionary JSON format support  
✔ Large combined JSON file handling  
✔ Unlimited packages support  
✔ Unlimited delivery agents  
✔ Unlimited warehouses  
✔ Euclidean distance calculation  
✔ Random delivery delay simulation  
✔ Automatic report generation  
✔ JSON report export  

---

# Technologies Used

- Python 3
- JSON
- Math Module
- Random Module

---

# Project Structure

```bash
FastBox/
│
├── main.py
├── data.json
├── report.json
└── README.md
```

---

# Input JSON Format

Example:

```json
{
    "warehouses": {
        "W1": [10, 20],
        "W2": [50, 60]
    },

    "agents": {
        "A1": [5, 5],
        "A2": [40, 40]
    },

    "packages": [
        {
            "id": "P1",
            "warehouse": "W1",
            "destination": [100, 120]
        },

        {
            "id": "P2",
            "warehouse": "W2",
            "destination": [200, 300]
        }
    ]
}
```

---

# How the System Works

## Step 1: Load JSON Data

The program loads:
- Warehouses
- Delivery agents
- Packages

from a JSON file.

---

## Step 2: Find Nearest Agent

For every package:
- The nearest available agent is selected
- Distance is calculated using Euclidean Distance Formula

Formula:

```python
distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
```

---

## Step 3: Calculate Delivery Distance

The system calculates:

```text
Agent -> Warehouse -> Destination
```

Total trip distance:

```text
distance_to_warehouse + warehouse_to_destination
```

---

## Step 4: Simulate Random Delay

A random delay between 1 and 10 minutes is generated for every package delivery.

---

## Step 5: Generate Final Report

The report contains:
- Packages delivered by each agent
- Total distance traveled
- Delivery efficiency
- Best performing agent

---

# How to Run the Project

## Step 1: Install Python

Download Python:

https://www.python.org/downloads/

---

## Step 2: Save Files

Save:
- `main.py`
- `data.json`

in the same folder.

---

## Step 3: Run Program

```bash
python main.py
```

---

## Step 4: Enter JSON File Name

Example:

```bash
Enter JSON filename: data.json
```

---

# Output Example

```text
Package ID      : P1
Warehouse       : W1
Assigned Agent  : A1
Destination     : [100, 120]
Trip Distance   : 145.34
Random Delay    : 6 minutes
Route           : A1 -> W1 -> [100, 120]
```

---

# Final Report Example

```json
{
    "A1": {
        "packages_delivered": 2,
        "total_distance": 220.45,
        "efficiency": 110.22
    },

    "best_agent": "A1",
    "total_packages": 2,
    "delivered_packages": 2
}
```

---

# Assumptions Made

Since some scenarios were not explicitly defined in the assignment, the following engineering assumptions were implemented:

1. If warehouse coordinates contain more than two values, only the first two values are considered as `(x, y)` coordinates.

2. If agent coordinates contain extra values, only the first two are used.

3. The nearest agent is selected purely based on minimum Euclidean distance.

4. In case multiple agents have the same minimum distance, the first encountered agent is selected.

5. Invalid warehouse IDs are skipped instead of terminating the program.

6. All agents are assumed to be always available.

7. Random delays do not affect delivery success.

8. Packages are processed sequentially in the order provided in JSON.

9. Efficiency is calculated as:

```text
total_distance / packages_delivered
```

Lower efficiency value indicates better performance.

---

# Error Handling

The system handles:
- Missing JSON files
- Invalid JSON format
- Invalid warehouse IDs

---

# Future Improvements

Possible enhancements:
- Real-time delivery tracking
- Agent availability management
- Traffic simulation
- Delivery priority system
- GUI dashboard
- Database integration
- Route optimization algorithms
- Parallel delivery processing

---

