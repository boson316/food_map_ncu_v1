# Streamlit Cloud × GitHub Deployment (NCU Food Map)

**Languages:** [English](streamlit-cloud-deploy.md) · [中文](streamlit-cloud-部署步驟.md)

> **Goal:** Free Streamlit Community Cloud hosting; share URL / QR with NCU students.

---

## 0. Pre-flight (local)

```powershell
cd C:\Users\User\Documents\code\food_map_ncu_v1
python -m pip install -r requirements.txt
$env:PYTHONPATH = "src"
python -m pytest -q --cov=src --cov-fail-under=70
streamlit run streamlit_app.py
```

Open `http://localhost:8501` — verify list + wheel tabs; default radius **2 km**, center **NCU Zhongli campus**.

---

## 1. Data strategy

| File | In Git? | On cloud |
|------|---------|----------|
| `data/places_cache.json` | No (`.gitignore`) | Not uploaded |
| `data/places_cache.public.json` | **Yes** (recommended) | ~500 restaurants (3 km pool) |
| Neither | — | 15 sample restaurants (Yilan demo coords; poor NCU UX) |

**Before deploy:**

```powershell
cd C:\Users\User\Documents\code\food_map_ncu_v1
copy data\places_cache.json data\places_cache.public.json
```

Ensure no API keys in JSON.

---

## 2. GitHub repo

| Item | Value |
|------|-------|
| Account | `boson316` |
| Repo | [food_map_ncu_v1](https://github.com/boson316/food_map_ncu_v1) |
| Visibility | Public recommended for QR sharing |

**Commit:** `src/`, `tests/`, `scripts/`, `requirements.txt`, `streamlit_app.py`, `README.md`, `README.zh-TW.md`, `PRD.md`, `data/places_cache.public.json`, `.github/workflows/`.

**Do not commit:** `.env`, `GOOGLE_MAPS_API_KEY`, `data/places_cache.json`, internal files listed in `.gitignore`.

---

## 3. Streamlit Community Cloud

1. https://share.streamlit.io → **Create app**
2. Repo: `boson316/food_map_ncu_v1`, branch `main`
3. **Main file path:** `streamlit_app.py` (repo root)
4. **Deploy**

**Live URL:** https://boson-food-map-ncu-v1.streamlit.app

**Secrets:** Not required for normal operation (reads JSON cache). Only needed if re-fetching Places on the server.

---

## 4. Post-deploy checklist

- [ ] Title: 國立中央大學 校園美食地圖
- [ ] Default sidebar radius **2 km**
- [ ] Restaurant list within 2 km (~250+)
- [ ] Wheel ≤ 40, excludes closed venues
- [ ] Map pin: NCU main campus
