"""
Indian Banks CD Ratio Analysis Dashboard
Styling & UI Components
"""

import streamlit as st
from config import COLORS

def get_custom_css():
    """Return custom CSS for the dashboard"""
    return f"""
    <style>
    /* Main page background */
    .main {{
        background-color: #F5F5F5;
    }}
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {{
        background-color: #F8F9FA;
    }}
    
    /* Headers styling */
    h1, h2, h3 {{
        color: {COLORS['primary_dark']};
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}
    
    /* Text styling */
    p {{
        color: {COLORS['text_dark']};
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}
    
    /* Metric boxes */
    [data-testid="stMetric"] {{
        background-color: #FFFFFF;
        border-radius: 10px;
        border-left: 5px solid {COLORS['primary_dark']};
        padding: 15px;
    }}
    
    /* Dataframe styling */
    [data-testid="stDataFrame"] {{
        background-color: #FFFFFF;
        border-radius: 8px;
    }}
    </style>
    """

def render_section_header(text):
    """Render section header with contrast background"""
    if st is None:
        return
    html_content = f'<div style="background-color: {COLORS["primary_dark"]}; color: {COLORS["gold"]}; padding: 20px; border-radius: 10px; margin-bottom: 20px;"><h2 style="margin: 0; font-size: 28px; font-weight: 700;">{text}</h2></div>'
    st.markdown(html_content, unsafe_allow_html=True)

def render_subsection_header(text):
    """Render subsection header"""
    if st is None:
        return
    st.markdown(f"#### {text}")

def render_divider():
    """Render a divider line"""
    if st is None:
        return
    st.markdown("---")

def render_info_box(content):
    """Render info box"""
    if st is None:
        return
    st.info(content)

def render_warning_box(content):
    """Render warning box"""
    if st is None:
        return
    st.warning(content)

def render_success_box(content):
    """Render success box"""
    if st is None:
        return
    st.success(content)

def render_error_box(content):
    """Render error box"""
    if st is None:
        return
    st.error(content)

def render_metric_card(label, value, delta=None):
    """Render a metric card with value"""
    if st is None:
        return
    
    if delta:
        st.metric(label=label, value=value, delta=delta)
    else:
        st.metric(label=label, value=value)

def render_cd_ratio_status(cd_ratio):
    """Return status indicator for CD ratio"""
    if cd_ratio >= 78 and cd_ratio <= 85:
        return "🟢 EXCELLENT"
    elif cd_ratio >= 70 and cd_ratio < 78:
        return "🟢 HEALTHY"
    elif cd_ratio >= 65 and cd_ratio < 70:
        return "🟡 MODERATE"
    elif cd_ratio < 65:
        return "⚠️ LOW"
    elif cd_ratio > 85 and cd_ratio <= 95:
        return "🟠 HIGH"
    else:
        return "🔴 CRITICAL"

def get_cd_ratio_color(cd_ratio):
    """Get color based on CD ratio value"""
    if cd_ratio >= 78 and cd_ratio <= 85:
        return COLORS["positive"]
    elif cd_ratio >= 70 and cd_ratio < 78:
        return COLORS["primary_dark"]
    elif cd_ratio >= 65 and cd_ratio < 70:
        return COLORS["neutral"]
    elif cd_ratio < 65:
        return COLORS["caution"]
    else:
        return COLORS["negative"]

def render_footer(author, brand_name, data_sources):
    """Render footer section"""
    if st is None:
        return
    
    st.markdown("---")
    footer_html = f"""
    <div style="text-align: center; color: #7F8C8D; font-size: 12px; padding: 20px;">
        <p><strong>{brand_name}</strong></p>
        <p>📊 Developed by {author}</p>
        <p>📚 Data Sources: {data_sources}</p>
        <p>© 2025 All Rights Reserved</p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

def display_styled_dataframe(df):
    """Display dataframe with custom styling"""
    if st is None:
        return
    
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            col: st.column_config.NumberColumn(format="%.2f") 
            for col in df.select_dtypes(include=['float64']).columns
        }
    )

def create_bank_type_badge(bank_type):
    """Create styled badge for bank type"""
    if bank_type == "PSB":
        return f'<span style="background-color: {COLORS["psb_color"]}; color: white; padding: 5px 10px; border-radius: 15px; font-size: 12px;">{bank_type}</span>'
    elif bank_type == "Private":
        return f'<span style="background-color: {COLORS["private_color"]}; color: white; padding: 5px 10px; border-radius: 15px; font-size: 12px;">{bank_type}</span>'
    else:
        return f'<span style="background-color: {COLORS["sfb_color"]}; color: white; padding: 5px 10px; border-radius: 15px; font-size: 12px;">{bank_type}</span>'
