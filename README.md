# Postman API Automation Portfolio

Automated API Testing using Postman on reqres.in

## Features Implemented
- **Authentication Chaining**: Login API se token nikal ke Get Users me use kiya
- **Response Validation**: Status code 200/201/204, total_pages, first_name check
- **Data Driven Testing**: forEach loop se saare users validate kiye
- **Headers**: x-api-key and Authorization Bearer token
- Full CRUD Operations: Create, Read, Update, Delete
- Header Validation: x-api-key authentication

## APIs Tested
1. POST /api/login - Token generation
2. GET /api/users?page=2 - Get all users with validation
3. PUT /api/users - Create user
4. DELETE /api/users/2 - Delete user
   
## How to Run
1. Download `My Collection.postman_collection.json`
2. Import in Postman
3. Add `x-api-key` in collection variables
4. Run with Collection Runner

## Tools Used
Postman | JavaScript
