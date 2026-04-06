import os
import glob
from datetime import datetime

directory = "/data/.openclaw/workspace/ai-website"
os.chdir(directory)

files = glob.glob("*_uutiset_*.html")
items = []
for f in files:
    parts = f.replace(".html", "").split("_")
    date_str = parts[-1]
    title = " ".join(parts[:-1]).capitalize().replace("-", " ")
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        items.append({"file": f, "date": dt, "title": title, "date_str": date_str})
    except:
        pass

items.sort(key=lambda x: x["date"], reverse=True)

html_content = """<!DOCTYPE html>
<html lang="fi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI-uutiskirjeet</title>
    <style>
        body { font-family: 'Helvetica Neue', Arial, sans-serif; background: #f4f4f0; color: #333; margin: 0; padding: 0; }
        .container { max-width: 800px; margin: 40px auto; padding: 20px; background: #fff; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        .header { background: #0d1b2a; color: white; padding: 30px 20px; border-radius: 8px 8px 0 0; margin: -20px -20px 20px -20px; text-align: center; }
        h1 { margin: 0; font-size: 28px; letter-spacing: 1px; }
        .header p { margin: 10px 0 0 0; color: #7db8e8; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; font-weight: bold; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 15px 0; padding: 20px; border: 1px solid #eee; border-left: 4px solid #2563c7; border-radius: 4px; transition: all 0.2s; background: #fafaf8; }
        li:hover { background: #fff; box-shadow: 0 2px 8px rgba(0,0,0,0.05); transform: translateX(2px); }
        a { text-decoration: none; color: #0d1b2a; font-size: 18px; font-weight: bold; display: block; }
        a:hover { color: #2563c7; }
        .date { font-size: 13px; color: #666; display: block; margin-top: 8px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Tekoälykatsaukset</h1>
            <p>Automatisoitu uutisvirta</p>
        </div>
        
        <h2 style="margin-bottom: 20px; color: #444;">Viimeisimmät julkaisut</h2>
        <ul>
"""

for item in items:
    display_title = item["title"]
    if "Paivan ai" in display_title:
        display_title = "Päivän tärkeimmät AI-uutiset"
    elif "Telco ai" in display_title:
        display_title = "Telco-sektorin AI-uutiset"
        
    html_content += f"""            <li>
                <a href="{item['file']}">{display_title}</a>
                <span class="date">{item['date'].strftime('%d.%m.%Y')}</span>
            </li>\n"""

html_content += """        </ul>
    </div>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html generated")
