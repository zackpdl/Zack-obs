# Create Meeting Note

## Purpose
Turn meeting context into a clear, time-bound note.

## Inputs
- Meeting title
- Date
- Participants
- Agenda or transcript
- Decisions and action items if known

## Workflow
1. Create a concise meeting title.
2. Capture context and participants.
3. Summarize discussion by topic.
4. Extract decisions.
5. Extract action items with owners and due dates when available.
6. Link to relevant Efforts or Atlas notes.

## Output Format
```markdown
# Meeting - Title

## Context

## Participants
- 

## Discussion
- 

## Decisions
- 

## Action Items
- [ ] Task - Owner - Due

## Related
- 
```

## Rules
- Store meeting notes in `Calendar/Meetings`.
- Do not turn meetings into permanent knowledge unless useful ideas should move to Atlas.
- Do not invent owners or deadlines.

## Example
Input: Transcript from a project sync.
Output: Meeting note with summary, decisions, action items, and project links.
