# --- IMPORT TOOLS ---
import streamlit as st 
import pandas as pd 
from typing import TypedDict, Annotated, Sequence 
import operator 
from langgraph.graph import StateGraph, START, END 
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage 

# --- PHASE 1: ERP CLEAN CORE MODERNIZATION (DATA PIPELINE) ---
@st.cache_data 
def load_clean_core_data():
    # 1. Create messy US data (USD)
    us_data = pd.DataFrame({
        'Transaction_ID': ['TX1', 'TX2', 'TX3'],
        'Product': ['Server Rack', 'Cloud Storage', 'Server Rack'],
        'Revenue': [50000, 12000, 45000],
        'Region': ['US', 'US', 'US']
    })
    
    # 2. Create messy India data (INR, different column names)
    india_data = pd.DataFrame({
        'Txn_No': ['IN1', 'IN2', 'IN3'],
        'Item_Name': ['Server Rack', 'Cloud Storage', 'Security Audit'],
        'Total_INR': [4200000, 840000, 1680000], 
        'Market': ['IND', 'IND', 'IND']
    })
    
    # 3. The "Clean Core" Transformation (Standardizing everything)
    clean_india = pd.DataFrame() 
    clean_india['Transaction_ID'] = india_data['Txn_No'] 
    clean_india['Product'] = india_data['Item_Name'] 
    clean_india['Revenue'] = india_data['Total_INR'] / 84.0 
    clean_india['Region'] = 'IN' 
    
    # 4. Merge them together into one global master database
    master_db = pd.concat([us_data, clean_india], ignore_index=True)
    return master_db

df = load_clean_core_data()

# --- PHASE 2: SIMULATED VECTOR DB & RAG (KNOWLEDGE BASE) ---
vector_db_mock = {
    "compliance": "Company Policy 402: All regional data must be stored in standardized USD formats. APAC region requires a 10% safety margin.",
    "tax": "Corporate Tax Protocol: US operations are taxed at 21%. India operations at 25%.",
    "erp": "Clean Core Strategy: No custom code is allowed in the SAP database layer."
}

# --- PHASE 3: ENTERPRISE GUARDRAILS (SECURITY) ---
def security_guardrail(user_text):
    forbidden_words = ["hack", "ignore instructions", "delete database", "drop table"]
    for word in forbidden_words:
        if word in user_text.lower():
            return False 
    return True 

# --- PHASE 4: LANGGRAPH MULTI-AGENT OS ---
class EnterpriseState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    sender: str

def data_analyst_node(state: EnterpriseState):
    total = df['Revenue'].sum() 
    reply = f"📊 **Data Analyst:** I queried the ERP Clean Core. Total consolidated revenue is **${total:,.2f} USD**."
    return {"messages": [AIMessage(content=reply)], "sender": "Data_Analyst"}

def risk_auditor_node(state: EnterpriseState):
    query = state["messages"][0].content.lower()
    
    retrieved_doc = "No specific policy retrieved."
    if "tax" in query: retrieved_doc = vector_db_mock["tax"]
    elif "compliance" in query or "policy" in query: retrieved_doc = vector_db_mock["compliance"]
    
    reply = f"🛡️ **Risk Auditor:** RAG Document Retrieved: '{retrieved_doc}'. All systems are compliant."
    return {"messages": [AIMessage(content=reply)], "sender": "Risk_Auditor"}

def supervisor_router(state: EnterpriseState):
    query = state["messages"][0].content.lower()
    
    if state.get("sender") in ["Data_Analyst", "Risk_Auditor"]:
        return END
        
    if "risk" in query or "tax" in query or "compliance" in query or "policy" in query:
        return "Risk_Auditor"
    else:
        return "Data_Analyst"

workflow = StateGraph(EnterpriseState) 
workflow.add_node("Data_Analyst", data_analyst_node) 
workflow.add_node("Risk_Auditor", risk_auditor_node) 
workflow.add_conditional_edges(START, supervisor_router) 
workflow.add_edge("Data_Analyst", END) 
workflow.add_edge("Risk_Auditor", END) 
agent_os = workflow.compile() 

# --- PHASE 5: THE STREAMLIT UI (CLIENT PRESENTATION) ---
st.set_page_config(page_title="Big 4 ERP Agentic OS", layout="wide") 

st.sidebar.title("System Controls")
view_mode = st.sidebar.radio("Select View Mode:", ["Global Overview", "Raw Data Audit"])
st.sidebar.markdown("---")
st.sidebar.markdown("**Active Modules:**\n✅ ERP Clean Core\n✅ VectorDB RAG\n✅ Guardrails")

st.title("🌐 Enterprise ERP Modernization & Agentic OS")

if view_mode == "Global Overview":
    col1, col2 = st.columns(2)
    col1.metric("Consolidated Revenue (USD)", f"${df['Revenue'].sum():,.2f}")
    col2.metric("Total Transactions", f"{len(df)} Records")
    st.bar_chart(df.groupby('Region')['Revenue'].sum()) 
else:
    st.subheader("Raw Master Database")
    st.dataframe(df, use_container_width=True)

st.write("---")
st.subheader("🤖 LangGraph AI Supervisor")

user_query = st.chat_input("Ask about 'revenue' or 'compliance policy'...")

if user_query:
    with st.chat_message("user"):
        st.write(user_query) 
        
    with st.chat_message("assistant"):
        if not security_guardrail(user_query):
            st.error("🚨 **GUARDRAIL TRIGGERED:** Prompt injection or unauthorized request detected. Action blocked.")
        else:
            st.write("*System: Request passed guardrails. Supervisor routing to specialist...*")
            initial_state = {"messages": [HumanMessage(content=user_query)], "sender": "User"}
            final_state = agent_os.invoke(initial_state) 
            st.write(final_state["messages"][-1].content)
