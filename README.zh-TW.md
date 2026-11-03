# 校園美食地圖 NCU v1

**Languages:** [English](README.md) · [中文](README.zh-TW.md)

> **狀態：** 已上線資料就緒 · **規格：** [docs/v1-規格.md](docs/v1-規格.md)  
> **Repo：** https://github.com/boson316/food_map_ncu_v1 · **Demo：** https://boson-food-map-ncu-v1.streamlit.app

國立中央大學中壢校本部周邊美食地圖。離線 Google Places 快取、黃氏星等×距離排序、15 類篩選、轉盤 Top 40。

## 校園參數（已鎖定）

| 項目 | 值 |
|------|-----|
| 中心點 | `24.9686, 121.1953`（中壢校本部） |
| 預設搜尋半徑 | **2 km** |
| Slider 上限 | **5 km** |
| 資料池 fetch | **3 km** |
| 轉盤 | Top **40** |

## 靜態網站版（GitHub Pages，免冷啟動）

Streamlit Community Cloud 免費方案閒置後會休眠。`web/` 是同功能的**純靜態** Leaflet 版本：篩選、距離、綜合分數、營業狀態、轉盤全部在瀏覽器計算，沒有伺服器，打開即用、不會休眠。前端與其他校區共用，學校設定只在 `scripts/export_static.py` 的 `SCHOOL`。

- 網址（啟用後）：https://boson316.github.io/food_map_ncu_v1/
- 資料：`python scripts/export_static.py` 產生 `web/data/places.json` 與 `web/data/config.json`。
- 部署：push 到 `main` 後 `.github/workflows/pages.yml` 自動重新匯出並部署。**首次需在 Settings → Pages → Source 選「GitHub Actions」。**
- 本機預覽：`python scripts/export_static.py && python -m http.server -d web 8000`

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
