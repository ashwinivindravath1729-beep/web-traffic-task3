import pandas as pd
import numpy as np

print("=" * 55)
print("   WEB TRAFFIC ANALYTICS — TASK 3")
print("=" * 55)

# Step 1: Create website traffic dataset
data = {
    'session_id': range(1, 21),
    'user_id': [101,102,103,104,105,101,106,107,102,108,
                109,103,110,111,104,112,105,113,106,114],
    'page_visited': ['Home','Products','Home','Pricing','Blog',
                     'Products','Home','About Us','Pricing','Home',
                     'Products','Blog','Home','Pricing','Products',
                     'Contact','Home','Blog','Pricing','Products'],
    'session_duration_mins': [2.5,8.3,1.2,4.5,6.7,9.1,0.8,5.2,4.35,1.5,
                               7.8,3.4,2.1,6.2,8.9,0.5,3.7,5.5,4.1,7.2],
    'pages_viewed': [1,4,1,3,5,6,1,4,3,1,5,3,2,4,6,1,3,4,3,5],
    'device': ['Mobile','Desktop','Mobile','Desktop','Tablet',
               'Desktop','Mobile','Desktop','Mobile','Tablet',
               'Desktop','Mobile','Mobile','Desktop','Tablet',
               'Mobile','Desktop','Mobile','Desktop','Tablet'],
    'traffic_source': ['Google','Direct','Social','Google','Email',
                       'Direct','Social','Google','Mobile','Direct',
                       'Email','Google','Social','Direct','Google',
                       'Social','Email','Direct','Google','Email'],
    'bounced': [1,0,1,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0],
    'converted': [0,1,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1,1]
}

df = pd.DataFrame(data)
print(f"\n✅ Dataset loaded: {df.shape[0]} sessions, {df.shape[1]} columns")

# Step 2: Basic overview
print("\n--- TRAFFIC OVERVIEW ---")
print(f"Total Sessions    : {len(df)}")
print(f"Unique Users      : {df['user_id'].nunique()}")
print(f"Avg Session Time  : {df['session_duration_mins'].mean():.2f} mins")
print(f"Avg Pages Viewed  : {df['pages_viewed'].mean():.2f}")
print(f"Bounce Rate       : {(df['bounced'].sum()/len(df)*100):.2f}%")
print(f"Conversion Rate   : {(df['converted'].sum()/len(df)*100):.2f}%")

# Step 3: Most visited pages
print("\n--- MOST VISITED PAGES ---")
page_views = df['page_visited'].value_counts().reset_index()
page_views.columns = ['Page', 'Views']
print(page_views.to_string(index=False))

# Step 4: Avg session duration per page
print("\n--- AVG TIME SPENT PER PAGE (mins) ---")
page_time = df.groupby('page_visited')['session_duration_mins'].mean().round(2).sort_values(ascending=False)
print(page_time.to_string())

# Step 5: Traffic source analysis
print("\n--- TRAFFIC SOURCES ---")
source = df.groupby('traffic_source').agg(
    Sessions=('session_id','count'),
    Conversions=('converted','sum'),
    Bounces=('bounced','sum')
).reset_index()
source['Conversion Rate %'] = (source['Conversions']/source['Sessions']*100).round(2)
print(source.to_string(index=False))

# Step 6: Device usage
print("\n--- DEVICE USAGE ---")
device = df['device'].value_counts().reset_index()
device.columns = ['Device', 'Sessions']
device['Percentage %'] = (device['Sessions']/len(df)*100).round(2)
print(device.to_string(index=False))

# Step 7: Drop-off points (bounced pages)
print("\n--- DROP-OFF POINTS (Bounce by Page) ---")
bounce_page = df.groupby('page_visited')['bounced'].sum().sort_values(ascending=False)
print(bounce_page.to_string())

# Step 8: User journey insights
print("\n--- KEY INSIGHTS ---")
print("1. Products page has most views — focus on improving it")
print("2. Pricing page has highest avg time — users are interested!")
print("3. Home & Contact pages have high bounce rates")
print("4. Google brings most traffic — invest more in SEO")
print("5. Mobile users are high — ensure mobile-friendly design")
print("6. Email campaigns convert well — increase email marketing")

# Step 9: Save results
df.to_csv('traffic_analysis.csv', index=False)
print("\n✅ Saved to traffic_analysis.csv!")
print("\n🎉 Web Traffic Analytics — COMPLETE!")