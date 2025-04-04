import streamlit as st
import pandas as pd
from scraper import search_google, extract_emails_from_site

st.set_page_config(page_title="LeadGen AI Tool", layout="wide")

# ----------- Stylish Header -----------
st.markdown("""
    <div style='text-align: center; padding: 10px 0;'>
        <h1 style='color: #4CAF50;'>🚀 LeadGen AI Scraper</h1>
        <p style='font-size: 18px;'>Find business emails from Google search results in one click</p>
    </div>
    <hr style="border: 1px solid #4CAF50;">
""", unsafe_allow_html=True)

# ----------- Input Section -----------
st.markdown("### 🔍 Search Configuration")
col1, col2 = st.columns([3, 1])
with col1:
    query = st.text_input("Search for companies (e.g., 'Marketing agencies in Delhi')", "")
with col2:
    num = st.slider("Number of Results", 5, 50, 10)

# ----------- Start Button -----------
scrape = st.button("🚀 Start Scraping")

# ----------- Lead Table -----------
if scrape and query:
    with st.spinner("⏳ Scraping leads from web..."):
        results = search_google(query, num_results=num)
        leads = []
        for r in results:
            emails = extract_emails_from_site(r["link"])
            leads.append({
                "Company": r["title"],
                "Website": r["link"],
                "Email(s)": ", ".join(emails) if emails else "Not found"
            })
        df = pd.DataFrame(leads)

    st.success(f"✅ Found {len(df)} leads for: **{query}**")

    # ----------- Summary Cards -----------
    col1, col2 = st.columns(2)
    with col1:
        st.metric("📈 Total Leads", len(df))
    with col2:
        found_emails = df[df["Email(s)"] != "Not found"]
        st.metric("📧 Emails Found", len(found_emails))

    # ----------- Table & Download -----------
    st.markdown("### 📊 Lead Results")
    st.dataframe(df, use_container_width=True, height=400)

    st.markdown("### 📥 Download Your Leads")
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="leads.csv",
        mime="text/csv",
        use_container_width=True
    )

elif scrape and not query:
    st.warning("⚠️ Please enter a search query first!")

# ----------- Footer -----------
st.markdown("""
    <hr>
    <div style='text-align: center; color: gray; font-size: 14px;'>
        Built for the LeadGen Challenge ⚡ | <a href="https://github.com/Laksh41" target="_blank">Laksh41</a>
    </div>
""", unsafe_allow_html=True)
