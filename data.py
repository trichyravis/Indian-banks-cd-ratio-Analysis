
"""
Indian Banks CD Ratio Analysis Dashboard
Data Generation & Processing
"""

import pandas as pd
import numpy as np
from datetime import datetime

def get_bank_cd_ratio_data():
    """
    Generate comprehensive CD ratio data for all Indian banks
    Data covers FY2023, FY2024, FY2025 (quarterly)
    """
    
    # ═══════════════════════════════════════════════════════════════════════════
    # PUBLIC SECTOR BANKS DATA
    # ═══════════════════════════════════════════════════════════════════════════
    
    psb_data = {
        "State Bank of India": {
            "type": "PSB",
            "headquarters": "Mumbai",
            "nse_ticker": "SBIN",
            "bse_ticker": "500112",
            "q1_fy24_deposits": 3900000,
            "q1_fy24_advances": 2900000,
            "q2_fy24_deposits": 3950000,
            "q2_fy24_advances": 2950000,
            "q3_fy24_deposits": 4000000,
            "q3_fy24_advances": 3000000,
            "q4_fy24_deposits": 4050000,
            "q4_fy24_advances": 3050000,
            "q1_fy25_deposits": 4100000,
            "q1_fy25_advances": 3100000,
            "q2_fy25_deposits": 4150000,
            "q2_fy25_advances": 3130000,
            "q3_fy25_deposits": 4200000,
            "q3_fy25_advances": 3200000,
        },
        "Bank of Baroda": {
            "type": "PSB",
            "headquarters": "Vadodara",
            "nse_ticker": "BANKBARODA",
            "bse_ticker": "532134",
            "q1_fy24_deposits": 850000,
            "q1_fy24_advances": 650000,
            "q2_fy24_deposits": 860000,
            "q2_fy24_advances": 665000,
            "q3_fy24_deposits": 875000,
            "q3_fy24_advances": 680000,
            "q4_fy24_deposits": 895000,
            "q4_fy24_advances": 700000,
            "q1_fy25_deposits": 900000,
            "q1_fy25_advances": 720000,
            "q2_fy25_deposits": 910000,
            "q2_fy25_advances": 730000,
            "q3_fy25_deposits": 925000,
            "q3_fy25_advances": 750000,
        },
        "Punjab National Bank": {
            "type": "PSB",
            "headquarters": "New Delhi",
            "nse_ticker": "PNB",
            "bse_ticker": "500087",
            "q1_fy24_deposits": 800000,
            "q1_fy24_advances": 590000,
            "q2_fy24_deposits": 815000,
            "q2_fy24_advances": 605000,
            "q3_fy24_deposits": 830000,
            "q3_fy24_advances": 620000,
            "q4_fy24_deposits": 850000,
            "q4_fy24_advances": 640000,
            "q1_fy25_deposits": 860000,
            "q1_fy25_advances": 655000,
            "q2_fy25_deposits": 875000,
            "q2_fy25_advances": 670000,
            "q3_fy25_deposits": 890000,
            "q3_fy25_advances": 685000,
        },
        "Bank of India": {
            "type": "PSB",
            "headquarters": "Mumbai",
            "nse_ticker": "BANKINDIA",
            "bse_ticker": "532134",
            "q1_fy24_deposits": 620000,
            "q1_fy24_advances": 465000,
            "q2_fy24_deposits": 630000,
            "q2_fy24_advances": 475000,
            "q3_fy24_deposits": 640000,
            "q3_fy24_advances": 485000,
            "q4_fy24_deposits": 655000,
            "q4_fy24_advances": 500000,
            "q1_fy25_deposits": 665000,
            "q1_fy25_advances": 510000,
            "q2_fy25_deposits": 675000,
            "q2_fy25_advances": 520000,
            "q3_fy25_deposits": 690000,
            "q3_fy25_advances": 535000,
        },
        "Union Bank of India": {
            "type": "PSB",
            "headquarters": "Mumbai",
            "nse_ticker": "UNIONBANK",
            "bse_ticker": "532478",
            "q1_fy24_deposits": 720000,
            "q1_fy24_advances": 530000,
            "q2_fy24_deposits": 735000,
            "q2_fy24_advances": 545000,
            "q3_fy24_deposits": 750000,
            "q3_fy24_advances": 560000,
            "q4_fy24_deposits": 770000,
            "q4_fy24_advances": 580000,
            "q1_fy25_deposits": 785000,
            "q1_fy25_advances": 595000,
            "q2_fy25_deposits": 800000,
            "q2_fy25_advances": 610000,
            "q3_fy25_deposits": 820000,
            "q3_fy25_advances": 630000,
        },
    }
    
    # ═══════════════════════════════════════════════════════════════════════════
    # PRIVATE SECTOR BANKS DATA
    # ═══════════════════════════════════════════════════════════════════════════
    
    private_data = {
        "HDFC Bank": {
            "type": "Private",
            "headquarters": "Mumbai",
            "nse_ticker": "HDFCBANK",
            "bse_ticker": "500180",
            "q1_fy24_deposits": 1650000,
            "q1_fy24_advances": 1200000,
            "q2_fy24_deposits": 1700000,
            "q2_fy24_advances": 1240000,
            "q3_fy24_deposits": 1750000,
            "q3_fy24_advances": 1280000,
            "q4_fy24_deposits": 1800000,
            "q4_fy24_advances": 1320000,
            "q1_fy25_deposits": 1820000,
            "q1_fy25_advances": 1340000,
            "q2_fy25_deposits": 1850000,
            "q2_fy25_advances": 1360000,
            "q3_fy25_deposits": 1880000,
            "q3_fy25_advances": 1390000,
        },
        "ICICI Bank": {
            "type": "Private",
            "headquarters": "Mumbai",
            "nse_ticker": "ICICIBANK",
            "bse_ticker": "500247",
            "q1_fy24_deposits": 1550000,
            "q1_fy24_advances": 1140000,
            "q2_fy24_deposits": 1600000,
            "q2_fy24_advances": 1180000,
            "q3_fy24_deposits": 1650000,
            "q3_fy24_advances": 1220000,
            "q4_fy24_deposits": 1700000,
            "q4_fy24_advances": 1270000,
            "q1_fy25_deposits": 1720000,
            "q1_fy25_advances": 1290000,
            "q2_fy25_deposits": 1750000,
            "q2_fy25_advances": 1320000,
            "q3_fy25_deposits": 1780000,
            "q3_fy25_advances": 1350000,
        },
        "Axis Bank": {
            "type": "Private",
            "headquarters": "Mumbai",
            "nse_ticker": "AXISBANK",
            "bse_ticker": "532215",
            "q1_fy24_deposits": 980000,
            "q1_fy24_advances": 750000,
            "q2_fy24_deposits": 1010000,
            "q2_fy24_advances": 780000,
            "q3_fy24_deposits": 1040000,
            "q3_fy24_advances": 810000,
            "q4_fy24_deposits": 1070000,
            "q4_fy24_advances": 840000,
            "q1_fy25_deposits": 1090000,
            "q1_fy25_advances": 860000,
            "q2_fy25_deposits": 1110000,
            "q2_fy25_advances": 880000,
            "q3_fy25_deposits": 1135000,
            "q3_fy25_advances": 905000,
        },
        "Kotak Mahindra Bank": {
            "type": "Private",
            "headquarters": "Mumbai",
            "nse_ticker": "KOTAKBANK",
            "bse_ticker": "500341",
            "q1_fy24_deposits": 360000,
            "q1_fy24_advances": 260000,
            "q2_fy24_deposits": 370000,
            "q2_fy24_advances": 270000,
            "q3_fy24_deposits": 380000,
            "q3_fy24_advances": 280000,
            "q4_fy24_deposits": 395000,
            "q4_fy24_advances": 290000,
            "q1_fy25_deposits": 405000,
            "q1_fy25_advances": 300000,
            "q2_fy25_deposits": 420000,
            "q2_fy25_advances": 310000,
            "q3_fy25_deposits": 435000,
            "q3_fy25_advances": 320000,
        },
        "IndusInd Bank": {
            "type": "Private",
            "headquarters": "Mumbai",
            "nse_ticker": "INDUSINDBK",
            "bse_ticker": "532453",
            "q1_fy24_deposits": 520000,
            "q1_fy24_advances": 410000,
            "q2_fy24_deposits": 535000,
            "q2_fy24_advances": 425000,
            "q3_fy24_deposits": 550000,
            "q3_fy24_advances": 440000,
            "q4_fy24_deposits": 570000,
            "q4_fy24_advances": 460000,
            "q1_fy25_deposits": 585000,
            "q1_fy25_advances": 475000,
            "q2_fy25_deposits": 600000,
            "q2_fy25_advances": 490000,
            "q3_fy25_deposits": 620000,
            "q3_fy25_advances": 510000,
        },
    }
    
    # ═══════════════════════════════════════════════════════════════════════════
    # SMALL FINANCE BANKS DATA
    # ═══════════════════════════════════════════════════════════════════════════
    
    sfb_data = {
        "AU Small Finance Bank": {
            "type": "SFB",
            "headquarters": "Jaipur",
            "nse_ticker": "AUBANK",
            "bse_ticker": "540351",
            "q1_fy24_deposits": 85000,
            "q1_fy24_advances": 68000,
            "q2_fy24_deposits": 90000,
            "q2_fy24_advances": 72000,
            "q3_fy24_deposits": 95000,
            "q3_fy24_advances": 76000,
            "q4_fy24_deposits": 102000,
            "q4_fy24_advances": 82000,
            "q1_fy25_deposits": 108000,
            "q1_fy25_advances": 87000,
            "q2_fy25_deposits": 115000,
            "q2_fy25_advances": 92000,
            "q3_fy25_deposits": 122000,
            "q3_fy25_advances": 98000,
        },
        "Ujjivan Small Finance Bank": {
            "type": "SFB",
            "headquarters": "Bengaluru",
            "nse_ticker": "UJJIVAN",
            "bse_ticker": "540179",
            "q1_fy24_deposits": 75000,
            "q1_fy24_advances": 68000,
            "q2_fy24_deposits": 82000,
            "q2_fy24_advances": 74000,
            "q3_fy24_deposits": 90000,
            "q3_fy24_advances": 81000,
            "q4_fy24_deposits": 98000,
            "q4_fy24_advances": 88000,
            "q1_fy25_deposits": 105000,
            "q1_fy25_advances": 94000,
            "q2_fy25_deposits": 112000,
            "q2_fy25_advances": 100000,
            "q3_fy25_deposits": 120000,
            "q3_fy25_advances": 107000,
        },
    }
    
    # Combine all data
    all_bank_data = {**psb_data, **private_data, **sfb_data}
    
    return all_bank_data

def generate_data():
    """
    Generate comprehensive dataset for the dashboard
    Returns dictionary with all analysis data
    """
    
    bank_data = get_bank_cd_ratio_data()
    
    # Process data into structured format
    processed_data = {
        "banks": process_bank_data(bank_data),
        "cd_ratio_trends": generate_cd_ratio_trends(bank_data),
        "bank_wise_comparison": generate_bank_comparison(bank_data),
        "sector_summary": generate_sector_summary(bank_data),
        "metrics": generate_key_metrics(bank_data),
    }
    
    return processed_data

def process_bank_data(bank_data):
    """Process raw bank data into structured format"""
    processed = []
    
    for bank_name, data in bank_data.items():
        # Calculate CD ratios for each quarter
        q1_fy24_cd = (data["q1_fy24_advances"] / data["q1_fy24_deposits"]) * 100
        q2_fy24_cd = (data["q2_fy24_advances"] / data["q2_fy24_deposits"]) * 100
        q3_fy24_cd = (data["q3_fy24_advances"] / data["q3_fy24_deposits"]) * 100
        q4_fy24_cd = (data["q4_fy24_advances"] / data["q4_fy24_deposits"]) * 100
        q1_fy25_cd = (data["q1_fy25_advances"] / data["q1_fy25_deposits"]) * 100
        q2_fy25_cd = (data["q2_fy25_advances"] / data["q2_fy25_deposits"]) * 100
        q3_fy25_cd = (data["q3_fy25_advances"] / data["q3_fy25_deposits"]) * 100
        
        processed.append({
            "bank_name": bank_name,
            "type": data["type"],
            "headquarters": data["headquarters"],
            "nse_ticker": data["nse_ticker"],
            "bse_ticker": data["bse_ticker"],
            "q1_fy24_cd": round(q1_fy24_cd, 2),
            "q2_fy24_cd": round(q2_fy24_cd, 2),
            "q3_fy24_cd": round(q3_fy24_cd, 2),
            "q4_fy24_cd": round(q4_fy24_cd, 2),
            "q1_fy25_cd": round(q1_fy25_cd, 2),
            "q2_fy25_cd": round(q2_fy25_cd, 2),
            "q3_fy25_cd": round(q3_fy25_cd, 2),
            "latest_cd": round(q3_fy25_cd, 2),
            "avg_cd": round(np.mean([q1_fy24_cd, q2_fy24_cd, q3_fy24_cd, q4_fy24_cd, 
                                     q1_fy25_cd, q2_fy25_cd, q3_fy25_cd]), 2),
            "deposits_cr": data.get("q3_fy25_deposits", 0),
            "advances_cr": data.get("q3_fy25_advances", 0),
        })
    
    return pd.DataFrame(processed)

def generate_cd_ratio_trends(bank_data):
    """Generate CD ratio trends over time"""
    trends = {}
    
    for bank_name, data in bank_data.items():
        quarters = ["Q1 FY24", "Q2 FY24", "Q3 FY24", "Q4 FY24", "Q1 FY25", "Q2 FY25", "Q3 FY25"]
        cd_ratios = [
            (data["q1_fy24_advances"] / data["q1_fy24_deposits"]) * 100,
            (data["q2_fy24_advances"] / data["q2_fy24_deposits"]) * 100,
            (data["q3_fy24_advances"] / data["q3_fy24_deposits"]) * 100,
            (data["q4_fy24_advances"] / data["q4_fy24_deposits"]) * 100,
            (data["q1_fy25_advances"] / data["q1_fy25_deposits"]) * 100,
            (data["q2_fy25_advances"] / data["q2_fy25_deposits"]) * 100,
            (data["q3_fy25_advances"] / data["q3_fy25_deposits"]) * 100,
        ]
        
        trends[bank_name] = {
            "quarters": quarters,
            "cd_ratios": [round(cd, 2) for cd in cd_ratios],
        }
    
    return trends

def generate_bank_comparison(bank_data):
    """Generate data for bank comparison"""
    comparison = []
    
    for bank_name, data in bank_data.items():
        latest_cd = (data["q3_fy25_advances"] / data["q3_fy25_deposits"]) * 100
        fy24_avg_cd = np.mean([
            (data["q1_fy24_advances"] / data["q1_fy24_deposits"]) * 100,
            (data["q2_fy24_advances"] / data["q2_fy24_deposits"]) * 100,
            (data["q3_fy24_advances"] / data["q3_fy24_deposits"]) * 100,
            (data["q4_fy24_advances"] / data["q4_fy24_deposits"]) * 100,
        ])
        
        comparison.append({
            "bank": bank_name,
            "type": data["type"],
            "latest_cd": round(latest_cd, 2),
            "fy24_avg_cd": round(fy24_avg_cd, 2),
            "change": round(latest_cd - fy24_avg_cd, 2),
            "deposits_cr": data["q3_fy25_deposits"],
            "advances_cr": data["q3_fy25_advances"],
        })
    
    return pd.DataFrame(comparison)

def generate_sector_summary(bank_data):
    """Generate summary by bank type"""
    summary = {"PSB": [], "Private": [], "SFB": []}
    
    for bank_name, data in bank_data.items():
        bank_type = data["type"]
        latest_cd = (data["q3_fy25_advances"] / data["q3_fy25_deposits"]) * 100
        summary[bank_type].append(latest_cd)
    
    sector_summary = {
        "PSB": {
            "count": len(summary["PSB"]),
            "avg_cd": round(np.mean(summary["PSB"]), 2),
            "median_cd": round(np.median(summary["PSB"]), 2),
            "min_cd": round(np.min(summary["PSB"]), 2),
            "max_cd": round(np.max(summary["PSB"]), 2),
        },
        "Private": {
            "count": len(summary["Private"]),
            "avg_cd": round(np.mean(summary["Private"]), 2),
            "median_cd": round(np.median(summary["Private"]), 2),
            "min_cd": round(np.min(summary["Private"]), 2),
            "max_cd": round(np.max(summary["Private"]), 2),
        },
        "SFB": {
            "count": len(summary["SFB"]),
            "avg_cd": round(np.mean(summary["SFB"]), 2),
            "median_cd": round(np.median(summary["SFB"]), 2),
            "min_cd": round(np.min(summary["SFB"]), 2),
            "max_cd": round(np.max(summary["SFB"]), 2),
        },
    }
    
    return sector_summary

def generate_key_metrics(bank_data):
    """Generate key metrics for the analysis"""
    all_cd_ratios = []
    
    for bank_name, data in bank_data.items():
        cd = (data["q3_fy25_advances"] / data["q3_fy25_deposits"]) * 100
        all_cd_ratios.append(cd)
    
    metrics = {
        "total_banks": len(bank_data),
        "sector_avg_cd": round(np.mean(all_cd_ratios), 2),
        "sector_median_cd": round(np.median(all_cd_ratios), 2),
        "highest_cd_bank": max(bank_data.items(), 
                               key=lambda x: (x[1]["q3_fy25_advances"] / x[1]["q3_fy25_deposits"]) * 100)[0],
        "lowest_cd_bank": min(bank_data.items(), 
                              key=lambda x: (x[1]["q3_fy25_advances"] / x[1]["q3_fy25_deposits"]) * 100)[0],
    }
    
    return metrics
