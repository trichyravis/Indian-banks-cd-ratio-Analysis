
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
    **Banks Covered:** 28 major Indian banks
    **Categories:** PSBs, Private Banks, Small Finance Banks
    
    This dashboard provides comprehensive CD ratio analysis across all major categories
    of Indian banks, enabling investors and analysts to track lending trends and
    banking health indicators.
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
        comparison_df[["bank", "type", "latest_cd", "fy24_avg_cd", "change", "Status"]],
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
    render_section_header("📈 CD Ratio Drivers & Analysis")
    
    st.markdown("**What drives CD ratios and how to interpret changes**")
    
    render_divider()
    
    render_subsection_header("🎯 Key Drivers of CD Ratio")
    
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
        render_warning_box(
            "**Factors Decreasing CD Ratio:**\n\n"
            "⚠️ High loan delinquencies\n"
            "⚠️ Weak credit demand\n"
            "⚠️ High interest rates\n"
            "⚠️ Liquidity management\n"
            "⚠️ Regulatory constraints"
        )

elif page_index == 8:
    render_section_header("💡 Investment Insights & Implications")
    
    st.markdown("**What CD ratios tell investors about banking sector**")
    
    render_divider()
    
    render_info_box(
        "**CD Ratio as Investment Signal:**\n\n"
        "🔷 **High CD (80-85%):** Bank is aggressively deploying deposits, growth story but monitor liquidity\n"
        "🔷 **Optimal CD (72-78%):** Balanced approach, steady growth with safety margin\n"
        "🔷 **Low CD (<70%):** Underutilized capacity, excess liquidity, potential profitability headwind\n"
        "🔷 **Rising CD:** Positive for growth story, indicates credit demand recovery\n"
        "🔷 **Falling CD:** Could signal credit stress or deposit accumulation"
    )

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
