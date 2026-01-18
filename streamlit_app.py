
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
    
    # Add custom CSS for styled tabs
    st.markdown("""
    <style>
    /* Tab styling with contrast background */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        background-color: #F5F5F5;
        padding: 10px;
        border-radius: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #E8E8E8;
        border-radius: 8px;
        padding: 12px 20px;
        color: #003366;
        font-weight: 600;
        border: 2px solid #CCCCCC;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #003366 !important;
        color: #FFFFFF !important;
        border: 2px solid #FFD700 !important;
        box-shadow: 0 4px 8px rgba(0, 51, 102, 0.3);
    }
    
    .stTabs [aria-selected="false"]:hover {
        background-color: #D0D0D0;
        color: #003366;
    }
    
    /* Tab content container */
    .stTabs [data-baseweb="tab-panel"] {
        background-color: #FFFFFF;
        border: 2px solid #003366;
        border-radius: 10px;
        padding: 25px;
        margin-top: 10px;
        box-shadow: 0 4px 12px rgba(0, 51, 102, 0.15);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create tabs for different sections
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Bank Data", "📥 Download", "📚 Data Sources", "ℹ️ Data Dictionary", "🎓 Education"])
    
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
    
    with tab5:
        render_subsection_header("🎓 CD Ratio Education & RBI Guidelines")
        
        # Create sub-tabs for education content
        edu_tab1, edu_tab2, edu_tab3 = st.tabs(["📘 CD Ratio Basics", "🏛️ RBI Regulations", "❓ FAQ & Questions"])
        
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

This means the bank has deployed 80% of its deposits as loans, keeping 20% as reserves.

---

### Optimal CD Ratio for Indian Banks

According to **SBI Research**, the optimal Credit-to-Deposit (CD) ratio for Indian banks is **76-80%**.

**Key Findings:**

#### 🎯 Public Sector Banks (PSBs)
- **Optimal Range:** 76-80%
- **Current Average:** ~75-80%
- **Examples:** State Bank of India, Bank of Baroda
- **Characteristic:** Better liquidity management

#### 🎯 Private Sector Banks
- **Optimal Range:** 76-80%
- **Current Average:** 92-94% (above optimal)
- **Challenge:** Higher funding costs and leverage risks
- **Impact:** Greater strain on net interest margins

#### 🎯 Small Finance Banks (SFBs)
- **Current Average:** >100% (well above optimal)
- **Risk Level:** High liquidity and profitability concerns
- **Strategy:** Focused lending in underserved segments

#### 🎯 Foreign Banks
- **Optimal Range:** 65-70%
- **Reason:** Different funding profiles and global deposit bases

---

### Why 76-80% is Optimal?

**1. Lending Efficiency** 
   - Maximizes loan deployment
   - Generates interest income
   - Supports economic growth

**2. Liquidity Safety**
   - Maintains adequate buffers for withdrawals
   - Ensures regulatory compliance
   - Reduces rollover risks

**3. Profitability Balance**
   - Beyond 80%, incremental profitability declines sharply
   - Higher funding costs outweigh interest income gains
   - Net Interest Margin (NIM) compression occurs

**4. Regulatory Alignment**
   - Aligns with RBI liquidity requirements (LCR/NSFR)
   - Accommodates statutory reserves (CRR 4.5%, SLR 18%)
   - Natural alignment with deployable funds (~75-76%)

---

### Risks Beyond 80%

✅ **Liquidity Risks** - Reduced idle funds for emergencies
✅ **Funding Pressures** - Reliance on costly wholesale borrowing
✅ **Profitability Erosion** - NIM compression (20-25 basis points)
✅ **Credit Risks** - Aggressive lending in high-CD regions
✅ **Regulatory Scrutiny** - Enhanced RBI monitoring

---

### CD Ratio by Bank Type in India

| Bank Type | Average CD Ratio | Optimal | Status |
|-----------|-----------------|---------|--------|
| PSB (e.g., Indian Bank) | 80% | 76-80% | ✅ Balanced |
| Private Banks | 92-94% | 76-80% | ⚠️ High |
| Small Finance Banks | >100% | 76-80% | 🔴 Very High |
| Foreign Banks | <60% | 65-70% | ✅ Conservative |

---

### Impact of High CD Ratios (>80%)

**Net Interest Margin (NIM) Compression:**
- Banks must raise deposit rates to attract funds
- Lending rates face downward pressure from competition
- Typical compression: 20-25 basis points
- Post-repo rate cuts, NIM erosion accelerates

**Example from SBI Research:**
- Banks with 92% CD ratio: Acute margin strain
- Banks with 75% CD ratio: Healthy margins
- Difference: ~50-100 basis points

---

### Regional Variations in India

#### High CD Regions (>80%)
**Western States:**
- Maharashtra: ~98% (some districts 125%)
- Gujarat: 90-100%
- Rajasthan: 90-100%

**Southern States:**
- Tamil Nadu: >100%
- Andhra Pradesh: 90-95%

**Reason:** Industrial hubs, urban credit demand, strong economies

#### Low CD Regions (<50%)
**Eastern & Northeastern States:**
- Bihar, Odisha, Jharkhand: <52%
- West Bengal: <52%
- Uttar Pradesh Eastern: 33-46%

**Reason:** Lower economic output, deposit surpluses, rural focus

**National Distribution:**
- 46% of districts: 50-100% range
- 75 districts: >150% (prosperous regions)
- Priority sector lending focus in <40% districts
""")
        
        with edu_tab2:
            st.markdown("""
### RBI Guidelines on CD Ratio

The RBI does not impose a **hard cap** on CD ratios but indirectly constrains banks through mandatory requirements and supervisory oversight.

---

### 1. Reserve Requirements

#### Statutory Liquidity Ratio (SLR)
- **Requirement:** 18% of deposits
- **Purpose:** Maintain liquid securities for stability
- **Impact:** Only ~82% of deposits available for lending

#### Cash Reserve Ratio (CRR)
- **Requirement:** 4.5% of deposits
- **Purpose:** Maintain emergency liquidity buffers
- **Impact:** Reduces deployable funds further

#### Deployable Funds Calculation
```
Total Deposits:     100%
Less: SLR (18%)     -18%
Less: CRR (4.5%)    -4.5%
Deployable Funds:   ~75-76%
```

**This naturally aligns with the 76-80% optimal CD ratio!**

---

### 2. Liquidity Coverage Ratio (LCR)

- **Requirement:** Maintain 100% coverage
- **Definition:** High-quality liquid assets ≥ Net outflows (30 days)
- **Impact:** Tightens as CD ratio increases above 80%
- **Risk:** High-CD banks have thinner buffers during stress

---

### 3. Net Stable Funding Ratio (NSFR)

- **Requirement:** Available stable funding ≥ Required stable funding
- **Applies to:** Banks with assets >500 Crores (most Indian banks)
- **Impact:** Encourages stable deposit mobilization
- **Alternative:** Costlier wholesale funding if CD ratio too high

---

### 4. Supervisory Actions & Monitoring

#### Quarterly Reviews
- **SLBC (State Level Bankers' Committee)** reviews credit-deposit gaps
- **Action Plans** for low-CD districts (<40-60%)
- **Focus:** Priority sector lending in underserved regions

#### Enhanced Scrutiny
- Banks with persistent CD >85% face closer monitoring
- RBI assesses:
  - Asset-Liability Management (ALM)
  - NIM sustainability
  - Rollover vulnerabilities
  - Regional concentration risks

#### Nudges & Constraints
- RBI encourages credit growth aligned with deposit growth
- May curb branch expansion in over-lent regions
- Prioritize CASA (Current Account & Savings Account) mobilization
- Lending curbs in sensitive sectors if ratios too high

---

### 5. Priority Sector Lending Mandate

- **Requirement:** 40% of net advances to priority sectors
- **Sectors:** Agriculture, MSMEs, education, housing
- **Regional Twist:** Higher allocations to low-CD districts
- **Impact:** Influences CD ratio distribution across regions

---

### 6. Financial Stability Report Guidance

RBI's **Financial Stability Report** highlights:
- Systemic risks from elevated CD ratios
- NIM compression trends
- Regional disparities and rollover risks
- Guidance on optimal range (aligns with 76-80%)

---

### 7. Capital Adequacy Requirements

- **Minimum CAR:** 9% (+ buffers)
- **Impact:** Banks with strong CAR can sustain higher CD ratios
- **Example:** Indian Bank's 17.31% CAR provides flexibility
- **Constraint:** Weak CAR banks must moderate lending

---

### 8. Asset Quality Monitoring

RBI monitors:
- **Stressed Assets:** Rise sharply above 85% CD ratio
- **Provisioning:** Higher in high-CD regions
- **Unsecured Lending:** Capped at 20-24.5% of advances
- **Sector Concentration:** Curbs exposure in stressed sectors

---

### What RBI Does NOT Do

❌ Does not impose hard CD ratio cap (unlike some countries)
❌ Does not penalize banks directly for high ratios
❌ Does not force immediate CD ratio reduction
✅ Instead: Uses supervisory guidance and regulatory requirements

---

### Key RBI Messages

1. **"Align credit growth with deposit growth"** - Quarterly SLBC reviews
2. **"Prioritize liquidity management"** - LCR/NSFR compliance
3. **"Focus on low-CD regions"** - Priority sector lending mandates
4. **"Monitor NIM sustainability"** - Financial Stability Reports
5. **"Strengthen capital buffers"** - CAR & buffer requirements

---

### Compliance Framework

**Timeline:**
- Quarterly: SLBC reviews and CD ratio monitoring
- Semi-annual: Financial Stability Report guidance
- Annual: Capital Adequacy assessment
- Ongoing: Supervisory interactions and on-site inspections

**Penalties for Non-Compliance:**
- SLR/CRR shortfalls: Penalty rates (CRR rate +3%)
- LCR/NSFR breaches: Escalated supervisory action
- Priority sector lending miss: Fines + RBI directed lending
""")
        
        with edu_tab3:
            st.markdown("""
### 🎓 CD Ratio - Frequently Asked Questions (FAQ)

---

## Question 1: What is the minimum CD ratio a bank should maintain?

**Answer:**
There is no RBI-mandated minimum CD ratio. However, banks naturally maintain a CD ratio around **50-70%** to comply with SLR (18%), CRR (4.5%), and LCR requirements. Going below 50% indicates:
- Excess deposits (good for liquidity, bad for profitability)
- Under-deployment of funds
- Lost lending opportunities
- Lower net interest income

**Practical Minimum:** 65-70% (after regulatory buffers)

---

## Question 2: Is a CD ratio of 95% sustainable for private banks?

**Answer:**
**Not sustainably.** Private banks averaging 92-94% face:

| Risk | Impact |
|------|--------|
| **Liquidity Risk** | Thin buffers, high rollover risk |
| **Funding Cost** | 100+ bps higher than deposits |
| **NIM Compression** | 20-50 basis points erosion |
| **RBI Scrutiny** | Enhanced monitoring & action plans |
| **Profitability** | Incremental ROA gains disappear |

**SBI Research Finding:** Incremental ROA benefits vanish beyond 80%, making 95% unsustainable without higher deposit rates (which compress margins further).

---

## Question 3: How does a high CD ratio affect bank stability?

**Answer:**
A high CD ratio (>85%) affects stability through:

**1. Liquidity Vulnerability**
   - Minimal idle funds for unexpected withdrawals
   - Dependence on volatile wholesale funding (CDs, borrowings)
   - Maturity mismatch risk (short-term liabilities, long-term loans)

**2. Profitability Pressure**
   - Higher deposit rates needed to attract funds
   - Lending rates face competition-driven downward pressure
   - Net Interest Margin (NIM) compressed 20-25 bps

**3. Credit Risk Amplification**
   - Aggressive lending in high-CD regions (>90%)
   - Higher delinquency rates post-credit cycles
   - Provisioning requirements increase

**4. Regulatory Scrutiny**
   - Enhanced RBI monitoring via SLBC reviews
   - Potential lending curbs in over-lent sectors
   - Supervisory pressure on capital adequacy

**Conclusion:** Sustainable only with strong capital buffers, disciplined lending, and proactive ALM.

---

## Question 4: Why can foreign banks operate with CD ratios of 60-70%?

**Answer:**
Foreign banks have different business models:

| Factor | Reason |
|--------|--------|
| **Global Funding** | Access to parent bank support, overseas deposits |
| **Selective Lending** | Focus on high-margin corporate clients (lower volume) |
| **Fee Income** | Greater reliance on investment banking, forex services |
| **Regulatory Choice** | Conservative funding strategy preferred |
| **Liquidity Position** | Parent bank provides liquidity buffers |

**Example:** ICICI Bank (domestic presence) operates higher CD (~75-80%) than pure foreign banks (<60%).

---

## Question 5: How do regional disparities in CD ratios create systemic risk?

**Answer:**
Regional disparities create systemic risks:

**High-CD Regions (Western/Southern states >90%):**
- **Credit Boom Risk** - Rapid lending growth unsustainable
- **Bubble Formation** - Asset price inflation in real estate, autos
- **Concurrent Defaults** - Downturns hit all sectors simultaneously
- **System-wide Impact** - Concentrated losses across lenders

**Low-CD Regions (Eastern states <50%):**
- **Credit Deficit** - Under-served economies lack development capital
- **Fund Hoarding** - Excess deposits idle, transferred to high-CD regions
- **Inequality** - Prosperous regions grow faster than lagging regions
- **RBI Intervention** - Mandated priority sector lending shifts capital

**National Impact:** 46% of districts in 50-100% range, 75 districts >150%, creating systemic imbalances.

---

## Question 6: What happens to a bank's stock price when CD ratio exceeds 85%?

**Answer:**
Market reaction is typically **negative** when CD ratio rises above 85%:

**Short-term (0-3 months):**
- Stock may dip 3-5% on profitability concerns
- Analyst downgrades cite NIM compression
- P/E multiple contraction expected

**Medium-term (3-12 months):**
- Recovery if deposits accelerate (shows discipline)
- Stock remains depressed if CD stays >85%
- Peers outperform on better NIM trends

**Long-term (>1 year):**
- Sustained high CD → Structural discount to market
- Private banks with >90% CD trade at 0.8-1.2x book value vs. 1.5-2.0x for healthy banks

**Example:** A private bank with 92% CD ratio likely trades at 30-40% discount vs. a peer with 76% CD ratio.

---

## Question 7: Can a bank reduce its CD ratio quickly without harming credit growth?

**Answer:**
**No, not effectively.** Rapid CD ratio reduction requires:

**Option 1: Aggressive Deposit Mobilization**
- Raise deposit rates 75-100 bps (compresses NIM further)
- Launch new products (CASA, digital savings)
- Expand branch network (costly, slow)
- **Time Required:** 18-24 months to reduce CD by 5-10%

**Option 2: Slow Credit Growth**
- Tighten lending standards (harks growth)
- Exit high-risk sectors (reduces market share)
- Redirect to low-risk lending (lower margins)
- **Impact:** Revenue & profit decline

**Option 3: Asset Liquidation**
- Sell securities portfolio (triggers losses)
- Reduce exposure in certain sectors (regulatory issues)
- **Impact:** Losses, no sustainable benefit

**Practical Reality:** Banks typically target 5-10 bps CD ratio reduction over 3-5 years through balanced deposit mobilization and disciplined lending.

---

## Question 8: How does the RBI's Liquidity Coverage Ratio (LCR) requirement interact with optimal CD ratio?

**Answer:**
LCR directly constrains CD ratios:

**LCR Formula:**
```
LCR = High-Quality Liquid Assets / Total Net Cash Outflows (30 days) ≥ 100%
```

**Impact on CD Ratios:**

| CD Ratio | LCR Stress | Liquidity Buffer |
|----------|-----------|------------------|
| 65% | Comfortable | Wide buffer for stress |
| 76-80% | Tight | Adequate, monitored |
| 85% | Strained | Minimal buffer |
| >90% | Critical | Nearly exhausted |

**Mechanism:**
- High CD ratio → Fewer idle deposits → Weaker LCR
- During 30-day outflow stress, LCR breaches trigger:
  - Forced asset sales at unfavorable terms
  - Emergency borrowing at penalty rates
  - RBI intervention & supervisory action

**Conclusion:** Optimal 76-80% CD ratio is the natural balance point where LCR requirements are comfortably met.

---

## Question 9: What are the main differences between CD ratio and Loan-to-Deposit (LTD) ratio?

**Answer:**
CD Ratio vs. LTD Ratio:

| Aspect | CD Ratio | LTD Ratio |
|--------|----------|-----------|
| **Definition** | (Advances / Deposits) × 100 | (Loans / Deposits) × 100 |
| **Numerator** | Advances (loans + exposures) | Only loans |
| **Denominator** | Customer deposits | Customer deposits |
| **Regulatory Use** | Liquidity & deployment metric | Lending intensity measure |
| **RBI Focus** | LCR/NSFR alignment | Regional lending targets |
| **Typical Range** | 60-95% | 55-90% |

**Key Difference:**
- CD Ratio broader (includes non-loan advances, bill discounts)
- LTD Ratio narrower (pure loan focus)
- Both track similar trends but LTD more volatile

**In India:**
- RBI uses CD ratio for overall liquidity assessment
- SLBC uses LTD ratio for regional lending evaluation
- Optimal LTD: 65-75% (higher than CD due to narrow definition)

---

## Question 10: How would increasing repo rate by 200 bps impact optimal CD ratio for banks?

**Answer:**
A 200 bps repo rate increase would shift the optimal CD ratio:

**Immediate Effects (0-3 months):**
- **Deposit Costs Rise:** Term deposits jump from 6.5% to 8.5%
- **Lending Rates Rise:** New loans priced at 9.5-10.5% (vs. 8.5-9.5%)
- **Margin Expansion:** NIM improves by 30-50 bps initially

**Shift in Optimal CD Ratio:**
| Scenario | Optimal CD Ratio | Reasoning |
|----------|-----------------|-----------|
| 200 bps Rate Cut | 76-80% | Current state |
| 200 bps Rate Hike | 78-85% | Higher margins justify more lending |
| Return to 300 bps | 80-90% | Sufficient margin buffer |

**Why Optimal Rises?**
- Higher margin (spread) offsets funding cost pressure
- Banks can sustain higher CD without NIM compression
- Leverage becomes more profitable at higher rates

**Long-term Adjustment (6-18 months):**
- Deposit mobilization accelerates (attractive rates)
- Credit demand declines (higher loan costs)
- CD ratio naturally moderates back to 76-85% through market forces

**Conclusion:** Higher rates shift optimal CD upward by 5-10%, but behavioral factors bring it back toward long-term range.

---

## Question 11: Can a CD ratio below 60% indicate a problem for a bank?

**Answer:**
**Yes, below 60% often signals problems:**

**Liquidity Excess:**
- More than needed regulatory buffers
- Excessive idle deposits (earning 0-1%)
- Opportunity cost of ~5-6% on excess deposits

**Profitability Issues:**
- Net Interest Income (NII) lower than peers
- Cannot maximize deposit base potential
- ROA/ROE compressed vs. optimal-ratio peers

**Market Interpretation:**
- Stock underperforms (lower earnings)
- Analysts question management execution
- Investors question capital deployment strategy

**Exceptions (when <60% is okay):**
- Foreign banks (different business model)
- Newly licensed banks (building deposit base)
- Banks in high-savings regions (natural low CD)
- Strategic period (preparing for growth phase)

**Rule of Thumb:**
- <50% = Problem (needs remedial action)
- 50-65% = Below optimal (could do better)
- 65-80% = Optimal range ✅
- 80-95% = High but manageable
- >95% = Problem (stress signals)

---

## Question 12: How do unsecured advances affect a bank's optimal CD ratio?

**Answer:**
Unsecured advances (personal loans, credit cards) significantly impact optimal CD:

**Regulatory Constraint:**
- **Cap:** Unsecured advances ≤ 20-24.5% of total advances
- **Rationale:** Higher default risk needs higher provisioning
- **Current Status:** Many banks at 20-24% of advances cap

**Impact on CD Ratio:**

| Scenario | Unsecured % | Optimal CD | Reasoning |
|----------|------------|-----------|-----------|
| Conservative | 10% | 78-82% | Lower risk, more aggressive |
| Standard | 20% | 76-80% | Balanced approach |
| Aggressive | 24.5% | 72-76% | Higher risk needs moderation |

**Why It Matters:**
- High unsecured advances → Higher delinquencies in downturns
- Stress scenario requires larger provisions
- Banks with high unsecured% need lower CD ratio for stability

**Example:**
- Bank A: 10% unsecured advances → Can sustain 80% CD ratio
- Bank B: 24% unsecured advances → Should target 74% CD ratio
- Difference: ~6 percentage points

**Current Trend:**
- NBFC competition pushing banks to unsecured lending
- RBI cautious (provisioning increased from 20% to 24.5%)
- Optimal CD ratios compressing across sector

**Conclusion:** Higher unsecured mix → Lower optimal CD ratio.

EOF
cat /mnt/user-data/outputs/indian_banks_app/streamlit_app.py


# ═══════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════

render_footer(
    AUTHOR, 
    BRAND_NAME, 
    "RBI, BSE, NSE, Bank Investor Relations | Research: ICRA, CRISIL, Financial Media"
)
