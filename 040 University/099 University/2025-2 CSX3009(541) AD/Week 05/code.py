from collections import deque

# ---------- INPUT ----------
def input_processes():
    while True:
        n = int(input("Enter number of processes (max 5): "))
        if 1 <= n <= 5:
            break
        print("❌ Maximum allowed processes is 5. Try again.\n")

    processes = []
    print("\nEnter Burst Time and Priority:")
    for i in range(n):
        pid = f"P{i+1}"
        burst = int(input(f"Burst Time of {pid}: "))
        priority = int(input(f"Priority of {pid}: "))
        processes.append((pid, burst, priority))
        print()

    return processes


# ---------- FCFS ----------
def fcfs(processes):
    time = 0
    total_waiting = 0

    print("\n===== FCFS Scheduling =====")
    print("Process | Burst | Priority | Waiting (ms)")
    print("-" * 50)

    for pid, burst, priority in processes:
        waiting = time
        total_waiting += waiting
        time += burst

        print(f"{pid:^7} | {burst:^5} | {priority:^8} | {waiting:^12}")

    avg_waiting = total_waiting / len(processes)
    print("\nAverage Waiting Time =", avg_waiting, "ms")


# ---------- ROUND ROBIN ----------
def round_robin(processes, quantum):
    remaining = {p[0]: p[1] for p in processes}
    burst = {p[0]: p[1] for p in processes}

    queue = deque([p[0] for p in processes])
    completed = {}
    time = 0

    while queue:
        pid = queue.popleft()
        exec_time = min(quantum, remaining[pid])
        time += exec_time
        remaining[pid] -= exec_time

        if remaining[pid] > 0:
            queue.append(pid)
        else:
            completed[pid] = time

    print("\n===== Round Robin Scheduling =====")
    print("Process | Waiting Time (ms)")
    print("-" * 30)

    total_waiting = 0
    for pid, b, _ in processes:
        waiting = completed[pid] - b
        total_waiting += waiting
        print(f"{pid:^7} | {waiting:^15}")

    avg_waiting = total_waiting / len(processes)
    print("\nAverage Waiting Time =", avg_waiting, "ms")


# ---------- MAIN MENU ----------
def main():
    processes = input_processes()

    while True:
        print("\n===== CPU Scheduling Menu =====")
        print("1. FCFS Scheduling")
        print("2. Round Robin Scheduling")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            fcfs(processes)

        elif choice == "2":
            quantum = int(input("Enter Time Quantum: "))
            round_robin(processes, quantum)

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("❌ Invalid choice. Try again.\n")


# ---------- RUN ----------
main()
