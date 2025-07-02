import sqlite3
import csv

conn = sqlite3.connect("questions.db")
c = conn.cursor()

with open("Bitcoin-Test-Q.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute(
            "INSERT INTO questions (level, question, choice1, choice2, choice3, choice4, correct) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                int(row["level"]),
                row["question"],
                row["choice1"],
                row["choice2"],
                row["choice3"],
                row["choice4"],
                row["correct"]
            )
        )

conn.commit()
conn.close()
print("Import completed.")
