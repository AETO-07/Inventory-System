# Inventory Management System

A command-line inventory management system built with Python, object-oriented programming, JSON persistence, input validation, and exception handling.

## Overview

This project manages a collection of products and provides a command-line interface for adding, searching, updating, removing, and viewing inventory.

It was built as a practical Python project to apply object-oriented programming concepts to a real-world style problem while also working with persistent data and user input.

## Features

* Add products to the inventory
* View all stored products
* Search for products by name
* Prevent duplicate product names
* Remove products from the inventory
* Add stock to existing products
* Remove stock from existing products
* Calculate individual product stock value
* Calculate total inventory value
* Save inventory data to JSON
* Load previously saved inventory data
* Validate user input
* Handle invalid numeric input and file errors
* Confirm before exiting the application

## Technologies & Concepts

* Python
* Object-Oriented Programming (OOP)
* Classes and objects
* Methods and class methods
* Composition
* Encapsulation of product and inventory behavior
* JSON serialization and deserialization
* File handling
* `try` / `except` exception handling
* Input validation
* CLI application design
* Code refactoring

## Project Structure

```text
Inventory-System/
├── inventory-system.py
├── inventory.json        # Generated locally; ignored by Git
└── .gitignore
```

## How to Run

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/AETO-07/Inventory-System.git
cd Inventory-System
```

Run the application:

```bash
python inventory-system.py
```

The application will load an existing `inventory.json` file if one is available. Otherwise, it starts with an empty inventory.

## Usage

The application provides a menu with the following options:

```text
1. Add Product
2. View Products
3. Search Product
4. Remove Product
5. Add Stock
6. Remove Stock
7. Total Inventory Value
8. Save Inventory
9. Exit
```

Inventory changes can be saved to `inventory.json` using the **Save Inventory** option.

## Data Persistence

Product data is converted into dictionaries before being written to JSON.

When the application starts, the saved JSON data is converted back into `Product` objects using the `from_dict()` class method.

This allows the application to preserve inventory data between sessions.

## V2 Ideas

Potential improvements for a future version include:

* Graphical user interface (GUI)
* Better handling of product variants, such as different package sizes
* More flexible duplicate-product handling
* Automatic saving before exit
* Improved inventory filtering and sorting
* More advanced reporting
* Database persistence instead of JSON
* Additional automated tests
