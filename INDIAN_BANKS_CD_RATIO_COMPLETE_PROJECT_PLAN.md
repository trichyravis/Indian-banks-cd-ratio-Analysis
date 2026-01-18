# Indian Banks CD Ratio Analysis Dashboard
## Comprehensive Project Plan & Technical Architecture

**Project Name:** Indian Banking Insights - CD Ratio Analysis & Stress Testing Platform
**Version:** 1.0.0 (MVP)
**Status:** Project Initiation
**Last Updated:** January 18, 2025

---

## 📋 TABLE OF CONTENTS

1. [Research Framework & Academic Positioning](#1-research-framework--academic-positioning)
2. [Data Architecture & Sources](#2-data-architecture--sources)
3. [Metrics & Formulas](#3-metrics--formulas)
4. [Data Pipeline](#4-data-pipeline)
5. [Dashboard Architecture](#5-dashboard-architecture)
6. [Visual Design System](#6-visual-design-system)
7. [Analytical Layers](#7-analytical-layers)
8. [Interpretation Framework](#8-interpretation-framework)
9. [Deployment Strategy](#9-deployment-strategy)
10. [Future Enhancements](#10-future-enhancements)

---

## 1. RESEARCH FRAMEWORK & ACADEMIC POSITIONING

### 1.1 Research Objective

**Primary Objective:**
Develop a data-driven framework to analyze and interpret Credit-to-Deposit (CD) ratios across Indian banking sector, enabling:
- Real-time monitoring of banking sector health indicators
- Comparative analysis of lending capacity utilization
- Early warning signals for liquidity stress
- Investment decision support for equity and credit market participants

**Academic Context:**
The CD ratio serves as a critical proxy for:
- **Banking Sector Liquidity:** Measures deposit float vs. credit deployment
- **Growth Phase Identification:** Rising CD = expansion phase; Falling CD = credit stress
- **Systemic Risk Indicators:** Aggregate CD ratios signal macro banking health
- **Asset-Liability Management (ALM):** Banks balance liquidity coverage with earning assets

### 1.2 Research Questions

**Primary Questions:**
1. What are current CD ratios across major Indian bank categories?
2. How does CD ratio evolution indicate banking sector credit cycles?
3. Are there early warning signals for liquidity stress?
4. What are optimal CD ranges for different bank types?
5. How do CD ratios correlate with profitability and risk metrics?

**Secondary Questions:**
6. What deposit-advance growth divergence patterns exist?
7. Which lending segments (retail, corporate, MSME) drive CD changes?
8. How does RBI policy (rate changes, CRR, SLR) impact CD ratios?
9. Can CD ratios predict NPA trends and credit cycles?
10. What are stress scenarios for banking sector liquidity?

### 1.3 Hypothesis & Framework

**Core Hypothesis:**
"CD ratios in the 70-80% band indicate optimal balance between growth and liquidity safety. Ratios above 85% signal liquidity stress risk; below 65% indicate underutilized lending capacity."

**Analytical Framework:**
```
CD Ratio Analysis
├── Descriptive Analytics
│   ├── Current state (Q3 FY25)
│   ├── Historical trends (7 quarters)
│   └── Cross-sectional comparisons
├── Diagnostic Analytics
│   ├── Deposit-advance divergence
│   ├── Growth decomposition
│   └── Risk indicators
├── Predictive Analytics
│   ├── Trend projections
│   ├── Stress scenarios
│   └── Early warning signals
└── Prescriptive Analytics
    ├── Optimal CD bands
    ├── Policy implications
    └── Investment signals
```

---

## 2. DATA ARCHITECTURE & SOURCES

### 2.1 Exact Public Data Sources

#### **TIER 1: Official Regulatory Data (Mandatory, Most Reliable)**

**Source 1: RBI (Reserve Bank of India)**

```
Primary Website: https://www.rbi.org.in/
Key Publications:
├── Monthly Banking Statistics
│   ├── URL: https://www.rbi.org.in/Scripts/PublicationsListLatest.aspx
│   ├── Format: Excel, PDF
│   ├── Frequency: Monthly
│   ├── Key Tables:
│   │   ├── Table 1: Bank-wise Deposits
│   │   ├── Table 2: Bank-wise Advances
│   │   ├── Table 3: Advances by Category
│   │   └── Table 4: Deposits by Category
│   └── Data Quality: ⭐⭐⭐⭐⭐ (Official)
├── Financial Stability Report
│   ├── Frequency: Semi-annual (June & December)
│   ├── Contains: Sector-wide CD ratios, stress tests
│   └── Key Metrics: Liquidity ratios, capital adequacy
├── Monetary Policy Statements
│   ├── Frequency: Bi-monthly
│   ├── Impact: Policy rates affect deposit/advance dynamics
│   └── Relevance: Context for CD ratio interpretation
└── Banking Regulation Department Reports
    ├── Contains: Supervisory data, NPA trends
    └── Key for: Liquidity stress analysis
```

**Data Access Implementation:**
```python
import pandas as pd
import requests
from datetime import datetime

class RBIDataFetcher:
    def __init__(self):
        self.base_url = "https://www.rbi.org.in/"
        self.data_folder = "data/rbi_monthly_stats/"
    
    def fetch_latest_monthly_stats(self):
        """
        Fetch latest RBI monthly banking statistics
        Sources: Excel files from RBI website
        """
        # URL pattern for monthly releases
        year = datetime.now().year
        month = datetime.now().month
        
        urls = {
            'deposits': f"{self.base_url}scripts/bankingstats_deposits_{year}_{month}.xlsx",
            'advances': f"{self.base_url}scripts/bankingstats_advances_{year}_{month}.xlsx",
        }
        
        data = {}
        for key, url in urls.items():
            try:
                # Download and parse
                df = pd.read_excel(url)
                data[key] = df
                print(f"✅ Fetched {key} data successfully")
            except:
                print(f"⚠️ Failed to fetch {key} from RBI")
        
        return data
    
    def parse_bank_wise_deposits_advances(self, df_deposits, df_advances):
        """Parse bank-wise deposits and advances"""
        # Extract scheduled commercial banks data
        scheduled_banks = df_deposits[df_deposits['Category'] == 'Scheduled Commercial Banks']
        
        # Merge deposits and advances
        merged = pd.merge(
            scheduled_banks[['Bank_Name', 'Deposits_Crores']],
            df_advances[['Bank_Name', 'Advances_Crores']],
            on='Bank_Name'
        )
        
        # Calculate CD ratio
        merged['CD_Ratio'] = (merged['Advances_Crores'] / merged['Deposits_Crores']) * 100
        
        return merged
```

---

**Source 2: Stock Exchange Filings (BSE/NSE)**

```
BSE Website: https://www.bseindia.com/
NSE Website: https://www.nseindia.com/

Corporate Action Data:
├── Quarterly Financial Results
│   ├── Format: PDF (Corporate Announcements), HTML
│   ├── Frequency: Within 45 days of quarter-end
│   ├── Data Points:
│   │   ├── Balance Sheet → Total Deposits (Liabilities)
│   │   ├── Balance Sheet → Total Advances (Assets)
│   │   ├── Notes → Segment-wise advances breakdown
│   │   └── MDA → Management commentary
│   ├── Access: Free via corporate action search
│   └── Data Quality: ⭐⭐⭐⭐⭐ (Mandatory regulatory filing)
├── Stock Exchange Announcements
│   ├── Format: PDF, TXT
│   ├── Contains: Earnings summaries
│   └── Useful for: Quick reference data
└── Investor Presentations
    ├── Format: PDF, PowerPoint
    ├── Frequency: Post-results
    └── Contains: Management guidance, trends
```

**Implementation:**
```python
import pdfplumber
from bs4 import BeautifulSoup
import requests

class StockExchangeFetcher:
    def __init__(self):
        self.bse_url = "https://www.bseindia.com/corporates/"
        self.nse_url = "https://www.nseindia.com/"
    
    def fetch_quarterly_results(self, bank_name, quarter, fiscal_year):
        """
        Fetch quarterly results from stock exchange
        quarter: 'Q1', 'Q2', 'Q3', 'Q4'
        fiscal_year: 2025 (for FY2025)
        """
        # Search for announcements
        search_url = f"{self.bse_url}corpann_search.aspx"
        
        params = {
            'company': bank_name,
            'fromdate': self.get_quarter_start_date(quarter, fiscal_year),
            'todate': self.get_quarter_end_date(quarter, fiscal_year),
            'announcementtype': 'Financial Results'
        }
        
        response = requests.get(search_url, params=params)
        # Parse results and download PDF
        return self.extract_financial_data_from_pdf(response)
    
    def extract_financial_data_from_pdf(self, pdf_path):
        """Extract balance sheet data from quarterly results PDF"""
        with pdfplumber.open(pdf_path) as pdf:
            data = {
                'deposits': None,
                'advances': None,
                'quarter': None,
                'date': None
            }
            
            for page in pdf.pages:
                text = page.extract_text()
                tables = page.extract_tables()
                
                # Find balance sheet table
                for table in tables:
                    df = pd.DataFrame(table[1:], columns=table[0])
                    
                    # Extract deposits
                    deposits_row = df[df[0].str.contains('Deposits', case=False, na=False)]
                    if not deposits_row.empty:
                        data['deposits'] = float(deposits_row.iloc[0, 1].replace(',', ''))
                    
                    # Extract advances
                    advances_row = df[df[0].str.contains('Advances', case=False, na=False)]
                    if not advances_row.empty:
                        data['advances'] = float(advances_row.iloc[0, 1].replace(',', ''))
            
            return data
```

---

**Source 3: Individual Bank Investor Relations Websites**

```
Major Banks & IR Portals:

PUBLIC SECTOR BANKS:
├── SBI: https://www.sbi.co.in/investor-relations/
│   └── Path: /financial-results/quarterly/
├── Bank of Baroda: https://www.bankofbaroda.in/investor-relations/
│   └── Path: /financial-results/
├── PNB: https://www.pnbindia.in/investor-relations/
│   └── Path: /quarterly-results/
├── Union Bank: https://www.unionbankofindia.co.in/investor-relations/
│   └── Path: /results-announcements/
└── [5+ more PSBs follow similar structure]

PRIVATE BANKS:
├── HDFC Bank: https://investor.hdfcbank.com/financial-information/
│   └── Files: Quarterly results (PDF), Investor presentations
├── ICICI Bank: https://www.icicibank.com/investor-relations/
│   └── Files: Financial results, Annual reports
├── Axis Bank: https://www.axisbank.com/investors/financial-results/
│   └── Files: Q results, MD&A sections
└── [More private banks...]

SMALL FINANCE BANKS:
├── AU Small Finance: https://www.aubank.in/investor-relations/
├── Ujjivan SFB: https://www.ujjivan.com/investor-relations/
└── [SFBs list...]

Data Extract Pattern:
├── Q1 Results (July 15-31)
├── Q2 Results (October 15-31)
├── Q3 Results (January 15-31)
└── Q4 Results (May 15-31)
```

**Implementation:**
```python
import os
from pathlib import Path

class BankIRFetcher:
    def __init__(self):
        self.banks_ir_config = {
            'SBI': {
                'base_url': 'https://www.sbi.co.in/investor-relations/',
                'results_path': '/financial-results/quarterly/',
                'ticker': 'SBIN'
            },
            'HDFC Bank': {
                'base_url': 'https://investor.hdfcbank.com/',
                'results_path': '/financial-information/',
                'ticker': 'HDFCBANK'
            },
            # ... all 28 banks
        }
    
    def download_quarterly_reports(self, bank_name, quarter, fiscal_year):
        """
        Download quarterly reports from bank IR website
        Stores locally for extraction
        """
        config = self.banks_ir_config.get(bank_name)
        if not config:
            return None
        
        # Construct URL pattern
        quarter_folder = f"q{quarter[1]}_fy{fiscal_year}"
        url = f"{config['base_url']}{config['results_path']}{quarter_folder}/"
        
        try:
            response = requests.get(url)
            pdf_links = self.extract_pdf_links(response.content)
            
            # Download PDFs
            local_folder = f"data/bank_reports/{bank_name}/{fiscal_year}/"
            os.makedirs(local_folder, exist_ok=True)
            
            for pdf_link in pdf_links:
                pdf_response = requests.get(pdf_link)
                filename = pdf_link.split('/')[-1]
                filepath = os.path.join(local_folder, filename)
                
                with open(filepath, 'wb') as f:
                    f.write(pdf_response.content)
                
                print(f"✅ Downloaded {filename}")
            
            return local_folder
        except Exception as e:
            print(f"❌ Error downloading {bank_name}: {e}")
            return None
    
    def extract_deposits_advances(self, pdf_path):
        """Extract deposits and advances from balance sheet"""
        import pdfplumber
        
        deposits = None
        advances = None
        
        with pdfplumber.open(pdf_path) as pdf:
            # Typically balance sheet is page 1-2
            for page_num in range(min(3, len(pdf.pages))):
                page = pdf.pages[page_num]
                tables = page.extract_tables()
                
                for table in tables:
                    df = pd.DataFrame(table)
                    
                    # Search for deposits (usually in liabilities)
                    for idx, row in df.iterrows():
                        cell_text = str(row[0]).lower() if row[0] else ""
                        
                        if 'deposit' in cell_text and deposits is None:
                            try:
                                deposits = float(str(row[1]).replace(',', ''))
                            except:
                                pass
                        
                        if 'advance' in cell_text and advances is None:
                            try:
                                advances = float(str(row[1]).replace(',', ''))
                            except:
                                pass
        
        return {'deposits': deposits, 'advances': advances}
```

---

#### **TIER 2: Secondary Data Sources**

**Source 4: Credit Rating Agency Reports**

```
ICRA: https://www.icra.in/research/
├── Banking Sector Reports (Quarterly)
├── Individual Bank Ratings & Reports
└── Data: CD ratio analysis, sector comparisons

CRISIL: https://www.crisil.com/research
├── Banking Sector Outlook
├── Individual Bank Reviews
└── Emerging Trends in Banking

Access:
├── Free reports: Public research
├── Paid reports: Detailed analysis
└── Data: Supplementary validation, sector context
```

**Source 5: Financial Data APIs**

```
Financial Modeling Prep:
├── URL: https://financialmodelingprep.com/
├── Endpoint: /balance-sheet-statement/{ticker}
├── Format: JSON
├── Frequency: Quarterly (auto-updated)
└── Cost: Free tier (limited calls), Paid tiers

Alpha Vantage:
├── URL: https://www.alphavantage.co/
├── Endpoint: /query?function=BALANCE_SHEET
├── Format: JSON
└── Cost: Free tier available

Twelve Data:
├── URL: https://twelvedata.com/
├── Features: Real-time financial data
└── Cost: Paid API
```

---

### 2.2 Data Dictionary

```python
# Complete data schema for CD Ratio dashboard

BANK_MASTER_DATA = {
    'bank_id': str,              # Unique identifier (e.g., 'SBI001')
    'bank_name': str,            # Full name
    'bank_type': str,            # 'PSB', 'Private', 'SFB'
    'headquarters': str,         # City
    'nse_ticker': str,           # NSE listing symbol
    'bse_ticker': str,           # BSE listing symbol
    'established_year': int,
    'total_branches': int,
    'total_employees': int,
}

QUARTERLY_CD_DATA = {
    'bank_id': str,
    'fiscal_year': int,          # 2024, 2025, etc.
    'quarter': str,              # 'Q1', 'Q2', 'Q3', 'Q4'
    'quarter_end_date': date,
    
    # Core metrics
    'total_deposits_crores': float,
    'total_advances_crores': float,
    'cd_ratio_percent': float,   # Calculated: (advances/deposits)*100
    
    # Deposit breakdown
    'deposits_savings_crores': float,
    'deposits_current_crores': float,
    'deposits_term_crores': float,
    
    # Advance breakdown
    'advances_retail_crores': float,
    'advances_corporate_crores': float,
    'advances_msme_crores': float,
    'advances_agricultural_crores': float,
    
    # Risk metrics
    'npa_gross_crores': float,
    'npa_gross_ratio_percent': float,
    'npa_net_crores': float,
    'npa_net_ratio_percent': float,
    'provisions_crores': float,
    
    # Capital metrics
    'capital_adequacy_ratio_percent': float,
    'tier1_capital_ratio_percent': float,
    
    # Growth metrics
    'deposit_growth_yoy_percent': float,
    'advance_growth_yoy_percent': float,
    'cd_ratio_change_qoq_points': float,
    
    # Source & quality
    'data_source': str,          # 'RBI', 'BSE', 'Bank_IR'
    'extraction_date': datetime,
    'data_quality_flag': str,    # 'Verified', 'Preliminary', 'Estimated'
}

SECTOR_AGGREGATE_DATA = {
    'quarter_end_date': date,
    'fiscal_year': int,
    'quarter': str,
    
    'sector_cd_ratio_percent': float,
    'sector_deposits_crores': float,
    'sector_advances_crores': float,
    
    'psb_cd_ratio_percent': float,
    'psb_count': int,
    'psb_deposits_crores': float,
    'psb_advances_crores': float,
    
    'private_cd_ratio_percent': float,
    'private_count': int,
    'private_deposits_crores': float,
    'private_advances_crores': float,
    
    'sfb_cd_ratio_percent': float,
    'sfb_count': int,
    'sfb_deposits_crores': float,
    'sfb_advances_crores': float,
    
    'sector_npa_gross_ratio_percent': float,
    'sector_capital_adequacy_percent': float,
    'sector_deposit_growth_yoy_percent': float,
    'sector_advance_growth_yoy_percent': float,
}
```

---

## 3. METRICS & FORMULAS

### 3.1 Core CD Ratio Metrics

```python
"""
PRIMARY METRIC: Credit-to-Deposit Ratio
"""

CD_RATIO = (Total_Advances / Total_Deposits) × 100

# Example calculation
def calculate_cd_ratio(advances_crores, deposits_crores):
    """
    Calculate CD Ratio
    
    Args:
        advances_crores: Total advances in crores (rupees)
        deposits_crores: Total deposits in crores (rupees)
    
    Returns:
        cd_ratio: CD ratio as percentage
    
    Interpretation:
        70-80%: Healthy range
        <70%: Underutilized capacity
        >85%: Aggressive lending, liquidity risk
    """
    if deposits_crores <= 0:
        return None
    
    cd_ratio = (advances_crores / deposits_crores) * 100
    return round(cd_ratio, 2)


"""
SECONDARY METRICS: Growth Decomposition
"""

# Year-over-Year Deposit Growth
DEPOSIT_GROWTH_YOY = ((Deposits_Current_Year - Deposits_Previous_Year) / 
                      Deposits_Previous_Year) × 100

def calculate_deposit_growth_yoy(current_deposits, previous_year_deposits):
    """Calculate YoY deposit growth rate"""
    if previous_year_deposits <= 0:
        return None
    
    growth = ((current_deposits - previous_year_deposits) / previous_year_deposits) * 100
    return round(growth, 2)


# Year-over-Year Advance Growth
ADVANCE_GROWTH_YOY = ((Advances_Current_Year - Advances_Previous_Year) / 
                      Advances_Previous_Year) × 100

def calculate_advance_growth_yoy(current_advances, previous_year_advances):
    """Calculate YoY advance growth rate"""
    if previous_year_advances <= 0:
        return None
    
    growth = ((current_advances - previous_year_advances) / previous_year_advances) * 100
    return round(growth, 2)


# Growth Divergence Analysis
GROWTH_DIVERGENCE = Advance_Growth_YoY - Deposit_Growth_YoY

def calculate_growth_divergence(advance_growth, deposit_growth):
    """
    Calculate growth divergence
    
    Interpretation:
        Positive divergence (>0): Advances growing faster → CD ratio rising
        Negative divergence (<0): Deposits growing faster → CD ratio falling
        Zero divergence: Balanced growth → CD ratio stable
    
    Strategic Meaning:
        +5%+: Credit cycle expansion, aggressive lending
        +2% to +5%: Moderate credit expansion
        -2% to +2%: Balanced growth
        -5% to -2%: Deposit accumulation, credit slowdown
        <-5%: Significant credit stress
    """
    divergence = advance_growth - deposit_growth
    return round(divergence, 2)


"""
TERTIARY METRICS: Segment-wise CD Ratios
"""

# Retail CD Ratio
RETAIL_CD = (Retail_Advances / Total_Deposits) × 100

# Corporate CD Ratio
CORPORATE_CD = (Corporate_Advances / Total_Deposits) × 100

# MSME CD Ratio
MSME_CD = (MSME_Advances / Total_Deposits) × 100

# Agricultural CD Ratio
AGRI_CD = (Agricultural_Advances / Total_Deposits) × 100

def calculate_segment_cd_ratios(segments_dict, total_deposits):
    """
    Calculate CD ratio by lending segment
    
    Args:
        segments_dict: {'retail': value, 'corporate': value, ...}
        total_deposits: Total deposits
    
    Returns:
        dict: CD ratios by segment
    """
    result = {}
    for segment, advances in segments_dict.items():
        cd = (advances / total_deposits) * 100
        result[f"{segment}_cd"] = round(cd, 2)
    
    return result


"""
QUATERNARY METRICS: Risk & Quality Metrics
"""

# NPA Gross Ratio
NPA_GROSS_RATIO = (Gross_NPA / Total_Advances) × 100

def calculate_npa_gross_ratio(gross_npa, total_advances):
    """Calculate gross NPA ratio"""
    if total_advances <= 0:
        return None
    
    npa_ratio = (gross_npa / total_advances) * 100
    return round(npa_ratio, 2)


# NPA Net Ratio
NPA_NET_RATIO = (Net_NPA / Total_Advances) × 100

def calculate_npa_net_ratio(net_npa, total_advances):
    """Calculate net NPA ratio"""
    if total_advances <= 0:
        return None
    
    npa_ratio = (net_npa / total_advances) * 100
    return round(npa_ratio, 2)


# Provision Coverage Ratio
PROVISION_COVERAGE = (Provisions / Gross_NPA) × 100

def calculate_provision_coverage(provisions, gross_npa):
    """Calculate provision coverage ratio"""
    if gross_npa <= 0:
        return None
    
    coverage = (provisions / gross_npa) * 100
    return round(coverage, 2)


"""
COMPOSITE METRICS: Health Indices
"""

def create_bank_health_scorecard(bank_data):
    """
    Create comprehensive health scorecard
    Combines multiple metrics into holistic assessment
    """
    scorecard = {
        'cd_ratio': bank_data['cd_ratio'],
        'cd_status': assess_cd_ratio_health(bank_data['cd_ratio']),
        
        'growth_divergence': bank_data['advance_growth'] - bank_data['deposit_growth'],
        'growth_status': assess_growth_health(bank_data['advance_growth'], 
                                               bank_data['deposit_growth']),
        
        'npa_gross': bank_data['npa_gross_ratio'],
        'npa_status': assess_npa_health(bank_data['npa_gross_ratio']),
        
        'capital_adequacy': bank_data['capital_adequacy_ratio'],
        'capital_status': assess_capital_health(bank_data['capital_adequacy_ratio']),
        
        'overall_health_score': calculate_health_score(
            bank_data['cd_ratio'],
            bank_data['npa_gross_ratio'],
            bank_data['capital_adequacy_ratio']
        )
    }
    
    return scorecard

def calculate_health_score(cd_ratio, npa_ratio, capital_adequacy):
    """
    Calculate composite health score (0-100)
    
    Components:
    - CD Ratio (40% weight): 70-80% is optimal
    - NPA Ratio (30% weight): Lower is better, <2% is excellent
    - Capital Adequacy (30% weight): >10.5% is healthy
    """
    
    # CD Ratio scoring
    if 70 <= cd_ratio <= 80:
        cd_score = 100
    elif 65 <= cd_ratio < 70 or 80 < cd_ratio <= 85:
        cd_score = 80
    elif 60 <= cd_ratio < 65 or 85 < cd_ratio <= 90:
        cd_score = 60
    else:
        cd_score = 40
    
    # NPA scoring
    if npa_ratio <= 2:
        npa_score = 100
    elif npa_ratio <= 3:
        npa_score = 80
    elif npa_ratio <= 4:
        npa_score = 60
    else:
        npa_score = 40
    
    # Capital adequacy scoring
    if capital_adequacy >= 12:
        capital_score = 100
    elif capital_adequacy >= 10.5:
        capital_score = 80
    elif capital_adequacy >= 9:
        capital_score = 60
    else:
        capital_score = 40
    
    # Weighted average
    health_score = (cd_score * 0.4 + npa_score * 0.3 + capital_score * 0.3)
    
    return round(health_score, 1)
```

---

## 4. DATA PIPELINE

### 4.1 Complete Data Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    DATA SOURCES (Tier-wise)                      │
├──────────────────┬──────────────────┬──────────────────────────┤
│   RBI Monthly    │  Stock Exchange  │  Bank IR Websites &     │
│   Statistics     │  Filings (BSE)   │  Financial APIs         │
│   (Excel/CSV)    │  (PDF)           │  (JSON/PDF)             │
└────────┬──────────┴────────┬─────────┴───────────────┬──────────┘
         │                   │                         │
         ▼                   ▼                         ▼
┌────────────────────────────────────────────────────────────────┐
│           DATA EXTRACTION LAYER (Python Scripts)               │
├────────────────────────────────────────────────────────────────┤
│ • RBI Excel Extractor: Parses monthly banking statistics       │
│ • BSE PDF Parser: Extracts balance sheet from quarterly filings│
│ • Bank IR Fetcher: Downloads & parses investor presentations   │
│ • API Client: Fetches data from financial data APIs            │
└────────────┬─────────────────────────────────────────────────┬─┘
             │                                                 │
             ▼                                                 ▼
┌────────────────────────────────────────────────────────────────┐
│        DATA VALIDATION & CLEANING LAYER                         │
├────────────────────────────────────────────────────────────────┤
│ • Schema validation (correct data types)                       │
│ • Range checks (deposits > advances)                           │
│ • Cross-source verification (RBI vs BSE match)                 │
│ • Outlier detection (sudden spikes)                            │
│ • Data quality flagging (Verified/Preliminary/Estimated)       │
└────────────┬──────────────────────────────────────────────────┘
             │
             ▼
┌────────────────────────────────────────────────────────────────┐
│       DATA TRANSFORMATION & ENRICHMENT LAYER                    │
├────────────────────────────────────────────────────────────────┤
│ • Calculate CD ratios & derived metrics                         │
│ • Compute YoY growth rates                                      │
│ • Segment-wise decomposition                                   │
│ • Aggregate to sector level                                    │
│ • Calculate health scores                                      │
│ • Generate trend indicators                                    │
└────────────┬──────────────────────────────────────────────────┘
             │
             ▼
┌────────────────────────────────────────────────────────────────┐
│        DATA STORAGE LAYER (Database & Cache)                    │
├────────────────────────────────────────────────────────────────┤
│ • PostgreSQL: Bank master, quarterly data, metrics              │
│ • Redis Cache: Latest CD ratios, trending data                 │
│ • CSV Backup: Monthly snapshots for audit trail                │
│ • Parquet: Historical data for analytics                        │
└────────────┬──────────────────────────────────────────────────┘
             │
             ▼
┌────────────────────────────────────────────────────────────────┐
│      STREAMLIT APPLICATION LAYER (Visualization)               │
├────────────────────────────────────────────────────────────────┤
│ • Dashboard Overview (sector snapshot)                         │
│ • Bank-wise Comparison (sortable tables, filters)              │
│ • Trend Analysis (time series charts)                          │
│ • Stress Testing (scenario visualization)                      │
│ • Risk Signals (early warning dashboard)                       │
│ • Data Export (CSV, Excel download)                            │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Python Data Pipeline Implementation

```python
"""
Complete Data Pipeline: RBI Excel → Pandas → SQLite → Streamlit
"""

import pandas as pd
import numpy as np
import requests
from datetime import datetime, timedelta
from pathlib import Path
import sqlite3
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data_pipeline.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class CDRatioDataPipeline:
    """
    Complete data pipeline for CD ratio analysis
    Handles extraction, transformation, validation, and loading
    """
    
    def __init__(self, data_dir='data/', db_path='cd_ratio.db'):
        self.data_dir = Path(data_dir)
        self.db_path = db_path
        self.data_dir.mkdir(exist_ok=True)
        self.init_database()
    
    # ═══════════════════════════════════════════════════════════════════════════
    # STEP 1: DATA EXTRACTION
    # ═══════════════════════════════════════════════════════════════════════════
    
    def extract_rbi_data(self, month_offset=0):
        """
        Extract latest RBI monthly banking statistics
        
        Args:
            month_offset: 0 for current month, 1 for previous month, etc.
        
        Returns:
            dict: Raw RBI data (deposits, advances by bank)
        """
        logger.info("🔄 Extracting RBI data...")
        
        # For MVP: Load from pre-downloaded Excel files
        # Production: Implement automated download from RBI website
        
        rbi_folder = self.data_dir / 'rbi_monthly'
        rbi_folder.mkdir(exist_ok=True)
        
        try:
            # File naming pattern: rbi_stats_2025_01.xlsx
            current_date = datetime.now() - timedelta(days=30*month_offset)
            year = current_date.year
            month = current_date.month
            
            deposits_file = rbi_folder / f'rbi_deposits_{year}_{month:02d}.xlsx'
            advances_file = rbi_folder / f'rbi_advances_{year}_{month:02d}.xlsx'
            
            if deposits_file.exists() and advances_file.exists():
                deposits_df = pd.read_excel(deposits_file)
                advances_df = pd.read_excel(advances_file)
                
                logger.info(f"✅ RBI data loaded: {year}-{month:02d}")
                return {
                    'deposits': deposits_df,
                    'advances': advances_df,
                    'source_date': current_date
                }
            else:
                logger.warning("⚠️ RBI files not found, using cached data")
                return self.load_cached_rbi_data()
        
        except Exception as e:
            logger.error(f"❌ Error extracting RBI data: {e}")
            return None
    
    def extract_bse_data(self, bank_name, quarter, fiscal_year):
        """
        Extract quarterly data from stock exchange filings
        
        Args:
            bank_name: Name of bank (e.g., 'SBI', 'HDFC')
            quarter: 'Q1', 'Q2', 'Q3', 'Q4'
            fiscal_year: 2025 for FY2025
        
        Returns:
            dict: Extracted deposits and advances
        """
        logger.info(f"📥 Extracting BSE data for {bank_name} {quarter} FY{fiscal_year}...")
        
        bse_folder = self.data_dir / 'bse_filings' / bank_name / str(fiscal_year) / quarter
        bse_folder.mkdir(parents=True, exist_ok=True)
        
        # Look for PDF files
        pdf_files = list(bse_folder.glob('*.pdf'))
        
        if not pdf_files:
            logger.warning(f"⚠️ No PDF files found for {bank_name} {quarter} FY{fiscal_year}")
            return None
        
        extracted_data = {
            'bank_name': bank_name,
            'quarter': quarter,
            'fiscal_year': fiscal_year,
            'deposits': None,
            'advances': None,
            'balance_sheet_date': None
        }
        
        for pdf_file in pdf_files:
            try:
                data = self._extract_from_pdf(pdf_file)
                if data:
                    extracted_data.update(data)
                    logger.info(f"✅ Extracted data from {pdf_file.name}")
                    break
            except Exception as e:
                logger.warning(f"⚠️ Error processing {pdf_file.name}: {e}")
                continue
        
        return extracted_data
    
    def _extract_from_pdf(self, pdf_path):
        """Extract balance sheet data from PDF"""
        import pdfplumber
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                # Usually balance sheet is in first 3 pages
                for page_num in range(min(3, len(pdf.pages))):
                    page = pdf.pages[page_num]
                    tables = page.extract_tables()
                    
                    if not tables:
                        continue
                    
                    for table in tables:
                        df = pd.DataFrame(table[1:], columns=table[0])
                        
                        # Find deposits and advances
                        for idx, row in df.iterrows():
                            row_text = str(row.iloc[0]).lower() if row.iloc[0] else ""
                            
                            if 'deposit' in row_text:
                                try:
                                    deposits = float(str(row.iloc[1]).replace(',', ''))
                                    return {'deposits': deposits}
                                except:
                                    pass
                            
                            if 'advance' in row_text:
                                try:
                                    advances = float(str(row.iloc[1]).replace(',', ''))
                                    return {'advances': advances}
                                except:
                                    pass
        except Exception as e:
            logger.error(f"Error extracting from PDF: {e}")
        
        return None
    
    # ═══════════════════════════════════════════════════════════════════════════
    # STEP 2: DATA VALIDATION
    # ═══════════════════════════════════════════════════════════════════════════
    
    def validate_data(self, bank_name, deposits, advances):
        """
        Validate extracted data against business rules
        
        Returns:
            tuple: (is_valid, error_message, quality_flag)
        """
        errors = []
        
        # Check 1: Non-zero values
        if deposits is None or deposits <= 0:
            errors.append("Deposits is zero or null")
        
        if advances is None or advances <= 0:
            errors.append("Advances is zero or null")
        
        if errors:
            return False, "; ".join(errors), "Invalid"
        
        # Check 2: Advances cannot exceed deposits
        if advances > deposits:
            return False, "Advances exceed deposits (impossible)", "Invalid"
        
        # Check 3: CD ratio within reasonable range
        cd_ratio = (advances / deposits) * 100
        if cd_ratio < 40 or cd_ratio > 100:
            errors.append(f"CD ratio {cd_ratio:.1f}% outside expected range (40-100%)")
        
        # Check 4: Cross-source validation
        # (Compare with RBI data if available)
        rbi_cd = self.get_expected_cd_ratio(bank_name)
        if rbi_cd:
            cd_diff = abs(cd_ratio - rbi_cd)
            if cd_diff > 5:  # Allow 5% tolerance
                errors.append(f"CD ratio deviates {cd_diff:.1f}% from RBI estimate")
        
        if errors:
            quality_flag = "Preliminary"  # Needs review
        else:
            quality_flag = "Verified"  # Passed all checks
        
        return True, "All validations passed", quality_flag
    
    # ═══════════════════════════════════════════════════════════════════════════
    # STEP 3: DATA TRANSFORMATION
    # ═══════════════════════════════════════════════════════════════════════════
    
    def transform_data(self, bank_data, previous_quarter_data=None):
        """
        Transform raw data into analysis-ready format
        Calculates metrics and enriches data
        """
        
        transformed = {
            'bank_name': bank_data['bank_name'],
            'fiscal_year': bank_data['fiscal_year'],
            'quarter': bank_data['quarter'],
            'extraction_date': datetime.now(),
            
            # Raw data
            'deposits_crores': bank_data['deposits'],
            'advances_crores': bank_data['advances'],
            
            # Calculated metrics
            'cd_ratio_percent': (bank_data['advances'] / bank_data['deposits']) * 100,
        }
        
        # Calculate growth if previous data available
        if previous_quarter_data:
            prev_deposits = previous_quarter_data['deposits_crores']
            prev_advances = previous_quarter_data['advances_crores']
            prev_cd = previous_quarter_data['cd_ratio_percent']
            
            transformed.update({
                'deposit_growth_qoq_percent': ((bank_data['deposits'] - prev_deposits) / prev_deposits) * 100,
                'advance_growth_qoq_percent': ((bank_data['advances'] - prev_advances) / prev_advances) * 100,
                'cd_ratio_change_qoq_points': transformed['cd_ratio_percent'] - prev_cd,
            })
        
        return transformed
    
    # ═══════════════════════════════════════════════════════════════════════════
    # STEP 4: DATA LOADING
    # ═══════════════════════════════════════════════════════════════════════════
    
    def init_database(self):
        """Initialize SQLite database with required tables"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Banks master table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS banks (
                bank_id TEXT PRIMARY KEY,
                bank_name TEXT NOT NULL,
                bank_type TEXT NOT NULL,
                headquarters TEXT,
                nse_ticker TEXT,
                bse_ticker TEXT,
                established_year INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Quarterly CD data table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS quarterly_cd_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                bank_id TEXT NOT NULL,
                fiscal_year INTEGER NOT NULL,
                quarter TEXT NOT NULL,
                quarter_end_date DATE,
                
                total_deposits_crores REAL,
                total_advances_crores REAL,
                cd_ratio_percent REAL,
                
                deposit_growth_yoy_percent REAL,
                advance_growth_yoy_percent REAL,
                cd_ratio_change_qoq_points REAL,
                
                npa_gross_percent REAL,
                capital_adequacy_percent REAL,
                
                data_source TEXT,
                data_quality_flag TEXT,
                extraction_date TIMESTAMP,
                
                UNIQUE(bank_id, fiscal_year, quarter),
                FOREIGN KEY(bank_id) REFERENCES banks(bank_id)
            )
        ''')
        
        conn.commit()
        conn.close()
        logger.info("✅ Database initialized")
    
    def load_to_database(self, data):
        """Load transformed data into SQLite database"""
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Insert or update
            cursor.execute('''
                INSERT OR REPLACE INTO quarterly_cd_data
                (bank_id, fiscal_year, quarter, total_deposits_crores, 
                 total_advances_crores, cd_ratio_percent, extraction_date)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                data['bank_id'],
                data['fiscal_year'],
                data['quarter'],
                data['deposits_crores'],
                data['advances_crores'],
                data['cd_ratio_percent'],
                data['extraction_date']
            ))
            
            conn.commit()
            conn.close()
            logger.info(f"✅ Loaded {data['bank_name']} {data['quarter']} data")
        
        except Exception as e:
            logger.error(f"❌ Error loading to database: {e}")
    
    # ═══════════════════════════════════════════════════════════════════════════
    # COMPLETE PIPELINE
    # ═══════════════════════════════════════════════════════════════════════════
    
    def run_complete_pipeline(self, banks_list, fiscal_year, quarter):
        """
        Run complete ETL pipeline for multiple banks
        
        Args:
            banks_list: List of bank names to process
            fiscal_year: Fiscal year (2025)
            quarter: Quarter ('Q1', 'Q2', 'Q3', 'Q4')
        """
        
        logger.info(f"🚀 Starting pipeline for FY{fiscal_year} {quarter}")
        
        results = {
            'successful': [],
            'failed': [],
            'skipped': []
        }
        
        for bank_name in banks_list:
            try:
                # Extract
                logger.info(f"→ Processing {bank_name}...")
                bse_data = self.extract_bse_data(bank_name, quarter, fiscal_year)
                
                if not bse_data or not bse_data.get('deposits'):
                    logger.warning(f"⊗ No data found for {bank_name}")
                    results['skipped'].append(bank_name)
                    continue
                
                # Validate
                is_valid, message, quality_flag = self.validate_data(
                    bank_name,
                    bse_data['deposits'],
                    bse_data['advances']
                )
                
                if not is_valid:
                    logger.error(f"✗ Validation failed for {bank_name}: {message}")
                    results['failed'].append({'bank': bank_name, 'error': message})
                    continue
                
                # Transform
                transformed_data = self.transform_data(bse_data)
                transformed_data['data_quality_flag'] = quality_flag
                
                # Load
                self.load_to_database(transformed_data)
                results['successful'].append(bank_name)
                
            except Exception as e:
                logger.error(f"✗ Error processing {bank_name}: {e}")
                results['failed'].append({'bank': bank_name, 'error': str(e)})
        
        # Summary
        logger.info(f"""
        ═══════════════════════════════════════════════════════
        Pipeline Complete - FY{fiscal_year} {quarter}
        ───────────────────────────────────────────────────────
        ✅ Successful: {len(results['successful'])} banks
        ✗ Failed: {len(results['failed'])} banks
        ⊗ Skipped: {len(results['skipped'])} banks
        ═══════════════════════════════════════════════════════
        """)
        
        return results
    
    # ═══════════════════════════════════════════════════════════════════════════
    # DATA RETRIEVAL FOR STREAMLIT
    # ═══════════════════════════════════════════════════════════════════════════
    
    def get_latest_cd_ratios(self, bank_type=None):
        """Get latest CD ratios (latest quarter)"""
        
        conn = sqlite3.connect(self.db_path)
        
        query = '''
            SELECT b.bank_name, b.bank_type, q.cd_ratio_percent, q.quarter, q.fiscal_year
            FROM quarterly_cd_data q
            JOIN banks b ON q.bank_id = b.bank_id
            WHERE (q.fiscal_year, q.quarter) = (
                SELECT fiscal_year, quarter FROM quarterly_cd_data
                ORDER BY fiscal_year DESC, quarter DESC LIMIT 1
            )
        '''
        
        if bank_type:
            query += f" AND b.bank_type = '{bank_type}'"
        
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        return df
    
    def get_cd_ratio_trends(self, bank_name):
        """Get historical CD ratio trends for a bank"""
        
        conn = sqlite3.connect(self.db_path)
        
        query = '''
            SELECT quarter, fiscal_year, cd_ratio_percent, deposit_growth_yoy_percent,
                   advance_growth_yoy_percent
            FROM quarterly_cd_data
            WHERE bank_id = (SELECT bank_id FROM banks WHERE bank_name = ?)
            ORDER BY fiscal_year ASC, quarter ASC
        '''
        
        df = pd.read_sql_query(query, conn, params=(bank_name,))
        conn.close()
        
        return df


# ═══════════════════════════════════════════════════════════════════════════
# USAGE EXAMPLE
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    
    # Initialize pipeline
    pipeline = CDRatioDataPipeline()
    
    # List of major banks
    major_banks = [
        'State Bank of India',
        'HDFC Bank',
        'ICICI Bank',
        'Axis Bank',
        'Kotak Mahindra Bank',
        # ... more banks
    ]
    
    # Run complete pipeline
    results = pipeline.run_complete_pipeline(
        banks_list=major_banks,
        fiscal_year=2025,
        quarter='Q3'
    )
    
    # Get latest data for dashboard
    latest_cd_data = pipeline.get_latest_cd_ratios()
    print(latest_cd_data)
```

---

## 5. DASHBOARD ARCHITECTURE

### 5.1 Dashboard Pages & Functionality

```
┌─────────────────────────────────────────────────────────────────┐
│        INDIAN BANKS CD RATIO ANALYSIS DASHBOARD                 │
└─────────────────────────────────────────────────────────────────┘

┌─ PAGE 1: OVERVIEW ──────────────────────────────────────────────┐
│ ├─ Key Metrics
│ │  ├─ Sector Average CD Ratio (70-80% range indicator)
│ │  ├─ Total Banks Tracked (28 major banks)
│ │  ├─ Highest CD Bank & Lowest CD Bank
│ │  └─ Sector-wise breakdown (PSB, Private, SFB)
│ │
│ ├─ Executive Summary Charts
│ │  ├─ CD Ratio Distribution (Box plot by bank type)
│ │  ├─ Top 10 Banks by CD Ratio (Bar chart)
│ │  ├─ CD Ratio Heatmap (Quarter vs Bank type)
│ │  └─ Sector Trends (Line chart 7 quarters)
│ │
│ └─ Quick Alerts
│    ├─ Banks entering high risk zone (CD > 85%)
│    ├─ Banks with rapid CD changes (>3% QoQ)
│    └─ Liquidity stress indicators
└─────────────────────────────────────────────────────────────────┘

┌─ PAGE 2: BANK-WISE COMPARISON ─────────────────────────────────┐
│ ├─ Interactive Data Table
│ │  ├─ Sortable columns (CD Ratio, Bank Type, Growth, etc.)
│ │  ├─ Filters (Bank Type, CD Range, Growth Rate)
│ │  ├─ Color coding (Green < 75%, Yellow 75-85%, Red > 85%)
│ │  └─ Export to CSV/Excel
│ │
│ ├─ Comparison Visualizations
│ │  ├─ Scatter plot (Deposits vs CD Ratio)
│ │  ├─ Bubble chart (Deposits, Advances, CD Ratio)
│ │  ├─ Radar chart (Comparative metrics)
│ │  └─ Gantt-like timeline (CD changes over quarters)
│ │
│ └─ Bank Selection & Drill-down
│    ├─ Select bank for detailed view
│    ├─ View historical CD ratio trend
│    ├─ See segment-wise advances breakdown
│    └─ Compare with sector average
└─────────────────────────────────────────────────────────────────┘

┌─ PAGE 3: SECTOR ANALYSIS ──────────────────────────────────────┐
│ ├─ PSB (Public Sector Banks)
│ │  ├─ Average CD Ratio: 74.2%
│ │  ├─ CD Range: 70-78%
│ │  ├─ Individual bank list with CD ratios
│ │  ├─ Trend analysis (7 quarters)
│ │  └─ Risk assessment by PSB
│ │
│ ├─ Private Banks
│ │  ├─ Average CD Ratio: 74.8%
│ │  ├─ CD Range: 72-82%
│ │  ├─ Growth comparison with PSBs
│ │  └─ Segment-wise analysis
│ │
│ └─ Small Finance Banks (SFBs)
│    ├─ Average CD Ratio: 82.5% (higher expected)
│    ├─ Microfinance focus strategy
│    └─ Growth trajectories
└─────────────────────────────────────────────────────────────────┘

┌─ PAGE 4: STRESS TESTING & RISK VIEW ───────────────────────────┐
│ ├─ Liquidity Stress Signals
│ │  ├─ Banks in "High Risk" zone (CD > 85%)
│ │  ├─ Banks with rapid CD increases
│ │  ├─ NPA ratio trends
│ │  ├─ Deposit stability indicators
│ │  └─ Alert dashboard
│ │
│ ├─ Scenario Analysis
│ │  ├─ Base Case: Current trends continue
│ │  ├─ Bear Case: 30% deposit withdrawal
│ │  │   └─ Shows revised CD ratios, liquidity stress
│ │  ├─ Bull Case: 20% credit growth
│ │  │   └─ Shows expanded lending capacity
│ │  └─ Stress Scenario: RBI rate hikes + NPA spike
│ │      └─ Impact on CD ratio and risk
│ │
│ └─ Health Scorecard
│    ├─ CD Ratio Score (0-100)
│    ├─ Growth Score (0-100)
│    ├─ Risk Score (0-100)
│    └─ Overall Bank Health Index
└─────────────────────────────────────────────────────────────────┘

┌─ PAGE 5: GROWTH DECOMPOSITION ─────────────────────────────────┐
│ ├─ Deposit vs Advance Growth Analysis
│ │  ├─ YoY Deposit Growth % (sector, by bank)
│ │  ├─ YoY Advance Growth % (sector, by bank)
│ │  ├─ Growth Divergence Analysis
│ │  │   ├─ Positive: Advances growing faster → CD rising
│ │  │   ├─ Negative: Deposits growing faster → CD falling
│ │  │   └─ Interpretation by magnitude
│ │  └─ Stacked bar/area charts
│ │
│ ├─ Segment-wise Growth Breakdown
│ │  ├─ Retail Advances Growth
│ │  ├─ Corporate Advances Growth
│ │  ├─ MSME Advances Growth
│ │  ├─ Agricultural Advances Growth
│ │  └─ 3-year trend analysis
│ │
│ └─ Deposit Composition
│    ├─ Savings Deposits %
│    ├─ Current Deposits %
│    ├─ Term Deposits %
│    └─ Stability & cost implications
└─────────────────────────────────────────────────────────────────┘

┌─ PAGE 6: ADVANCED ANALYTICS ───────────────────────────────────┐
│ ├─ Correlation Analysis
│ │  ├─ CD Ratio vs NPA Ratio
│ │  ├─ CD Ratio vs Profitability (ROA/ROE)
│ │  ├─ Deposit Growth vs Advance Growth
│ │  └─ CD Ratio vs Capital Adequacy
│ │
│ ├─ Regression Analysis
│ │  ├─ Drivers of CD ratio changes
│ │  ├─ Predictive model for next quarter CD
│ │  └─ Confidence intervals
│ │
│ └─ Early Warning System
│    ├─ Anomaly detection (outlier CD ratios)
│    ├─ Trend breaks (sudden CD changes)
│    └─ Risk scoring (composite risk indicator)
└─────────────────────────────────────────────────────────────────┘

┌─ PAGE 7: DATA EXPLORER & EXPORT ───────────────────────────────┐
│ ├─ Raw Data Table
│ │  ├─ All metrics for all banks
│ │  ├─ Sortable, filterable
│ │  ├─ Search functionality
│ │  └─ Summary statistics
│ │
│ └─ Data Export Options
│    ├─ Download as CSV (latest quarter)
│    ├─ Download as Excel (with charts)
│    ├─ Download historical data (7 quarters)
│    └─ Export analysis report (PDF)
└─────────────────────────────────────────────────────────────────┘
```

---

## 6. VISUAL DESIGN SYSTEM

### 6.1 Color Palette & Typography

```python
COLORS = {
    # Primary Banking Colors
    "primary_dark": "#003366",      # Dark Blue (Trust, Banking)
    "primary_light": "#004d80",
    "primary_bright": "#1E90FF",    # Bright Blue
    
    # Accent Colors
    "gold": "#FFD700",              # Premium accent
    "silver": "#C0C0C0",            # Secondary accent
    
    # Status Colors
    "optimal": "#27AE60",           # Green (CD 70-80%)
    "moderate": "#F39C12",          # Orange (CD 80-85%)
    "warning": "#E67E22",           # Orange-Red (CD 85-90%)
    "critical": "#E74C3C",          # Red (CD > 90%)
    "underutilized": "#3498DB",     # Blue (CD < 70%)
    
    # Bank Type Colors
    "psb_color": "#0066CC",         # Blue (PSBs)
    "private_color": "#008000",     # Green (Private)
    "sfb_color": "#FF8C00",         # Orange (SFBs)
    
    # UI Colors
    "bg_light": "#F5F5F5",
    "bg_white": "#FFFFFF",
    "text_dark": "#2C3E50",
    "text_light": "#7F8C8D",
    "border": "#BDC3C7",
}

# Typography
FONTS = {
    "header": "Segoe UI, sans-serif",
    "body": "Segoe UI, sans-serif",
    "mono": "Courier New, monospace",
}
```

### 6.2 Plotly Visualization Templates

```python
import plotly.graph_objects as go
import plotly.express as px

# Template 1: CD Ratio Distribution (Box Plot)
def create_cd_distribution_chart(data, title="CD Ratio Distribution by Bank Type"):
    fig = go.Figure()
    
    for bank_type in ['PSB', 'Private', 'SFB']:
        bank_data = data[data['type'] == bank_type]['latest_cd']
        
        fig.add_trace(go.Box(
            y=bank_data,
            name=bank_type,
            marker_color=COLORS[f'{bank_type.lower()}_color'],
            boxmean='sd'
        ))
    
    fig.update_layout(
        title=title,
        yaxis_title="CD Ratio (%)",
        xaxis_title="Bank Type",
        template="plotly_white",
        hovermode="closest",
        height=500
    )
    
    return fig

# Template 2: CD Ratio Trend (Time Series)
def create_cd_trend_chart(bank_data, bank_name):
    fig = go.Figure()
    
    quarters = bank_data['quarter']
    cd_ratios = bank_data['cd_ratio_percent']
    
    fig.add_trace(go.Scatter(
        x=quarters,
        y=cd_ratios,
        mode='lines+markers',
        name='CD Ratio %',
        line=dict(color=COLORS['primary_dark'], width=3),
        marker=dict(size=10),
        fill='tozeroy',
        fillcolor=COLORS['primary_dark'],
        fillalpha=0.1
    ))
    
    # Add optimal range
    fig.add_hrect(
        y0=70, y1=80,
        fillcolor=COLORS['optimal'],
        opacity=0.1,
        annotation_text="Optimal Range",
        annotation_position="right"
    )
    
    # Add warning zone
    fig.add_hrect(
        y0=85, y1=100,
        fillcolor=COLORS['warning'],
        opacity=0.1,
        annotation_text="Warning Zone",
        annotation_position="right"
    )
    
    fig.update_layout(
        title=f"{bank_name} - CD Ratio Trend (7 Quarters)",
        xaxis_title="Quarter",
        yaxis_title="CD Ratio (%)",
        hovermode="x unified",
        template="plotly_white",
        height=500
    )
    
    return fig

# Template 3: Comparative Bar Chart
def create_bank_comparison_chart(banks_df):
    fig = px.bar(
        banks_df.sort_values('cd_ratio_percent', ascending=False),
        x='bank_name',
        y='cd_ratio_percent',
        color='cd_ratio_percent',
        color_continuous_scale='Blues',
        title='Bank-wise CD Ratio Comparison',
        labels={'cd_ratio_percent': 'CD Ratio (%)', 'bank_name': 'Bank'},
        height=600
    )
    
    fig.update_xaxes(tickangle=-45)
    return fig

# Template 4: Growth Decomposition (Stacked Area Chart)
def create_growth_decomposition_chart(data):
    fig = go.Figure()
    
    # Deposit growth
    fig.add_trace(go.Scatter(
        x=data['quarter'],
        y=data['deposit_growth_yoy'],
        name='Deposit Growth YoY %',
        mode='lines',
        line=dict(width=3, color=COLORS['primary_dark']),
        fill='tozeroy'
    ))
    
    # Advance growth
    fig.add_trace(go.Scatter(
        x=data['quarter'],
        y=data['advance_growth_yoy'],
        name='Advance Growth YoY %',
        mode='lines',
        line=dict(width=3, color=COLORS['gold']),
        fill='tonexty'
    ))
    
    fig.update_layout(
        title='Deposit vs Advance Growth - Growth Decomposition',
        xaxis_title='Quarter',
        yaxis_title='Growth Rate (%)',
        hovermode='x unified',
        template='plotly_white',
        height=500
    )
    
    return fig

# Template 5: Stress Scenario Visualization
def create_stress_scenario_chart(bank_data, stress_scenarios):
    fig = go.Figure()
    
    # Base case
    fig.add_trace(go.Bar(
        x=bank_data['bank_name'],
        y=bank_data['cd_ratio_percent'],
        name='Base Case (Current)',
        marker_color=COLORS['primary_dark']
    ))
    
    # Bear case
    fig.add_trace(go.Bar(
        x=bank_data['bank_name'],
        y=stress_scenarios['bear_case_cd'],
        name='Bear Case (-30% Deposits)',
        marker_color=COLORS['critical']
    ))
    
    # Bull case
    fig.add_trace(go.Bar(
        x=bank_data['bank_name'],
        y=stress_scenarios['bull_case_cd'],
        name='Bull Case (+20% Advances)',
        marker_color=COLORS['optimal']
    ))
    
    fig.update_layout(
        title='CD Ratio Stress Scenarios',
        barmode='group',
        xaxis_title='Bank',
        yaxis_title='CD Ratio (%)',
        template='plotly_white',
        height=500
    )
    
    return fig
```

---

## 7. ANALYTICAL LAYERS

### 7.1 Growth Decomposition

```python
def analyze_growth_decomposition(bank_data_current, bank_data_previous):
    """
    Decompose CD ratio changes into deposit & advance components
    """
    
    deposit_current = bank_data_current['deposits']
    advance_current = bank_data_current['advances']
    
    deposit_previous = bank_data_previous['deposits']
    advance_previous = bank_data_previous['advances']
    
    # Growth rates
    deposit_growth = ((deposit_current - deposit_previous) / deposit_previous) * 100
    advance_growth = ((advance_current - advance_previous) / advance_previous) * 100
    
    # CD ratio change decomposition
    cd_current = (advance_current / deposit_current) * 100
    cd_previous = (advance_previous / deposit_previous) * 100
    cd_change = cd_current - cd_previous
    
    # Interpretation
    growth_divergence = advance_growth - deposit_growth
    
    analysis = {
        'deposit_growth_yoy_percent': round(deposit_growth, 2),
        'advance_growth_yoy_percent': round(advance_growth, 2),
        'growth_divergence_percent': round(growth_divergence, 2),
        'cd_change_qoq_points': round(cd_change, 2),
        
        'interpretation': interpret_growth_divergence(growth_divergence),
        'credit_cycle_phase': identify_credit_cycle_phase(growth_divergence),
    }
    
    return analysis

def interpret_growth_divergence(divergence):
    """Interpret the growth divergence metric"""
    
    if divergence > 5:
        return {
            'status': '🔴 EXPANSION PHASE',
            'meaning': 'Advances growing significantly faster than deposits',
            'implication': 'CD ratio rising - aggressive lending cycle',
            'risk': 'Watch for liquidity stress if continues'
        }
    elif divergence > 2:
        return {
            'status': '🟡 MODERATE EXPANSION',
            'meaning': 'Advances growth outpacing deposit growth',
            'implication': 'CD ratio gradually rising - normal credit growth',
            'risk': 'Monitor for sustainability'
        }
    elif divergence > -2:
        return {
            'status': '🟢 BALANCED GROWTH',
            'meaning': 'Deposit and advance growth in sync',
            'implication': 'CD ratio stable - healthy balance',
            'risk': 'Low - optimal state'
        }
    elif divergence > -5:
        return {
            'status': '🟡 DEPOSIT ACCUMULATION',
            'meaning': 'Deposits growing faster than advances',
            'implication': 'CD ratio falling - underutilized capacity',
            'risk': 'Credit demand weakness or policy constraints'
        }
    else:
        return {
            'status': '🔴 CREDIT STRESS',
            'meaning': 'Deposits growing much faster than advances',
            'implication': 'CD ratio declining sharply - credit demand collapse',
            'risk': 'Potential economic slowdown or banking stress'
        }
```

### 7.2 Liquidity Stress Signals

```python
def identify_liquidity_stress_signals(bank_data):
    """
    Detect early warning signals for banking sector liquidity stress
    """
    
    signals = []
    
    # Signal 1: High CD ratio (>85%)
    if bank_data['cd_ratio_percent'] > 85:
        signals.append({
            'type': 'HIGH_CD_RATIO',
            'severity': 'HIGH',
            'threshold': 85,
            'value': bank_data['cd_ratio_percent'],
            'message': f"CD ratio {bank_data['cd_ratio_percent']:.1f}% exceeds safe limit",
            'action': 'Monitor deposit stability and liquidity ratios'
        })
    
    # Signal 2: Rapid CD increase
    if bank_data.get('cd_ratio_change_qoq_points', 0) > 3:
        signals.append({
            'type': 'RAPID_CD_INCREASE',
            'severity': 'MEDIUM',
            'threshold': 3,
            'value': bank_data['cd_ratio_change_qoq_points'],
            'message': f"CD increased {bank_data['cd_ratio_change_qoq_points']:.1f}% in one quarter",
            'action': 'Analyze drivers - credit surge or deposit slowdown?'
        })
    
    # Signal 3: High NPA with high CD
    if (bank_data.get('cd_ratio_percent', 0) > 80 and 
        bank_data.get('npa_gross_ratio_percent', 0) > 3):
        signals.append({
            'type': 'HIGH_CD_HIGH_NPA',
            'severity': 'CRITICAL',
            'message': 'High CD ratio combined with high NPA - dual stress',
            'action': 'Escalate - potential asset quality deterioration'
        })
    
    # Signal 4: Advance growth outpacing deposit growth significantly
    divergence = bank_data.get('advance_growth_yoy_percent', 0) - bank_data.get('deposit_growth_yoy_percent', 0)
    if divergence > 10:
        signals.append({
            'type': 'HIGH_GROWTH_DIVERGENCE',
            'severity': 'MEDIUM',
            'value': divergence,
            'message': f"Advances growing {divergence:.1f}% faster than deposits",
            'action': 'Assess credit quality and funding sustainability'
        })
    
    # Signal 5: Low capital adequacy with high CD
    if (bank_data.get('cd_ratio_percent', 0) > 75 and 
        bank_data.get('capital_adequacy_ratio_percent', 0) < 10.5):
        signals.append({
            'type': 'LOW_CAPITAL_HIGH_CD',
            'severity': 'MEDIUM',
            'message': 'Low capital adequacy constraining CD expansion',
            'action': 'Monitor capital buffers - may limit credit growth'
        })
    
    return signals

def create_liquidity_stress_dashboard(all_banks_data):
    """Create risk dashboard showing all stress signals"""
    
    stress_data = []
    
    for bank in all_banks_data:
        signals = identify_liquidity_stress_signals(bank)
        
        if signals:
            for signal in signals:
                stress_data.append({
                    'bank': bank['bank_name'],
                    'bank_type': bank['bank_type'],
                    'signal_type': signal['type'],
                    'severity': signal['severity'],
                    'message': signal['message'],
                    'action': signal['action']
                })
    
    return pd.DataFrame(stress_data)
```

### 7.3 Scenario Analysis

```python
def run_stress_scenarios(bank_data, scenarios=None):
    """
    Run stress test scenarios on bank CD ratios
    """
    
    current_deposits = bank_data['deposits_crores']
    current_advances = bank_data['advances_crores']
    current_cd = (current_advances / current_deposits) * 100
    
    if not scenarios:
        scenarios = {
            'base_case': {},
            'bear_case_deposits': {'deposit_change': -0.30},  # -30% deposits
            'bull_case_advances': {'advance_change': 0.20},   # +20% advances
            'stress_combined': {'deposit_change': -0.20, 'advance_change': -0.10},
            'extreme_stress': {'deposit_change': -0.40, 'advance_change': -0.20},
        }
    
    results = {'bank': bank_data['bank_name'], 'current_cd': current_cd}
    
    for scenario_name, scenario_params in scenarios.items():
        
        # Apply scenario parameters
        deposits_scenario = current_deposits * (1 + scenario_params.get('deposit_change', 0))
        advances_scenario = current_advances * (1 + scenario_params.get('advance_change', 0))
        
        # Calculate stressed CD ratio
        cd_scenario = (advances_scenario / deposits_scenario) * 100
        
        # Classify severity
        if cd_scenario > 90:
            severity = 'CRITICAL'
        elif cd_scenario > 85:
            severity = 'HIGH'
        elif cd_scenario > 80:
            severity = 'MEDIUM'
        else:
            severity = 'NORMAL'
        
        results[scenario_name] = {
            'cd_ratio': round(cd_scenario, 2),
            'change_points': round(cd_scenario - current_cd, 2),
            'severity': severity
        }
    
    return results
```

---

## 8. INTERPRETATION FRAMEWORK

### 8.1 CD Ratio Assessment Framework

```python
CD_RATIO_FRAMEWORK = {
    # Healthy Range
    (70, 80): {
        'status': '🟢 HEALTHY',
        'interpretation': 'Optimal balance between growth and liquidity',
        'characteristics': [
            '✅ Sufficient deposit buffer for ALM',
            '✅ Active credit deployment',
            '✅ Stable funding position',
            '✅ Manageable liquidity risk'
        ],
        'action': 'Monitor for changes, maintain stability',
        'investment_signal': 'Neutral - stable growth'
    },
    
    # Conservative Range
    (60, 70): {
        'status': '⚠️ CONSERVATIVE',
        'interpretation': 'Underutilized lending capacity',
        'characteristics': [
            '⚠️ Excess deposits on balance sheet',
            '⚠️ Potential profitability drag',
            '⚠️ Room for credit expansion',
            '✅ Strong liquidity buffers'
        ],
        'action': 'Investigate: Why not deploying deposits? Credit demand? Policy?',
        'investment_signal': 'Potential growth upside if CD increases'
    },
    
    # Moderate-High Range
    (80, 85): {
        'status': '🟡 MODERATE-HIGH',
        'interpretation': 'Approaching high lending position',
        'characteristics': [
            '⚠️ Tighter liquidity cushion',
            '🔄 Active credit growth',
            '⚠️ Monitor deposit stability',
            '⚠️ Regulatory attention possible'
        ],
        'action': 'Monitor deposit trends, NPA ratios, capital adequacy',
        'investment_signal': 'Monitor - growth with caution'
    },
    
    # High-Risk Range
    (85, 95): {
        'status': '🔴 HIGH-RISK',
        'interpretation': 'Aggressive lending with liquidity stress risk',
        'characteristics': [
            '🔴 Thin liquidity buffer',
            '🔴 Vulnerable to deposit outflows',
            '🔴 Limited room for adverse shocks',
            '⚠️ Regulatory scrutiny likely'
        ],
        'action': 'Escalate monitoring - assess deposit stability, term structure, funding costs',
        'investment_signal': 'High risk - monitor liquidity events'
    },
    
    # Critical Range
    (95, 100): {
        'status': '🔴 CRITICAL',
        'interpretation': 'Severe liquidity stress situation',
        'characteristics': [
            '🔴 Almost no liquidity buffer',
            '🔴 Extreme vulnerability to funding stress',
            '🔴 High probability of regulatory intervention',
            '🔴 Refinancing risk'
        ],
        'action': 'Critical alert - immediate escalation needed',
        'investment_signal': 'Avoid - systemic risk'
    }
}

def assess_cd_ratio_health(cd_ratio):
    """Determine health status based on CD ratio"""
    
    for (lower, upper), assessment in CD_RATIO_FRAMEWORK.items():
        if lower <= cd_ratio < upper:
            return assessment
    
    return CD_RATIO_FRAMEWORK[(95, 100)]  # Default to critical

# Usage in Streamlit
def render_cd_assessment(cd_ratio):
    assessment = assess_cd_ratio_health(cd_ratio)
    
    st.markdown(f"### {assessment['status']}")
    st.markdown(f"**{assessment['interpretation']}**")
    
    st.markdown("**Key Characteristics:**")
    for char in assessment['characteristics']:
        st.markdown(f"- {char}")
    
    st.markdown(f"**Recommended Action:** {assessment['action']}")
    st.markdown(f"**Investment Signal:** {assessment['investment_signal']}")
```

---

## 9. DEPLOYMENT STRATEGY

### 9.1 Deployment Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│              DEPLOYMENT ARCHITECTURE                            │
└─────────────────────────────────────────────────────────────────┘

┌─ DEVELOPMENT ENVIRONMENT ───────────────────────────────────────┐
│ ├─ Local Development
│ │  ├─ Python 3.10+
│ │  ├─ Streamlit local server
│ │  ├─ SQLite database
│ │  └─ Test data pipeline
│ │
│ └─ Version Control
│    ├─ GitHub repository
│    ├─ Branch strategy (main, develop, feature)
│    └─ CI/CD pipeline
└─────────────────────────────────────────────────────────────────┘

┌─ STAGING ENVIRONMENT ───────────────────────────────────────────┐
│ ├─ Streamlit Cloud (Free tier or Pro)
│ ├─ PostgreSQL database (AWS RDS or similar)
│ ├─ Automated data updates (Cloud Functions)
│ └─ User acceptance testing
└─────────────────────────────────────────────────────────────────┘

┌─ PRODUCTION ENVIRONMENT ────────────────────────────────────────┐
│ ├─ Streamlit Cloud (Enterprise tier) or Self-hosted
│ ├─ PostgreSQL production database
│ ├─ Automated daily data pipeline
│ ├─ Monitoring & alerting
│ ├─ Backup & disaster recovery
│ └─ Performance optimization
└─────────────────────────────────────────────────────────────────┘

┌─ DATA PIPELINE (Automated) ─────────────────────────────────────┐
│ ├─ Daily: Download latest RBI data
│ ├─ Quarterly (within 45 days of quarter-end): Stock exchange filings
│ ├─ Weekly: Bank IR website checks
│ ├─ Validation & quality checks
│ ├─ Database updates
│ └─ Alert generation (if stress signals detected)
└─────────────────────────────────────────────────────────────────┘
```

### 9.2 Deployment Steps

**Step 1: Prepare Deployment Package**

```bash
# Create requirements.txt
pip freeze > requirements.txt

# Structure
indian_banks_app/
├── config.py
├── data.py
├── styles.py
├── streamlit_app.py
├── requirements.txt
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
├── data/
│   ├── rbi_monthly/
│   ├── bse_filings/
│   └── historical_data.csv
├── README.md
└── .github/
    └── workflows/
        └── deploy.yml (CI/CD)
```

**Step 2: Deploy to Streamlit Cloud**

```yaml
# GitHub Actions workflow for automatic deployment
name: Deploy to Streamlit Cloud

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Push to Streamlit Cloud
        run: |
          streamlit run streamlit_app.py --logger.level=debug
```

**Step 3: Database Setup**

```sql
-- Create PostgreSQL database
CREATE DATABASE indian_banks_cd_ratio;

-- Create tables (migration script)
-- [See Section 4.2 for schema]

-- Create indexes for performance
CREATE INDEX idx_bank_quarter ON quarterly_cd_data(bank_id, fiscal_year, quarter);
CREATE INDEX idx_cd_ratio ON quarterly_cd_data(cd_ratio_percent);
CREATE INDEX idx_quality_flag ON quarterly_cd_data(data_quality_flag);
```

---

## 10. FUTURE ENHANCEMENTS

### 10.1 Phase 2: Advanced Analytics

```
┌─ ALM GAP ANALYSIS ──────────────────────────────────────────┐
│ ├─ Asset-Liability Maturity Mismatch
│ │  ├─ Track deposit maturity profile
│ │  ├─ Match with advance maturity profile
│ │  ├─ Identify liquidity gaps by time bucket
│ │  └─ Visualize ALM ladder
│ │
│ ├─ Liquidity Coverage Ratio (LCR)
│ │  ├─ Calculate high-quality liquid assets (HQLA)
│ │  ├─ Estimate 30-day net cash outflow
│ │  ├─ Monitor LCR vs regulatory minimums
│ │  └─ Stress test scenarios
│ │
│ └─ Net Stable Funding Ratio (NSFR)
│    ├─ Available stable funding
│    ├─ Required stable funding
│    └─ Monitor vs 100% threshold
└─────────────────────────────────────────────────────────────┘

┌─ STRESS TESTING FRAMEWORK ──────────────────────────────────┐
│ ├─ Regulatory Stress Tests
│ │  ├─ RBI stress testing framework
│ │  ├─ Adverse scenario modeling
│ │  └─ Capital impact assessment
│ │
│ ├─ Bank-Specific Stress Tests
│ │  ├─ Deposit beta assumptions
│ │  ├─ NPA surge scenarios
│ │  ├─ Credit concentration risk
│ │  └─ Funding cost changes
│ │
│ └─ Macro Scenarios
│    ├─ Economic slowdown
│    ├─ Interest rate shock
│    ├─ Credit event
│    └─ Sector-specific crisis
└─────────────────────────────────────────────────────────────┘

┌─ MACHINE LEARNING EARLY WARNING SYSTEM ─────────────────────┐
│ ├─ Predictive Models
│ │  ├─ CD ratio forecasting (ARIMA/Prophet)
│ │  ├─ NPA prediction
│ │  ├─ Deposit outflow probability
│ │  └─ Liquidity stress detection
│ │
│ ├─ Anomaly Detection
│ │  ├─ Isolation Forest for outliers
│ │  ├─ One-class SVM for novelty detection
│ │  └─ Auto-encoder for complex patterns
│ │
│ └─ Risk Scoring
│    ├─ Composite liquidity risk score
│    ├─ Early warning signals
│    └─ Automated alert generation
└─────────────────────────────────────────────────────────────┘

┌─ INTEGRATION WITH OTHER DATASOURCES ────────────────────────┐
│ ├─ Fund Flow Data
│ │  └─ Mutual fund deposit/withdrawal patterns
│ │
│ ├─ Capital Market Data
│ │  ├─ Credit default swap spreads
│ │  ├─ Equity valuations
│ │  └─ Debt issuance trends
│ │
│ ├─ Macro Data
│ │  ├─ GDP growth rates
│ │  ├─ Inflation indices
│ │  ├─ Policy rate changes
│ │  └─ Forex data
│ │
│ └─ Real-Time Data
│    ├─ Deposit inflow/outflow tracking
│    ├─ Inter-bank lending rates
│    └─ Liquidity indicator index
└─────────────────────────────────────────────────────────────┘
```

### 10.2 Phase 3: Portfolio & Investment Tools

```
┌─ PORTFOLIO ANALYTICS ───────────────────────────────────────┐
│ ├─ Portfolio CD Ratio
│ │  ├─ Weighted average CD for portfolio of banks
│ │  ├─ Sector allocation analysis
│ │  └─ Concentration risk
│ │
│ ├─ Liquidity Risk Dashboard
│ │  ├─ Portfolio-level liquidity stress
│ │  ├─ Correlation of liquidity events
│ │  └─ Diversification benefits
│ │
│ └─ Performance Attribution
│    ├─ CD ratio impact on returns
│    ├─ Contribution by bank
│    └─ Tracking error analysis
└─────────────────────────────────────────────────────────────┘

┌─ INVESTMENT SIGNALS ────────────────────────────────────────┐
│ ├─ Buy/Sell Indicators
│ │  ├─ Banks with rising CD (growth signal)
│ │  ├─ Banks with stable CD (stability signal)
│ │  ├─ Banks with falling CD (risk signal)
│ │  └─ Relative valuation vs CD
│ │
│ ├─ Rotation Signals
│ │  ├─ PSB vs Private vs SFB rotation
│ │  ├─ Risk-on/risk-off indicators
│ │  └─ Cycle timing
│ │
│ └─ Alert System
│    ├─ Email/SMS alerts for stress signals
│    ├─ Customizable thresholds
│    └─ Backtesting of signals
└─────────────────────────────────────────────────────────────┘
```

### 10.3 Phase 4: Regulatory & Compliance

```
┌─ REGULATORY COMPLIANCE ─────────────────────────────────────┐
│ ├─ RBI Compliance Dashboard
│ │  ├─ Statutory CD ratio tracking (if mandated)
│ │  ├─ Liquidity Coverage Ratio compliance
│ │  ├─ Net Stable Funding Ratio compliance
│ │  └─ Capital Adequacy Ratio
│ │
│ ├─ Regulatory Reporting
│ │  ├─ Automated report generation
│ │  ├─ RBI disclosure requirements
│ │  ├─ Prudential Returns (PR)
│ │  └─ Form-wise submissions
│ │
│ └─ Compliance Scoring
│    ├─ Regulatory adherence score
│    ├─ Red flags for violations
│    └─ Automated corrective action alerts
└─────────────────────────────────────────────────────────────┘
```

---

## PROJECT TIMELINE

```
PHASE 1 - MVP (Jan-Mar 2025)
├── Month 1: Data collection & pipeline setup
├── Month 2: Dashboard development (5 pages)
└── Month 3: Testing, deployment, documentation

PHASE 2 - Advanced Analytics (Apr-Jun 2025)
├── ALM gap analysis
├── Stress testing framework
└── ML early warning system

PHASE 3 - Investment Tools (Jul-Sep 2025)
├── Portfolio analytics
├── Investment signal generation
└── Alert system

PHASE 4 - Compliance & Governance (Oct-Dec 2025)
├── Regulatory reporting
├── Compliance dashboards
└── Enterprise features
```

---

## SUCCESS METRICS

- **User Adoption:** >500 active users within 6 months
- **Data Quality:** 99% accuracy in CD ratio calculations
- **System Performance:** <2 second dashboard load time
- **Alert Effectiveness:** >80% signal accuracy for stress detection
- **User Satisfaction:** >4.5/5 NPS score

---

**Document Status:** Ready for Development
**Next Step:** Execute Phase 1 (MVP) as per timeline
**Questions?** Refer to sections 1-10 for detailed technical specifications

EOF
cat /mnt/user-data/outputs/INDIAN_BANKS_CD_RATIO_COMPLETE_PROJECT_PLAN.md
