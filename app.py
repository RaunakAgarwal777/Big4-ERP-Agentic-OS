# --- IMPORT NECESSARY TOOLS ---
import streamlit as st 
import pandas as pd 
import numpy as np 
import time 
from sklearn.linear_model import LinearRegression 
from typing import TypedDict, Annotated, Sequence 
import operator 
from langgraph.graph import StateGraph, START, END 
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage 

# --- MODULE 1: ERP CLEAN CORE & DATA PIPELINE ---
@st.cache_data 
def load_clean_core_data():
    raw_data = pd.DataFrame({
        'Transaction_ID': ['TX1', 'TX2', 'TX3', 'TX4', 'TX5', 'TX6'],
        'Month': [1, 2, 3, 4, 5, 6],
        'Product': ['Sugarcane Punch', 'Mango Smoothie', 'Sugarcane Punch', 'Mango Smoothie', 'Sugarcane Punch', 'Mango Smoothie'],
        'Revenue': [50000, 52000, 60000, 180000, 75000, 85000], 
        'Region': ['US', 'IN', 'US', 'EU', 'US', 'IN']
    })
    return raw_data

df = load_clean_core_data()

# --- MODULE 2: AI ANOMALY DETECTION ENGINE ---
def detect_anomalies(data):
    threshold = data['Revenue'].mean() * 1.8 
    anomalies = data[data['Revenue'] > threshold] 
    return anomalies

# --- MODULE 3: KPI FORECASTING ENGINE (MACHINE LEARNING) ---
def forecast_revenue(data):
    X = data[["Month"]] 
    y = data["Revenue"] 
    
    model = LinearRegression()
    model.fit(X, y)
    
    future_months = np.array([[7], [8], [9]])
    predictions = model.predict(future_months)
    return predictions

# --- MODULE 4: AI GOVERNANCE & RISK SCORING ---
def calculate_risk_score(query):
    risk_keywords = ["delete", "hack", "override", "bypass", "drop table"]
    score = 0
    for word in risk_keywords:
        if word in query.lower():
            score += 25
            
    if score >= 50: status = "HIGH RISK 🔴"
    elif score > 0: status = "MEDIUM RISK 🟡"
    else: status = "LOW RISK 🟢"
    
    return score, status

# --- MODULE 5: LANGGRAPH MULTI-AGENT OS ---
class EnterpriseState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    sender: str

def data_analyst_node(state: EnterpriseState):
    total = df['Revenue'].sum() 
    reply = f"📊 **Data Analyst:** Total global revenue sits at **${total:,.2f}**."
    return {"messages": [AIMessage(content=reply)], "sender": "Data_Analyst"}

def risk_auditor_node(state: EnterpriseState):
    reply = "🛡️ **Risk Auditor:** System compliant. All data localized to regional standards."
    return {"messages": [AIMessage(content=reply)], "sender": "Risk_Auditor"}

def finance_agent_node(state: EnterpriseState):
    revenue = df['Revenue'].sum()
    tax = revenue * 0.21 
    reply = f"💰 **Finance Agent:** Estimated enterprise tax exposure across all regions is **${tax:,.2f}**."
    return {"messages": [AIMessage(content=reply)], "sender": "Finance_Agent"}

def supply_chain_node(state: EnterpriseState):
    reply = "📦 **Supply Chain Agent:** Sugarcane Punch inventory is running low in the US sector. Restock advised."
    return {"messages": [AIMessage(content=reply)], "sender": "Supply_Chain"}

def supervisor_router(state: EnterpriseState):
    query = state["messages"][0].content.lower()
    
    if state.get("sender") in ["Data_Analyst", "Risk_Auditor", "Finance_Agent", "Supply_Chain"]:
        return END
        
    if "tax" in query or "margin" in query or "finance" in query: return "Finance_Agent"
    elif "inventory" in query or "stock" in query or "supply" in query: return "Supply_Chain"
    elif "risk" in query or "audit" in query: return "Risk_Auditor"
    else: return "Data_Analyst"

workflow = StateGraph(EnterpriseState) 
workflow.add_node("Data_Analyst", data_analyst_node) 
workflow.add_node("Risk_Auditor", risk_auditor_node) 
workflow.add_node("Finance_Agent", finance_agent_node)
workflow.add_node("Supply_Chain", supply_chain_node)

workflow.add_conditional_edges(START, supervisor_router) 
workflow.add_edge("Data_Analyst", END) 
workflow.add_edge("Risk_Auditor", END) 
workflow.add_edge("Finance_Agent", END)
workflow.add_edge("Supply_Chain", END)

agent_os = workflow.compile() 

# --- MODULE 6: THE STREAMLIT UI (CLIENT DASHBOARD) ---
st.set_page_config(page_title="AEGIS Control Tower", layout="wide") 

st.sidebar.title("🔐 Enterprise Identity")
user_role = st.sidebar.selectbox("Select Access Role", ["CIO (Full Access)", "CFO (Finance Only)", "Auditor (Risk Only)"])
st.sidebar.markdown("---")

st.title("🛡️ AEGIS Enterprise AI: Global Control Tower")

st.sidebar.subheader("☁️ S/4HANA Cloud Migration Status")
migration_status = {"Legacy Tables": 1200, "Migrated": 980}
completion = (migration_status["Migrated"] / migration_status["Legacy Tables"])
st.sidebar.progress(completion) 
st.sidebar.write(f"**{completion*100:.1f}% Complete**")

if user_role == "CIO (Full Access)" or user_role == "CFO (Finance Only)":
    col1, col2, col3 = st.columns(3)
    col1.metric("Consolidated Revenue", f"${df['Revenue'].sum():,.2f}")
    
    forecasts = forecast_revenue(df)
    col2.metric("Q3 Revenue Forecast", f"${forecasts.sum():,.2f}", "+14% Trend")
    col3.metric("Global Operations", f"{len(df)} Active Nodes")
    
    anomalies = detect_anomalies(df)
    if not anomalies.empty:
        st.error("🚨 **AI ALERT: Financial Anomalies Detected in Ledger**")
        st.dataframe(anomalies, use_container_width=True)

st.write("---")
st.subheader("🧠 AEGIS Multi-Agent Operating System")

user_query = st.chat_input("Interact with the AEGIS System (e.g., 'What is our tax exposure?', 'Check inventory')")

if user_query:
    with st.chat_message("user"):
        st.write(user_query) 
        
    with st.chat_message("assistant"):
        score, status = calculate_risk_score(user_query)
        
        if score >= 50:
            st.error(f"🚨 **GOVERNANCE BLOCK:** Prompt rejected. Risk Status: {status}")
        else:
            st.caption(f"Governance Check Passed. Risk: {status} (Score: {score}/100)")
            
            start_time = time.time() 
            
            initial_state = {"messages": [HumanMessage(content=user_query)], "sender": "User"}
            final_state = agent_os.invoke(initial_state) 
            
            end_time = time.time() 
            latency = round(end_time - start_time, 3)
            
            st.write(final_state["messages"][-1].content) 
            
            st.caption(f"⚙️ *System Observability: Routed by Supervisor to {final_state['sender']} | Latency: {latency}s*")
