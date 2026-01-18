
"""
Indian Banks Credit-to-Deposit Ratio Analysis Dashboard
Main Application File
Version 1.0.0
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

from config import (
    BRAND_NAME, PROJECT_TITLE, PROJECT_SUBTITLE, AUTHOR, EXPERIENCE, 
    LOCATION, YEAR, COLORS, PAGES, PSB_BANKS, PRIVATE_BANKS, SFB_BANKS,
    CD_RATIO_BENCHMARKS, SECTOR_AVERAGES, ANALYSIS_PERIOD
)
from data import generate_data
from styles import (
    get_custom_css, render_section_header, render_subsection_header,
    render_divider, render_info_box, render_warning_box, render_success_box,
    render_footer, render_cd_ratio_status
)

# ═══════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="Indian Banks CD Ratio Analysis",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════════════════════

st.markdown("""
<div style="background-color: #003366; color: #FFD700; padding: 20px 20px; border-radius: 0; margin: -16px -16px 25px -16px; text-align: center;">
    <h1 style="margin: 0 0 8px 0; font-size: 24px; font-weight: 700;">
        🏦 Indian Banking Insights - CD Ratio Analysis
    </h1>
    <h2 style="margin: 0 0 8px 0; font-size: 24px; font-weight: 700; color: #FFD700;">
        Credit-to-Deposit Ratio Trends & Banking Health Indicators
    </h2>
    <p style="margin: 0; font-size: 24px; font-weight: 700; color: #FFD700; letter-spacing: 0.5px;">
        Understanding Bank Lending Capacity & Deposit Utilization
    </p>
    <p style="margin: 10px 0 0 0; font-size: 14px; color: #B0B0B0;">
        [Data Period: Q1 FY24 - Q3 FY25 (7 Quarters) | 43 Major Indian Banks]
    </p>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# SIDEBAR NAVIGATION
# ═══════════════════════════════════════════════════════════════════════════

st.sidebar.markdown(f"# 🏦 {BRAND_NAME}")
st.sidebar.markdown("---")
st.sidebar.markdown(f"**{AUTHOR}**")
st.sidebar.markdown(f"*{EXPERIENCE}*")
st.sidebar.markdown("---")

# Navigation pages
pages_list = [
    "📚 About This Analysis",
    "🏦 Dashboard Overview",
    "📊 CD Ratio Trends",
    "🔍 Bank-wise Comparison",
    "🏛️ PSB Analysis",
    "🏢 Private Bank Analysis",
    "🏪 Small Finance Banks",
    "📈 CD Ratio Drivers",
    "💡 Investment Insights",
    "📋 Data Explorer",
    "🎓 Education",
]

page = st.sidebar.radio(
    "📍 Choose Analysis:",
    pages_list,
    key="main_nav"
)

# Convert page selection to index
page_index = pages_list.index(page) if page in pages_list else 0

st.sidebar.markdown("---")
st.sidebar.markdown(f"📍 {LOCATION} | {YEAR}")
st.sidebar.markdown("---")

# Social Links
st.sidebar.markdown("""
**Connect with me:**

[📧 LinkedIn](https://www.linkedin.com/in/trichyravis)  
[💻 GitHub](https://github.com/trichyravis)
""")

# ═══════════════════════════════════════════════════════════════════════════
# LOAD DATA
# ═══════════════════════════════════════════════════════════════════════════

@st.cache_data
def load_dashboard_data():
    return generate_data()

data = load_dashboard_data()

# ═══════════════════════════════════════════════════════════════════════════
# PAGE 0: ABOUT THIS ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════

if page_index == 0:
    render_section_header("📚 About This CD Ratio Analysis")
    
    st.markdown("""
    **Indian Banking Sector Credit-to-Deposit (CD) Ratio Analysis**
    
    A comprehensive research dashboard analyzing the CD ratio trends across Indian banks,
    tracking lending capacity, deposit utilization, and banking sector health indicators.
    """)
    
    render_divider()
    
    render_subsection_header("🎯 Research Objective")
    
    render_info_box(
        "**Understanding Bank Lending Capacity**\n\n"
        "This analysis investigates the Credit-to-Deposit (CD) ratios across Indian banking sector "
        "to understand how effectively banks are deploying customer deposits into loans and advances. "
        "By tracking CD ratios by bank type (PSB, Private, SFB), we identify growth patterns, risk indicators, "
        "and investment implications."
    )
    
    render_divider()
    
    render_subsection_header("❓ Key Research Questions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Primary Questions:**
        
        1. What are current CD ratios across major Indian banks?
        2. How do PSBs, Private Banks, and SFBs compare?
        3. Is CD ratio trending up or down?
        4. Which banks are aggressively lending?
        5. What's the sector average and outliers?
        """)
    
    with col2:
        st.markdown("""
        **Secondary Questions:**
        
        6. How has CD ratio evolved over quarters?
        7. Is deposit growth matching advance growth?
        8. What's the liquidity position of banks?
        9. Are there red flags in lending ratios?
        10. What are investment implications?
        """)
    
    render_divider()
    
    render_subsection_header("📊 CD Ratio Explained")
    
    render_success_box(
        "**CD Ratio = (Total Advances / Total Deposits) × 100**\n\n"
        "- **70-80%:** Healthy range - balanced growth & liquidity\n"
        "- **Below 70%:** Underutilized capacity - excess deposits\n"
        "- **Above 85%:** Aggressive lending - lower liquidity buffer\n"
        "- **Above 95%:** Critical - potential liquidity risk"
    )
    
    render_divider()
    
    render_subsection_header("📈 Analysis Coverage")
    
    st.markdown(f"""
    **Period:** {ANALYSIS_PERIOD}
    
    **Data Frequency:** Quarterly (Q1, Q2, Q3, Q4)
    - Q1 FY24, Q2 FY24, Q3 FY24, Q4 FY24
    - Q1 FY25, Q2 FY25, Q3 FY25
    - Total: 7 quarters of historical data
    
    **Banks Covered:** 43 major Indian banks (+54% expansion)
    
    **Bank Categories:**
    - **Public Sector Banks (PSBs):** 12 banks (10 original + 2 new)
    - **Private Sector Banks:** 10 banks
    - **Small Finance Banks (SFBs):** 8 banks
    - **Foreign Banks:** 8 banks (DBS, StanChart, HSBC, Citi, BoA, JPM, Deutsche, Barclays)
    - **Historical PSBs:** 5 banks (merged institutions for trend analysis)
    
    **Market Coverage:**
    - **Market Capitalization:** 98%+ of Indian banking sector
    - **Total Assets:** ₹50+ lakh crore
    - **Geographic Reach:** Pan-India + International operations
    
    **Business Segments Covered:**
    - Retail Banking
    - Corporate Banking
    - MSME Lending
    - Investment Banking
    - Microfinance
    
    This dashboard provides comprehensive CD ratio analysis across all major categories
    of Indian banks, enabling investors and analysts to track lending trends, liquidity
    management, and banking health indicators across diverse market segments.
    """)

# ═══════════════════════════════════════════════════════════════════════════
# PAGE 1: DASHBOARD OVERVIEW
# ═══════════════════════════════════════════════════════════════════════════

elif page_index == 1:
    render_section_header("🏦 Dashboard Overview - Banking Sector CD Ratio Summary")
    
    st.markdown("""
    **Real-time summary of CD ratios across Indian banking sector**
    """)
    
    render_divider()
    
    # Key metrics
    render_subsection_header("📊 Key Sector Metrics")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            label="Total Banks",
            value=data["metrics"]["total_banks"],
            delta="28 Major Banks"
        )
    
    with col2:
        st.metric(
            label="Sector Avg CD",
            value=f"{data['metrics']['sector_avg_cd']:.2f}%",
            delta="Healthy Range"
        )
    
    with col3:
        st.metric(
            label="Sector Median CD",
            value=f"{data['metrics']['sector_median_cd']:.2f}%",
            delta="Central Tendency"
        )
    
    with col4:
        st.metric(
            label="Highest CD Bank",
            value=data["metrics"]["highest_cd_bank"][:15],
            delta="Most Aggressive"
        )
    
    with col5:
        st.metric(
            label="Lowest CD Bank",
            value=data["metrics"]["lowest_cd_bank"][:15],
            delta="Most Conservative"
        )
    
    render_divider()
    
    # Sector summary
    render_subsection_header("🏛️ CD Ratio by Bank Type")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        render_success_box(
            f"**Public Sector Banks (PSBs)**\n\n"
            f"Count: {data['sector_summary']['PSB']['count']}\n"
            f"Avg CD: {data['sector_summary']['PSB']['avg_cd']:.2f}%\n"
            f"Range: {data['sector_summary']['PSB']['min_cd']:.2f}% - {data['sector_summary']['PSB']['max_cd']:.2f}%"
        )
    
    with col2:
        render_info_box(
            f"**Private Banks**\n\n"
            f"Count: {data['sector_summary']['Private']['count']}\n"
            f"Avg CD: {data['sector_summary']['Private']['avg_cd']:.2f}%\n"
            f"Range: {data['sector_summary']['Private']['min_cd']:.2f}% - {data['sector_summary']['Private']['max_cd']:.2f}%"
        )
    
    with col3:
        render_warning_box(
            f"**Small Finance Banks (SFBs)**\n\n"
            f"Count: {data['sector_summary']['SFB']['count']}\n"
            f"Avg CD: {data['sector_summary']['SFB']['avg_cd']:.2f}%\n"
            f"Range: {data['sector_summary']['SFB']['min_cd']:.2f}% - {data['sector_summary']['SFB']['max_cd']:.2f}%"
        )
    
    render_divider()
    
    render_subsection_header("💡 Key Insights")
    
    st.markdown("""
    **Banking Sector CD Ratio Analysis:**
    
    - **PSBs:** Operating at 74.2% CD ratio on average - healthy balance of growth and liquidity
    - **Private Banks:** Slightly more aggressive at 74.8% - pursuing higher lending growth
    - **SFBs:** Highest CD ratio at 82.5% - typical for specialized micro-lending segment
    - **Sector Average:** 73.5% - within healthy 70-80% range
    
    **Investment Perspective:**
    Banks with CD ratio in 72-78% range are optimally positioned for growth without liquidity stress.
    """)

# ═══════════════════════════════════════════════════════════════════════════
# PAGE 2: CD RATIO TRENDS
# ═══════════════════════════════════════════════════════════════════════════

elif page_index == 2:
    render_section_header("📊 CD Ratio Trends Analysis")
    
    st.markdown("""
    **Track CD ratio evolution across quarters (FY2024-FY2025)**
    """)
    
    render_divider()
    
    # Select bank for trend analysis
    render_subsection_header("📈 Select Bank for Trend Analysis")
    
    selected_bank = st.selectbox(
        "Choose a bank:",
        options=data["banks"]["bank_name"].unique(),
        key="bank_selector"
    )
    
    # Get trend data for selected bank
    if selected_bank in data["cd_ratio_trends"]:
        trend_data = data["cd_ratio_trends"][selected_bank]
        
        # Create chart
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=trend_data["quarters"],
            y=trend_data["cd_ratios"],
            mode='lines+markers',
            name='CD Ratio %',
            line=dict(color=COLORS["primary_dark"], width=3),
            marker=dict(size=10)
        ))
        
        # Add benchmark line
        fig.add_hline(
            y=75,
            line_dash="dash",
            line_color="green",
            annotation_text="Healthy Range (70-80%)",
            annotation_position="right"
        )
        
        fig.update_layout(
            title=f"{selected_bank} - CD Ratio Quarterly Trend",
            xaxis_title="Quarter",
            yaxis_title="CD Ratio (%)",
            hovermode="x unified",
            height=500,
            template="plotly_white"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Summary statistics
        render_subsection_header("📊 Trend Summary")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Latest CD Ratio", f"{trend_data['cd_ratios'][-1]:.2f}%")
        
        with col2:
            st.metric("Q1 FY24", f"{trend_data['cd_ratios'][0]:.2f}%")
        
        with col3:
            change = trend_data['cd_ratios'][-1] - trend_data['cd_ratios'][0]
            st.metric("Change (7 Q)", f"{change:.2f}%", delta=f"{change:+.2f}%")
        
        with col4:
            avg_cd = sum(trend_data['cd_ratios']) / len(trend_data['cd_ratios'])
            st.metric("Average CD", f"{avg_cd:.2f}%")

# ═══════════════════════════════════════════════════════════════════════════
# PAGE 3: BANK-WISE COMPARISON
# ═══════════════════════════════════════════════════════════════════════════

elif page_index == 3:
    render_section_header("🔍 Bank-wise CD Ratio Comparison")
    
    st.markdown("""
    **Compare CD ratios across all major Indian banks**
    """)
    
    render_divider()
    
    render_subsection_header("📊 Latest CD Ratios - All Banks")
    
    # Sort by latest CD ratio
    comparison_df = data["bank_wise_comparison"].sort_values("latest_cd", ascending=False)
    
    # Color code based on status
    comparison_df["Status"] = comparison_df["latest_cd"].apply(render_cd_ratio_status)
    
    st.dataframe(
        comparison_df[["bank_name", "bank_type", "latest_cd", "cd_change"]].rename(columns={
            "bank_name": "Bank Name",
            "bank_type": "Type",
            "latest_cd": "Latest CD %",
            "cd_change": "Change from Q2 %"
        }),
        use_container_width=True,
        hide_index=True
    )
    
    render_divider()
    
    render_subsection_header("📈 CD Ratio Distribution")
    
    # Create distribution chart
    fig = px.box(
        data["banks"],
        x="type",
        y="latest_cd",
        color="type",
        color_discrete_map={
            "PSB": COLORS["psb_color"],
            "Private": COLORS["private_color"],
            "SFB": COLORS["sfb_color"]
        },
        title="CD Ratio Distribution by Bank Type",
        labels={"type": "Bank Type", "latest_cd": "CD Ratio (%)"}
    )
    
    fig.update_layout(height=500, template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════
# PAGE 4-10: ADDITIONAL ANALYSIS PAGES
# ═══════════════════════════════════════════════════════════════════════════

elif page_index == 4:
    render_section_header("🏛️ PSB (Public Sector Banks) - CD Ratio Analysis")
    
    st.markdown("**Detailed analysis of PSBs CD ratios and trends**")
    
    render_divider()
    
    # Filter PSB data
    psb_df = data["banks"][data["banks"]["type"] == "PSB"].sort_values("latest_cd", ascending=False)
    
    render_subsection_header("📊 PSB CD Ratios (Sorted)")
    
    st.dataframe(
        psb_df[["bank_name", "latest_cd", "avg_cd", "deposits_cr", "advances_cr"]],
        use_container_width=True,
        hide_index=True
    )
    
    render_divider()
    
    render_subsection_header("📈 PSB CD Ratio Comparison")
    
    fig = px.bar(
        psb_df,
        x="bank_name",
        y="latest_cd",
        color="latest_cd",
        color_continuous_scale="Blues",
        title="Public Sector Banks - CD Ratio Comparison"
    )
    
    fig.update_layout(height=500, template="plotly_white", xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

elif page_index == 5:
    render_section_header("🏢 Private Banks - CD Ratio Analysis")
    
    st.markdown("**Detailed analysis of Private Banks CD ratios and trends**")
    
    render_divider()
    
    # Filter Private bank data
    private_df = data["banks"][data["banks"]["type"] == "Private"].sort_values("latest_cd", ascending=False)
    
    render_subsection_header("📊 Private Bank CD Ratios (Sorted)")
    
    st.dataframe(
        private_df[["bank_name", "latest_cd", "avg_cd", "deposits_cr", "advances_cr"]],
        use_container_width=True,
        hide_index=True
    )
    
    render_divider()
    
    render_subsection_header("📈 Private Bank CD Ratio Comparison")
    
    fig = px.bar(
        private_df,
        x="bank_name",
        y="latest_cd",
        color="latest_cd",
        color_continuous_scale="Greens",
        title="Private Banks - CD Ratio Comparison"
    )
    
    fig.update_layout(height=500, template="plotly_white", xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

elif page_index == 6:
    render_section_header("🏪 Small Finance Banks (SFBs) - CD Ratio Analysis")
    
    st.markdown("**Detailed analysis of SFBs CD ratios and trends**")
    
    render_divider()
    
    # Filter SFB data
    sfb_df = data["banks"][data["banks"]["type"] == "SFB"].sort_values("latest_cd", ascending=False)
    
    render_subsection_header("📊 SFB CD Ratios (Sorted)")
    
    st.dataframe(
        sfb_df[["bank_name", "latest_cd", "avg_cd", "deposits_cr", "advances_cr"]],
        use_container_width=True,
        hide_index=True
    )
    
    render_divider()
    
    render_subsection_header("📈 SFB CD Ratio Comparison")
    
    fig = px.bar(
        sfb_df,
        x="bank_name",
        y="latest_cd",
        color="latest_cd",
        color_continuous_scale="Oranges",
        title="Small Finance Banks - CD Ratio Comparison"
    )
    
    fig.update_layout(height=500, template="plotly_white", xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)


elif page_index == 7:
    render_section_header("📈 CD Ratio Drivers & Comprehensive Analysis")
    
    st.markdown("**What drives CD ratios and how to interpret changes**")
    
    render_divider()
    
    # ===== PART 1: KEY DRIVERS OVERVIEW =====
    render_subsection_header("🎯 Key Drivers of CD Ratio - Complete Framework")
    
    st.markdown("""
The CD ratio is driven by the **supply-demand dynamics** between loans (advances) and deposits. Understanding these drivers helps investors anticipate bank performance changes.

**Core Principle:**
```
CD Ratio = (Total Advances / Total Deposits) × 100
```

When advances grow faster than deposits → CD rises (growth phase)
When deposits grow faster than advances → CD falls (consolidation phase)
""")
    
    render_divider()
    
    # ===== PART 2: FACTORS INCREASING CD RATIO =====
    st.markdown("### 🟢 FACTORS THAT INCREASE CD RATIO")
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_success_box(
            "**Factors Increasing CD Ratio:**\n\n"
            "✅ Strong loan demand\n"
            "✅ Expanding credit business\n"
            "✅ Competitive pricing\n"
            "✅ Growing customer base\n"
            "✅ Retail & MSME focus"
        )
    
    with col2:
        st.markdown("""
#### **Why These Drive CD Higher:**
- Banks deploy deposits into loans
- Faster loan growth than deposit growth
- Economic expansion attracts borrowing
- Market competition forces pricing down
- Higher lending volumes increase advances
""")
    
    st.markdown("""
#### **Detailed Factor Analysis:**

**1️⃣ Strong Loan Demand** (Impact: 9/10)
- **What:** Customers actively seeking loans
- **Driven by:** Economic growth, low interest rates, business expansion
- **Effect on CD:** Advances grow 15-20% → CD rises
- **Example:** Post-COVID recovery (2020-2021) → CD rose from 78% to 84%
- **Bank Perspective:** Growth story, profitability opportunity
- **Investor Signal:** ✅ POSITIVE if deposits keep pace

**2️⃣ Expanding Credit Business** (Impact: 8/10)
- **What:** Bank actively growing loan portfolio
- **Driven by:** Market share strategy, new product launches, geographic expansion
- **Effect on CD:** Loan portfolio grows faster than deposits
- **Example:** Bank targets MSME lending → loan book grows 22% YoY
- **Bank Perspective:** Strategic growth initiative
- **Investor Signal:** ✅ POSITIVE for long-term growth

**3️⃣ Competitive Pricing** (Impact: 7/10)
- **What:** Bank cutting loan rates to win market share
- **Driven by:** Excess liquidity in system, RBI rate cuts, market wars
- **Effect on CD:** Lower rates attract more borrowers
- **Example:** Private banks competing for auto loans → prices fall 50 bps
- **Bank Perspective:** Growth at cost of NIM
- **Investor Signal:** ⚠️ CAUTION on profitability

**4️⃣ Growing Customer Base** (Impact: 8/10)
- **What:** Bank successfully acquiring new customers
- **Driven by:** Digital banking, branch expansion, partnerships
- **Effect on CD:** More customers = more loans + deposits, but loans grow faster
- **Example:** Fintech partnership adds 500K customers → loan book +18%
- **Bank Perspective:** Long-term franchise strength
- **Investor Signal:** ✅ POSITIVE indicator

**5️⃣ Retail & MSME Focus** (Impact: 8/10)
- **What:** Shift toward high-growth lending segments
- **Driven by:** Government incentives, profit margins, growth potential
- **Effect on CD:** Retail/MSME loans grow 25%+ while corporate grows 5%
- **Example:** Bank targets retail lending → CD rises from 75% to 80%
- **Bank Perspective:** Profitable growth, diversification
- **Investor Signal:** ✅ POSITIVE for sustainability

**6️⃣ Economic Growth** (Impact: 9/10)
- **What:** GDP expansion boosting credit demand
- **Driven by:** Industrial production, government spending, employment
- **Effect on CD:** Across-the-board increase in loan demand
- **Example:** GDP growth 8%+ → banking CD rises 2-3%
- **Bank Perspective:** Rising tide lifts all boats
- **Investor Signal:** ✅ STRONGLY POSITIVE

**7️⃣ Market Share Gains** (Impact: 7/10)
- **What:** Bank gaining share vs competitors
- **Driven by:** Service quality, pricing, customer experience
- **Effect on CD:** Loan growth outpacing system average
- **Example:** Bank's loan growth 18% vs industry 12% → CD rises
- **Bank Perspective:** Competitive advantage
- **Investor Signal:** ✅ POSITIVE
""")
    
    # Interactive chart for increasing factors
    st.markdown("#### 📊 Impact Strength of CD Increasing Factors")
    
    import plotly.graph_objects as go
    
    factors_inc = {
        'Strong Loan Demand': 9,
        'Economic Growth': 9,
        'Expanding Credit': 8,
        'Customer Growth': 8,
        'Retail/MSME Focus': 8,
        'Competitive Pricing': 7,
        'Market Share Gains': 7
    }
    
    fig_inc = go.Figure(data=[
        go.Bar(
            y=list(factors_inc.keys()),
            x=list(factors_inc.values()),
            orientation='h',
            marker=dict(color='#27AE60', opacity=0.8),
            text=list(factors_inc.values()),
            textposition='outside',
        )
    ])
    
    fig_inc.update_layout(
        title='Impact Strength on CD Ratio (Higher = Stronger Impact)',
        xaxis_title='Impact Strength (1-10)',
        yaxis_title='',
        height=400,
        showlegend=False,
        margin=dict(l=150, r=50, t=50, b=50),
        font=dict(size=11),
        xaxis=dict(range=[0, 10])
    )
    
    st.plotly_chart(fig_inc, use_container_width=True)
    
    render_divider()
    
    # ===== PART 3: FACTORS DECREASING CD RATIO =====
    st.markdown("### 🔴 FACTORS THAT DECREASE CD RATIO")
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_warning_box(
            "**Factors Decreasing CD Ratio:**\n\n"
            "⚠️ High loan delinquencies\n"
            "⚠️ Weak credit demand\n"
            "⚠️ High interest rates\n"
            "⚠️ Liquidity management\n"
            "⚠️ Regulatory constraints"
        )
    
    with col2:
        st.markdown("""
#### **Why These Drive CD Lower:**
- Banks reduce lending due to risks
- Deposits grow faster than loans
- Economic contraction kills demand
- Interest rate hikes deter borrowing
- Regulatory restrictions limit lending
""")
    
    st.markdown("""
#### **Detailed Factor Analysis:**

**1️⃣ High Loan Delinquencies** (Impact: 9/10)
- **What:** Many customers unable/unwilling to repay
- **Driven by:** Economic slowdown, unemployment, sectoral stress
- **Effect on CD:** Bank tightens lending → advances decline
- **Example:** COVID-19 → auto loan defaults surge → banks pause new lending
- **Bank Perspective:** Risk management priority
- **Investor Signal:** 🔴 VERY NEGATIVE for growth

**2️⃣ Weak Credit Demand** (Impact: 8/10)
- **What:** Customers/businesses reluctant to borrow
- **Driven by:** Recession, high rates, uncertainty, deleveraging
- **Effect on CD:** Loan growth stalls while deposits accumulate
- **Example:** Post-2008 crisis → credit demand fell 30%+ → CD collapsed
- **Bank Perspective:** Lost opportunity to deploy funds
- **Investor Signal:** 🔴 NEGATIVE - Growth headwind

**3️⃣ Rising Interest Rates** (Impact: 6/10)
- **What:** RBI/market rates increasing
- **Driven by:** Inflation control, monetary tightening, global factors
- **Effect on CD:** Higher borrowing costs reduce demand
- **Example:** RBI rate hikes 225 bps in 2022-23 → credit growth slowed
- **Bank Perspective:** Mixed (margins widen but volume falls)
- **Investor Signal:** ⚠️ MIXED - Watch profitability

**4️⃣ Liquidity Management** (Impact: 7/10)
- **What:** Bank deliberately keeping high deposits
- **Driven by:** Regulatory requirements (LCR), conservative stance, ALM
- **Effect on CD:** Deposits grow while lending stays moderate
- **Example:** Bank raises CASA deposits aggressively → CD falls 80% to 75%
- **Bank Perspective:** Balance sheet strengthening
- **Investor Signal:** ✅ POSITIVE if intentional

**5️⃣ Regulatory Constraints** (Impact: 7/10)
- **What:** RBI/regulators impose lending restrictions
- **Driven by:** Sectoral caps, concentration limits, prudence norms
- **Effect on CD:** Bank forced to reduce or redirect lending
- **Example:** RBI caps real estate at 15% → bank reduces RE lending
- **Bank Perspective:** Compliance necessity
- **Investor Signal:** ⚠️ NEUTRAL to NEGATIVE

**6️⃣ Recession/Economic Slowdown** (Impact: 8/10)
- **What:** GDP contraction, business failure
- **Driven by:** Macro shocks, demand collapse, layoffs
- **Effect on CD:** Loan demand falls, delinquencies rise, CD tumbles
- **Example:** 2008-09 crisis → credit demand fell 20%+ → CD fell significantly
- **Bank Perspective:** Survival mode
- **Investor Signal:** 🔴 VERY NEGATIVE

**7️⃣ Deleveraging Cycle** (Impact: 6/10)
- **What:** Households/corporates reducing debt levels
- **Driven by:** Balance sheet cleanup, risk aversion, forced sales
- **Effect on CD:** Prepayments rise, new lending falls, CD declines
- **Example:** Post-bubble collapse → customers pay off loans faster
- **Bank Perspective:** Lost growth opportunity
- **Investor Signal:** 🟡 CAUTION - Monitor for stabilization
""")
    
    # Interactive chart for decreasing factors
    st.markdown("#### 📊 Impact Strength of CD Decreasing Factors")
    
    factors_dec = {
        'High Delinquencies': 9,
        'Recession': 8,
        'Weak Demand': 8,
        'Regulatory Limits': 7,
        'Liquidity Mgmt': 7,
        'Rising Rates': 6,
        'Deleveraging': 6
    }
    
    fig_dec = go.Figure(data=[
        go.Bar(
            y=list(factors_dec.keys()),
            x=list(factors_dec.values()),
            orientation='h',
            marker=dict(color='#E74C3C', opacity=0.8),
            text=list(factors_dec.values()),
            textposition='outside',
        )
    ])
    
    fig_dec.update_layout(
        title='Impact Strength on CD Ratio (Higher = Stronger Impact)',
        xaxis_title='Impact Strength (1-10)',
        yaxis_title='',
        height=400,
        showlegend=False,
        margin=dict(l=150, r=50, t=50, b=50),
        font=dict(size=11),
        xaxis=dict(range=[0, 10])
    )
    
    st.plotly_chart(fig_dec, use_container_width=True)
    
    render_divider()
    
    # ===== PART 4: DRIVERS COMPARISON =====
    st.markdown("### ⚖️ Increasing vs Decreasing Drivers - Side-by-Side")
    
    comparison_data = {
        'Driver': [
            'Strong Loan Demand',
            'Weak Credit Demand',
            'Economic Growth',
            'Recession',
            'Expanding Credit',
            'Delinquencies',
            'Customer Growth',
            'Deleveraging',
            'Low Interest Rates',
            'High Interest Rates'
        ],
        'Effect': [
            'CD ↑↑',
            'CD ↓↓',
            'CD ↑',
            'CD ↓',
            'CD ↑',
            'CD ↓↓',
            'CD ↑',
            'CD ↓',
            'CD ↑',
            'CD ↓'
        ],
        'Timeline': [
            'Immediate (1-2 qtrs)',
            'Delayed (2-3 qtrs)',
            'Gradual (2-4 qtrs)',
            'Rapid (1-2 qtrs)',
            'Medium-term',
            'Immediate',
            'Gradual (6-12 m)',
            'Delayed (6+ m)',
            'Gradual (1-2 qtrs)',
            'Immediate'
        ],
        'Investor Signal': [
            '✅ BUY',
            '🔴 SELL',
            '✅ BUY',
            '🔴 SELL',
            '✅ BUY',
            '🔴 SELL',
            '✅ BUY',
            '🟡 MONITOR',
            '✅ BUY',
            '⚠️ CAUTION'
        ]
    }
    
    import pandas as pd
    comparison_df = pd.DataFrame(comparison_data)
    st.dataframe(comparison_df, use_container_width=True, hide_index=True)
    
    render_divider()
    
    # ===== PART 5: CD DRIVER COMBINATIONS =====
    st.markdown("### 🔄 CD Driver Combinations - Real-World Scenarios")
    
    st.markdown("""
#### **Scenario 1: Growth Phase (Multiple Increasing Drivers)**
```
Drivers Active:
✅ Strong Loan Demand (9/10) + Economic Growth (9/10)
✅ Growing Customer Base (8/10) + Retail Focus (8/10)
✅ Low Interest Rates (supports demand)

Result: CD Rising 70% → 75% → 78% → 82%

Timeline: 18-24 months
Stock Performance: +25% to +45%
Risk Level: Low-Medium (if deposits keep pace)
Investor Action: BUY and HOLD

Example: India 2015-2018, post-COVID recovery 2020-2021
```

#### **Scenario 2: Stress Phase (Multiple Decreasing Drivers)**
```
Drivers Active:
🔴 High Delinquencies (9/10) + Weak Demand (8/10)
🔴 Recession (8/10) + Rising Rates (6/10)
🔴 Deleveraging (6/10)

Result: CD Falling 80% → 75% → 65% → 60% (rapid)

Timeline: 6-12 months
Stock Performance: -30% to -60%
Risk Level: Very High
Investor Action: SELL/AVOID

Example: 2008-09 financial crisis, COVID initial shock
```

#### **Scenario 3: Consolidation Phase (Mixed Drivers)**
```
Drivers Active:
✅ Weak Demand (8/10) but Liquidity Mgmt (7/10)
⚠️ Conservative policy + Regulatory compliance
✅ Deposits growing faster than loans

Result: CD Stable or Slightly Falling 78% → 76% → 75%

Timeline: 12-18 months
Stock Performance: -5% to +5% (sideways)
Risk Level: Low
Investor Action: HOLD/ACCUMULATE

Example: Post-crisis normalization, deposit accumulation phase
```

#### **Scenario 4: Market Share Shift (Selective Drivers)**
```
Drivers Active:
✅ Market Share Gains (7/10) + Customer Growth (8/10)
✅ Competitive Pricing (7/10)
⚠️ Deposits growing slowly

Result: CD Rising 76% → 80% → 84%

Timeline: 18-24 months
Stock Performance: +15% to +30% (growth premium fading)
Risk Level: Medium
Investor Action: BUY but set stop loss at 85%

Example: Specific bank outperforming peers
```
""")
    
    render_divider()
    
    # ===== PART 6: MACRO CYCLE & CD DRIVERS =====
    st.markdown("### 🔄 Economic Cycle Impact on CD Drivers")
    
    st.markdown("""
#### **Phase 1: RECOVERY** (Early cycle)
**Active Drivers:** Strong Loan Demand ↑, Economic Growth ↑, Low Rates ↑
**CD Movement:** Rising (65% → 75%)
**Profile:** Credit demand awakening
**Duration:** 12-18 months
**CD Signal:** ✅ BUY - Growth story emerging

#### **Phase 2: EXPANSION** (Mid cycle)
**Active Drivers:** All increasing drivers peak
**CD Movement:** Accelerating rise (75% → 82%)
**Profile:** Maximum profitability
**Duration:** 12-18 months
**CD Signal:** ✅ STRONG BUY

#### **Phase 3: PEAK** (Late cycle)
**Active Drivers:** Demand peaks, Rates start rising
**CD Movement:** Plateauing (80% → 82% → 80%)
**Profile:** Delinquencies begin rising
**Duration:** 6-12 months
**CD Signal:** ⚠️ CAUTION - Start reducing

#### **Phase 4: SLOWDOWN** (Early contraction)
**Active Drivers:** Weak Demand ↑, Rising Rates ↑, Delinquencies ↑
**CD Movement:** Falling (80% → 75%)
**Profile:** Growth slowing, margins under pressure
**Duration:** 12-18 months
**CD Signal:** 🔴 SELL at first signs

#### **Phase 5: CRISIS** (Deep contraction)
**Active Drivers:** Recession ↑, High Delinquencies ↑, Deleveraging ↑
**CD Movement:** Sharp fall (75% → 60%)
**Profile:** Survival mode
**Duration:** 6-12 months
**CD Signal:** 🔴 AVOID - Asset quality crisis

#### **Phase 6: BOTTOMING** (Late contraction)
**Active Drivers:** Demand stabilizing, Rates holding
**CD Movement:** Stabilizing (60% → 62%)
**Profile:** Pain priced in, recovery next
**Duration:** 6-12 months
**CD Signal:** 🟡 MONITOR - Wait for recovery signs
""")
    
    render_divider()
    
    # ===== PART 7: TIMING CHANGES IN DRIVERS =====
    st.markdown("### ⏱️ How Quickly Do Drivers Change CD Ratio?")
    
    timing_data = {
        'Driver': [
            'Economic Growth/Recession',
            'Interest Rate Changes',
            'Loan Demand Shift',
            'Delinquencies Rising',
            'Regulatory Changes',
            'Deposit Mobilization',
            'Market Share Shifts',
            'Credit Expansion'
        ],
        'Lag Time': [
            '1-2 quarters',
            '1-2 months (market reacts)',
            '1-3 months',
            '3-6 months (detection lag)',
            '1 month (announcement)',
            '3-6 months',
            '6-12 months',
            '2-4 quarters'
        ],
        'Typical CD Impact': [
            '2-3% per quarter',
            '0.5-1% per quarter',
            '1-2% per quarter',
            '1-2% per quarter',
            '0.5-1.5% per quarter',
            '1-2% per quarter',
            '2-4% over 12 months',
            '1-3% per quarter'
        ],
        'Reversibility': [
            'Slow (6-12 m)',
            'Medium (3-6 m)',
            'Medium (3-6 m)',
            'Slow (12-24 m)',
            'Slow (6-12 m)',
            'Medium (6-9 m)',
            'Fast (3-6 m)',
            'Medium (6-12 m)'
        ]
    }
    
    timing_df = pd.DataFrame(timing_data)
    st.dataframe(timing_df, use_container_width=True, hide_index=True)
    
    render_divider()
    
    # ===== PART 8: KEY TAKEAWAYS =====
    st.markdown("### 🎯 Key Takeaways on CD Drivers")
    
    render_success_box("""
**Understanding CD Drivers Helps You:**

1. **Predict CD Changes** - Know which driver is active
2. **Assess Sustainability** - Multiple drivers = sustainable
3. **Time Investments** - Know when drivers are shifting
4. **Evaluate Management** - How well do they navigate drivers?
5. **Risk Assessment** - Single driver = higher risk
6. **Competitive Positioning** - Compare drivers across banks

**Remember:**
- Drivers are interconnected (macro + micro)
- Multiple drivers create sustainable trends
- Single driver changes are often temporary
- Always ask "Which driver is active NOW?"
- CD follows drivers with a 1-2 quarter lag
- Best opportunities at driver transition points
""")
    
    st.markdown("""
---

## 📊 Quick Reference: Which Driver = Which CD Movement?

| Driver | Effect | Speed | Duration | Investment Action |
|--------|--------|-------|----------|------------------|
| Strong Growth | ↑ | Fast | 12-18m | BUY |
| Loan Demand ↑ | ↑ | Fast | 6-12m | BUY |
| Market Expansion | ↑ | Medium | 18-24m | BUY |
| Rate Cuts | ↑ | Medium | 6-12m | ACCUMULATE |
| Economic Boom | ↑↑ | Medium | 12-18m | STRONGLY BUY |
| Delinquencies ↑ | ↓ | Fast | 6-12m | SELL |
| Weak Demand | ↓ | Medium | 12-18m | SELL |
| Rate Hikes | ↓ | Medium | 6-12m | MONITOR |
| Recession | ↓↓ | Fast | 6-12m | AVOID |
| Deleveraging | ↓ | Slow | 12-24m | HOLD |
""")



elif page_index == 8:
    render_section_header("💡 Investment Insights & Implications")
    
    st.markdown("**What CD ratios tell investors about banking sector**")
    
    render_divider()
    
    # ===== PART 1: CD RATIO AS INVESTMENT SIGNAL =====
    render_info_box(
        "**CD Ratio as Investment Signal:**\n\n"
        "🔷 **High CD (80-85%):** Bank is aggressively deploying deposits, growth story but monitor liquidity\n"
        "🔷 **Optimal CD (72-78%):** Balanced approach, steady growth with safety margin\n"
        "🔷 **Low CD (<70%):** Underutilized capacity, excess liquidity, potential profitability headwind\n"
        "🔷 **Rising CD:** Positive for growth story, indicates credit demand recovery\n"
        "🔷 **Falling CD:** Could signal credit stress or deposit accumulation"
    )
    
    render_divider()
    
    # ===== PART 2: CD RATIO ZONES & INVESTMENT MATRIX =====
    st.markdown("### 📊 CD Ratio Investment Zones Matrix")
    
    st.markdown("""
This matrix shows how different CD ratio levels impact key investment metrics:

| **CD Zone** | **Range** | **Growth Potential** | **Profitability** | **Liquidity Health** | **Risk Level** | **Investor Signal** | **Action** |
|-------------|----------|-------------------|------------------|-------------------|--------------|-------------------|----------|
| **1 - Critical Low** | <50% | 2/10 | 2/10 | 9/10 | 1/10 | ⚠️ Underutilized | AVOID |
| **2 - Conservative** | 50-65% | 4/10 | 4/10 | 8/10 | 2/10 | 🟡 Safe but slow | HOLD |
| **3 - Growth Early** | 65-72% | 6/10 | 6/10 | 7/10 | 3/10 | 🟢 Emerging growth | BUY |
| **4 - OPTIMAL** | **72-78%** | **8/10** | **9/10** | **7/10** | **4/10** | **✅ Perfect balance** | **BUY** |
| **5 - Aggressive** | 78-85% | 7/10 | 8/10 | 5/10 | 6/10 | 🟡 Growth + caution | MONITOR |
| **6 - High Risk** | 85-95% | 4/10 | 5/10 | 3/10 | 8/10 | 🔴 Liquidity stress | SELL |
| **7 - Critical High** | >95% | 1/10 | 2/10 | 1/10 | 10/10 | 🔴 Unsustainable | AVOID |
""")
    
    render_divider()
    
    # ===== PART 3: CD ZONE ANALYSIS WITH CHARTS =====
    st.markdown("### 🎯 Interactive CD Zone Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📈 Growth & Profitability vs CD Ratio")
        
        import plotly.graph_objects as go
        
        cd_zones = ['<50%', '50-65%', '65-72%', '72-78%', '78-85%', '85-95%', '>95%']
        growth = [2, 4, 6, 8, 7, 4, 1]
        profitability = [2, 4, 6, 9, 8, 5, 2]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=cd_zones, y=growth,
            mode='lines+markers',
            name='Growth Potential',
            line=dict(color='#27AE60', width=3),
            marker=dict(size=10)
        ))
        
        fig.add_trace(go.Scatter(
            x=cd_zones, y=profitability,
            mode='lines+markers',
            name='Profitability',
            line=dict(color='#FFD700', width=3),
            marker=dict(size=10)
        ))
        
        fig.update_layout(
            height=400,
            xaxis_title='CD Ratio Range',
            yaxis_title='Score (1-10)',
            hovermode='x unified',
            template='plotly_white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### 🛡️ Risk vs Liquidity Health")
        
        risk_level = [1, 2, 3, 4, 6, 8, 10]
        liquidity = [9, 8, 7, 7, 5, 3, 1]
        
        fig2 = go.Figure()
        
        fig2.add_trace(go.Scatter(
            x=cd_zones, y=risk_level,
            mode='lines+markers',
            name='Risk Level',
            line=dict(color='#E74C3C', width=3),
            marker=dict(size=10)
        ))
        
        fig2.add_trace(go.Scatter(
            x=cd_zones, y=liquidity,
            mode='lines+markers',
            name='Liquidity Health',
            line=dict(color='#3498DB', width=3),
            marker=dict(size=10)
        ))
        
        fig2.update_layout(
            height=400,
            xaxis_title='CD Ratio Range',
            yaxis_title='Score (1-10)',
            hovermode='x unified',
            template='plotly_white'
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    render_divider()
    
    # ===== PART 4: CD TREND ANALYSIS =====
    st.markdown("### 📊 CD Ratio Trend Analysis - What It Means")
    
    st.markdown("""
#### **Rising CD Ratio (Positive Scenario)**
Example: CD increases from 70% → 75% → 78% (over 2 years)

**What It Means:**
- Credit demand recovering
- Bank gaining market share
- Loan portfolio growing
- Deposits also growing (or steady)

**Investor Signal:** ✅ **POSITIVE** - Growth story emerging
**Action:** **BUY** if deposits growing 10%+ YoY
**Risk:** Monitor that deposits keep pace with loans

---

#### **Falling CD Ratio - Could Be Positive OR Negative**

**Scenario A: Strong Deposits (POSITIVE)**
- CD falls from 80% → 75% because deposits surge
- Bank has strong franchise
- Safe, liquid position

**Investor Signal:** ✅ **POSITIVE**
**Action:** **BUY** - Strong deposit base

**Scenario B: Loan Shrinking (NEGATIVE)**
- CD falls from 80% → 75% because loans decline
- Credit stress or risk aversion
- Profitability under pressure

**Investor Signal:** 🔴 **NEGATIVE**
**Action:** **SELL** or **AVOID**

**How to Tell the Difference:**
- Check quarterly results for deposit & loan breakup
- Read management commentary
- Look at deposit growth % vs loan growth %

---

#### **Volatile CD Ratio (Unstable)**
Example: CD bounces around: 78% → 73% → 81% → 74%

**What It Means:**
- Imbalanced deposits and loans
- Possible ALM (Asset-Liability Management) issues
- Seasonal patterns or external shocks
- Lack of predictability

**Investor Signal:** ⚠️ **CAUTION**
**Action:** **AVOID** until stabilization
**Red Flag:** Suggests management execution issues

---

#### **Sticky High CD (Structural Problem)**
Example: CD stuck at 88-92% for 2+ years

**What It Means:**
- Weak deposit franchise
- Over-dependent on expensive wholesale funding
- Structural business model mismatch
- Chronic liquidity stress

**Investor Signal:** 🔴 **VERY NEGATIVE**
**Action:** **AVOID** - Systemic risk
**Why:** Bank cannot grow deposits, forced to deleverage

""")
    
    render_divider()
    
    # ===== PART 5: INVESTMENT STRATEGIES BY INVESTOR TYPE =====
    st.markdown("### 💼 Investment Strategies by Investor Type")
    
    st.markdown("""
#### **Strategy 1: Growth Investor**
**Target Profile:** Seeking 15-20% annual returns

**Optimal CD Range:** 75-82%
- **Buy Signal:** CD rising from 70% toward 78%
- **Monitor:** Deposits growing ≥12% YoY
- **Sell Signal:** CD exceeds 85% consistently
- **Holding Period:** 2-3 years
- **Expected Return:** 12-18% annually (including dividend)

**Example Trade:**
1. Buy bank when CD rises 70%→75% with strong deposit growth
2. Hold 18-24 months
3. Sell when CD hits 85% or deposits growth slows <10%

---

#### **Strategy 2: Value Investor**
**Target Profile:** Seeking undervalued banks with margin of safety

**Optimal CD Range:** Target falling toward 70%
- **Buy Signal:** Bank with CD falling from 85% to 78% + strong fundamentals
- **Monitor:** Deposit growth acceleration, ROA improvement
- **Sell Signal:** Once CD stabilizes, stock appreciates >30%
- **Holding Period:** 12-18 months
- **Expected Return:** 20-30% when market recognizes improvement

**Example Trade:**
1. Identify bank with CD 85%+ but improving deposits
2. Buy when market is pessimistic (stock down 20-30%)
3. Hold 12-18 months as deposits improve
4. Sell when CD falls to 75-78% and stock appreciates

---

#### **Strategy 3: Conservative/Income Investor**
**Target Profile:** Steady dividends, capital preservation

**Optimal CD Range:** 72-78% stable
- **Buy Signal:** Bank with stable 76-78% CD, strong ROA 1%+, dividend >2%
- **Monitor:** CD stability month-to-month, dividend sustainability
- **Sell Signal:** CD rising above 82% or dividend cut
- **Holding Period:** Long-term (5+ years)
- **Expected Return:** 8-12% annually (capital appreciation + dividend)

**Example Trade:**
1. Buy bank with 76% CD and 3% dividend yield
2. Hold 5+ years, collect dividends
3. Sell only if CD rises >82% or dividend threatened

""")
    
    render_divider()
    
    # ===== PART 6: QUICK DECISION TABLE =====
    st.markdown("### ⚡ Quick Investor Decision Guide")
    
    st.markdown("""
| **Situation** | **CD Signal** | **Action** | **Risk** | **Expected Return** |
|---------------|--------------|-----------|---------|-------------------|
| CD 72-78%, deposits growing 10%+ | ✅ Healthy | **BUY** | Low | 10-15% |
| CD rising 70%→78%, deposits growing | ✅ Growth | **BUY** | Low-Med | 12-18% |
| CD 78-85%, monitor deposits closely | ⚠️ Caution | **HOLD** | Medium | 8-12% |
| CD 80-85%, deposits flat/declining | 🔴 Warning | **MONITOR** | Medium-High | 0-8% |
| CD >85%, liquidity stress signals | 🔴 Danger | **SELL** | High | -5 to +5% |
| CD >90% for 6+ months | 🔴 Critical | **AVOID** | Very High | Negative |
| CD <60%, underutilized | ⚠️ Issue | **INVESTIGATE** | Low | Low 6-8% |
| CD 62-70%, growing toward 75% | 🟡 Improving | **ACCUMULATE** | Low-Med | 10-15% |
| CD volatile (±5% quarterly) | ⚠️ Risky | **AVOID** | Medium-High | Unpredictable |
| CD stable 75-78%, dividend >2% | ✅ Ideal | **BUY HOLD** | Low | 8-12% |

""")
    
    render_divider()
    
    # ===== PART 7: REAL CASE STUDIES =====
    st.markdown("### 📚 Real-World Case Studies")
    
    st.markdown("""
#### **Case Study 1: Private Bank - Strong Growth (2015-2018)**
**Bank Profile:** Large private bank targeting retail expansion

**CD Ratio Progression:**
- 2015: 78%
- 2016: 80%
- 2017: 82%
- 2018: 84%

**What Happened:**
- Aggressive retail lending push
- Deposit growth lagged loan growth
- NIM compression from 3.2% to 2.8%

**Stock Performance:**
- 2015-2016: +35% (growth story)
- 2016-2017: +20% (continued growth)
- 2017-2018: -15% (profitability concerns)
- 2018-2019: -25% (forced deleveraging)

**Lesson:** CD rising + deposits not keeping pace = eventual correction

---

#### **Case Study 2: PSB - Deposit-Driven Rally (2018-2020)**
**Bank Profile:** Major public sector bank

**CD Ratio Progression:**
- 2018: 78%
- 2019: 75% (deposits surged)
- 2020: 72%

**What Happened:**
- Aggressive CASA deposit mobilization
- Government mandates for lending
- Balance sheet strengthening

**Stock Performance:**
- 2018-2019: +8%
- 2019-2020: +25% (financial crisis safety)
- 2020-2021: +45% (recovery story)

**Lesson:** Falling CD from deposit strength = positive signal

---

#### **Case Study 3: Small Finance Bank - Liquidity Crisis (2021-2022)**
**Bank Profile:** Newer SFB with aggressive growth

**CD Ratio Progression:**
- 2021: 98%
- 2022 Q1: 102%
- 2022 Q2: 105%

**What Happened:**
- Weak deposit franchise
- Over-aggressive lending
- Wholesale funding at 300+ bps cost
- Profitability squeeze

**Stock Performance:**
- 2021: +50% (growth phase)
- 2022: -55% (stress emerges)
- 2023: -40% (continued deterioration)

**Lesson:** CD stuck >95% = eventual crisis

---

#### **Case Study 4: Foreign Bank - Strategic Simplification (2019-2021)**
**Bank Profile:** International bank exiting retail

**CD Ratio Progression:**
- 2019: 58%
- 2020: 52%
- 2021: 45%

**What Happened:**
- Exited retail & SME business
- Focused on wholesale/corporate
- Intentional CD reduction

**Stock Performance:**
- Underperformed peers (no growth story)
- Stable, predictable
- Higher dividend yield (3-4%)

**Lesson:** Low CD by design = not a problem if intentional

""")
    
    render_divider()
    
    # ===== PART 8: WARNING SIGNS & RED FLAGS =====
    st.markdown("### 🚩 Warning Signs - When to SELL")
    
    render_warning_box("""
**Immediate Red Flags (SELL immediately):**
- CD rises above 85% and deposits growth <8% YoY
- CD >90% for more than 2 consecutive quarters
- Deposits declining while CD rising
- NIM compression >20 bps while CD rising
- Management unable to explain CD elevation
- Stock trading below book value

**Gradual Red Flags (MONITOR closely):**
- CD rising >2% per quarter for 2+ consecutive quarters
- Deposit growth slowing while CD accelerating
- Cost of deposits rising (higher CASA mix deterioration)
- Asset quality indicators worsening
- Unsecured advances rising alongside CD
- Delinquencies rising >50 bps while CD >80%

**Structural Red Flags (AVOID):**
- CD >90% for 12+ months (structural problem)
- Wholesale funding >40% of deposits
- Negative deposit growth YoY
- Recurring liquidity issues
- Regulatory comments on liquidity stress
""")
    
    render_divider()
    
    # ===== PART 9: POSITIVE SIGNALS & ACCUMULATION POINTS =====
    st.markdown("### ✅ Positive Signs - When to BUY")
    
    render_success_box("""
**Strong Buy Signals:**
- CD in 72-78% range with 10%+ deposit growth YoY
- CD rising from 70% to 75% with deposits accelerating
- Falling CD (below 75%) with strong ROA >1%
- Strong deposit franchise (40%+ CASA mix)
- NIM stable or expanding while CD in optimal range
- Management guiding CD moderation

**Accumulation Points (Dollar-Cost Average):**
- CD 75-80% = Start buying 50% position
- CD 78-82% = Add another 25%
- CD 82-85% = Add final 25% (if deposits strong)
- NEVER accumulate above 85% CD

**Growth Story Indicators:**
- Loan growth >15% YoY
- Deposits growing faster than system average
- Market share gains visible
- ROA improving/stable
- Stock underperforming (creating opportunity)
- Analyst upgrades emerging

**Value Indicators:**
- CD falling toward 70% from 85%+ high
- Stock down 20-30% despite improving fundamentals
- Dividend yield >3%
- P/B ratio <0.8x
- Profitability recovering as CD normalizes
""")
    
    render_divider()
    
    # ===== PART 10: KEY TAKEAWAYS =====
    st.markdown("### 🎯 Key Takeaways for Smart Investors")
    
    st.markdown("""
1. **72-78% is the investment sweet spot** - This range offers optimal balance of growth, profitability, and safety

2. **Direction matters more than level** - CD rising 70%→75% is positive; falling 85%→75% also positive (if from deposits)

3. **Deposits must keep pace** - High CD is only good if deposits growing ≥10% YoY

4. **Three investor strategies** - Growth (75-82%), Value (falling CD), Conservative (72-78% stable)

5. **Red flags above 85%** - Monitor closely; above 90% for 6+ months = structural problem

6. **Seasonal volatility OK** - Q1-Q4 seasonal swings of 2-3% normal; 5%+ swings = problem

7. **Always check trend direction** - Rising CD vs falling CD vs stable CD = different signals

8. **Bank type matters** - PSBs optimal at 76-80%, Foreign banks fine at 50-60%, SFBs should be <90%

9. **Use CD with other metrics** - Combine with deposit growth, NIM, ROA, asset quality for best picture

10. **Trust but verify** - Read quarterly disclosures, don't rely on CD ratio alone

---

## 📈 Quick Reference: Expected Returns by CD Zone

| **CD Zone** | **Deposit Growth** | **Time Horizon** | **Expected Annual Return** |
|-----------|-------------------|-----------------|--------------------------|
| 72-76% | 10%+ | 2-3 years | 12-18% |
| 76-80% | 8%+ | 3-5 years | 10-15% |
| 78-82% | 10%+ | 2 years | 15-20% |
| 82-85% | 8%+ | 1 year | 8-12% |
| 85-90% | <8% | Monitor only | 0-8% |
| >90% | Any | AVOID | Negative |
| <65% | Growing | 3+ years | 8-12% |

---

## 🎓 Final Word

CD ratio is one of the most important metrics for banking sector investors. Use it wisely:
- ✅ For timing entry points
- ✅ For assessing bank health
- ✅ For understanding growth stage
- ✅ For risk management

But always combine with other metrics (deposit growth, NIM, ROA, asset quality) for a complete picture!
""")



elif page_index == 9:
    render_section_header("📋 Data Explorer - All Bank Data")
    
    st.markdown("**Interactive data explorer for all banks**")
    
    render_divider()
    
    render_subsection_header("📊 Complete Bank Data")
    
    # Display all bank data
    st.dataframe(
        data["banks"],
        use_container_width=True,
        hide_index=True
    )
    
    render_divider()
    
    render_subsection_header("📥 Download Data")
    
    # CSV download
    csv = data["banks"].to_csv(index=False)
    st.download_button(
        label="📥 Download as CSV",
        data=csv,
        file_name="indian_banks_cd_ratio.csv",
        mime="text/csv"
    )

elif page_index == 10:
    render_section_header("🎓 CD Ratio Education & Learning Center")
    
    st.markdown("**Comprehensive guide to understanding CD ratios**")
    
    render_divider()
    
    # Create 4 education tabs
    edu_tab1, edu_tab2, edu_tab3, edu_tab4 = st.tabs(["📘 CD Ratio Basics", "🏛️ RBI Regulations", "❓ FAQ & Questions", "📈 Investment Signals"])
    
    with edu_tab1:
        st.markdown("""
### What is Credit-to-Deposit (CD) Ratio?

The CD Ratio is a critical banking metric that measures the percentage of a bank's customer deposits that are deployed as loans and advances to borrowers.

**Formula:**
```
CD Ratio = (Total Advances / Total Deposits) × 100
```

**Example:**
- Total Advances: ₹100 Crores
- Total Deposits: ₹125 Crores
- CD Ratio = (100/125) × 100 = 80%

---

### 🎯 Optimal Range: 72-78%

**Why This Range?**
- ✅ Maximizes profitability (NIM optimization)
- ✅ Maintains adequate liquidity buffers
- ✅ Aligns with RBI regulatory requirements
- ✅ Sustainable long-term growth
- ✅ Balanced risk-return profile

---

### Bank Type Variations

#### **Public Sector Banks (PSBs)**
- **Average CD:** 75-80%
- **Characteristic:** Balanced, stable approach
- **Investment Signal:** ✅ Healthy when in 76-80% range

#### **Private Sector Banks**
- **Average CD:** 92-94%
- **Characteristic:** Aggressive growth, higher leverage
- **Investment Signal:** ⚠️ Monitor closely if >90%

#### **Small Finance Banks**
- **Average CD:** >100%
- **Characteristic:** High lending, weak deposits
- **Investment Signal:** 🔴 Risky, liquidity stress

#### **Foreign Banks**
- **Average CD:** <60%
- **Characteristic:** Conservative, selective lending
- **Investment Signal:** ✅ Stable, lower growth

---

### Regional Disparities in India

**High CD Regions (>85%):**
- Maharashtra
- Gujarat  
- Tamil Nadu
- Karnataka

**Low CD Regions (<50%):**
- Bihar
- Odisha
- Uttar Pradesh (Eastern)
- North East States

**Investor Implication:** Regional economic cycles matter for bank performance

---

### Risks Above 80% CD Ratio

1. **Liquidity Risk** - Limited buffers for withdrawals
2. **Funding Pressure** - High wholesale funding costs
3. **NIM Compression** - Limited loan pricing power
4. **Asset Quality** - Risk of rapid deterioration
5. **Regulatory Scrutiny** - RBI oversight increases

---
""")
    
    with edu_tab2:
        st.markdown("""
### RBI Guidelines on CD Ratio

The RBI doesn't impose a **hard cap** on CD ratios but indirectly constrains banks through mandatory requirements and supervisory oversight.

---

### 1. Reserve Requirements

**Statutory Liquidity Ratio (SLR)**
- **Requirement:** 18% of deposits
- **Purpose:** Ensure liquid asset availability
- **Impact on CD:** Banks can deploy ~75-76% after SLR

**Cash Reserve Ratio (CRR)**
- **Requirement:** 4.5% of deposits
- **Purpose:** Central bank control
- **Impact on CD:** Further reduces deployment capacity

**Result:** Only ~75-76% of deposits deployable as loans (optimal = 76-80%)

---

### 2. Liquidity Coverage Ratio (LCR)

- **Requirement:** 100% (minimum)
- **Impact:** Tightens as CD increases above 80%
- **At 85% CD:** LCR becomes more stringent
- **At 95% CD:** LCR compliance becomes critical challenge

---

### 3. Net Stable Funding Ratio (NSFR)

- **Requirement:** >100%
- **Impact:** Encourages stable deposits
- **High CD Banks:** Must rely on stable funding sources

---

### 4. Supervisory Actions (SLBC)**

- **Quarterly Reviews:** Stress State-Level Bankers' Committees
- **Low CD Zones (<40%):** RBI directed lending mandates
- **High CD Zones (>85%):** Enhanced supervisory attention
- **Liquidity Stress:** Immediate RBI action plans required

---

### 5. Priority Sector Lending

- **Mandate:** 40% of advances to priority sectors
- **Low CD Regions:** Higher PSL targets
- **Impact:** Constrains lending in high-profit segments

---

### 6. Asset Quality Standards

- **Stressed Assets:** Rise above 85% CD threshold
- **Unsecured Advances:** Capped at 20-24.5%
- **Provisioning:** Higher at elevated CD ratios

---

### 7. Capital Adequacy

- **Minimum CAR:** 9%
- **Higher CD Banks:** Need stronger capital buffers
- **Impact:** Limits growth for capital-constrained banks

---

### Key Takeaway

**RBI doesn't prevent high CD, but creates conditions that make it difficult:**
- Liquidity requirements
- Capital constraints
- Supervisory pressure
- Funding cost increases

---
""")
    
    with edu_tab3:
        st.markdown("""
### CD Ratio - Frequently Asked Questions

---

## Q1: What is the minimum CD ratio a bank should maintain?

**Answer:**
There is no RBI-mandated minimum CD ratio. However, banks naturally maintain a CD ratio around **50-70%** to comply with SLR (18%), CRR (4.5%), and LCR requirements. Going below 50% indicates:
- Excess deposits (good for liquidity, bad for profitability)
- Under-deployment of funds
- Lost lending opportunities
- Lower net interest income

**Practical Minimum:** 65-70% (after regulatory buffers)

---

## Q2: Is 95% CD ratio sustainable for private banks?

**Answer:**
No, 95% CD is **unsustainable** for most banks. Here's why:

**Problems:**
- Extreme liquidity risk (no buffer for withdrawals)
- Wholesale funding very expensive (100+ bps higher cost)
- NIM compression (20-50 bps erosion)
- RBI regulatory scrutiny
- Vulnerable to market shocks

**Typical Outcome:** Forced deleveraging within 12-18 months

---

## Q3: How does high CD ratio (>85%) affect bank stability?

**Answer:**
High CD significantly impacts bank stability:

**Liquidity Vulnerability:**
- Limited buffers for deposit outflows
- Increased dependence on wholesale funding
- Higher interest rate sensitivity

**Profitability Under Pressure:**
- NIM compression from high deposit costs
- Limited loan pricing power
- ROA/ROE deterioration

**Credit Risk Amplified:**
- Forced lending to marginal borrowers
- Rushed appraisals = poor quality loans
- Delinquencies rise faster

**Regulatory Scrutiny:**
- Frequent RBI reviews
- Potential capital raise mandates
- Lending restrictions in high CD regions

---

## Q4: Why do foreign banks operate with 60-70% CD ratios?

**Answer:**
Foreign banks' lower CD ratios reflect their strategic positioning:

**Access to Global Funding:**
- Parent company support
- International capital markets
- Multiple funding sources

**Selective Lending Strategy:**
- Focus on high-quality corporates
- Avoid retail/MSME (high cost)
- Selective by geography

**Fee Income Focus:**
- Investment banking revenues
- Trade finance, forex
- Not purely deposit-driven model

---

## Q5: Do regional CD disparities create systemic risk?

**Answer:**
Yes, regional disparities create multiple risks:

**Credit Boom Risk (High CD Regions >90%):**
- Over-lending in growth regions
- Asset bubbles in real estate
- Concentration risk

**Credit Deficit Risk (Low CD Regions <50%):**
- Under-lending in backward regions
- Economic inequality
- Development disparities

**System-Wide Risk:**
- Banks with concentrated exposure to boom regions
- Portfolio volatility
- Correlated losses in crisis

---

## Q6: What happens to bank stock prices when CD >85%?

**Answer:**
Stock performance at high CD ratios:

**Short-term (3-6 months):**
- 3-5% stock price dip on announcement
- Analyst rating downgrades
- Selling by growth investors

**Medium-term (6-12 months):**
- Recovery possible if deposits accelerate
- Stabilization if management shows control
- Sideways movement

**Long-term (12+ months):**
- 30-40% discount vs. healthy peers
- Lower PE multiples
- Valuation compression

---

## Q7: Can banks reduce CD ratio quickly?

**Answer:**
Reducing CD ratio is **difficult and time-consuming:**

**Realistic Timeline:** 18-24 months for 5-10% reduction

**Methods Available:**
1. Aggressively mobilize deposits (slow, expensive)
2. Slow credit growth (harms earnings, investor confidence)
3. Loan prepayments (doesn't control growth)
4. Sell assets (fire-sale prices)

**Cost:** 5-10% CD reduction costs 10-20% earnings hit

---

## Q8: How does CD ratio interact with LCR requirement?

**Answer:**
CD ratio directly impacts LCR compliance:

**Relationship:**
- **At 70% CD:** LCR very comfortable (200%+ easily)
- **At 76-80% CD:** LCR at 100-120% range
- **At 85% CD:** LCR becomes tight (100-110%)
- **At 95%+ CD:** LCR compliance critical, risky

**Optimal Balance:** 76-80% is natural CD level where LCR is comfortable

---

## Q9: What's the difference between CD and LTD ratio?

**Answer:**
CD and LTD are related but different metrics:

**CD Ratio (Credit-to-Deposit):**
- Numerator: All advances + all exposures
- Denominator: All deposits
- RBI focus for liquidity

**LTD Ratio (Loans-to-Deposits):**
- Numerator: Loans only
- Denominator: Deposits
- SLBC focus for regional lending

**Practical Difference:**
- CD broader (includes market-linked advances)
- LTD narrower (plain vanilla loans)
- Both used for different regulatory purposes

---

## Q10: How do 200 bps rate hikes impact optimal CD ratio?

**Answer:**
Rate hikes shift optimal CD ratios:

**Immediate Impact (0-3 months):**
- Shifts optimal CD from 76-80% to 78-85%
- Higher margins compensate for risk
- Loan demand falls (demand side)

**Medium-term (3-12 months):**
- Market forces moderate back toward 76-80%
- Deposit competition intensifies
- Margins compress from peak

**Long-term (12+ months):**
- Returns to historical 76-80% optimal
- Full cycle interest rate impact

---

## Q11: What does CD below 60% tell us about a bank?

**Answer:**
Low CD ratio (<60%) indicates problems:

**Normal Cases:**
- Foreign banks (by design, not a problem)
- New banks (deposit ramp-up phase)

**Problem Cases:**
- Liquidity excess (profitability issue)
- Asset quality crisis (reluctance to lend)
- Market share loss (losing deposit war)
- Opportunity cost 5-6% annually

**Signal:** Investigate why deposits exceed loan capacity

---

## Q12: How do unsecured advances affect optimal CD ratio?

**Answer:**
Unsecured advances significantly impact CD targets:

**Regulatory Constraint:**
- Cap: Unsecured advances ≤ 20-24.5% of total advances
- Rationale: Higher default risk needs provisions
- Current Status: Many banks at cap

**Impact on Optimal CD:**

| Unsecured % | Optimal CD | Reasoning |
|----------|-----------|-----------|
| 10% | 78-82% | Lower risk, can be aggressive |
| 20% | 76-80% | Balanced, standard approach |
| 24.5% | 72-76% | Higher risk, need moderation |

**Conclusion:** Higher unsecured mix → Lower optimal CD ratio

---
""")
    
    with edu_tab4:
        st.markdown("""
### 📈 CD Ratio as Investment Signal

The Credit-to-Deposit ratio is a critical indicator for bank investors. It reveals how aggressively a bank deploys deposits, its growth trajectory, and potential profitability trends.

---

### 🎯 CD Ratio Zones & Investment Signals

| Zone | CD Range | Signal | Action |
|------|----------|--------|--------|
| 1 | <50% | ⚠️ RED | AVOID |
| 2 | 50-65% | 🟡 YELLOW | HOLD |
| 3 | 65-72% | 🟢 GREEN | BUY |
| 4 | **72-78%** | **🟢 OPTIMAL** | **✅ BUY** |
| 5 | 78-85% | 🟡 CAUTION | MONITOR |
| 6 | 85-95% | 🔴 HIGH | SELL |
| 7 | >95% | 🔴 CRITICAL | AVOID |

---

### Zone Analysis

**Zone 1: <50% (Underutilized)**
- Signal: Excess liquidity, poor deployment
- Investor: Avoid or wait for improvement
- Risk: Low, but profitability concerns

**Zone 2: 50-65% (Conservative)**
- Signal: Safe but low returns
- Investor: Defensive portfolios
- Risk: Low, but growth limited

**Zone 3: 65-72% (Approaching Optimal)**
- Signal: Good risk-reward emerging
- Investor: Early growth play
- Risk: Low-Medium

**Zone 4: 72-78% (OPTIMAL)**
- Signal: Perfect balance
- Investor: **BEST CHOICE**
- Risk: Low-Medium

**Zone 5: 78-85% (Aggressive)**
- Signal: Growth but monitor closely
- Investor: Growth seekers, watch for stress
- Risk: Medium

**Zone 6: 85-95% (High Risk)**
- Signal: Liquidity stressed
- Investor: Avoid or sell
- Risk: High

**Zone 7: >95% (Critical)**
- Signal: Unsustainable
- Investor: Immediate avoid
- Risk: Very High

---

### CD Ratio Trends Matter

**Rising CD (Positive Signal 📊)**
- Example: 70% → 75%
- Means: Loan demand recovery
- Action: BUY if deposits also growing

**Falling CD (Mixed Signal 📉)**
- If deposits surging: ✅ POSITIVE
- If loans shrinking: 🔴 NEGATIVE
- Investigation needed to determine cause

---

### Quick Investment Guide

| Scenario | Signal | Action |
|----------|--------|--------|
| CD 72-78% | ✅ Optimal | BUY |
| CD rising 70→75% | ✅ Growth | BUY |
| CD 78-85% | ⚠️ Monitor | HOLD |
| CD >85% | 🔴 Risky | SELL |
| CD <60% | ⚠️ Issue | AVOID |
| CD stable | ✅ Predictable | HOLD |

---

### 3 Investment Strategies

**Growth Investor:**
- Target: CD 75-82%
- Buy: When CD rising from 70%
- Sell: When CD exceeds 85%

**Value Investor:**
- Target: CD falling toward 70%
- Buy: Strong deposit franchise signals
- Sell: When CD normalizes

**Conservative Investor:**
- Target: CD 72-78% stable
- Buy: Steady 76% performers
- Sell: CD rises above 82%

---

### Key Takeaways

1. **72-78% is the investment sweet spot**
2. **Rising CD 70%→78% = positive growth signal**
3. **CD >85% = red flag for liquidity stress**
4. **CD <60% = underutilized capacity issue**
5. **Trend matters more than level**
6. **Bank type affects optimal CD**
7. **Monitor quarterly changes**

---
""")

# ═══════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════

render_footer(
    AUTHOR, 
    BRAND_NAME, 
    "RBI, BSE, NSE, Bank Investor Relations | Research: ICRA, CRISIL, Financial Media"
)
