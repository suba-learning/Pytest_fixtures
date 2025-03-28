# pytest_fixtures
Here’s a well-structured **`README.md`** for your API Testing with Pytest Fixtures repository:  

---

# 💰 API Testing with Pytest Fixtures - Fixer Currency Exchange API  

This repository contains API tests using **Python**, **Pytest**, and **Fixtures** to validate the functionality of the [Fixer API](https://fixer.io/documentation). The Fixer API provides real-time and historical exchange rate data for 170 world currencies.  

## 🔧 Technologies Used  
- **Python 3**  
- **Pytest**  
- **Requests**  
- **JSON Handling**  

## 📂 Project Structure  
```
├── test_fixer_api.py   # Contains the API tests using Pytest fixtures  
├── README.md           # Project documentation  
└── requirements.txt    # (Optional) Dependencies list  
```

## ✅ Test Cases Overview  

### 📌 Functional Tests  
1. **Get Currency Symbols**  
   - Fetches the list of available currency symbols.  
   - Verifies the success flag in the response.  

2. **Get Exchange Rate for Specific Currencies (EUR Base)**  
   - Fetches exchange rates for *USD, CAD, AUD* with EUR as the base currency.  

3. **Get Exchange Rate for Specific Currencies (INR Base)**  
   - Attempts to fetch exchange rates with INR as the base currency (Restricted in Free Plan).  

4. **Get Exchange Rate for a Single Currency**  
   - Fetches exchange rate for *INR* using *EUR* as the base currency.  

5. **Get Historical Currency Rate**  
   - Fetches exchange rates for a past date (e.g., `2013-12-24`).  

### ⚠️ Negative Test Cases  
6. **Fetch Historical Rate for an Old Date (<1999)**  
   - Attempts to fetch a rate before `1999-01-01` (Restricted by API).  

7. **Fetch Historical Rate for a Future Date**  
   - Attempts to fetch exchange rates for a future date (Expected failure).  

8. **Fetch Historical Rate with Incorrect Date Format**  
   - Uses an invalid date format and validates the error response.  

9. **Currency Conversion Endpoint**  
   - Tests the currency conversion feature (Restricted in Free Plan).  

## 🚀 How to Run the Tests  

### 1️⃣ Clone the Repository  
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2️⃣ (Optional) Create a Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```
If `requirements.txt` is not available, install manually:  
```bash
pip install pytest requests
```

### 4️⃣ Run the Tests  
```bash
pytest test_fixer_api.py -v
```

## 📌 Notes  
- A **valid Fixer API key** is required (replace `acc_key` with your own).  
- Free-tier API access is **limited** (certain endpoints may be restricted).  
- Pytest **fixtures** are used for parameter reuse.  

## 🔥 Future Enhancements  
- Implement **parameterized tests** for multiple currency combinations.  
- Integrate **schema validation** with `jsonschema`.  
- Replace print statements with proper **logging**.  
- Add **CI/CD integration** (e.g., GitHub Actions).  

## 🤝 Contributions  
Feel free to fork this repository, improve the test cases, and submit a PR!  
