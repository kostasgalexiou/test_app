# streamlit_app.py

# import streamlit as st
# from supabase import create_client, Client

# streamlit_app.py

import streamlit as st
from st_supabase_connection import SupabaseConnection

# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# Perform query.
rows = conn.query("*", table="mytable", ttl="10m").execute()

# Print results.
for row in rows.data:
    st.write(f"{row['name']} has a :{row['pet']}:")
# print(st.secrets)
# print(st.secrets['connections']['supabase']["SUPABASE_URL"], '$$$$$$$$$$$$$$$$$$$$$$$$')
# # Initialize connection.
# # Uses st.cache_resource to only run once.
# @st.cache_resource
# def init_connection():
#     url = st.secrets['connections']['supabase']["SUPABASE_URL"]
#     key = st.secrets['connections']['supabase']["SUPABASE_KEY"]
#     return create_client(url, key)
#
#
# supabase = init_connection()
#
#
# # Perform query.
# # Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=600)
# def run_query():
#     return supabase.table("mytable").select("*").execute()
#
#
# rows = run_query()
#
# # Print results.
# for row in rows.data:
#     st.write(f"{row['name']} has a :{row['pet']}:")