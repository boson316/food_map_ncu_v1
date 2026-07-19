# 校園美食地圖 CCU v1 — 專案總結

**Languages:** [English](SUMMARY.en.md) · [中文](SUMMARY.md)

> **路徑：** `c:\Users\User\Documents\code\food_map_ccu_v1` · **更新：** 2026-06-26  
> **產出方式：** project_bootstrap + 人工規劃

---

## 一句話

中正大學民雄校本部美食地圖 v1：Fork 宜大 v2，**預設搜尋 3 km、資料池 8 km、轉盤 Top 40**。

---

## 雙指標

| 指標 | 進度 | 含義 |
|------|------|------|
| **code_complete** | **~90%** | Fork + 快取 631 家 + 測試綠；待 Cloud |
| **go_to_market** | **~20%** | 有快取；待 GitHub push + Streamlit URL |

---

## 目錄結構（目前）

```
food_map_ccu_v1/
├── docs/v1-規格.md      # 完整規格
├── PRD.md / ROADMAP.md / TASKS.md
├── src/app.py             # bootstrap 占位（Phase 1 替換為 foodmap）
├── tests/                 # bootstrap 占位
└── artifacts/decision_*.md
```

**Phase 1 後預期：** 與 `校園美食地圖_v2` 同構（`src/foodmap/`、`streamlit_app.py` 等）。

---

## 已鎖定決策

| 項目 | 決策 |
|------|------|
| 多校策略 | 獨立 repo `food_map_ccu_v1` |
| 預設搜尋 | **3 km**（非 8 km） |
| 資料池 | **8 km** fetch |
| NTU 參數 | 另 repo；fetch 2 km、預設 1 km |

---

## 驗證（Phase 1 後）

```powershell
cd food_map_ccu_v1
$env:PYTHONPATH = "src"
pytest -q --cov=src --cov-fail-under=70
```

---

## 文件索引

[docs/v1-規格.md](docs/v1-規格.md) · [PRD.md](PRD.md) · [PLANNING.md](PLANNING.md)
