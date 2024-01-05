import random

tasks = [
    "Warehouse Walkthrough",
    "Inventory Analysis",
    "WMS Integration",
    "SKU/ICR/Barcode Implementation",
    "Reconfigure Storage Layout",
    "Cross-Training",
    "Safety and Efficiency Training",
    "Establish KPIs",
    "Technology Optimization",
    "Free Afternoon!",
    "Free Mate Day!"
]

random.shuffle(tasks)

days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]

tasks_per_day = {day: [] for day in days}
for task in tasks:
    random_day = random.choice(days)
    tasks_per_day[random_day].append(task)

print("Randomized Itinerary:")
for day, day_tasks in tasks_per_day.items():
    print(f"\n{day}:")
    for task in day_tasks:
        print(f"  - {task}")