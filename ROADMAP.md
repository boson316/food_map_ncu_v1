# ROADMAP — 校園美食地圖 CCU v1

**Languages:** [English](ROADMAP.en.md) · [中文](ROADMAP.md)

> **時間預算：** 6–8 h（含 API fetch）· **策略：** Fork 宜大 v2 → 獨立部署  
> **對齊：** [PRD.md](PRD.md) · [docs/v1-規格.md](docs/v1-規格.md)

---

## 總覽

| 階段 | 時間 | 重點 | 交付 |
|------|------|------|------|
| Phase 0 | 完成 | 規劃 + bootstrap | 本 repo 規格文件 |
| Phase 1 | 0.5 h | Fork 宜大 v2、改常數 | `pytest -q` 綠 |
| Phase 2 | 3–5 h | Fetch 8 km + overrides | `places_cache.public.json` |
| Phase 3 | 0.5 h | Streamlit Cloud | 公開 URL |
| Phase 4 | 0.5 h | 作品集卡片 | portfolio 更新 |

---

## 目前進度

| 指標 | 進度 |
|------|------|
| code_complete | **5%**（僅規劃 scaffold） |
| go_to_market | **0%** |

```
code_complete    [█░░░░░░░░░]  5%
go_to_market     [░░░░░░░░░░]  0%
```

---

## Phase 1 — Fork + 常數

- **In scope：** 複製 `校園美食地圖_v2` 的 `src/foodmap/`、`tests/`、`scripts/`（美食相關）
- **常數：** 中心 `23.5615,120.4808`；預設半徑 `3.0`；slider max `8.0`
- **驗收：** `pytest -q` 全綠

## Phase 2 — 資料

- Fetch `--radius-m 8000 --grid 10 --target 1000`
- `enrich` + `stats` + 手動 overrides
- **驗收：** CLI smoke + 地圖有店

## Phase 3 — 部署

- GitHub `boson316/food_map_ccu_v1`
- Streamlit Cloud · Main file `streamlit_app.py`

## v1.1（Out of Scope）

- 轉盤 pin 常去店
- 嘉義市次中心點
- `foodmap-core` 共用 package

---

## 相關

[SUMMARY.md](SUMMARY.md) · [TECH_DEBT.md](TECH_DEBT.md) · [TASKS.md](TASKS.md)
