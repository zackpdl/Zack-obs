# CSX3008 OS Quiz 2 Study Guide (Obsidian-ready)

## Fast Facts
- Exam scope: deadlocks, Banker/safety, memory management (binding, fragmentation, allocation), paging + page tables, page replacement, I/O models (programmed, interrupt, DMA) and system calls/interrupts basics.
- Timebox drills: 3 hours / 60 pts; practice under clock.

## Deadlock & Resource Allocation
- Definition: processes wait forever because each holds resources the others need.
- RAG reduction: if no node can be removed (all processes still waiting), deadlock exists; RAG limits—only models single-unit requests.
- Four conditions: mutual exclusion, hold & wait, no preemption, circular wait. Break any one to avoid deadlock.
- Banker’s/safety check: need = max - alloc; safe if there exists a full completion sequence. Unsafe ≠ deadlock but risky.

## Safety-Check Drill (Banker)
1. Compute `Need = Max - Allocation` per process.
2. Available = Total - sum(Allocation).
3. Find a process with Need ≤ Available; mark complete, add its Allocation back to Available.
4. Repeat. If all finish → safe; otherwise list processes that finished before halt (unsafe state).

## Memory Binding & Addressing
- Compile-time binding → static; run-time binding → dynamic; logical address comes from CPU; physical is after translation.
- Dynamic loading: routine loaded only when called.
- Base/limit protection: physical = base + logical; trap if logical ≥ limit. Example from solution: logical 0–1999, base 3000 → physical 3000–4999.

## Contiguous Allocation
- Fragmentation: external = many small holes; internal = wasted inside fixed blocks.
- Placement strategies: first-fit, best-fit (usually least leftover), worst-fit.
- Drill with holes 530/440/180/600/220 KB and jobs 160/570/450/390/190 KB; best-fit leaves smallest total hole in the provided solution.

## Paging Basics
- Page table rows = 2^(VA bits − offset bits). For 32-bit VA, 4 KB pages: 2^(32−12) = 2^20 rows.
- Page table entry: frame number + valid/invalid bit (page in memory?).
- Page fault path: trap → OS loads page into a free frame or performs replacement → update PTE → resume.

## VA→PA Translation Drill
- Split VA into page number + offset.
- If v/i = valid, PA = frame << offset_bits | offset.
- If invalid → page fault.
- Practice with given table mapping pages: 0→A, 1→7, 2→0, 3→B, E→8, F→C.

## Page Replacement
- Optimal: replace page not used for longest future time (benchmark only).
- FIFO: replace oldest in memory; suffers Belady’s anomaly.
- LRU: replace least recently used approximation of optimal.
- Reference string 213425125312513 with 3 frames (solution): Optimal 4 replacements; FIFO 9; LRU 9. Distinguish page fault vs replacement-triggered fault.

## I/O & Interrupts
- Programmed (polling): CPU waits/polls device.
- Interrupt-driven: CPU issues request, continues; device IRQ notifies completion/error.
- DMA: best for large transfers; controller issues DRQ, CPU sends DACK, bus is cycle-stolen, data moves device↔memory without CPU moves, signals done.
- System call: software interrupt from user → kernel. Device controller IRQ: hardware interrupt. Page fault: exception (not user-maskable interrupt).

## Quick Formulas
- Rows in page table = 2^(VA bits − offset bits).
- Physical addr (base/limit) = base + logical.
- Need = Max − Allocation; Available = Total − ΣAllocation.

## 4-Day Cram Plan
- Day 1: Deadlock theory + RAG reduction + 5 Banker safety drills (vary totals/needs).
- Day 2: Binding/base-limit + fragmentation + first/best/worst-fit exercises (at least 5 scenarios).
- Day 3: Paging math + VA→PA translations + implement a small page-table calculator; redo the quiz table questions.
- Day 4: Page replacement drill (optimal/FIFO/LRU) on 5 reference strings; I/O flows (programmed vs interrupt vs DMA) sketch signals.

## Practice Checklist (tick in Obsidian)
- [ ] Derive a safe sequence or prove unsafe for a new 5-process/4-resource snapshot.
- [ ] Redraw RAG and attempt reduction until stuck; state reason.
- [ ] Compute external fragmentation after first/best/worst fit for 5 jobs.
- [ ] Translate 5 virtual addresses given a custom page table; handle a page fault case.
- [ ] Run FIFO/LRU on a fresh reference string and count replacements.
- [ ] Write a 6-step DMA transfer narrative with signals (DRQ/DACK/bus).

## Exam-Day Reminders
- Draw tables cleanly: Need, Allocation, Available, Finish flags.
- Always state if “unsafe” vs “deadlock”; list which processes completed.
- For address questions: show split (page|offset) and decimal conversions.
- Note whether a fault caused replacement or used a free frame.
- For I/O figures, mention who drives the bus and how CPU is notified.
