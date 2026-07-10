# Coding Workflow

## Purpose
Use AI as a coding collaborator while preserving understanding and control.

## Inputs
- Goal or bug
- Relevant files
- Constraints
- Current errors or tests

## Workflow
1. Clarify expected behavior.
2. Inspect relevant files before editing.
3. Identify the smallest safe change.
4. Implement with existing project patterns.
5. Run relevant checks when possible.
6. Summarize changed files and verification.

## Output Format
```markdown
## Goal

## Approach

## Changes
- 

## Verification
- 

## Remaining Risks
- 
```

## Rules
- Do not rewrite unrelated code.
- Do not hide uncertainty.
- Prefer simple, maintainable changes.
- Explain enough for the human to learn.

## Example
Input: Broken Java assignment code.
Output: Diagnosis, patch, test result, and explanation.
