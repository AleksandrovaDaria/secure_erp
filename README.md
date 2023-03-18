# Secure ERP
This is project from CodeCool. ERP software need for the administration of company daily operations.solution that is super secure: a short and clean codebase that works on local files, strictly on offline computers.

## What are you going to learn?
- Collaborate with team.
- Use modular design, MVC pattern.
- Search, filter, and transform data.
- Write clean code.
- Conform to requirements.

## TODO BEFOR PRESENTATION
- add csv and main function in CRM module
- add and implement additional functions instead of imported (forbidden)
  
# Tasks
## CRM module
Implement the CRM module with basic and special operations.
1. Once the CRM module is selected, choosing option 1 asks the user to type the name, email, and subscription status for a new customer. When the last field is filled in, a new customer is introduced with an random ID.

2. Once the CRM module is selected, choosing option 2 prints all the customers.

3. Once the CRM module is selected, choosing option 3 asks the user for the ID of a customer. If the ID belongs to an existing customer, the user enters new values for the name, email, and subscription status. When the last field is filled in, the customer fields are updated with the given values.

4. Once the CRM module is selected, choosing option 4 asks the user for the ID of a customer. If the ID belongs to an existing customer, the customer is deleted from the database.

5. (5) Get the emails of subscribed customers.


## Sales module
Implement the Sales module with basic and special operations.

1. (1-4) Provide basic CRUD operations.

2. (5) Get the transaction that made the biggest revenue.

3. (6) Get the product that made the biggest revenue altogether.

4. (7) Count the number of transactions between two dates.

5. (8) Sum the price of transactions between two dates.

## HR module
Implement the HR module with basic and special operations.

1. Provide basic CRUD operations.

2. (5) Return the names of the oldest and the youngest employees as a tuple.

3. (6) Return the average age of employees.

4. (7) Return the names of employees who have birthdays within two weeks from the input date.

5. (8) Return the number of employees who have at least the input clearance level.

6. (9) Return the number of employees per department in a dictionary (like {'dep1': 5, 'dep2': 11}).

## General requirements

- No external modules are used, except for those already in the files. (External = its code is not written inside your code repo.)

- Only model files import data_manager. Model files do not import the view at all.
