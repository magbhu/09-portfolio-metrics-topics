import streamlit as st
import json

# Load JSON from file
with open("topics-overview.json", encoding="utf-8") as f:
    data = json.load(f)

# Sidebar: Language selection
language = st.sidebar.selectbox("🌐 Select Language / மொழி / भाषा", ["English", "தமிழ்", "हिन्दी"])
lang_map = {"English": "en", "தமிழ்": "ta", "हिन्दी": "hi"}
lang = lang_map[language]

# Page title
st.title(data["title"][lang])

# Summary table
st.header("📊 Summary of Risk-Return Metrics")
summary_rows = []
for item in data["sections"]:
    summary_rows.append({
        "Metric": item["metric"],
        "Portfolio View": item["portfolio_view"][lang],
        "Stock View": item["stock_view"][lang]
    })

import pandas as pd
df = pd.DataFrame(summary_rows)
st.dataframe(df, use_container_width=True, hide_index=True)

# Detailed collapsibles
st.header("📖 Detailed Explanation")
for item in data["sections"]:
    with st.expander(f"📌 {item['metric']}"):
        st.markdown(f"**📁 Portfolio View**: {item['portfolio_view'][lang]}")
        st.markdown(f"**📈 Stock View**: {item['stock_view'][lang]}")

# Remarks section (you can connect dynamic logic here)
st.header("📝 Key Remarks & Use Cases")
st.markdown(
    f"""
    - Use **Beta** and **Sharpe Ratio** to filter high-risk underperformers.
    - Watch for **High Alpha + Low Downside Beta** stocks as stable outperformers.
    - Prefer **Low Correlation** for portfolio diversification.
    - Re-evaluate holdings where **R² is high** but volatility is excessive.
    """
)
