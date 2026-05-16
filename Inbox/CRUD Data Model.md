

---

### **1. Read All Customers**

|**Route**|**GET /api/customer**|
|---|---|
|**Payload (body)**|-|
|**Response**|[ { … }, { … }, … ]|
|**File**|/app/api/customer/route.js|
|**Test**|curl -X GET http://localhost:3000/api/customer|

---

### **2. Create New Customer**

|**Route**|**POST /api/customer**|
|---|---|
|**Payload (body)**|{ “name”: “John Doe”, “dateOfBirth”: “1990-05-15T00:00:00.000Z”, “memberNumber”: 1, “interests”: “movies, football” }|
|**Response**|{ “_id”: “…”, “name”: “John Doe”, “dateOfBirth”: “…”, “memberNumber”: 1, “interests”: “movies, football” }|
|**File**|/app/api/customer/route.js|
|**Test**|curl -X POST http://localhost:3000/api/customer -H “Content-Type: application/json” -d ‘{“name”:“John Doe”,“dateOfBirth”:“1990-05-15T00:00:00.000Z”,“memberNumber”:1,“interests”:“movies, football”}’|

---

### **3. Update Existing Customer**

|**Route**|**PUT /api/customer**|
|---|---|
|**Payload (body)**|{ “_id”: “507f1f77bcf86cd799439011”, “name”: “John Smith”, “dateOfBirth”: “1990-05-15T00:00:00.000Z”, “memberNumber”: 1, “interests”: “movies, football, gaming” }|
|**Response**|{ “_id”: “…”, “name”: “John Smith”, “dateOfBirth”: “…”, “memberNumber”: 1, “interests”: “movies, football, gaming” }|
|**File**|/app/api/customer/route.js|
|**Test**|curl -X PUT http://localhost:3000/api/customer -H “Content-Type: application/json” -d ‘{”_id”:“507f1f77bcf86cd799439011”,“name”:“John Smith”,“dateOfBirth”:“1990-05-15T00:00:00.000Z”,“memberNumber”:1,“interests”:“movies, football, gaming”}’|

---

### **4. Delete Customer**

|**Route**|**DELETE /api/customer**|
|---|---|
|**Payload (body)**|{ “_id”: “507f1f77bcf86cd799439011” }|
|**Response**|“Customer deleted successfully”|
|**File**|/app/api/customer/route.js|
|**Test**|curl -X DELETE http://localhost:3000/api/customer -H “Content-Type: application/json” -d ‘{”_id”:“507f1f77bcf86cd799439011”}’|

---

