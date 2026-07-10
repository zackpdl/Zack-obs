# 🤖 Study with Hermes

> Hermes Agent helps you study by querying your vault, generating quizzes, and keeping you on track.

## Commands You Can Use

| Ask Hermes | What Happens |
|------------|-------------|
| *"Summarize my AI for Business notes"* | Reads and condenses course notes |
| *"Quiz me on Blockchain"* | Generates questions from your notes |
| *"What did I study this week?"* | Scans recent notes for a digest |
| *"Create a study guide for Ethics"* | Compiles a structured review doc |
| *"Explain [concept] from my notes"* | Answers based on your own materials |

## Daily Study Workflow

1. **Morning:** Open Obsidian → check Home.md for today's focus
2. **In class:** Take notes directly in the course folder
3. **After class:** Ask Hermes to summarize + generate quiz questions
4. **Weekly:** Export key notes → upload to NotebookLM for Audio Overview
5. **Exam prep:** NotebookLM generates study guides from all materials

## Integration with Calendar

Your courses are already in Google Calendar. Hermes can:
- Pull today's schedule and prepare relevant notes
- Send a daily study briefing
- Remind you of upcoming midterms/finals

## Cron Job Ideas

- `hermes cron create "daily 8am" --prompt "Review today's classes and prepare a study focus"`
- `hermes cron create "weekly fri 6pm" --prompt "Summarize this week's notes for NotebookLM export"`
