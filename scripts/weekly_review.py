#!/usr/bin/env python3
"""Weekly review helper — prompts the user to complete their review."""

from datetime import datetime, timedelta
today = datetime.now()
week_start = today - timedelta(days=today.weekday())

print("📅 WEEKLY REVIEW TRIGGERED")
print(f"Week of: {week_start.strftime('%Y-%m-%d')}")
print()
print("Open [[monk_mode]] and [[journal]] to complete.")
print()
print("REVIEW PROMPT:")
print("1. What were your 3 biggest wins this week?")
print("2. What went wrong? Why?")
print("3. What will you adjust next week?")
print("4. Discipline score: x/7")
print("5. Check habit completion — any consistently missed?")
print("6. Body metrics: measure weight, check progress")
print("7. Content: did you ship this week?")
