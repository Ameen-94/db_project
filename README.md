# db_project
 
 
## Task 1: JSON-backed Database
 
**Objective**: Create a class (e.g. `LibraryDatabase` or `ContactList`) that stores records in memory and can **save/load** them as a **JSON file**.
 
---
 
### Requirements
 
1. **Record Structure**  
   - Use `namedtuple` from the `collections` module to define the structure of each record.  
   - Example: A `Book` with fields like `title`, `author`, and `year`.
 
2. **Enumerations**  
   - Use `Enum` from the `enum` module to define any **fixed categories**.  
   - Example: Book `Genre` or contact `Status`.
 
3. **Data Encapsulation**  
   - Store records in a **private** list or dictionary within the class.
 
4. **CRUD Operations**  
   - Implement methods for:  
     - **Create**  
     - **Read**  
     - **Update**  
     - **Delete**
 
5. **Input Validation & Processing**  
   - Use **control flow** (`if` / `else`) and **loops** to validate and process records.
 
6. **String Formatting**  
   - Use `f-strings` or `.format()` to neatly display information.
 
7. **Built-in Math Functions**  
   - Use the `math` module to compute values such as:  
     - Averages  
     - Totals  
     - Other statistics
 
8. **File and Directory Handling**  
   - Use the `os` module to:  
     - Handle file paths  
     - Ensure the storage directory exists  
     - Examples: `os.makedirs()`, `os.path.exists()`
 
9. **JSON I/O**  
   - **Saving**:  
     - Convert the record data to JSON format  
     - Use `json.dump()` to write to a file  
   - **Loading**:  
     - Use `json.load()` to read from a file  
     - Reconstruct records into the proper format
 
10. **Unicode Support**  
    - Ensure all data (including Arabic text) is stored and displayed correctly.  
    - JSON natively supports Unicode — no additional encoding is necessary.
