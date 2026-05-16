import subprocess
import re
import os

def run_script_and_parse(script_name, input_file):
    try:
        command = f"python3 {script_name} < {input_file}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        output = result.stdout

        max_value_match = re.search(r"Maximum value in Knapsack = (\d+)", output)
        recursive_calls_match = re.search(r"Recursive calls = (\d+)", output)
        execution_time_match = re.search(r"Execution time: (\d+\.\d+)", output)

        max_value = int(max_value_match.group(1)) if max_value_match else "N/A"
        recursive_calls = int(recursive_calls_match.group(1)) if recursive_calls_match else "N/A"
        execution_time = float(execution_time_match.group(1)) if execution_time_match else "N/A"

        return max_value, recursive_calls, execution_time
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name} with {input_file}: {e}")
        print(f"Stderr: {e.stderr}")
        return "—", "—", "—"
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "—", "—", "—"

results = []
knapsack_files = [f"knapsacktests/knapsack{i}.in" for i in range(8)]

for i, input_file in enumerate(knapsack_files):
    print(f"Processing {input_file}...")
    knapsack_id = i
    
    # Run task1v1.py
    v1_max_value, v1_calls, v1_time = run_script_and_parse("task1v1.py", input_file)
    
    # Run task1v2.py
    v2_max_value, v2_calls, v2_time = run_script_and_parse("task1v2.py", input_file)
    
    # Run task1v3.py (Memoization)
    v3_max_value, v3_calls, v3_time = run_script_and_parse("task1v3.py", input_file)

    # The final answer should be consistent across all successful methods
    final_answer = v1_max_value if v1_max_value != "N/A" else \
                   v2_max_value if v2_max_value != "N/A" else \
                   v3_max_value if v3_max_value != "N/A" else "N/A"

    results.append({
        "id": knapsack_id,
        "v1_time": v1_time,
        "v1_calls": v1_calls,
        "v2_time": v2_time,
        "v2_calls": v2_calls,
        "v3_time": v3_time,
        "v3_calls": v3_calls,
        "final_answer": final_answer
    })

# Format results into a markdown table
table_header = """| Knapsack ID | **Brute Force (1-State)** |            | **Brute Force (2-State)** |            | **Memoization** |            | Final Answer |
| ----------- | ------------------------- | ---------- | ------------------------- | ---------- | --------------- | ---------- | ------------ |
|             | Time (s)                  | Calls      | Time (s)                  | Calls      | Time (s)        | Calls      |              |"""

table_rows = []
for row_data in results:
    table_rows.append(
        f"| **{row_data['id']}**       | {row_data['v1_time']:.6f}                  | {row_data['v1_calls']:,}         | {row_data['v2_time']:.6f}                  | {row_data['v2_calls']:,}         | {row_data['v3_time']:.6f}        | {row_data['v3_calls']:,}         | {row_data['final_answer']:,}           |"
    )

# Handle cases where values are "—"
formatted_rows = []
for row_data in results:
    v1_time_str = f"{row_data['v1_time']:.6f}" if isinstance(row_data['v1_time'], float) else "—"
    v1_calls_str = f"{row_data['v1_calls']:,}" if isinstance(row_data['v1_calls'], int) else "—"
    v2_time_str = f"{row_data['v2_time']:.6f}" if isinstance(row_data['v2_time'], float) else "—"
    v2_calls_str = f"{row_data['v2_calls']:,}" if isinstance(row_data['v2_calls'], int) else "—"
    v3_time_str = f"{row_data['v3_time']:.6f}" if isinstance(row_data['v3_time'], float) else "—"
    v3_calls_str = f"{row_data['v3_calls']:,}" if isinstance(row_data['v3_calls'], int) else "—"
    final_answer_str = f"{row_data['final_answer']:,}" if isinstance(row_data['final_answer'], int) else "—"

    formatted_rows.append(
        f"| **{row_data['id']}**       | {v1_time_str:<25} | {v1_calls_str:<10} | {v2_time_str:<25} | {v2_calls_str:<10} | {v3_time_str:<17} | {v3_calls_str:<10} | {final_answer_str:<12} |"
    )


full_table = table_header + "\n" + "\n".join(formatted_rows)

with open("knapsack_results.md", "w") as f:
    f.write(full_table)

print("Results saved to knapsack_results.md")
