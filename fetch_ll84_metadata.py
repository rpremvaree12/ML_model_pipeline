import requests
import pandas as pd

meta = requests.get('https://data.cityofnewyork.us/api/views/5zyy-y8am.json').json()
cols = meta['columns']

rows = []
for col in cols:
    rows.append({
        'column': col.get('fieldName', ''),
        'description': col.get('description', ''),
        'type': col.get('dataTypeName', '')
    })

df_meta = pd.DataFrame(rows)

html = df_meta.to_html(index=False)

styled = f"""
<html>
<head>
<style>
    body {{ font-family: sans-serif; padding: 20px; }}
    table {{ border-collapse: collapse; width: 100%; table-layout: fixed; }}
    th, td {{ border: 1px solid #ddd; padding: 8px; vertical-align: top; word-wrap: break-word; }}
    th {{ background-color: #f2f2f2; }}
    col:nth-child(1) {{ width: 20%; }}
    col:nth-child(2) {{ width: 70%; }}
    col:nth-child(3) {{ width: 10%; }}
</style>
</head>
<body>
{html}
</body>
</html>
"""

with open('ll84_metadata.html', 'w') as f:
    f.write(styled)

print(f'Wrote {len(rows)} columns to ll84_metadata.html')