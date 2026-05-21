import streamlit as st
import pandas as pd
import plotly.express as px

# =============================
# PAGE SETTINGS
# =============================
st.set_page_config(page_title="Attrition Dashboard", layout="wide")

# =============================
# LOAD DATA
# =============================
df = pd.read_csv("Palo Alto Networks.csv")
df.columns = df.columns.str.strip()

# Convert Attrition if needed
if df["Attrition"].dtype == "object":
    df["Attrition"] = df["Attrition"].map({"Yes": 1, "No": 0})

# =============================
# SIDEBAR FILTERS
# =============================
st.sidebar.title("Filters")

department = st.sidebar.multiselect(
    "Select Department", df["Department"].unique()
)

jobrole = st.sidebar.multiselect(
    "Select Job Role", df["JobRole"].unique()
)

overtime = st.sidebar.selectbox(
    "OverTime", ["All", "Yes", "No"]
)

# Apply filters
filtered_df = df.copy()

if department:
    filtered_df = filtered_df[filtered_df["Department"].isin(department)]

if jobrole:
    filtered_df = filtered_df[filtered_df["JobRole"].isin(jobrole)]

if overtime != "All":
    filtered_df = filtered_df[filtered_df["OverTime"] == overtime]

# =============================
# TITLE
# =============================
st.title("📊 Workforce Attrition Dashboard")

# =============================
# KPIs
# =============================
col1, col2, col3 = st.columns(3)

col1.metric("Total Employees", len(filtered_df))

col2.metric(
    "Attrition Rate (%)",
    round(filtered_df["Attrition"].mean() * 100, 2)
)

col3.metric(
    "Active Employees",
    len(filtered_df) - filtered_df["Attrition"].sum()
)

# =============================
# DEPARTMENT ATTRITION
# =============================
st.subheader("Department-wise Attrition")

dept = filtered_df.groupby("Department")["Attrition"].mean().reset_index()
dept["Attrition %"] = dept["Attrition"] * 100

fig1 = px.bar(
    dept,
    x="Department",
    y="Attrition %",
    color="Attrition %",
    title="Attrition by Department"
)

st.plotly_chart(fig1, use_container_width=True)

# =============================
# JOB ROLE ATTRITION
# =============================
st.subheader("Job Role Attrition")

role = filtered_df.groupby("JobRole")["Attrition"].mean().reset_index()
role["Attrition %"] = role["Attrition"] * 100

fig2 = px.bar(
    role.sort_values(by="Attrition %", ascending=False).head(10),
    x="JobRole",
    y="Attrition %",
    color="Attrition %",
    title="Top 10 High Attrition Roles"
)

st.plotly_chart(fig2, use_container_width=True)

# =============================
# AGE DISTRIBUTION
# =============================
st.subheader("Age vs Attrition")

fig3 = px.histogram(
    filtered_df,
    x="Age",
    color="Attrition",
    title="Age Distribution"
)

st.plotly_chart(fig3, use_container_width=True)

# =============================
# OVERTIME IMPACT
# =============================
st.subheader("Overtime Impact")

ot = filtered_df.groupby("OverTime")["Attrition"].mean().reset_index()
ot["Attrition %"] = ot["Attrition"] * 100

fig4 = px.bar(
    ot,
    x="OverTime",
    y="Attrition %",
    color="Attrition %",
    title="Overtime vs Attrition"
)

st.plotly_chart(fig4, use_container_width=True)