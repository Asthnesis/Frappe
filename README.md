# Library Management System (Frappe / ERPNext)

This is a simple Frappe-based Library Management System to demonstrate the following:

### Features
- **Books**: Allows a user to add books with rental fees and quantities
- **Members**: Track users and their outstanding amounts
-  **Transactions**: Issue/return books with automatic stock and debt tracking
-  **Payments**: Settle outstanding dues for continued borrowing
-  **Debt Limit**: Prevent issuing if projected debt exceeds set limit

###  How to Run
Clone this repo and follow [Frappe Docker Setup](https://github.com/frappe/frappe_docker) to run locally. Install the `library` app using:

# inside your container or dev env
bench get-app library https://github.com/Asthnesis/library.git

bench --site your-site install-app library


###  Screenshots
- Book
![Book Form View](image-2.png)
Create a book and set quantity and fee
![Book List View](image-1.png)
View all books and available quantity

- Member
![Creating a new member](image-3.png)

![Members List](image-11.png)
View all members and their outstanding amounts

- Issue or Return a book
![Select member name](image-12.png)

![Fill form details](image-13.png)
Fill form details
![Submit](image-14.png)
Submit the form

![View all transactions](image-15.png)
View transaction list

![qty](image-16.png)
Quantity reduces by 1 to 9

![Return](image-17.png)
Do a return

![quantity increase](image-18.png)
The quantity increments by 1 to 10

![outstanding amt](image-19.png)
Outstanding amount increases by 50

If the member tries to borrow a book that will exceed the fee by 500, a warning is given
![Fee above 500](image-20.png)


A member can clear dues using payment:
![Payment](image-21.png)

Outstanding amount is therefore reduced to 0 and they can borrow another book
![0 Outstanding amount](image-22.png)

###  Tech Stack
- Frappe v15.65.0
- ERPNext v15.58.2
- Python 3.10+

### License

mit
