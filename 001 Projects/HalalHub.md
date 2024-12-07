### **Project Proposal: Halal Food Place Website**

#### **1. Project Title**

"Halal Finder: Connecting Users with Halal Food Establishments"

#### **2. Project Overview**

This project aims to develop a web-based platform where hosts can list their Halal-certified restaurants, and users can search, review, and rate these establishments. The website will also allow users to save their favorite places, making it easier for them to access their preferred options.

#### **3. Objectives**

- To create a centralized platform for Halal food seekers.
- To provide restaurant hosts with a user-friendly interface to list and manage their establishments.
- To implement a reliable database system for managing restaurant, user, and review data.
- To enable users to submit and read reviews for listed restaurants.

#### **4. Key Features**

- **For Users:**
    
    - Search for Halal food places by name, location, or cuisine.
    - Leave and view reviews and ratings for establishments.
    - Save favorite restaurants for easy access.
- **For Hosts:**
    
    - Register their restaurant with relevant details (e.g., Halal certification, menu, location).
    - Update restaurant details and manage user reviews.
- **Admin Panel:**
    
    - Manage restaurant listings and ensure compliance with Halal standards.
    - Monitor user activity and review content.

#### **5. Technical Requirements**

- **Frontend:** HTML5, CSS, JavaScript (React.js for dynamic UI).
- **Backend:** Node.js with Express for server-side development.
- **Database:** MongoDB for data storage, indexing, and queries.
- **Tools:**
    - Version Control: GitHub
    - Design: Figma for prototyping
    - Deployment: AWS or Heroku

#### **6. Database Design**

- **Entities:**
    
    - **Users:**`UserID`,`Name`,`Email`,`Password`,`Favorites`.
    - **Restaurants:**`RestaurantID`,`Name`,`Location`,`Cuisine`,`CertificationDetails`,`Rating`.
    - **Reviews:**`ReviewID`,`UserID`,`RestaurantID`,`Rating`,`Comment`,`Timestamp`.
    - **Admins:**`AdminID`,`Name`,`Email`,`Password`.
- **Relationships:**
    
    - Users and Reviews (1-to-Many).
    - Restaurants and Reviews (1-to-Many).

#### **7. Benefits of the Project**

- **To Users:** Access to verified Halal food places, contributing to community insights through reviews.
- **To Hosts:** A platform to reach the Halal food-seeking audience.
- **To Society:** Promotes transparency and accessibility in Halal certification.

#### **8. Timeline**

|Week|Task|
|---|---|
|1|Finalize project requirements & design|
|2-3|Develop database schema|
|4-5|Implement backend functionalities|
|6-7|Build frontend interface|
|8|Testing and deployment|
- Registration: `/host/register`
- Dashboard: `/host/dashboard`
- Admin login /admin/login
- User Revies n saveds = /profile
- For user to reivew n save = /restaurant/:id


```
// Public Routes
"/" - Home page with featured restaurants ✔️
"/auth" - User authentication (sign in/sign up) ✔️

// User Routes
"/restaurants" - List of all restaurants
"/restaurant/:id" - Individual restaurant details ✔️
"/profile" - User profile page ✔️


// Host (Restaurant Partner) Routes
"/host/login" - Restaurant partner login ✔️
"/host/register" - Restaurant registration ✔️
"/host/dashboard" - Restaurant management dashboard ✔️

"/host/menu"

// Admin Routes
"/admin/login" - Admin login ✔️
"/admin/dashboard" - Admin management dashboard ✔️
```