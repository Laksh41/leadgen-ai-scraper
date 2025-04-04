# 📄 LeadGen AI Scraper — 5-Hour Challenge Report

## 🎯 Goal
To build a fast, accurate lead generation tool that extracts real company emails based on Google search queries — in under 5 hours.

## 💡 Idea
Sales teams need verified, actionable leads. This tool lets you enter a niche/industry and location (like "HR firms in Mumbai") and returns:
- Company names
- Website links
- Publicly available email addresses

All results can be downloaded in a clean CSV format for sales outreach.

## 🛠️ Tech Stack
- **Language:** Python
- **Frontend/UI:** Streamlit
- **Scraping API:** SerpAPI (Google Search Results)
- **HTML Parsing:** BeautifulSoup
- **Data Handling:** Pandas
- **Secret Management:** python-dotenv

## 🔍 Data Preprocessing
- Uses SerpAPI to get top websites for a query
- Visits each website using `requests`
- Extracts text and uses string-matching to find emails
- Removes duplicates and formats output

## ✅ Business Use Case
The tool solves a real sales problem: how to find decision-makers or contact info for outreach. Unlike generic scrapers, this focuses on:
- Real, working emails
- Industry/location targeting
- Simple UI anyone can use

This could help agencies, freelancers, and B2B marketers save hours on lead collection.

## 📊 Model/Logic Used
- No AI model — instead uses Google + deterministic logic for scraping emails
- This avoids complex training and delivers **real-time, accurate results**

## 🏁 Outcome
A working, modern, single-screen Streamlit app that takes input, scrapes leads, shows results, and downloads CSV — all in minutes.

---
Built in under 5 hours for the LeadGen Tool Challenge 💼  
By [Laksh41](https://github.com/Laksh41)
