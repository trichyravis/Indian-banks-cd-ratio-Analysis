"""
Indian Banks Credit-to-Deposit Ratio Analysis Dashboard
Configuration File - Colors, Constants, and Settings
Version 1.0.0
"""

# ═══════════════════════════════════════════════════════════════════════════
# BRANDING & PROJECT INFORMATION
# ═══════════════════════════════════════════════════════════════════════════

BRAND_NAME = "Indian Banking Insights - CD Ratio Analysis"
PROJECT_TITLE = "Indian Banks Credit-to-Deposit Ratio Analysis Dashboard"
PROJECT_SUBTITLE = "CD Ratio Trends, Comparisons & Banking Health Indicators"
AUTHOR = "Prof. V. Ravichandran"
EXPERIENCE = "28+ Years Corporate Finance & Banking Experience | 10+ Years Academic Excellence"
LOCATION = "Bangalore, India"
YEAR = "2025"

# ═══════════════════════════════════════════════════════════════════════════
# COLOR SCHEME - Banking Sector Theme
# ═══════════════════════════════════════════════════════════════════════════

COLORS = {
    # Primary Colors - Banking/Trust theme
    "primary_dark": "#003366",      # Dark Blue (Trust, Banking)
    "primary_light": "#004d80",     # Medium Dark Blue
    "primary_bright": "#1E90FF",    # Bright Blue
    
    # Accent Colors
    "gold": "#FFD700",              # Gold (Premium)
    "silver": "#C0C0C0",            # Silver (Secondary)
    "green": "#2ECC71",             # Green (Positive/Healthy)
    
    # Status Colors
    "positive": "#27AE60",          # Green (CD rising)
    "neutral": "#F39C12",           # Orange (Stable)
    "negative": "#E74C3C",          # Red (CD declining)
    "caution": "#E67E22",           # Orange (Monitor)
    
    # Bank Type Colors
    "psb_color": "#0066CC",         # Blue (PSBs)
    "private_color": "#008000",     # Green (Private)
    "sfb_color": "#FF8C00",         # Orange (SFBs)
    
    # Background & Text
    "bg_light": "#F5F5F5",          # Light gray background
    "bg_white": "#FFFFFF",          # White
    "text_dark": "#2C3E50",         # Dark text
    "text_light": "#7F8C8D",        # Light text
    "border": "#BDC3C7",            # Border color
}

# ═══════════════════════════════════════════════════════════════════════════
# PAGE NAVIGATION
# ═══════════════════════════════════════════════════════════════════════════

PAGES = [
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
    "📚 Data Sources"
]

# ═══════════════════════════════════════════════════════════════════════════
# BANK CATEGORIES & CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════════

# Public Sector Banks
PSB_BANKS = [
    "State Bank of India",
    "Bank of Baroda",
    "Punjab National Bank",
    "Bank of India",
    "Central Bank of India",
    "Indian Bank",
    "Union Bank of India",
    "Canara Bank",
    "Syndicate Bank",
    "Corporation Bank"
]

# Major Private Sector Banks
PRIVATE_BANKS = [
    "HDFC Bank",
    "ICICI Bank",
    "Axis Bank",
    "Kotak Mahindra Bank",
    "IndusInd Bank",
    "Yes Bank",
    "Federal Bank",
    "South Indian Bank",
    "IDFC First Bank",
    "Bandhan Bank"
]

# Small Finance Banks
SFB_BANKS = [
    "AU Small Finance Bank",
    "Ujjivan Small Finance Bank",
    "RBL Bank",
    "ICICI Bank Small Finance",
    "TMB (Tamil Nadu Mercantile) Bank",
    "Suryoday Small Finance Bank",
    "Shivalik Small Finance Bank",
    "North East Small Finance Bank"
]

ALL_MAJOR_BANKS = PSB_BANKS + PRIVATE_BANKS + SFB_BANKS

# ═══════════════════════════════════════════════════════════════════════════
# CD RATIO BENCHMARKS & HEALTH INDICATORS
# ═══════════════════════════════════════════════════════════════════════════

CD_RATIO_BENCHMARKS = {
    "excellent": (78, 85),          # Optimal lending
    "healthy": (70, 78),            # Balanced growth & liquidity
    "moderate": (65, 70),           # Conservative
    "low": (50, 65),                # Underutilized capacity
    "high": (85, 95),               # Aggressive lending
    "critical": (95, 100),          # Liquidity risk
}

CD_RATIO_STATUS = {
    "excellent": "🟢 EXCELLENT",
    "healthy": "🟢 HEALTHY",
    "moderate": "🟡 MODERATE",
    "low": "⚠️ LOW",
    "high": "🟠 HIGH",
    "critical": "🔴 CRITICAL"
}

# ═══════════════════════════════════════════════════════════════════════════
# INDUSTRY AVERAGES & COMPARISON METRICS
# ═══════════════════════════════════════════════════════════════════════════

SECTOR_AVERAGES = {
    "banking_sector_cd_ratio": 73.5,
    "psb_average_cd_ratio": 74.2,
    "private_bank_average_cd_ratio": 74.8,
    "sfb_average_cd_ratio": 82.5,
}

# ═══════════════════════════════════════════════════════════════════════════
# DATA SOURCES
# ═══════════════════════════════════════════════════════════════════════════

DATA_SOURCES = {
    "RBI": "Reserve Bank of India - Monthly Banking Statistics",
    "BSE": "Bombay Stock Exchange - Corporate Filings",
    "NSE": "National Stock Exchange - Corporate Filings",
    "Bank_IR": "Individual Bank Investor Relations",
    "ICRA": "ICRA Credit Rating Agency",
    "CRISIL": "CRISIL Research"
}

# ═══════════════════════════════════════════════════════════════════════════
# QUARTERLY FISCAL YEARS
# ═══════════════════════════════════════════════════════════════════════════

FISCAL_YEARS = {
    "FY2023": {"start": "2022-04-01", "end": "2023-03-31"},
    "FY2024": {"start": "2023-04-01", "end": "2024-03-31"},
    "FY2025": {"start": "2024-04-01", "end": "2025-03-31"},
}

QUARTERS = ["Q1", "Q2", "Q3", "Q4"]

# ═══════════════════════════════════════════════════════════════════════════
# KEY METRICS & FORMULAS
# ═══════════════════════════════════════════════════════════════════════════

METRICS = {
    "cd_ratio": "CD Ratio % = (Total Advances / Total Deposits) × 100",
    "loan_growth": "YoY Loan Growth % = ((Current Year Advances - Previous Year Advances) / Previous Year Advances) × 100",
    "deposit_growth": "YoY Deposit Growth % = ((Current Year Deposits - Previous Year Deposits) / Previous Year Deposits) × 100",
    "npa_ratio": "NPA Ratio % = (Non-Performing Assets / Total Assets) × 100",
    "growth_divergence": "Growth Divergence = Advance Growth % - Deposit Growth %",
}

# ═══════════════════════════════════════════════════════════════════════════
# ANALYSIS PERIODS
# ═══════════════════════════════════════════════════════════════════════════

ANALYSIS_PERIOD = "FY2023 - FY2025 (3 years of data)"
DATA_FREQUENCY = "Quarterly"
LAST_UPDATE = "January 2025"

# ═══════════════════════════════════════════════════════════════════════════
# MESSAGES & LABELS
# ═══════════════════════════════════════════════════════════════════════════

MESSAGES = {
    "app_description": """
    Comprehensive analysis of Indian banking sector CD (Credit-to-Deposit) ratios.
    Track lending trends, compare bank performance, and understand banking health indicators.
    """,
    
    "cd_ratio_explanation": """
    **Credit-to-Deposit (CD) Ratio** measures what percentage of customer deposits 
    a bank has deployed as loans and advances. It indicates banking sector health 
    and credit growth momentum.
    """,
    
    "healthy_cd_range": """
    A CD ratio of **70-80%** is generally considered healthy, balancing growth aspirations 
    with liquidity requirements. Below 70% indicates unutilized capacity; above 85% signals 
    aggressive lending.
    """,
}

# ═══════════════════════════════════════════════════════════════════════════
# STYLING PRESETS
# ═══════════════════════════════════════════════════════════════════════════

# Header styling
HEADER_STYLE = {
    "bg_color": COLORS["primary_dark"],
    "text_color": COLORS["gold"],
    "font_size": 24,
    "font_weight": 700,
}

# Section header styling
SECTION_STYLE = {
    "bg_color": COLORS["primary_dark"],
    "text_color": COLORS["gold"],
    "font_size": 18,
    "font_weight": 700,
}

# ═══════════════════════════════════════════════════════════════════════════
# CHART COLORS & VISUALIZATION
# ═══════════════════════════════════════════════════════════════════════════

CHART_COLORS = {
    "psb": COLORS["psb_color"],
    "private": COLORS["private_color"],
    "sfb": COLORS["sfb_color"],
    "line": COLORS["primary_dark"],
    "positive": COLORS["positive"],
    "negative": COLORS["negative"],
}

# ═══════════════════════════════════════════════════════════════════════════
# EXPORT FORMATS
# ═══════════════════════════════════════════════════════════════════════════

EXPORT_FORMATS = {
    "csv": "📊 CSV Format",
    "excel": "📈 Excel Format",
    "json": "📋 JSON Format",
}

# ═══════════════════════════════════════════════════════════════════════════
# APP METADATA
# ═══════════════════════════════════════════════════════════════════════════

APP_VERSION = "1.0.0"
LAST_UPDATED = "January 18, 2025"
DEVELOPER = "Prof. V. Ravichandran"
GITHUB_REPO = "trichyravis/indian-banks-cd-ratio-dashboard"
LINKEDIN_PROFILE = "https://www.linkedin.com/in/trichyravis"
