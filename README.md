# Workforce Attrition Analysis – Palo Alto Networks (Data Analytics)

This project performs an end‑to‑end workforce attrition analysis for a Palo Alto Networks–style cybersecurity organization. It focuses on understanding **why** employees leave, **which** segments are at highest risk, and **how** data can support proactive retention strategies.

The work includes:
- Exploratory data analysis (EDA) on a structured HR dataset  
- A Streamlit dashboard for interactive analytics  
- A detailed report with insights and recommendations for HR and business leaders  

---

## 1. Project Overview

Modern cybersecurity companies depend on specialized talent, long ramp‑up cycles, and deep institutional knowledge. Employee attrition therefore has a **multiplicative impact** on productivity, incident response, and product delivery.

This project analyzes a dataset of **1,470 employees** with **31 attributes** covering:
- Demographics  
- Job roles and levels  
- Compensation metrics  
- Work environment factors (e.g., overtime, travel)  
- Satisfaction indicators  
- Tenure and career progression  

The goal is to move beyond basic HR reporting and identify **behavioral patterns** and **risk clusters** that drive employee exits.

---

## 2. Key Questions

The analysis is designed around core strategic HR questions:

- Which departments and job roles have the highest attrition?  
- Does overtime or workload intensity correlate with higher exit risk?  
- Are employees leaving due to career stagnation, compensation, or both?  
- At what tenure stage (0–2 years, mid‑career, senior) is attrition most likely?  
- How do demographic factors such as age relate to workforce stability?

---

## 3. Dataset Description

- **Records:** 1,470 employees  
- **Features:** 31 attributes  
- **Target variable:** `Attrition` (0 = Stayed, 1 = Left)

Main feature groups:

- **Demographic:** Age, Gender, Marital Status  
- **Job‑related:** Department, JobRole, JobLevel, JobInvolvement  
- **Compensation:** MonthlyIncome, PercentSalaryHike, StockOptionLevel  
- **Work environment:** OverTime, BusinessTravel, DistanceFromHome  
- **Satisfaction:** JobSatisfaction, EnvironmentSatisfaction, WorkLifeBalance  
- **Tenure & growth:** YearsAtCompany, YearsInCurrentRole, YearsWithCurrManager, promotion‑related fields  

---

## 4. Methodology

The analysis follows a simple, reproducible pipeline:

1. **Data cleaning and validation**  
   - Check for missing values and duplicates  
   - Standardize categorical labels and value ranges  

2. **Feature engineering**  
   - Create age groups (e.g., 18–25, 26–35, 36–45, 46–60)  
   - Create tenure buckets (early, mid, senior career stages)  
   - Encode `Attrition` as a binary variable  

3. **Exploratory data analysis (EDA)**  
   - Department‑wise, role‑wise, age‑wise, and tenure‑wise attrition patterns  
   - Overtime vs. attrition behavior  
   - Satisfaction and work‑life balance trends  

4. **Visualization and dashboarding**  
   - Static plots with Matplotlib / Seaborn  
   - Interactive Streamlit dashboard for HR stakeholders  

---

## 5. Core Insights

Some of the major findings from the analysis:

- **Overall attrition rate:** ~16.12% (around 1 in 6 employees leave)  
- **Department concentration:** Higher attrition in Sales and HR compared to other functions  
- **Workload and overtime:** Employees working overtime show a noticeably higher attrition probability  
- **Early tenure risk:** The first 0–2 years at the company are the most vulnerable retention period  
- **Age‑based mobility:** Younger employees display higher mobility and switching behavior  

These patterns suggest that attrition is **predictable** and closely related to workload, early‑career experience, and department‑level pressures.

---

## 6. Streamlit Dashboard

Live dashboard:  
*(replace this with your actual URL)*  

```text
https://attrition-analysis-q4zvy4urp5eft7tbmkrydc.streamlit.app/
```

Key dashboard modules:

- **Attrition Overview:**  
  - Overall attrition rate  
  - Retained vs. exited distribution  

- **Department & Role View:**  
  - Department‑wise and role‑wise attrition heatmaps  
  - High‑risk segments highlighted visually  

- **Demographic Explorer:**  
  - Filters for age, gender, and other demographics  

- **Tenure & Workload Analysis:**  
  - Attrition by tenure buckets  
  - Impact of overtime and business travel  

User controls:

- Department selector  
- Job role filter  
- Tenure range slider  
- Overtime and travel toggles  

---

## 7. How to Run Locally

### 7.1. Prerequisites

- Python 3.8+  
- pip (Python package manager)  

### 7.2. Clone the repository

```bash
git clone https://github.com/somyagra627-maker/Attrition-Analysis.git
cd Attrition-Analysis
```

### 7.3. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```

### 7.4. Install dependencies

```bash
pip install -r requirements.txt
```

### 7.5. Run the Streamlit app

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal (usually http://localhost:8501) in your browser.

---

## 8. Project Structure

Example structure (adapt to your repo):

```text
Attrition-Analysis/
├─ data/
│  └─ Palo_Alto_Networks.csv
├─ notebooks/
│  └─ eda_attrition.ipynb
├─ app.py
├─ requirements.txt
└─ README.md
```

- `data/` – HR dataset used for analysis  
- `notebooks/` – Jupyter notebooks for EDA and experimentation  
- `app.py` – Streamlit app entry point  
- `requirements.txt` – Python dependencies  

---

## 9. Business Interpretation

From a business perspective, the project highlights:

- The operational risk of losing early‑tenure and overtime‑burdened employees  
- Department‑specific pressure zones, especially in Sales and HR  
- The need for stronger onboarding, early engagement, and structured career visibility  
- The usefulness of overtime, tenure, and department signals as **early‑warning indicators** for attrition  

These insights can support more focused HR interventions and help leadership design data‑driven retention strategies.

---

## 10. References

- SHRM workforce analytics concepts  
- Public IBM HR attrition dataset studies  
- Research on people analytics in technology organizations  
- Pandas, Matplotlib, and Streamlit official documentation  
