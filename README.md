# 🧼 Mall Customer Dataset - Data Cleaning & Preprocessing Project

This project is part of a 45-day internship task focused on **data cleaning and preprocessing** using Python and Pandas. The dataset used is the [Mall Customer Segmentation Data](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python).

---

## 📁 Project Structure
Mall-Customer-Project/
├── original_data/
│ └── Mall_Customers.csv # Raw dataset
├── cleaned_data/
│ └── cleaned_mall_customers.csv # Cleaned output dataset
├── mall_cleaning_script.py # Python script for cleaning
└── README.md # Project info


---

## 🚀 Features of Cleaning Script

- ✅ Handled **missing values** using median/mean/forward fill
- ✅ Removed **duplicate records**
- ✅ Standardized **text formatting** (e.g., gender values)
- ✅ Renamed columns to snake_case format
- ✅ Converted columns to correct **data types** (`int`, `float`, `bool`)
- ✅ Added **feature engineering**:
  - `income_per_age`: Annual income divided by age
  - `high_spender`: Flag for customers with spending score > 50

---

## 🧪 Technologies Used

- Python 3.x
- Pandas

---

## 📝 How to Run

### 🖥️ Locally
1. Make sure you have Python and Pandas installed.
2. Place the dataset inside `original_data/` folder.
3. Run the script:
   ```bash
   python mall_cleaning_script.py


🌐 Google Colab
Open Google Colab

Upload the dataset and copy script code

Execute cells step-by-step

📊 Dataset Info
CustomerID: Unique ID

Gender

Age

Annual Income (k$)

Spending Score (1-100)


📦 Output
The cleaned dataset is saved as:

bash
Copy
Edit
cleaned_data/cleaned_mall_customers.csv

🙌 Acknowledgments
Dataset Source: Kaggle - Mall Customer Segmentation Data


