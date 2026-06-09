#!/usr/bin/env python3
"""Extract health metrics from markdown body text and add as frontmatter properties.
Run from vault root: python3 scripts/enrich_health_frontmatter.py

Adds: steps, sleep_hours, workout_minutes, hrv, resting_hr, active_calories, stand_hours
"""

import os
import re
import glob
from datetime import datetime, timedelta

VAULT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEALTH_DIR = os.path.join(VAULT_ROOT, "Health")


def parse_duration(text):
    """Parse duration strings like '1h 1m', '47m', '7h 22m' into total minutes."""
    h = re.search(r'(\d+)h', text)
    m = re.search(r'(\d+)m', text)
    total = 0
    if h:
        total += int(h.group(1)) * 60
    if m:
        total += int(m.group(1))
    return total


def parse_number(text):
    """Parse comma-formatted number, e.g. '6,048' -> 6048."""
    text = text.strip()
    if text == '-':
        return None
    try:
        return int(text.replace(',', ''))
    except ValueError:
        try:
            return float(text.replace(',', ''))
        except ValueError:
            return None


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split frontmatter from body
    fm_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not fm_match:
        return False

    fm_text = fm_match.group(1)
    body = fm_match.group(2)

    # Extract metrics from body text
    metrics = {}

    # Steps
    m = re.search(r'\*\*Steps:\*\*\s*([\d,]+)', body)
    if m:
        metrics['steps'] = parse_number(m.group(1))

    # Sleep total
    m = re.search(r'\*\*Total:\*\*\s*([\dhm\s]+)', body)
    if m:
        minutes = parse_duration(m.group(1))
        if minutes:
            metrics['sleep_minutes'] = minutes

    # Workout duration (multiple possible — sum them)
    workout_minutes = 0
    for m in re.finditer(r'\*\*Duration:\*\*\s*([\dhm\s]+)', body):
        workout_minutes += parse_duration(m.group(1))
    if workout_minutes > 0:
        metrics['workout_minutes'] = workout_minutes

    # HRV
    m = re.search(r'\*\*HRV:\*\*\s*([\d.]+)\s*ms', body)
    if m:
        metrics['hrv'] = float(m.group(1))

    # Resting HR
    m = re.search(r'\*\*Resting HR:\*\*\s*(\d+)', body)
    if m:
        metrics['resting_hr'] = int(m.group(1))

    # Active Calories
    m = re.search(r'\*\*Active Calories:\*\*\s*([\d,]+)\s*kcal', body)
    if m:
        metrics['active_calories'] = parse_number(m.group(1))

    # Stand Hours
    m = re.search(r'\*\*Stand Hours:\*\*\s*(\d+)', body)
    if m:
        metrics['stand_hours'] = int(m.group(1))

    # Walking/Running Distance (km)
    m = re.search(r'\*\*Walking/Running Distance:\*\*\s*([\d.]+)\s*km', body)
    if m:
        metrics['walk_km'] = float(m.group(1))

    # SpO2
    m = re.search(r'\*\*SpO2:\*\*\s*(\d+)%', body)
    if m:
        metrics['spo2'] = int(m.group(1))

    # Respiratory Rate
    m = re.search(r'\*\*Respiratory Rate:\*\*\s*([\d.]+)', body)
    if m:
        metrics['respiratory_rate'] = float(m.group(1))

    if not metrics:
        return False

    # Build new frontmatter
    # Start with existing frontmatter
    existing_lines = fm_text.split('\n')
    # Remove existing metric keys that we're adding (in case of re-run)
    metric_keys = {'steps', 'sleep_minutes', 'workout_minutes', 'hrv',
                    'resting_hr', 'active_calories', 'stand_hours', 'walk_km',
                    'spo2', 'respiratory_rate'}
    cleaned_lines = []
    for line in existing_lines:
        key = line.split(':')[0].strip()
        if key in metric_keys:
            continue
        cleaned_lines.append(line)

    # Append new metrics in consistent order
    order = ['steps', 'sleep_minutes', 'workout_minutes', 'hrv', 'resting_hr',
             'active_calories', 'stand_hours', 'walk_km', 'spo2', 'respiratory_rate']
    for key in order:
        if key in metrics:
            cleaned_lines.append(f"{key}: {metrics[key]}")

    new_fm = '\n'.join(cleaned_lines)
    new_content = f"---\n{new_fm}\n---\n{body}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True


def main():
    files = sorted(glob.glob(os.path.join(HEALTH_DIR, '*.md')))
    updated = 0
    for fp in files:
        if process_file(fp):
            updated += 1
    print(f"Processed {len(files)} files, enriched {updated} with metrics")


if __name__ == '__main__':
    main()
