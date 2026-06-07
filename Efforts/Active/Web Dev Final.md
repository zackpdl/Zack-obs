




# **Step-by-Step Exam Deployment Notes**



## **1️⃣ Prepare Project Locally**

1. **Skeleton code**
    
    - Always start from the given skeleton code to avoid -60 marks penalty.
        
    - Copy it to your working folder:
        
    

```
cp -r /path/to/skeleton web-project02
cd web-project02
```

1.   
    
2. **Install dependencies**
    

```
npm install
```

2.   
    
3. **Configure .env**
    
    - Add MongoDB URI, JWT secrets, or any required credentials:
        
    

```
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/dbname
JWT_SECRET=yourSecret
```

3. -   
        
    - **Do not commit .env to GitHub**.
        
    
4. **Set Next.js basePath (if required for deployment)**
    

```
// next.config.js
const nextConfig = {
  basePath: '/final',
};
module.exports = nextConfig;
```

4.   
    
5. **Build Next.js**
    

```
npm run build
```

5.   
    
6. **Test locally**
    

```
npm run start -p 3003
curl http://localhost:3003/final
```

  

---

## **2️⃣ Push to GitHub**

1. **Create repository** (e.g., final-exam-webapp)
    
2. **Initialize git**
    

```
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-github-url>
git push -u origin main
```

2.   
    
3. Confirm the **publishing date** reflects your submission time.
    

---

## **3️⃣ Set Up Azure VM**

1. **Create VM** (Ubuntu recommended)
    
    - Open inbound ports for **HTTP (80)** and **HTTPS (443)** in the Networking tab.
        
    - Optional: open port 3003 for direct access.
        
    
2. **SSH into VM**
    

```
ssh azureuser@<vm-ip>
```

2.   
    
3. **Install dependencies**
    

```
sudo apt update
sudo apt install -y nodejs npm nginx git ufw
```

3.   
    
4. **Clone your repo**
    

```
git clone <your-github-url> /app/web-project02
cd /app/web-project02
npm install
npm run build
```

  

---

## **4️⃣ Run with PM2**

1. Install PM2 globally (if not yet installed)
    

```
npm install -g pm2
```

1.   
    
2. Start your app on **port 3003**
    

```
pm2 start "npm run start -- -p 3003" --name webproject02
pm2 save
pm2 logs webproject02
```

2.   
    
3. Verify:
    

```
curl http://localhost:3003/final
```

  

---

## **5️⃣ Configure Nginx**

1. Edit Nginx site config:
    

```
sudo nano /etc/nginx/sites-available/webproject02
```

1.   
    
2. Add proxy configuration:
    

```
server {
    listen 80;
    server_name <vm-ip>;

    location /final/ {
        proxy_pass http://localhost:3003/final/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

2.   
    
3. Enable and restart Nginx:
    

```
sudo ln -s /etc/nginx/sites-available/webproject02 /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

3.   
    
4. Test in browser:
    

```
http://<vm-ip>/final
```

  

---

## **6️⃣ Prepare Submission**

1. **API Design Doc** (Word file) – include:
    
    - Endpoints
        
    - Request/response examples
        
    - Mongoose schema diagrams
        
    
2. **GitHub repo URL** – make sure it’s public or accessible by instructors.
    
3. **Live Deployment URL**
    
    - Format: http://<vm-ip>/final
        
    
4. **Video Recording link**
    
    - Show your CRUD UI in action: create, read, update, delete.
        
    - Keep in separate Teams Assignment slot.
        
    
5. **.env file**
    
    - Do **not submit** credentials.
        
    - Mention you will change them after grading.
        
    

---

## **7️⃣ Quick Checklist Before Submission**

- Base path /final works on VM
    
- PM2 running app on port 3003
    
- Nginx proxy configured for /final
    
- All CRUD operations work in UI
    
- GitHub repo URL correct and commit date matches submission
    
- Video recording uploaded separately
    
- API Design doc completed
    

---

Make sure to add inbound rule with the corresponding port










---


### Exam runbook (step-by-step)

- Preparation
  - Ensure skeleton project is cloned and clean.
  - 
  - Create a new branch for the exam; push to GitHub early.

- API design doc (Word)
  - Define entities, fields, types, relations.
  - List endpoints for each entity: method, path, request/response shapes, status codes, error cases.
  - Note auth assumptions if any.
  - Include pagination/filtering if used.
  - Save as Word (.docx).

- Data models (Mongoose)
  - Create schemas per API doc; include required fields, types, enums, defaults, timestamps.
  - Validate structure aligns with your UI and API doc.

- Implement API routes
  - Build CRUD for each model in `app/api/*` with proper methods (GET/POST/PUT/DELETE).
  - Use a centralized Mongo connection (e.g., `lib/mongodb.js`).
  - Return consistent JSON and errors.

- Build the CRUD UI (Usability/Design/Data compliance)
  - List/table view with pagination/search (optional).
  - Create/edit form with validation and helpful messages.
  - Delete with confirm dialog.
  - Wire to API with fetch; show loading/error/success states.
  - Keep styles consistent and accessible.

- Environment and configuration
  - Create `.env` with:
    - `MONGODB_URI=...`
    - `NEXT_PUBLIC_BASE_PATH=/final` (or your required base path)
  - In `next.config.mjs`:
    - Set `basePath: '/final'`.
    - Set `env.NEXT_PUBLIC_BASE_PATH` to match.
  - Update client fetches to be basePath-safe (helper or absolute URLs).

- Local test
  - `npm install`
  - `npm run dev` → verify CRUD end-to-end.
  - `npm run build` → fix all errors.
  - `npm start` → test production build locally.

- Deployment (VM)
  - Copy `.env` to server (keep private).
  - Build on server or deploy built artifacts.
  - Start with PM2:
    - `pm2 start npm --name webproject02 -- start` or `PORT=3003 pm2 start npm --name webproject02 -- start`
    - `pm2 save`
  - Ensure only one process listens on your port (resolve EADDRINUSE if needed).

- Live link at [your-vm]/final
  - If using basePath `/final`, serve Next.js on any port and reverse-proxy:
    - Nginx location block:
      - `location /final/ { proxy_pass http://127.0.0.1:3003/final/; ... }`
  - Test:
    - Home, list views, create, update, delete, API endpoints directly.

- GitHub
  - Push all code, include README with:
    - Setup steps
    - Env variables
    - Build/run commands
    - Base path used
  - Confirm “No modification after submission” by noting the repo last push datetime.

- Video recording
  - Record: brief API doc overview, schemas, UI walkthrough of CRUD, and live app demo.
  - Upload and copy link.

- Submission package (to MS Teams)
  - API Design doc (.docx)
  - GitHub repository URL
  - Live deployment link: `http(s)://<your-vm>/final`
  - Video recording link
  - `.env` file (submit privately as requested; change credentials after grading)

- Self-QA against grading criteria
  - API Design doc: complete, consistent with implementation.
  - Mongoose schemas: match API/UI fields; required validations in place.
  - CRUD UI (for each entity):
    - Usability: clear actions, validation, messages.
    - Design: consistent layout, spacing, responsive.
    - Data model compliance: all fields present and mapped correctly.
  - Tech checks:
    - No build errors.
    - Env vars present on server (`MONGODB_URI`).
    - Base path works for links, fetches, images.
    - PM2 process stable; only one listener on target port.
  - Penalties avoidance:
    - Live site reachable and not blank.
    - Uses skeleton code.
    - GitHub repo accessible.

- Common pitfalls and quick fixes
  - Build fails on env: set `MONGODB_URI` in `.env` on server and locally.
  - Base path issues: ensure `next.config.mjs` basePath matches reverse proxy; use basePath-aware fetch helper.
  - Port conflict: stop extra processes (`pm2 ls`, `pm2 delete <id>`).
  - Unescaped apostrophes in JSX: replace with `&apos;`.
  - Exhaustive-deps warnings: not blocking; wrap functions in `useCallback` if you want to clean warnings.

- Commands reference
  - Install/build/start:
    - `npm install && npm run build && npm start`
  - PM2:
    - `pm2 start npm --name webproject02 -- start`
    - `pm2 restart webproject02 -- start -- -p 3003`
    - `pm2 ls && pm2 logs webproject02 --lines 100 && pm2 save`
  - Env:
    - `printf "MONGODB_URI=...\nNEXT_PUBLIC_BASE_PATH=/final\n" > .env`

- Final check
  - Visit `http(s)://<your-vm>/final` and perform all CRUD operations successfully before submitting.
  - Take screenshots/time-stamp if needed to prove no post-submission changes.