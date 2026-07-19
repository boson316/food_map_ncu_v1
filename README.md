# Campus Food Map NCU v1

**Languages:** [English](README.md) · [中文](README.zh-TW.md)

> **Status:** Data ready · **Spec:** [docs/v1-規格.md](docs/v1-規格.md)  
> **Repo:** https://github.com/boson316/food_map_ncu_v1 · **Demo:** https://boson-food-map-ncu-v1.streamlit.app

Food map around National Central University (Zhongli campus). Offline Google Places cache, Huang-weighted rating × distance sort, 15 food categories, wheel Top 40.

## Campus parameters (locked)

| Item | Value |
|------|-------|
| Center | `24.9686, 121.1953` (Zhongli main campus) |
| Default search radius | **2 km** |
| Slider max | **5 km** |
| Fetch pool | **3 km** |
| Wheel | Top **40** |

## Run locally

```powershell
cd C:\Users\User\Documents\code\food_map_ncu_v1
python -m pip install -r requirements.txt
$env:PYTHONPATH = "src"
python -m pytest -q --cov=src --cov-fail-under=70
streamlit run streamlit_app.py
```

## CLI

```powershell
cd C:\Users\User\Documents\code\food_map_ncu_v1
$env:PYTHONPATH = "src"
python -m foodmap search --lat 24.9686 --lon 121.1953 --sort composite --data data/places_cache.public.json
```

## Fetch data (Google API key required)

```powershell
cd C:\Users\User\Documents\code\food_map_ncu_v1
$env:PYTHONPATH = "src"
$env:GOOGLE_MAPS_API_KEY = "YOUR_KEY"
python scripts/fetch_places_to_json.py
python scripts/enrich_food_groups.py data/places_cache.json
copy data\places_cache.json data\places_cache.public.json
```

## Docs

[PRD.md](PRD.md) · [ROADMAP.md](ROADMAP.md) · [SUMMARY.md](SUMMARY.md)
