### **README: How to Run API Calls and Save Data**

This scripts retrieves data from the Louisville Metro Open Data API for various data sets and saves it as a CSV file. Follow the instructions below to run the API calls and store the data.

---

### **Prerequisites**

Ensure you have the following installed:

* Python 3.10. + 
* Required libraries (install via `pip`):


  ```bash
  pip install pandas requests
  ```

### **Running the Script**

**Note:** Only run this script if you do not already have the current data (example: `citations_20-23.csv`).



1. Navigate to the Project Directory: \
Open your terminal or command prompt and navigate to the folder where this script is located.

    Run the Script: \
      ```bash 
      python script_name.py
      ```

2. Replace `script_name.py` with the actual script file name.

3. **Data Storage:**
    * The script will create a `data` folder in the project directory (if it doesn't already exist).
    * Retrieved data will be saved in a file named `file_name.csv` within the `data` folder.

4. **Output Message:**
    * If the data is retrieved successfully, you’ll see: \
    Data saved to: `data/file_name.csv`
    * If no data is retrieved or an error occurs, the script will display an appropriate message. (If and error occurs please submit a Pull Request)

---


### **API Details**

The script queries data from the endpoints using batch requests:

- Batch size: **1000 records per request**
- Some calls have several end points and can take several minutes to run
- If no data is retrieved or an error occurs, the script will display an appropriate message.

---

### **Customizing the Script**

**Change Output Directory:** \
  - To change the folder where the CSV is saved, modify the `output_directory` variable in the script.

---

### Projects and Data Needed to run:

**Hours vs Tickets** 
- `salary_api.py`
- `citation_2023_api.py`

**Machine Learning**
- `salary_api.py`

**Salary Dashboard**
- `salary_api.py`