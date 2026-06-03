import csv
from datetime import datetime

# Example values
# Later namma other modules output connect pannalam

total_customers = 25
loitering_alerts = 2
abandoned_objects = 1
most_active_zone = "Counter Area"

# Save CSV
with open("store_dashboard_report.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Metric", "Value"])

    writer.writerow(["Total Customers", total_customers])
    writer.writerow(["Loitering Alerts", loitering_alerts])
    writer.writerow(["Abandoned Objects", abandoned_objects])
    writer.writerow(["Most Active Zone", most_active_zone])
    writer.writerow(["Generated Time", datetime.now()])

print("\n=========================")
print("STORE INTELLIGENCE REPORT")
print("=========================")
print("Total Customers      :", total_customers)
print("Loitering Alerts     :", loitering_alerts)
print("Abandoned Objects    :", abandoned_objects)
print("Most Active Zone     :", most_active_zone)
print("=========================")
print("CSV Saved Successfully")