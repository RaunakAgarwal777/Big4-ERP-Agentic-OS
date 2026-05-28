# ==============================================================================
# app.py — ENTERPRISE AGENTIC AI CONTROL TOWER
# Big 4 Style ERP Modernization + Multi-Agent AI Platform
# PART 1 / 2
# ==============================================================================

# ==============================================================================
# IMPORTS
# ==============================================================================
import streamlit as st
import pandas as pd
import numpy as np
import time
import operator

from typing import TypedDict, Annotated, Sequence

from sklearn.linear_model import LinearRegression

from langgraph.graph import StateGraph, START, END
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage

# ==============================================================================
# PAGE CONFIG
# ==============================================================================
st.set_page_config(
    page_title="Enterprise Agentic AI OS",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# ENTERPRISE UI STYLING
# ==============================================================================
st.markdown(
    """
    <style>

    .main {
        background-color: #0f172a;
        color: white;
    }

    .stMetric {
        background-color: #111827;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #1f2937;
    }

    h1, h2, h3 {
        color: #f8fafc;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ==============================================================================
# MODULE 1 — ERP CLEAN CORE MODERNIZATION
# ==============================================================================
@st.cache_data
def load_clean_core_data():

    # --------------------------------------------------------------------------
    # US ERP SYSTEM
    # --------------------------------------------------------------------------
    us_data = pd.DataFrame({
        "Transaction_ID": ["TX1", "TX2", "TX3", "TX4"],
        "Product": [
            "Server Rack",
            "Cloud Storage",
            "AI Suite",
            "Cyber Audit"
        ],
        "Revenue": [50000, 12000, 80000, 25000],
        "Region": ["US", "US", "US", "US"]
    })

    # --------------------------------------------------------------------------
    # INDIA ERP SYSTEM
    # --------------------------------------------------------------------------
    india_data = pd.DataFrame({
        "Txn_No": ["IN1", "IN2", "IN3", "IN4"],
        "Item_Name": [
            "Server Rack",
            "Cloud Storage",
            "Security Audit",
            "AI Migration"
        ],
        "Total_INR": [4200000, 840000, 1680000, 6200000],
        "Market": ["IND", "IND", "IND", "IND"]
    })

    # --------------------------------------------------------------------------
    # CLEAN CORE TRANSFORMATION
    # --------------------------------------------------------------------------
    clean_india = pd.DataFrame()

    clean_india["Transaction_ID"] = india_data["Txn_No"]
    clean_india["Product"] = india_data["Item_Name"]

    # INR → USD Standardization
    clean_india["Revenue"] = india_data["Total_INR"] / 84.0

    clean_india["Region"] = "IN"

    # --------------------------------------------------------------------------
    # GLOBAL MASTER DATABASE
    # --------------------------------------------------------------------------
    master_db = pd.concat(
        [us_data, clean_india],
        ignore_index=True
    )

    return master_db


# Load Enterprise Data
DF = load_clean_core_data()

# ==============================================================================
# MODULE 2 — ENTERPRISE VECTOR DB + RAG
# ==============================================================================
VECTOR_DB = {

    "compliance":
        """
        Company Policy 402:
        All regional ERP financial data must be stored in standardized
        USD reporting formats. APAC region requires a 10% safety margin.
        """,

    "tax":
        """
        Corporate Tax Protocol:
        US operations taxed at 21%.
        India operations taxed at 25%.
        """,

    "erp":
        """
        ERP Clean Core Strategy:
        No custom code is permitted within SAP database layers.
        """,

    "cyber":
        """
        Zero Trust Cybersecurity Policy:
        MFA mandatory for ERP admin accounts.
        """,

    "cloud":
        """
        Cloud Transformation Governance:
        All workloads require resiliency validation before migration.
        """
}

# ==============================================================================
# MODULE 3 — ENTERPRISE SECURITY GUARDRAILS
# ==============================================================================
def security_guardrail(user_text):

    forbidden_words = [
        "hack",
        "delete database",
        "drop table",
        "ignore instructions",
        "bypass security",
        "override governance"
    ]

    for word in forbidden_words:

        if word in user_text.lower():
            return False

    return True

# ==============================================================================
# MODULE 4 — AI GOVERNANCE RISK ENGINE
# ==============================================================================
def calculate_risk_score(query):

    risk_keywords = [
        "hack",
        "delete",
        "override",
        "drop",
        "bypass"
    ]

    score = 0

    for word in risk_keywords:

        if word in query.lower():
            score += 20

    if score >= 60:
        status = "HIGH RISK"

    elif score > 0:
        status = "MEDIUM RISK"

    else:
        status = "LOW RISK"

    return score, status

# ==============================================================================
# MODULE 5 — KPI FORECASTING ENGINE
# ==============================================================================
def forecast_revenue():

    monthly_data = pd.DataFrame({
        "Month": [1, 2, 3, 4, 5, 6],
        "Revenue": [80, 85, 90, 100, 110, 125]
    })

    X = monthly_data[["Month"]]
    y = monthly_data["Revenue"]

    model = LinearRegression()
    model.fit(X, y)

    future_months = np.array([[7], [8], [9], [10]])

    predictions = model.predict(future_months)

    forecast_df = pd.DataFrame({
        "Month": [7, 8, 9, 10],
        "Forecasted_Revenue": predictions
    })

    return forecast_df

# ==============================================================================
# MODULE 6 — ANOMALY DETECTION ENGINE
# ==============================================================================
def detect_anomalies(dataframe):

    threshold = dataframe["Revenue"].mean() * 1.8

    anomalies = dataframe[
        dataframe["Revenue"] > threshold
    ]

    return anomalies

# ==============================================================================
# MODULE 7 — CLOUD ERP MIGRATION TRACKER
# ==============================================================================
def cloud_migration_status():

    migration_data = {
        "Legacy ERP Tables": 2400,
        "Migrated": 1760,
        "Pending": 640
    }

    completion = (
        migration_data["Migrated"] /
        migration_data["Legacy ERP Tables"]
    ) * 100

    return migration_data, completion

# ==============================================================================
# MODULE 8 — OBSERVABILITY + AUDIT LOGGING
# ==============================================================================
AUDIT_LOG = []

def log_audit_event(user_query, latency, sender):

    AUDIT_LOG.append({

        "Query": user_query,

        "Latency": latency,

        "Agent": sender,

        "Timestamp": time.strftime("%H:%M:%S")
    })

# ==============================================================================
# MODULE 9 — ROLE BASED ACCESS CONTROL (RBAC)
# ==============================================================================
def role_permissions(role):

    permissions = {

        "CFO": [
            "Finance",
            "Forecasting",
            "Revenue"
        ],

        "Auditor": [
            "Compliance",
            "Risk",
            "Audit"
        ],

        "CIO": [
            "Cloud",
            "Cybersecurity",
            "ERP"
        ],

        "Analyst": [
            "Dashboards",
            "Analytics"
        ]
    }

    return permissions.get(role, [])

# ==============================================================================
# MODULE 10 — LANGGRAPH ENTERPRISE MULTI-AGENT OS
# ==============================================================================
class EnterpriseState(TypedDict):

    messages: Annotated[
        Sequence[BaseMessage],
        operator.add
    ]

    sender: str

# ==============================================================================
# AGENT 1 — DATA ANALYST
# ==============================================================================
def data_analyst_node(state: EnterpriseState):

    total_revenue = DF["Revenue"].sum()

    reply = (
        f"📊 DATA ANALYST:\n\n"
        f"Global consolidated ERP revenue is "
        f"${total_revenue:,.2f} USD."
    )

    return {
        "messages": [AIMessage(content=reply)],
        "sender": "Data_Analyst"
    }

# ==============================================================================
# AGENT 2 — RISK AUDITOR
# ==============================================================================
def risk_auditor_node(state: EnterpriseState):

    query = state["messages"][0].content.lower()

    retrieved_doc = "No matching compliance document found."

    if "tax" in query:
        retrieved_doc = VECTOR_DB["tax"]

    elif "policy" in query or "compliance" in query:
        retrieved_doc = VECTOR_DB["compliance"]

    elif "cyber" in query:
        retrieved_doc = VECTOR_DB["cyber"]

    reply = (
        f"🛡️ RISK AUDITOR:\n\n"
        f"RAG Policy Retrieved:\n\n"
        f"{retrieved_doc}"
    )

    return {
        "messages": [AIMessage(content=reply)],
        "sender": "Risk_Auditor"
    }

# ==============================================================================
# AGENT 3 — FINANCE AGENT
# ==============================================================================
def finance_agent_node(state: EnterpriseState):

    revenue = DF["Revenue"].sum()

    tax_exposure = revenue * 0.21

    reply = (
        f"💰 FINANCE AGENT:\n\n"
        f"Estimated enterprise tax exposure is "
        f"${tax_exposure:,.2f}."
    )

    return {
        "messages": [AIMessage(content=reply)],
        "sender": "Finance_Agent"
    }

# ==============================================================================
# AGENT 4 — CLOUD TRANSFORMATION AGENT
# ==============================================================================
def cloud_agent_node(state: EnterpriseState):

    migration_data, completion = cloud_migration_status()

    reply = (
        f"☁️ CLOUD TRANSFORMATION AGENT:\n\n"
        f"ERP cloud migration is "
        f"{completion:.1f}% complete."
    )

    return {
        "messages": [AIMessage(content=reply)],
        "sender": "Cloud_Agent"
    }

# ==============================================================================
# AGENT 5 — CYBERSECURITY AGENT
# ==============================================================================
def cybersecurity_agent_node(state: EnterpriseState):

    reply = (
        f"🔐 CYBERSECURITY AGENT:\n\n"
        f"Zero Trust posture active. "
        f"No critical vulnerabilities detected."
    )

    return {
        "messages": [AIMessage(content=reply)],
        "sender": "Cybersecurity_Agent"
    } 
# ==============================================================================
# SUPERVISOR ROUTER
# ==============================================================================
def supervisor_router(state: EnterpriseState):

    query = state["messages"][0].content.lower()

    # --------------------------------------------------------------------------
    # Prevent Infinite Loops
    # --------------------------------------------------------------------------
    if state.get("sender") in [
        "Data_Analyst",
        "Risk_Auditor",
        "Finance_Agent",
        "Cloud_Agent",
        "Cybersecurity_Agent"
    ]:
        return END

    # --------------------------------------------------------------------------
    # Intelligent Query Routing
    # --------------------------------------------------------------------------
    if any(
        word in query
        for word in [
            "tax",
            "risk",
            "compliance",
            "policy",
            "audit"
        ]
    ):
        return "Risk_Auditor"

    elif any(
        word in query
        for word in [
            "finance",
            "revenue",
            "profit",
            "forecast"
        ]
    ):
        return "Finance_Agent"

    elif any(
        word in query
        for word in [
            "cloud",
            "migration",
            "sap",
            "oracle"
        ]
    ):
        return "Cloud_Agent"

    elif any(
        word in query
        for word in [
            "cyber",
            "security",
            "threat",
            "vulnerability"
        ]
    ):
        return "Cybersecurity_Agent"

    else:
        return "Data_Analyst"

# ==============================================================================
# BUILD LANGGRAPH WORKFLOW
# ==============================================================================
workflow = StateGraph(EnterpriseState)

workflow.add_node(
    "Data_Analyst",
    data_analyst_node
)

workflow.add_node(
    "Risk_Auditor",
    risk_auditor_node
)

workflow.add_node(
    "Finance_Agent",
    finance_agent_node
)

workflow.add_node(
    "Cloud_Agent",
    cloud_agent_node
)

workflow.add_node(
    "Cybersecurity_Agent",
    cybersecurity_agent_node
)

workflow.add_conditional_edges(
    START,
    supervisor_router
)

workflow.add_edge("Data_Analyst", END)
workflow.add_edge("Risk_Auditor", END)
workflow.add_edge("Finance_Agent", END)
workflow.add_edge("Cloud_Agent", END)
workflow.add_edge("Cybersecurity_Agent", END)

# Compile Enterprise AI OS
AGENT_OS = workflow.compile()

# ==============================================================================
# SIDEBAR — ENTERPRISE CONTROL PANEL
# ==============================================================================
st.sidebar.title("🧠 Enterprise AI Control Tower")

# ------------------------------------------------------------------------------
# ROLE BASED ACCESS
# ------------------------------------------------------------------------------
role = st.sidebar.selectbox(
    "Select Enterprise Role",
    [
        "CFO",
        "Auditor",
        "CIO",
        "Analyst"
    ]
)

permissions = role_permissions(role)

st.sidebar.markdown("---")

st.sidebar.subheader("Active Permissions")

for permission in permissions:
    st.sidebar.success(permission)

# ------------------------------------------------------------------------------
# PLATFORM VIEW MODES
# ------------------------------------------------------------------------------
st.sidebar.markdown("---")

view_mode = st.sidebar.radio(
    "Platform View",
    [
        "Executive Dashboard",
        "ERP Audit Database",
        "Forecasting Engine",
        "Migration Control Tower",
        "Observability Center"
    ]
)

# ==============================================================================
# MAIN TITLE
# ==============================================================================
st.title("🌐 Enterprise Agentic AI Transformation Platform")

st.caption(
    "Big 4 Style ERP Modernization + Multi-Agent Intelligence + AI Governance"
)

# ==============================================================================
# EXECUTIVE DASHBOARD
# ==============================================================================
if view_mode == "Executive Dashboard":

    total_revenue = DF["Revenue"].sum()

    anomalies = detect_anomalies(DF)

    # --------------------------------------------------------------------------
    # KPI ROW
    # --------------------------------------------------------------------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Global Revenue",
        f"${total_revenue:,.0f}"
    )

    col2.metric(
        "ERP Transactions",
        len(DF)
    )

    col3.metric(
        "AI Agents",
        "5 Active"
    )

    col4.metric(
        "Anomalies",
        len(anomalies)
    )

    st.markdown("---")

    # --------------------------------------------------------------------------
    # REVENUE DISTRIBUTION
    # --------------------------------------------------------------------------
    st.subheader("Regional Revenue Distribution")

    regional_chart = (
        DF.groupby("Region")["Revenue"]
        .sum()
    )

    st.bar_chart(regional_chart)

    # --------------------------------------------------------------------------
    # PRODUCT ANALYTICS
    # --------------------------------------------------------------------------
    st.subheader("Revenue by Product")

    product_chart = (
        DF.groupby("Product")["Revenue"]
        .sum()
    )

    st.line_chart(product_chart)

# ==============================================================================
# ERP AUDIT DATABASE
# ==============================================================================
elif view_mode == "ERP Audit Database":

    st.subheader("📂 ERP Clean Core Master Database")

    st.dataframe(
        DF,
        use_container_width=True
    )

    anomalies = detect_anomalies(DF)

    if not anomalies.empty:

        st.error("🚨 Financial anomalies detected")

        st.dataframe(
            anomalies,
            use_container_width=True
        )

# ==============================================================================
# FORECASTING ENGINE
# ==============================================================================
elif view_mode == "Forecasting Engine":

    st.subheader("📈 AI Forecasting Engine")

    forecast_df = forecast_revenue()

    st.dataframe(
        forecast_df,
        use_container_width=True
    )

    st.line_chart(
        forecast_df.set_index("Month")
    )

# ==============================================================================
# CLOUD MIGRATION CONTROL TOWER
# ==============================================================================
elif view_mode == "Migration Control Tower":

    st.subheader("☁️ ERP Cloud Transformation Tracker")

    migration_data, completion = cloud_migration_status()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Legacy Tables",
        migration_data["Legacy ERP Tables"]
    )

    col2.metric(
        "Migrated",
        migration_data["Migrated"]
    )

    col3.metric(
        "Pending",
        migration_data["Pending"]
    )

    st.progress(completion / 100)

    st.success(
        f"Migration Completion: {completion:.1f}%"
    )

# ==============================================================================
# OBSERVABILITY CENTER
# ==============================================================================
elif view_mode == "Observability Center":

    st.subheader("📡 AI Observability & Audit Monitoring")

    if len(AUDIT_LOG) == 0:

        st.info("No audit events captured yet.")

    else:

        audit_df = pd.DataFrame(AUDIT_LOG)

        st.dataframe(
            audit_df,
            use_container_width=True
        )

# ==============================================================================
# ENTERPRISE MULTI AGENT CHAT INTERFACE
# ==============================================================================
st.markdown("---")

st.subheader("🤖 Enterprise Multi-Agent AI Supervisor")

user_query = st.chat_input(
    "Ask about revenue, compliance, cloud migration, tax, cyber risk..."
)

# ==============================================================================
# CHAT EXECUTION PIPELINE
# ==============================================================================
if user_query:

    # --------------------------------------------------------------------------
    # USER MESSAGE
    # --------------------------------------------------------------------------
    with st.chat_message("user"):

        st.write(user_query)

    # --------------------------------------------------------------------------
    # ASSISTANT RESPONSE
    # --------------------------------------------------------------------------
    with st.chat_message("assistant"):

        # ----------------------------------------------------------------------
        # SECURITY GUARDRAIL
        # ----------------------------------------------------------------------
        if not security_guardrail(user_query):

            st.error(
                "🚨 GUARDRAIL TRIGGERED: "
                "Unauthorized or malicious request blocked."
            )

        else:

            # ------------------------------------------------------------------
            # GOVERNANCE RISK SCORE
            # ------------------------------------------------------------------
            score, status = calculate_risk_score(user_query)

            risk_col1, risk_col2 = st.columns(2)

            risk_col1.metric(
                "AI Governance Risk Score",
                f"{score}%"
            )

            risk_col2.metric(
                "Risk Classification",
                status
            )

            st.write(
                "*System: Request passed governance guardrails.*"
            )

            # ------------------------------------------------------------------
            # OBSERVABILITY TIMER
            # ------------------------------------------------------------------
            start_time = time.time()

            # ------------------------------------------------------------------
            # LANGGRAPH INVOCATION
            # ------------------------------------------------------------------
            initial_state = {
                "messages": [
                    HumanMessage(content=user_query)
                ],
                "sender": "User"
            }

            final_state = AGENT_OS.invoke(initial_state)

            end_time = time.time()

            latency = round(end_time - start_time, 2)

            # ------------------------------------------------------------------
            # AUDIT LOGGING
            # ------------------------------------------------------------------
            log_audit_event(
                user_query=user_query,
                latency=latency,
                sender=final_state["sender"]
            )

            # ------------------------------------------------------------------
            # OBSERVABILITY METRICS
            # ------------------------------------------------------------------
            obs_col1, obs_col2 = st.columns(2)

            obs_col1.metric(
                "Response Time",
                f"{latency}s"
            )

            obs_col2.metric(
                "Responding Agent",
                final_state["sender"]
            )

            # ------------------------------------------------------------------
            # FINAL AI RESPONSE
            # ------------------------------------------------------------------
            st.success("AI Supervisor Routing Complete")

            st.write(
                final_state["messages"][-1].content
            )

# ==============================================================================
# FOOTER
# ==============================================================================
st.markdown("---")

st.caption(
    "Enterprise Agentic AI Control Tower | "
    "ERP Modernization | Multi-Agent AI | "
    "AI Governance | Big 4 Transformation Platform"
)
