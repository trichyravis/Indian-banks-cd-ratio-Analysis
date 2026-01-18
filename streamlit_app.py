
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
    
    st.markdown("**Interactive data explorer for all banks with complete source documentation**")
    
    render_divider()
    
    # Create tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Bank Data", "📥 Download", "📚 Data Sources", "ℹ️ Data Dictionary"])
    
    with tab1:
        render_subsection_header("📊 Complete Bank Data")
        
        # Display all bank data
        st.dataframe(
            data["banks"],
            use_container_width=True,
            hide_index=True
        )
    
    with tab2:
        render_subsection_header("📥 Download Data")
        
        # CSV download
        csv = data["banks"].to_csv(index=False)
        st.download_button(
            label="📥 Download as CSV",
            data=csv,
            file_name="indian_banks_cd_ratio.csv",
            mime="text/csv"
        )
        
        st.markdown("**Format:** CSV (Comma-Separated Values)")
        st.markdown("**Records:** " + str(len(data["banks"])) + " banks")
        st.markdown("**Columns:** " + str(len(data["banks"].columns)) + " data fields")
    
    with tab3:
        render_subsection_header("📚 Data Sources")
        
        st.markdown("""
### Primary Data Sources

**Reserve Bank of India (RBI)**
- Fortnightly monetary policy statements
- Balance sheet data from bank returns
- Credit and deposit statistics
- Regulatory reporting frameworks
- Website: www.rbi.org.in

**Stock Exchange Data**
- NSE (National Stock Exchange): Real-time price data
- BSE (Bombay Stock Exchange): Historical financial data
- Quarterly financial disclosures
- Corporate announcements
- Website: www.nseindia.com, www.bseindia.com

**Bank Investor Relations**
- Quarterly financial statements (Q1-Q3 FY2024, Q1-Q3 FY2025)
- Annual reports and investor presentations
- Management guidance and conference calls
- Regulatory filings and disclosures
- Direct corporate sources

### Secondary Data Sources

**Credit Rating Agencies**
- ICRA (Investment Information and Credit Rating Agency)
  - Banking sector analysis reports
  - Risk assessment and ratings
  - Website: www.icra.in

- CRISIL (Credit Rating Information Services of India Limited)
  - Banking trends and outlooks
  - Peer benchmarking analysis
  - Website: www.crisil.com

**Financial Media & Research**
- Economic Times
- Moneycontrol
- LiveMint
- Bloomberg
- Reuters

### Data Validation & Accuracy

- Data sourced from official regulatory filings
- Cross-verified with multiple sources
- Calculations based on standard banking formulas
- CD Ratio = (Advances / Deposits) × 100

### Data Update Frequency

- Latest Data: Q3 FY2025 (December 2024)
- Historical Period: Q1 FY2024 to Q3 FY2025
- Update Frequency: Quarterly
- Last Updated: January 18, 2025

### Data Methodology

**CD Ratio Calculation:**
- Advances: Include all loans and advances provided by banks
- Deposits: Include all customer deposits and liabilities
- Formula: CD Ratio = (Total Advances / Total Deposits) × 100

**Bank Classification:**
- PSB (Public Sector Banks): Government-owned banks
- Private Banks: Privately held banking institutions
- SFB (Small Finance Banks): Banks focused on underserved segments

**Benchmarks Used:**
- Healthy Range: 70-80%
- Aggressive Range: 80-90%
- High Risk Range: >90%
""")
    
    with tab4:
        render_subsection_header("ℹ️ Data Dictionary")
        
        # Create data dictionary table
        dict_data = {
            "Column Name": [
                "bank_name",
                "type",
                "headquarters",
                "nse_ticker",
                "bse_ticker",
                "q1_fy24_cd",
                "q2_fy24_cd",
                "q3_fy24_cd",
                "q4_fy24_cd",
                "q1_fy25_cd",
                "q2_fy25_cd",
                "q3_fy25_cd",
                "latest_cd",
                "avg_cd",
                "deposits_cr",
                "advances_cr"
            ],
            "Description": [
                "Official name of the bank",
                "Bank category (PSB/Private/SFB)",
                "Bank headquarters location",
                "National Stock Exchange ticker symbol",
                "Bombay Stock Exchange ticker symbol",
                "CD Ratio for Q1 FY2024 (Apr-Jun 2023)",
                "CD Ratio for Q2 FY2024 (Jul-Sep 2023)",
                "CD Ratio for Q3 FY2024 (Oct-Dec 2023)",
                "CD Ratio for Q4 FY2024 (Jan-Mar 2024)",
                "CD Ratio for Q1 FY2025 (Apr-Jun 2024)",
                "CD Ratio for Q2 FY2025 (Jul-Sep 2024)",
                "CD Ratio for Q3 FY2025 (Oct-Dec 2024)",
                "Most recent CD Ratio (Q3 FY2025)",
                "Average CD Ratio across all quarters",
                "Total Deposits in Crores (Q3 FY2025)",
                "Total Advances in Crores (Q3 FY2025)"
            ],
            "Data Type": [
                "Text",
                "Text",
                "Text",
                "Text",
                "Text",
                "Percentage",
                "Percentage",
                "Percentage",
                "Percentage",
                "Percentage",
                "Percentage",
                "Percentage",
                "Percentage",
                "Percentage",
                "Numeric (Crores)",
                "Numeric (Crores)"
            ],
            "Source": [
                "RBI, Stock Exchange",
                "RBI Classification",
                "Bank Official Website",
                "NSE",
                "BSE",
                "Bank Financial Statements",
                "Bank Financial Statements",
                "Bank Financial Statements",
                "Bank Financial Statements",
                "Bank Financial Statements",
                "Bank Financial Statements",
                "Bank Financial Statements",
                "Calculated",
                "Calculated",
                "Bank Balance Sheet",
                "Bank Balance Sheet"
            ]
        }
        
        dict_df = pd.DataFrame(dict_data)
        st.dataframe(dict_df, use_container_width=True, hide_index=True)
        
        st.markdown("**Note:** All monetary values (deposits and advances) are in Indian Rupees (Crores). 1 Crore = 10 Million")

# ═══════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════

render_footer(
    AUTHOR, 
    BRAND_NAME, 
    "RBI, BSE, NSE, Bank Investor Relations | Research: ICRA, CRISIL, Financial Media"
)
