# streamlit_app.py
import pandas as pd
import time
import streamlit as st
from supabase import create_client, Client
from collections import OrderedDict as od

# streamlit_app.py

# import streamlit as st
# from st_supabase_connection import SupabaseConnection
#
# # Initialize connection.
# conn = st.connection("supabase",type=SupabaseConnection)
#
# # Perform query.
# rows = conn.query("*", table="mytable", ttl="10m").execute()
#
# # Print results.
# for row in rows.data:
#     st.write(f"{row['name']} has a :{row['pet']}:")

# Initialize connection.
# Uses st.cache_resource to only run once.

# url: str = os.environ.get("SUPABASE_URL")
# key: str = os.environ.get("SUPABASE_KEY")
url: str = st.secrets['connections']['supabase']["SUPABASE_URL"]
key: str = st.secrets['connections']['supabase']["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

user = st.text_input("Introduce your full name")
new_species = st.text_input(
    "Introduce the name of the species (Latin name or common name)"
)
alleles_file = st.file_uploader("Upload marker file", type=["txt", "csv"])

if alleles_file is not None and new_species is not None:
    alleles_list = pd.read_csv(alleles_file, header=None).values.tolist()
    markerlist = [x[0] for x in alleles_list]

    timestr = time.strftime("%Y-%m-%d")
    # markerlist.insert(0, {'marker_name': "marker_name", "person": "person", "uploadeddate": timestr})
    for i in alleles_list:
        markerlist.append({'Marker_name': i[0], 'Species': new_species, 'Person': user, 'Date': timestr})

    #    value = {'marker_name': "marker_name", "person": "person", "uploadeddate": timestr}
    #    supabase.table("almond").insert(value).execute()

    # for m in markerlist:
    #     supabase.table("speciesDB").insert(m).execute()

    st.success(
        "%s markers were added to the database correctly"
        % new_species.upper()
    )

all_data, count = supabase.table('speciesDB').select("*").execute()
info = list(all_data[1])
mlist = []
plist = []
tlist = []
slist = []
for d in info:
    m, p, t, s = list(d.values())
    mlist.append(m)
    plist.append(p)
    tlist.append(t)
    slist.append(s)
print(mlist)
print(set(plist))
print(set(tlist))
print(set(slist))
