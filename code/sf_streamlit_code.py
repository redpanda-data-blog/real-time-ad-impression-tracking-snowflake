# Import Python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title(" :blue[Campaign Analytics]" )
st.write(
    """ *** Engagement Metrics Dashboard *** """
)

# Get the current credentials
session = get_active_session()
  
# Calculate the sum of ad impressions 
impressions_data = session.sql("select AD_ID,SUM(AD_IMPRESSIONS) AS TOTAL_IMPRESSIONS from CAMPAIGN_ANALYTICS.ENGAGEMENT_METRICS.AD_RAW_DATA group by AD_ID")

# Execute the query and convert it into a pandas DataFrame
queried_impressions_data = impressions_data.to_pandas()


# Calculate the sum of ad clicks 
clicks_data = session.sql("select AD_ID,SUM(AD_CLICKS) AS TOTAL_CLICKS from CAMPAIGN_ANALYTICS.ENGAGEMENT_METRICS.AD_RAW_DATA group by AD_ID")

# Execute the query and convert it into a pandas DataFrame
queried_clicks_data = clicks_data.to_pandas()

a, b = st.columns(2)
with a:
    st.subheader("Impressions per ad")
    st.bar_chart(data=queried_impressions_data, x="AD_ID", y="TOTAL_IMPRESSIONS", color="#f4e941")
with b:
    st.subheader("Clicks per ad")
    st.bar_chart(data=queried_clicks_data, x="AD_ID", y="TOTAL_CLICKS", color="#4ece09")


# Ad with max & min clicks 
ad_max_clicks = session.sql("select AD_ID, sum(AD_CLICKS) AS total_clicks from  CAMPAIGN_ANALYTICS.ENGAGEMENT_METRICS.AD_RAW_DATA group by AD_ID order by total_clicks desc limit 1")
ad_min_clicks = session.sql("select AD_ID, sum(AD_CLICKS) AS total_clicks from  CAMPAIGN_ANALYTICS.ENGAGEMENT_METRICS.AD_RAW_DATA group by AD_ID order by total_clicks asc limit 1")
max_clicks_data = ad_max_clicks.to_pandas()
min_clicks_data = ad_min_clicks.to_pandas()


a, b = st.columns(2)
with a:
    st.subheader("Ad with maximum clicks")
    st.dataframe(max_clicks_data, use_container_width=True)
with b:
    st.subheader("Ad with minimum clicks")
    st.dataframe(min_clicks_data, use_container_width=True)


# Calculate the click-through rate
ctr_data = session.sql("select AD_ID, ROUND(SUM(AD_CLICKS)/SUM(AD_IMPRESSIONS) * 100,2) AS CTR_PERCENTAGE from CAMPAIGN_ANALYTICS.ENGAGEMENT_METRICS.AD_RAW_DATA group by AD_ID order by CTR_PERCENTAGE desc ")
queried_ctr_data = ctr_data.to_pandas()

st.subheader("CTR per ad")
st.dataframe(queried_ctr_data, use_container_width=True)


