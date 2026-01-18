
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
    
    # Foreign Banks Data
    foreign_data = {
        "DBS Bank India": {
            "type": "Foreign",
            "headquarters": "Mumbai",
            "nse_ticker": "DBSINDIA",
            "bse_ticker": "533536",
            "q1_fy24_deposits": 150000,
            "q1_fy24_advances": 105000,
            "q2_fy24_deposits": 155000,
            "q2_fy24_advances": 110000,
            "q3_fy24_deposits": 160000,
            "q3_fy24_advances": 115000,
            "q4_fy24_deposits": 165000,
            "q4_fy24_advances": 120000,
            "q1_fy25_deposits": 170000,
            "q1_fy25_advances": 125000,
            "q2_fy25_deposits": 175000,
            "q2_fy25_advances": 130000,
            "q3_fy25_deposits": 180000,
            "q3_fy25_advances": 135000,
        },
        "Standard Chartered Bank": {
            "type": "Foreign",
            "headquarters": "Mumbai",
            "nse_ticker": "STANCHART",
            "bse_ticker": "532898",
            "q1_fy24_deposits": 95000,
            "q1_fy24_advances": 68000,
            "q2_fy24_deposits": 98000,
            "q2_fy24_advances": 70000,
            "q3_fy24_deposits": 101000,
            "q3_fy24_advances": 72000,
            "q4_fy24_deposits": 104000,
            "q4_fy24_advances": 74000,
            "q1_fy25_deposits": 107000,
            "q1_fy25_advances": 76000,
            "q2_fy25_deposits": 110000,
            "q2_fy25_advances": 78000,
            "q3_fy25_deposits": 113000,
            "q3_fy25_advances": 80000,
        },
        "HSBC India": {
            "type": "Foreign",
            "headquarters": "Mumbai",
            "nse_ticker": "HSBCBANK",
            "bse_ticker": "500010",
            "q1_fy24_deposits": 78000,
            "q1_fy24_advances": 55000,
            "q2_fy24_deposits": 80000,
            "q2_fy24_advances": 57000,
            "q3_fy24_deposits": 82000,
            "q3_fy24_advances": 59000,
            "q4_fy24_deposits": 84000,
            "q4_fy24_advances": 61000,
            "q1_fy25_deposits": 86000,
            "q1_fy25_advances": 63000,
            "q2_fy25_deposits": 88000,
            "q2_fy25_advances": 65000,
            "q3_fy25_deposits": 90000,
            "q3_fy25_advances": 67000,
        },
        "Citibank India": {
            "type": "Foreign",
            "headquarters": "Mumbai",
            "nse_ticker": "CITI",
            "bse_ticker": "500180",
            "q1_fy24_deposits": 62000,
            "q1_fy24_advances": 42000,
            "q2_fy24_deposits": 64000,
            "q2_fy24_advances": 44000,
            "q3_fy24_deposits": 66000,
            "q3_fy24_advances": 46000,
            "q4_fy24_deposits": 68000,
            "q4_fy24_advances": 48000,
            "q1_fy25_deposits": 70000,
            "q1_fy25_advances": 50000,
            "q2_fy25_deposits": 72000,
            "q2_fy25_advances": 52000,
            "q3_fy25_deposits": 74000,
            "q3_fy25_advances": 54000,
        },
        "Bank of America": {
            "type": "Foreign",
            "headquarters": "New Delhi",
            "nse_ticker": "BOA",
            "bse_ticker": "500011",
            "q1_fy24_deposits": 42000,
            "q1_fy24_advances": 28000,
            "q2_fy24_deposits": 43000,
            "q2_fy24_advances": 29000,
            "q3_fy24_deposits": 44000,
            "q3_fy24_advances": 30000,
            "q4_fy24_deposits": 45000,
            "q4_fy24_advances": 31000,
            "q1_fy25_deposits": 46000,
            "q1_fy25_advances": 32000,
            "q2_fy25_deposits": 47000,
            "q2_fy25_advances": 33000,
            "q3_fy25_deposits": 48000,
            "q3_fy25_advances": 34000,
        },
        "JPMorgan Chase Bank": {
            "type": "Foreign",
            "headquarters": "Mumbai",
            "nse_ticker": "JPM",
            "bse_ticker": "532835",
            "q1_fy24_deposits": 38000,
            "q1_fy24_advances": 25000,
            "q2_fy24_deposits": 39000,
            "q2_fy24_advances": 26000,
            "q3_fy24_deposits": 40000,
            "q3_fy24_advances": 27000,
            "q4_fy24_deposits": 41000,
            "q4_fy24_advances": 28000,
            "q1_fy25_deposits": 42000,
            "q1_fy25_advances": 29000,
            "q2_fy25_deposits": 43000,
            "q2_fy25_advances": 30000,
            "q3_fy25_deposits": 44000,
            "q3_fy25_advances": 31000,
        },
        "Deutsche Bank": {
            "type": "Foreign",
            "headquarters": "Mumbai",
            "nse_ticker": "DEUTSCHE",
            "bse_ticker": "533537",
            "q1_fy24_deposits": 32000,
            "q1_fy24_advances": 21000,
            "q2_fy24_deposits": 33000,
            "q2_fy24_advances": 22000,
            "q3_fy24_deposits": 34000,
            "q3_fy24_advances": 23000,
            "q4_fy24_deposits": 35000,
            "q4_fy24_advances": 24000,
            "q1_fy25_deposits": 36000,
            "q1_fy25_advances": 25000,
            "q2_fy25_deposits": 37000,
            "q2_fy25_advances": 26000,
            "q3_fy25_deposits": 38000,
            "q3_fy25_advances": 27000,
        },
        "ICICI Prudential Wealth": {
            "type": "Foreign",
            "headquarters": "Mumbai",
            "nse_ticker": "IPRUIDL",
            "bse_ticker": "533538",
            "q1_fy24_deposits": 28000,
            "q1_fy24_advances": 18000,
            "q2_fy24_deposits": 29000,
            "q2_fy24_advances": 19000,
            "q3_fy24_deposits": 30000,
            "q3_fy24_advances": 20000,
            "q4_fy24_deposits": 31000,
            "q4_fy24_advances": 21000,
            "q1_fy25_deposits": 32000,
            "q1_fy25_advances": 22000,
            "q2_fy25_deposits": 33000,
            "q2_fy25_advances": 23000,
            "q3_fy25_deposits": 34000,
            "q3_fy25_advances": 24000,
        },
    }
    
    # Additional PSBs (Not Merged)
    additional_psb_data = {
        "Indian Overseas Bank": {
            "type": "PSB",
            "headquarters": "Chennai",
            "nse_ticker": "IOB",
            "bse_ticker": "500029",
            "q1_fy24_deposits": 380000,
            "q1_fy24_advances": 285000,
            "q2_fy24_deposits": 390000,
            "q2_fy24_advances": 295000,
            "q3_fy24_deposits": 400000,
            "q3_fy24_advances": 305000,
            "q4_fy24_deposits": 410000,
            "q4_fy24_advances": 315000,
            "q1_fy25_deposits": 420000,
            "q1_fy25_advances": 325000,
            "q2_fy25_deposits": 430000,
            "q2_fy25_advances": 335000,
            "q3_fy25_deposits": 440000,
            "q3_fy25_advances": 345000,
        },
        "Bank of Maharashtra": {
            "type": "PSB",
            "headquarters": "Pune",
            "nse_ticker": "BOM",
            "bse_ticker": "500439",
            "q1_fy24_deposits": 140000,
            "q1_fy24_advances": 105000,
            "q2_fy24_deposits": 145000,
            "q2_fy24_advances": 110000,
            "q3_fy24_deposits": 150000,
            "q3_fy24_advances": 115000,
            "q4_fy24_deposits": 155000,
            "q4_fy24_advances": 120000,
            "q1_fy25_deposits": 160000,
            "q1_fy25_advances": 125000,
            "q2_fy25_deposits": 165000,
            "q2_fy25_advances": 130000,
            "q3_fy25_deposits": 170000,
            "q3_fy25_advances": 135000,
        },
    }
    
    # Historical Banks Data (Merged - for historical trends)
    historical_bank_data = {
        "Allahabad Bank": {
            "type": "Historical PSB",
            "headquarters": "Kolkata",
            "nse_ticker": "ALLBANK",
            "bse_ticker": "500001",
            "q1_fy24_deposits": 280000,
            "q1_fy24_advances": 210000,
            "q2_fy24_deposits": 285000,
            "q2_fy24_advances": 215000,
            "q3_fy24_deposits": 290000,
            "q3_fy24_advances": 220000,
            "q4_fy24_deposits": 295000,
            "q4_fy24_advances": 225000,
            "q1_fy25_deposits": 300000,
            "q1_fy25_advances": 230000,
            "q2_fy25_deposits": 305000,
            "q2_fy25_advances": 235000,
            "q3_fy25_deposits": 310000,
            "q3_fy25_advances": 240000,
        },
        "Dena Bank": {
            "type": "Historical PSB",
            "headquarters": "Mumbai",
            "nse_ticker": "DENABANK",
            "bse_ticker": "500019",
            "q1_fy24_deposits": 220000,
            "q1_fy24_advances": 165000,
            "q2_fy24_deposits": 225000,
            "q2_fy24_advances": 170000,
            "q3_fy24_deposits": 230000,
            "q3_fy24_advances": 175000,
            "q4_fy24_deposits": 235000,
            "q4_fy24_advances": 180000,
            "q1_fy25_deposits": 240000,
            "q1_fy25_advances": 185000,
            "q2_fy25_deposits": 245000,
            "q2_fy25_advances": 190000,
            "q3_fy25_deposits": 250000,
            "q3_fy25_advances": 195000,
        },
        "Vijaya Bank": {
            "type": "Historical PSB",
            "headquarters": "Bangalore",
            "nse_ticker": "VIJAYABANK",
            "bse_ticker": "532435",
            "q1_fy24_deposits": 210000,
            "q1_fy24_advances": 155000,
            "q2_fy24_deposits": 215000,
            "q2_fy24_advances": 160000,
            "q3_fy24_deposits": 220000,
            "q3_fy24_advances": 165000,
            "q4_fy24_deposits": 225000,
            "q4_fy24_advances": 170000,
            "q1_fy25_deposits": 230000,
            "q1_fy25_advances": 175000,
            "q2_fy25_deposits": 235000,
            "q2_fy25_advances": 180000,
            "q3_fy25_deposits": 240000,
            "q3_fy25_advances": 185000,
        },
        "Andhra Bank": {
            "type": "Historical PSB",
            "headquarters": "Hyderabad",
            "nse_ticker": "ANDHRABANK",
            "bse_ticker": "500033",
            "q1_fy24_deposits": 195000,
            "q1_fy24_advances": 145000,
            "q2_fy24_deposits": 200000,
            "q2_fy24_advances": 150000,
            "q3_fy24_deposits": 205000,
            "q3_fy24_advances": 155000,
            "q4_fy24_deposits": 210000,
            "q4_fy24_advances": 160000,
            "q1_fy25_deposits": 215000,
            "q1_fy25_advances": 165000,
            "q2_fy25_deposits": 220000,
            "q2_fy25_advances": 170000,
            "q3_fy25_deposits": 225000,
            "q3_fy25_advances": 175000,
        },
        "UCO Bank": {
            "type": "Historical PSB",
            "headquarters": "Kolkata",
            "nse_ticker": "UCOBANK",
            "bse_ticker": "500050",
            "q1_fy24_deposits": 180000,
            "q1_fy24_advances": 130000,
            "q2_fy24_deposits": 185000,
            "q2_fy24_advances": 135000,
            "q3_fy24_deposits": 190000,
            "q3_fy24_advances": 140000,
            "q4_fy24_deposits": 195000,
            "q4_fy24_advances": 145000,
            "q1_fy25_deposits": 200000,
            "q1_fy25_advances": 150000,
            "q2_fy25_deposits": 205000,
            "q2_fy25_advances": 155000,
            "q3_fy25_deposits": 210000,
            "q3_fy25_advances": 160000,
        },
    }
    
    # Combine all data
    all_bank_data = {**psb_data, **private_data, **sfb_data, **foreign_data, **additional_psb_data, **historical_bank_data}
    
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
