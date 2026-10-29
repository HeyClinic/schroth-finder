# Builds index.html as one self-contained file from src/index.src.html + src/sites.json + src/zips.txt
import json, pathlib
here = pathlib.Path(__file__).parent
t = (here/"src/index.src.html").read_text()
sites = json.dumps(json.load(open(here/"src/sites.json")), separators=(",",":")).replace("</", "<\\/")
zips = (here/"src/zips.txt").read_text()
logo = "data:image/png;base64," + __import__("base64").b64encode((here/"src/heyclinic-logo.png").read_bytes()).decode()
(here/"index.html").write_text(t.replace("__SITES__", sites).replace("__ZIPS__", zips).replace("__LOGO__", logo))
print("built", (here/"index.html").stat().st_size)
