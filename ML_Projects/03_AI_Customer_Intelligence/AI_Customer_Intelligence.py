# ============================================================
# AI CUSTOMER INTELLIGENCE
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(page_title="AI SaaS Dashboard", layout="wide")

# ============================================================
# SIMPLE LOGIN SYSTEM (NO LIBRARY)
# ============================================================

USERS = {
    "Junaid": "admin123",
    "client": "client123"
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.user = username
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid credentials")

def logout():
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

# ============================================================
# DATA PROCESSING
# ============================================================

def preprocess(df):
    df = df.dropna()

    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
    df = df.dropna(subset=['InvoiceDate'])

    df['total_spent'] = df['Quantity'] * df['UnitPrice']

    customer_df = df.groupby('CustomerID').agg({
        'InvoiceNo': 'nunique',
        'total_spent': 'sum',
        'InvoiceDate': 'max'
    }).reset_index()

    customer_df.columns = ['CustomerID','num_orders','total_spent','last_order_date']

    today = df['InvoiceDate'].max()
    customer_df['days_since_last'] = (today - customer_df['last_order_date']).dt.days

    customer_df['message_length'] = np.random.randint(20, 200, len(customer_df))

    return customer_df

# ============================================================
# LABELS
# ============================================================

def create_labels(df):
    labels = []

    for i in range(len(df)):
        score = 0

        if df['total_spent'].iloc[i] > 2000: score += 3
        elif df['total_spent'].iloc[i] > 800: score += 1

        if df['num_orders'].iloc[i] > 20: score += 3
        elif df['num_orders'].iloc[i] > 10: score += 1

        if df['days_since_last'].iloc[i] < 30: score += 2
        elif df['days_since_last'].iloc[i] > 180: score -= 2

        if score >= 5:
            labels.append(2)
        elif score >= 2:
            labels.append(1)
        else:
            labels.append(0)

    df['customer_value'] = labels

    df['future_sales'] = (
        df['total_spent']*0.2 +
        df['num_orders']*10 -
        df['days_since_last']*0.4 +
        np.random.normal(0,30,len(df))
    ).clip(lower=0)

    return df

# ============================================================
# MODEL TRAINING
# ============================================================

def train(df):
    clf_scaler = StandardScaler()
    X_clf = clf_scaler.fit_transform(df[['num_orders','total_spent','days_since_last','message_length']])
    y_clf = df['customer_value']

    X_train, X_test, y_train, y_test = train_test_split(X_clf, y_clf, test_size=0.2, random_state=42)

    clf = LogisticRegression(max_iter=500) # create model
    clf.fit(X_train, y_train) # train model

    acc = accuracy_score(y_test, clf.predict(X_test))

    reg_scaler = StandardScaler()
    X_reg = reg_scaler.fit_transform(df[['num_orders','total_spent','days_since_last']])
    y_reg = df['future_sales']

    reg = LinearRegression()
    reg.fit(X_reg, y_reg)

    return clf, clf_scaler, reg, reg_scaler, acc

# ============================================================
# MAIN APP
# ============================================================

if not st.session_state.logged_in:
    login()

else:
    st.sidebar.write(f"👋 Welcome {st.session_state.user}")
    logout()

    st.title("🤖 AI Customer Intelligence Dashboard")

    uploaded_file = st.file_uploader("📂 Upload CSV", type=["csv"])

    if uploaded_file:

        try:
            df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')

            df = df.dropna()

            df = preprocess(df)
            df = create_labels(df)

            clf, clf_scaler, reg, reg_scaler, acc = train(df)

            df['segment'] = clf.predict(
                clf_scaler.transform(df[['num_orders','total_spent','days_since_last','message_length']])
            )

            df['predicted_sales'] = reg.predict(
                reg_scaler.transform(df[['num_orders','total_spent','days_since_last']])
            )

            label_map = {2:"High Value 🔥",1:"Medium ⚡",0:"Low 💤"}
            df['segment_label'] = df['segment'].map(label_map)

            # ====================================================
            # DASHBOARD
            # ====================================================

            st.success("✅ Analysis Complete")

            col1, col2, col3 = st.columns(3)
            col1.metric("Total Customers", len(df))
            col2.metric("High Value %", f"{(df['segment']==2).mean()*100:.1f}%")
            col3.metric("Accuracy", f"{acc*100:.1f}%")

            fig = px.pie(df, names='segment_label', title="Customer Segments")
            st.plotly_chart(fig, use_container_width=True)

            st.subheader("📊 processed Data Preview")
            st.dataframe(df)

            csv = df.to_csv(index=False).encode('utf-8')

            st.download_button(
                "📥 Download Results",
                csv,
                "results.csv"
            )

        except Exception as e:
            st.error("❌ Error processing file")
            st.text(str(e))

    else:
        st.info("⬆ Upload your CSV file to start analysis")