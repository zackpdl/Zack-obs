# Summarize Note

## Purpose
Turn one note into a concise, useful summary while preserving the original meaning.

## Inputs
- Note title
- Note content
- Optional goal for the summary

## Workflow
1. Identify the central idea.
2. Extract key points, decisions, facts, and open questions.
3. Remove repetition and filler.
4. Suggest related links only when obvious from context.
5. Keep the summary shorter than the original.

## Output Format
```markdown
## Summary

## Key Points
- 

## Open Questions
- 

## Suggested Links
- 
```

## Rules
- Do not invent facts.
- Do not overwrite nuance.
- Preserve action items if present.
- Use plain markdown only.

## Example
Input: A long note about Java classes.
Output: Summary of class/object concepts, key syntax, common mistakes, and links to related Java notes.
