

Build a full Nutrition Tracking page for the fitness app with:


IMPORTANT:
- NEVER hardcode API keys
- Use environment variables
- Follow CalorieNinjas official docs
- Use Supabase client properly

========================================
API INTEGRATIONS
========================================

1) CalorieNinjas API api key 
Endpoint:
GET https://api.calorieninjas.com/v1/nutrition?query=

Header:
X-Api-Key: process.env.CALORIE_NINJAS_KEY

2) Supabase
Use:
SUPABASE_URL=process.env.SUPABASE_URL
SUPABASE_ANON_KEY=process.env.SUPABASE_ANON_KEY

Use @supabase/supabase-js

========================================
FEATURES
========================================

1) Search Food
- Input: natural language (e.g. "2 eggs and rice")
- Backend calls CalorieNinjas
- Return items array

2) Save to Database
When user clicks "Add to Log":
Insert into Supabase table:

Table: daily_logs

Columns:
- id (uuid, primary key)
- name (text)
- calories (float)
- protein (float)
- carbs (float)
- fat (float)
- sugar (float)
- fiber (float)
- serving_size (float)
- log_date (date, default today)
- created_at (timestamp, default now())

3) Fetch Daily Logs
- GET /api/logs?date=YYYY-MM-DD
- Return logs for selected date

4) Delete Log
- DELETE /api/logs/:id

5) Dashboard Summary
Calculate:
- Total Calories
- Total Protein
- Total Carbs
- Total Fat

6) Graph
Use Recharts BarChart:
Display totals:
- Calories
- Protein
- Carbs
- Fat

Graph updates dynamically.

7) Date Selector
- User selects date
- Fetch logs for that date

========================================

BACKEND ROUTES
========================================

GET /api/nutrition?query=
GET /api/logs?date=
POST /api/logs
DELETE /api/logs/:id

Include:
- Proper async/await
- Error handling
- 400 for bad input
- 500 for server errors

========================================
SUPABASE SETUP
========================================

Provide:
- SQL to create daily_logs table
- Instructions to enable Row Level Security
- Example policy to allow public insert/select/delete

========================================
UI REQUIREMENTS
========================================

Clean minimal layout:
- Search at top
- Results section
- Daily log list
- Summary card
- Chart at bottom
- Responsive design

========================================

  
using supabase eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJpbmd3Y3dldm1udGFqbG5mZmhiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEyNzY4ODgsImV4cCI6MjA4Njg1Mjg4OH0.yCPhNmnJjR3lc62s_xXc8NUPfqjMrGyCMnyx8G8NYm0 = anon key 
ringwcwevmntajlnffhb = project ID 

calories ninja api key =  QtKzLpl8PXY0Ya4M2gfudw==QREnzBVimcpEaMIz






1) Due Dates

- Add a date picker
    
- Highlight overdue tasks in red
    

  

2) Priority Levels

- Low / Medium / High
    
- Show with colors or icons
    

  

3) Mark as Complete (with animation)

- Strike-through text
    
- Small fade or slide effect
    

  

4) Task Categories / Tags

Examples:

- Study
    
- Work
    
- Personal
    
- Gym

