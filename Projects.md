### **Project 3**

**Due Date**: Monday, 3 March 2025  
**Team Size**: Maximum 3 members  
**Marks**: 30 (10% of the course score)

---

### **Tasks to Complete**

1. **Repeat Module 10: Developing with Messaging Service**
    
    - Review and re-implement concepts from Module 10
    - Ensure correct integration with AWS services
2. **Create an "About" Page (`about.html`)**
    
    - Ensure accessibility at: `http://<your_s3_url>/about.html`
    - Display all team members with names, roles, and images
3. **Ensure Web App is Accessible via Root URL**
    
    - The main website must be accessible at: `http://<your_s3_url>/`
4. **Avoid Paid AWS Services**
    
    - Do not use CloudFront or any paid services
5. **Add Instructor (mchayapol@gmail.com) to VPC**
    
    - Assign appropriate IAM roles for observation
    - Provide necessary permissions (Read-Only)

---

### **Submission Requirements**

1. **URL of the Main Website**
    
    - Example: `http://your-s3-url/index.html`
2. **URL of the "About" Page**
    
    - Example: `http://your-s3-url/about.html`
3. **URL of the Inventory System App**
    
    - Example: `http://your-s3-url/inventory.html`
    - If not possible, add instructor (`mchayapol@gmail.com`) to VPC
4. **Login Details (if necessary)**
    
    - Provide credentials for AWS console (IAM) only if required




### **Project 2**

You will build a **Simple Employee CRUD App** with the following key components:

- **MySQL RDS Database** for employee data
- **AWS Lambda** functions for CRUD operations
- **Caching** to optimize query performance
- **Static Web App (S3)** with a simple UI
- **Security Group Configuration** to allow instructor access

---

## **Project Tasks and Requirements**

### **1. Set Up MySQL RDS**

- Create an **AWS RDS MySQL instance**
- Use the **Employee Sample Database** from [GitHub](https://github.com/datacharmer/test_db)
- Load the **large dataset** (`employees.sql`) into RDS
- **Expose RDS port 3306** (Security Group configuration) for instructor access

**Commands:**

bash

CopyEdit

`git clone https://github.com/datacharmer/test_db cd test_db mysql -h <hostname> -u root -p<password> < employees.sql`

### **2. Build a Static Webpage on S3**

- **Host the web app on AWS S3**
- **Ensure root access (`/`)**: `http://<your_s3_url>/`
- **Create an "About" Page (`about.html`)** accessible at:  
    `http://<your_s3_url>/about.html`
- First page **displays the result of the given query**

### **3. Implement CRUD Operations Using AWS Lambda**

- CRUD operations for **Employee table**
- May involve **salary, department, department-employee relations**
- **Can use any programming language**

### **4. Optimize Query Speed Using Cache**

- Prove that **caching improves query response time**
- Compare query performance **before and after cache**

#### **SQL Query to Display Top 10 Employees with High Salaries**



`SELECT e.emp_no, e.first_name, e.last_name, d.dept_name, MAX(s.salary) AS max_salary  FROM employees e  JOIN dept_emp de ON e.emp_no = de.emp_no  JOIN departments d ON de.dept_no = d.dept_no  JOIN (SELECT emp_no, salary FROM salaries WHERE to_date = '9999-01-01') s  ON e.emp_no = s.emp_no  WHERE s.salary > (SELECT AVG(salary) FROM salaries)  GROUP BY e.emp_no, e.first_name, e.last_name, d.dept_name  ORDER BY max_salary DESC  LIMIT 10;`

---

## **Submission Requirements**

1. **Video Presentation (Max 10 min)** demonstrating:
    
    - **Improved query speed with cache using ElastiCache**
    - **Working CRUD operations**
    - **MySQL connection to RDS**
2. **Source Code** of AWS Lambda functions
    
3. **Project URLs**
    
    - **Main Website**: `http://<your_s3_url>/`
    - **About Page**: `http://<your_s3_url>/about.html`
4. **Add Instructor (mchayapol@gmail.com) to VPC**
    
    - Provide **login details if necessary**