
import random

MaxProcess = 5


def main_header():
    print("\n" + "CPU SCHEDULING".center(60))
    print("==============".center(60) + "\n")


def process_table(n, at, bt, pr):
    print("\nProcess   Creation_time   Burst_time   Priority")
    print("-------   ------------    ---------    --------")
    for i in range(n):
        print(f"P{i+1:<6}  {at[i]:<14}  {bt[i]:<9}   {pr[i]}")
    print("==================================================")


def fcfs(n, at, bt):
    print("\n" + "FCFS CPU Scheduling Algorithm".center(60))
    print("=========================================\n")

    start = [0] * n
    end = [0] * n
    wt = [0] * n

    current_time = 0
    for i in range(n):
        if current_time < at[i]:
            current_time = at[i]

        start[i] = current_time
        end[i] = start[i] + bt[i] - 1
        wt[i] = start[i] - at[i]
        current_time = end[i] + 1

    print("Gantt Chart:")
    print("|", end="")
    for i in range(n):
        print(f" P{i+1}({start[i]}-{end[i]})|", end="")
    print("\n")

    for i in range(n):
        print(f"Waiting time of P{i+1} = {wt[i]} ms")

    print(f"\nAverage Waiting Time = {sum(wt)/n:.1f} ms\n")


def round_robin(n, at, bt):
    print("\n" + "Round Robin CPU Scheduling Algorithm".center(60))
    print("==============================================\n")

    quantum = int(input("Enter Time Quantum: "))

    rem = bt.copy()
    completion = [0] * n
    time = min(at)
    finished = 0

    print("Gantt Chart:")
    print("|", end="")

    while finished < n:
        progressed = False

        for i in range(n):
            if rem[i] > 0 and at[i] <= time:
                progressed = True
                run = min(quantum, rem[i])
                rem[i] -= run
                print(f" P{i+1}({run})|", end="")
                time += run

                if rem[i] == 0:
                    completion[i] = time
                    finished += 1

        if not progressed:
            time += 1

    print("\n")

    print("Waiting Time:")
    wt = []
    for i in range(n):
        w = completion[i] - at[i] - bt[i]
        wt.append(w)
        print(f"P{i+1} = {w} ms")

    print(f"\nAverage Waiting Time = {sum(wt)/n:.1f} ms\n")


def main():
    while True:
        main_header()

        n = int(input(f"Input the number of process <max {MaxProcess}>: "))
        if n < 1 or n > MaxProcess:
            print("Invalid number of processes")
            return

        at = list(range(n))  # arrival times: 0,1,2,...
        bt = []
        pr = []

        for i in range(n):
            bt.append(int(input(f"Enter Burst time of P{i+1}: ")))
            pr.append(int(input(f"Enter Priority of P{i+1}: ")))

        process_table(n, at, bt, pr)

        print("\nCPU Scheduling Algorithms")
        print("1. FCFS")
        print("2. Round Robin")

        choice = int(input("Enter choice: "))

        if choice == 1:
            fcfs(n, at, bt)
        elif choice == 2:
            round_robin(n, at, bt)
        else:
            print("Invalid choice")

        if input("Press Y to continue or any key to exit: ").lower() != "y":
            break


if __name__ == "__main__":
    main()
