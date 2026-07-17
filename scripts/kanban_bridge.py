#!/usr/bin/env python3
"""
Hermes Kanban Bridge — Read/write Obsidian Kanban boards from the terminal.
Works directly with obsidian-kanban markdown files in the vault.

Usage:
  python3 kanban_bridge.py boards                          # List boards
  python3 kanban_bridge.py ls <board>                      # List cards
  python3 kanban_bridge.py add <board> <column> <text>     # Add card
  python3 kanban_bridge.py move <board> <column> <text>    # Move card by text match
  python3 kanban_bridge.py cards <board> <column>          # Cards in specific column
  python3 kanban_bridge.py done <board>                    # Count done/total
"""

import sys
import re
import os

VAULT = os.path.expanduser("~/Documents/Obsidian/Zack-obs")
BOARDS_DIR = os.path.join(VAULT, "Kanban")

def list_boards():
    """List all kanban boards in the vault."""
    boards = []
    for f in sorted(os.listdir(BOARDS_DIR)):
        if f.endswith(".md") and f != "HOWTO.md":
            path = os.path.join(BOARDS_DIR, f)
            with open(path) as fh:
                content = fh.read()
            if "kanban-plugin: board" in content:
                boards.append(f.replace(".md", ""))
    return boards

def parse_board(name):
    """Parse a kanban board into {columns: {col_name: [cards]}, metadata: ...}"""
    path = os.path.join(BOARDS_DIR, f"{name}.md")
    if not os.path.exists(path):
        return None

    with open(path) as fh:
        lines = fh.readlines()

    columns = {}
    current_col = None
    current_cards = []

    for line in lines:
        stripped = line.rstrip()

        # Detect column headers (## ...)
        col_match = re.match(r'^##\s+(.+)$', stripped)
        if col_match:
            if current_col and current_cards:
                columns[current_col] = current_cards
            current_col = col_match.group(1).strip()
            current_cards = []
            continue

        # Detect checklist items (- [ ] ... or - [x] ...)
        if current_col:
            card_match = re.match(r'^(- \[.\]\s+.*)$', stripped)
            if card_match:
                current_cards.append(card_match.group(1))

    # Don't forget last column
    if current_col and current_cards:
        columns[current_col] = current_cards

    return {"columns": columns}

def print_boards():
    boards = list_boards()
    if not boards:
        print("❌ No Kanban boards found in Kanban/")
        return
    print("📋 Kanban Boards:")
    for b in boards:
        board = parse_board(b)
        total = sum(len(cards) for cards in board["columns"].values()) if board else 0
        print(f"  📌 {b} ({total} cards)")

def print_cards(board_name):
    board = parse_board(board_name)
    if not board:
        print(f"❌ Board '{board_name}' not found")
        return
    print(f"📋 {board_name}:")
    for col, cards in board["columns"].items():
        if cards:
            print(f"\n  [{col}]")
            for card in cards:
                print(f"    {card}")
    total = sum(len(c) for c in board["columns"].values())
    print(f"\n  Total: {total} card(s)")

def print_column_cards(board_name, column_name):
    board = parse_board(board_name)
    if not board:
        print(f"❌ Board '{board_name}' not found")
        return
    col = None
    for c in board["columns"]:
        if column_name.lower() in c.lower():
            col = c
            break
    if not col:
        print(f"❌ Column '{column_name}' not found in {board_name}")
        return
    cards = board["columns"][col]
    print(f"[{col}] ({len(cards)} cards):")
    for card in cards:
        print(f"  {card}")

def count_done(board_name):
    board = parse_board(board_name)
    if not board:
        print(f"❌ Board '{board_name}' not found")
        return
    total = 0
    done = 0
    for col, cards in board["columns"].items():
        for card in cards:
            total += 1
            if card.startswith("- [x]") or card.startswith("- [X]"):
                done += 1
    print(f"{board_name}: {done}/{total} cards done ({int(done/total*100) if total else 0}%)")

def add_card(board_name, column_name, card_text):
    """Add a card to a column. Finds the best matching column by substring."""
    path = os.path.join(BOARDS_DIR, f"{board_name}.md")
    if not os.path.exists(path):
        print(f"❌ Board '{board_name}' not found")
        return False

    with open(path) as fh:
        content = fh.read()

    # Find the column header
    col_pattern = re.compile(r'^(##\s+.*' + re.escape(column_name) + r'.*)$', re.IGNORECASE | re.MULTILINE)
    match = col_pattern.search(content)
    if not match:
        # Try broader match
        col_pattern = re.compile(r'^(##\s+.*' + re.escape(column_name.split()[-1]) + r'.*)$', re.IGNORECASE | re.MULTILINE)
        match = col_pattern.search(content)
    if not match:
        print(f"❌ Column '{column_name}' not found")
        return False

    header_line = match.group(1)
    # Find the position after the header line and insert the card
    pos = content.index(header_line) + len(header_line)

    # Check if there's a JSON settings block after this column
    rest = content[pos:]
    # Find the next column or settings block
    next_col = re.search(r'\n##\s+', rest)
    json_block = re.search(r'\n```\n', rest)

    if next_col and json_block:
        insert_pos = pos + min(next_col.start(), json_block.start())
    elif next_col:
        insert_pos = pos + next_col.start()
    elif json_block:
        insert_pos = pos + json_block.start()
    else:
        insert_pos = len(content)

    card_line = f"\n- [ ] {card_text}"
    new_content = content[:insert_pos] + card_line + content[insert_pos:]

    with open(path, 'w') as fh:
        fh.write(new_content)
    print(f"✅ Added: - [ ] {card_text}")
    return True

def move_card(board_name, column_name, search_text):
    """Move a card to a different column by matching text."""
    path = os.path.join(BOARDS_DIR, f"{board_name}.md")
    if not os.path.exists(path):
        print(f"❌ Board '{board_name}' not found")
        return False

    with open(path) as fh:
        content = fh.read()

    # Find the card containing search_text
    lines = content.split('\n')
    target_idx = None
    target_line = None
    for i, line in enumerate(lines):
        if search_text.lower() in line.lower() and re.match(r'^- \[.\]\s+', line):
            target_idx = i
            target_line = line
            break

    if target_idx is None:
        print(f"❌ Card containing '{search_text}' not found")
        return False

    # Find the target column header position
    col_pattern = re.compile(r'^(##\s+.*' + re.escape(column_name) + r'.*)$', re.IGNORECASE | re.MULTILINE)
    col_match = col_pattern.search(content)
    if not col_match:
        print(f"❌ Column '{column_name}' not found")
        return False

    col_end = col_match.end()
    col_line_num = content[:col_end].count('\n')

    # Remove from current position
    lines.pop(target_idx)

    # Insert after target column header line
    if target_idx < col_line_num:
        col_line_num -= 1  # Adjusted for removal
    lines.insert(col_line_num + 1, target_line)

    with open(path, 'w') as fh:
        fh.write('\n'.join(lines))
    print(f"✅ Moved to [{column_name}]: {target_line.strip()}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "boards":
        print_boards()
    elif cmd in ("ls", "list", "show"):
        if len(sys.argv) < 3:
            print("Usage: kanban_bridge.py ls <board>")
            sys.exit(1)
        print_cards(sys.argv[2])
    elif cmd in ("cards", "col"):
        if len(sys.argv) < 4:
            print("Usage: kanban_bridge.py cards <board> <column>")
            sys.exit(1)
        print_column_cards(sys.argv[2], " ".join(sys.argv[3:]))
    elif cmd == "done":
        if len(sys.argv) < 3:
            print("Usage: kanban_bridge.py done <board>")
            sys.exit(1)
        count_done(sys.argv[2])
    elif cmd == "add":
        if len(sys.argv) < 5:
            print("Usage: kanban_bridge.py add <board> <column> <card text>")
            sys.exit(1)
        add_card(sys.argv[2], sys.argv[3], " ".join(sys.argv[4:]))
    elif cmd == "move":
        if len(sys.argv) < 5:
            print("Usage: kanban_bridge.py move <board> <column> <card text>")
            sys.exit(1)
        move_card(sys.argv[2], sys.argv[3], " ".join(sys.argv[4:]))
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)
