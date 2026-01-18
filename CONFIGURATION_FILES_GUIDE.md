# Configuration Files Documentation

**Last Updated:** January 18, 2025

---

## 📋 Table of Contents

1. [.streamlit/config.toml](#streamlitconfigtoml)
2. [.env.example](#envexample)
3. [.gitignore](#gitignore)
4. [How to Use](#how-to-use)

---

## .streamlit/config.toml

**Location:** `.streamlit/config.toml`  
**Purpose:** Configure Streamlit app behavior and appearance

### Sections

#### **[theme]** - Visual Appearance
```toml
primaryColor = "#003366"           # Dark blue (primary accent color)
backgroundColor = "#FFFFFF"        # Main background (white)
secondaryBackgroundColor = "#F5F5F5" # Sidebar and widget backgrounds
textColor = "#2C3E50"              # Main text color
font = "sans serif"                # Font family
```

**Colors Used:**
- `#003366` - Dark Blue (banking, trust)
- `#FFFFFF` - White (clean, professional)
- `#F5F5F5` - Light Gray (subtle backgrounds)
- `#2C3E50` - Dark Gray (readable text)

#### **[client]** - Client-Side Behavior
```toml
showErrorDetails = true            # Show detailed error messages for debugging
toolbarMode = "developer"          # Show developer tools
showSidebarNavigation = true       # Display sidebar navigation
gatherUsageStats = false           # Privacy: Don't track usage
```

#### **[logger]** - Logging
```toml
level = "info"                     # Log level (debug, info, warning, error)
messageFormat = "..."              # Log message format
```

#### **[server]** - Server Configuration
```toml
maxUploadSize = 200                # Max file upload size (200 MB)
runOnSave = true                   # Rerun app when files change
headless = true                    # Run without GUI (for servers)
port = 8501                        # Default Streamlit port
enableXsrfProtection = true        # Security: Prevent XSRF attacks
enableCORS = false                 # Security: Disable CORS
```

#### **[browser]** - Browser Settings
```toml
gatherUsageStats = false           # Don't collect analytics
serverAddress = "localhost"        # Server address
serverPort = 8501                  # Port number
```

#### **[custom]** - App-Specific Settings
```toml
app_name = "..."                   # Application name
app_version = "1.0.0"              # Version number
environment = "development"        # Environment type
debug_mode = false                 # Debug flag
```

### Customization

**For Development:**
```toml
[client]
toolbarMode = "developer"          # Show dev tools
showErrorDetails = true            # Detailed errors

[logger]
level = "debug"                    # See all logs
```

**For Production:**
```toml
[client]
toolbarMode = "viewer"             # Hide dev tools
showErrorDetails = false           # Hide error details

[logger]
level = "warning"                  # Only important logs

[server]
enableXsrfProtection = true        # Enable security
enableCORS = false                 # Disable CORS
```

---

## .env.example

**Location:** `.env.example`  
**Purpose:** Template for environment variables

### How to Use

1. **Copy the template:**
   ```bash
   cp .env.example .env
   ```

2. **Edit .env with your values:**
   ```bash
   # Edit with your text editor
   nano .env
   # or
   code .env
   ```

3. **Never commit .env to git** (it contains secrets!)

### Main Configuration Sections

#### **Application Configuration**
```
APP_ENV=development          # Environment type
DEBUG_MODE=false             # Debugging enabled?
APP_NAME=...                 # Application name
APP_VERSION=1.0.0            # Version
```

#### **Database Configuration**

**SQLite (Development):**
```
DB_TYPE=sqlite
DB_NAME=cd_ratio.db
DB_PATH=data/cd_ratio.db
```

**PostgreSQL (Production):**
```
DB_TYPE=postgresql
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=your_password
DB_NAME_POSTGRES=cd_ratio
```

#### **Data Source Configuration**
```
RBI_DATA_FOLDER=data/rbi_monthly
BSE_FILINGS_FOLDER=data/bse_filings
HISTORICAL_DATA_CSV=data/historical_data.csv
```

#### **Logging Configuration**
```
STREAMLIT_LOGGER_LEVEL=info       # Log level
LOG_FILE_PATH=logs/app.log        # Log file location
LOG_TO_CONSOLE=true               # Also log to console
```

#### **API Keys (Optional - Phase 2)**
```
FINANCIAL_MODELING_PREP_API_KEY=your_key
ALPHA_VANTAGE_API_KEY=your_key
NEWS_API_KEY=your_key
```

#### **Alert Configuration (Phase 2)**
```
ENABLE_ALERTS=false
ALERT_EMAIL=your_email@example.com
SLACK_WEBHOOK_URL=https://hooks.slack.com/...
```

#### **Security Configuration**
```
SECRET_KEY=change_this_in_production
CORS_ALLOWED_ORIGINS=localhost:8501
MAX_UPLOAD_SIZE=200
```

#### **Feature Flags**
```
ENABLE_ML_FEATURES=false
ENABLE_STRESS_TESTING=true
ENABLE_PORTFOLIO_ANALYTICS=false
ENABLE_ALERTS=false
```

### Important Notes

⚠️ **NEVER COMMIT .env** - Add to .gitignore (already done)

🔒 **Secure Your Secrets:**
- Change default passwords
- Use strong random strings for SECRET_KEY
- Rotate API keys regularly
- Use environment-specific values

🚀 **For Production:**
- Use environment variables on server
- Use managed database (RDS, Cloud SQL)
- Enable XSRF protection
- Use SSL/TLS certificates
- Disable debug mode

---

## .gitignore

**Location:** `.gitignore`  
**Purpose:** Tell Git which files NOT to track

### Key Patterns Ignored

#### **Python Files**
```
__pycache__/              # Python cache
*.pyc, *.pyo             # Compiled Python files
*.egg-info/              # Package info
venv/, env/              # Virtual environments
```

#### **Environment & Secrets**
```
.env                     # Environment variables (CRITICAL)
.streamlit/secrets.toml  # Streamlit secrets (CRITICAL)
*.key, *.pem             # Private keys
db_credentials.txt       # Database credentials
```

#### **IDE & Editor**
```
.vscode/                 # VS Code settings
.idea/                   # PyCharm settings
*.swp, *.swo            # Vim temp files
```

#### **System Files**
```
.DS_Store               # macOS
Thumbs.db               # Windows
.directory              # Linux
```

#### **Database Files**
```
*.db, *.sqlite          # Database files
*.sqlite3
data/cache/             # Cache files
```

#### **Logs & Backups**
```
*.log                   # Log files
logs/                   # Log directory
*.bak, *.backup        # Backup files
```

### Exceptions (DO track these)

```
!.env.example           # Include template, not secrets
!.gitkeep               # Keep empty directories
```

---

## How to Use

### Initial Setup

```bash
# 1. Copy configuration files
cp .env.example .env
cp .streamlit/config.toml.example .streamlit/config.toml  # if provided

# 2. Edit .env with your values
nano .env
# Update:
# - DB_TYPE, DB_NAME, DB_PATH
# - API keys if using external APIs
# - Email/Slack settings if using alerts
# - Other environment-specific settings

# 3. Never commit secrets
# (already in .gitignore)

# 4. Verify setup
python -c "from dotenv import load_dotenv; load_dotenv(); print('✓ .env loaded')"
```

### For Local Development

**.env:**
```
APP_ENV=development
DEBUG_MODE=true
DB_TYPE=sqlite
STREAMLIT_LOGGER_LEVEL=debug
ENABLE_ALERTS=false
```

**.streamlit/config.toml:**
```
[client]
toolbarMode = "developer"
showErrorDetails = true

[logger]
level = "debug"
```

### For Production

**.env:**
```
APP_ENV=production
DEBUG_MODE=false
DB_TYPE=postgresql
DB_HOST=your_prod_db_host
STREAMLIT_LOGGER_LEVEL=warning
ENABLE_ALERTS=true
```

**.streamlit/config.toml:**
```
[client]
toolbarMode = "viewer"
showErrorDetails = false

[logger]
level = "warning"

[server]
enableXsrfProtection = true
enableCORS = false
```

---

## Security Best Practices

### ✅ DO:
- ✅ Keep .env in .gitignore
- ✅ Use strong passwords
- ✅ Rotate API keys regularly
- ✅ Use environment-specific configs
- ✅ Keep secrets in environment variables
- ✅ Review .gitignore before committing

### ❌ DON'T:
- ❌ Commit .env to git
- ❌ Share API keys in messages
- ❌ Use default passwords
- ❌ Hardcode secrets in code
- ❌ Commit secrets.toml
- ❌ Use same secrets for dev and prod

---

## Common Issues & Solutions

### Issue 1: .env file not being read

**Solution:**
```python
# In your Python code
from dotenv import load_dotenv
import os

load_dotenv()
db_host = os.getenv('DB_HOST')
```

### Issue 2: Streamlit not recognizing config

**Solution:**
```bash
# Restart Streamlit
streamlit run streamlit_app.py --logger.level=debug
```

### Issue 3: Accidentally committed .env

**Solution:**
```bash
# Remove from git (but keep file locally)
git rm --cached .env

# Add to .gitignore if not already there
echo ".env" >> .gitignore

# Commit the removal
git commit -m "Remove .env from tracking"

# Rotate secrets immediately!
```

---

## File Checklist

```
✅ .streamlit/config.toml      (Streamlit settings)
✅ .env.example                (Environment template)
✅ .env                        (Actual env - DON'T commit)
✅ .gitignore                  (Git ignore rules)
✅ config.py                   (App configuration constants)
✅ streamlit_app.py            (Main app)
```

---

## Reference

### .streamlit/config.toml Reference
- [Streamlit Config Docs](https://docs.streamlit.io/library/advanced-features/configuration)

### Environment Variables
- [python-dotenv Docs](https://python-dotenv.readthedocs.io/)

### .gitignore
- [GitHub .gitignore Docs](https://git-scm.com/docs/gitignore)

---

**All configuration files are ready to use!** ✨

