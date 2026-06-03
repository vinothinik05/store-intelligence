import csv
from datetime import datetime
import os

CSV_FILE = "event_stream.csv"

def log_event(visitor_id, event_type):

    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "visitor_id",
                "event_type",
                "timestamp"
            ])

        writer.writerow([
            visitor_id,
            event_type,
            datetime.now()
        ])