# 校園美食地圖 NCU v1

**Languages:** [English](README.md) · [中文](README.zh-TW.md)

> **狀態：** 已上線資料就緒 · **規格：** [docs/v1-規格.md](docs/v1-規格.md)  
> **Repo：** https://github.com/boson316/food_map_ncu_v1 · **Demo：** https://food-map-ncu-v1.streamlit.app（部署後）

國立中央大學中壢校本部周邊美食地圖。離線 Google Places 快取、黃氏星等×距離排序、15 類篩選、轉盤 Top 40。

## 校園參數（已鎖定）

| 項目 | 值 |
|------|-----|
| 中心點 | `24.9686, 121.1953`（中壢校本部） |
| 預設搜尋半徑 | **2 km** |
| Slider 上限 | **5 km** |
| 資料池 fetch | **3 km** |
| 轉盤 | Top **40** |

## 本機執行

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

## 資料抓取（需 Google API Key）

```powershell
cd C:\Users\User\Documents\code\food_map_ncu_v1
$env:PYTHONPATH = "src"
$env:GOOGLE_MAPS_API_KEY = "AIzaSy..."   # Google Cloud Console → Places API Key
python scripts/fetch_places_to_json.py
python scripts/enrich_food_groups.py data/places_cache.json
copy data\places_cache.json data\places_cache.public.json
```

## 文件索引

[PRD.md](PRD.md) · [ROADMAP.md](ROADMAP.md) · [SUMMARY.md](SUMMARY.md)
