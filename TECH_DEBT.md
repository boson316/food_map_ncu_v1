# TECH_DEBT — 校園美食地圖 CCU v1

> **P0** = 上線前必關 · 更新：2026-06-26

## P0（阻擋 go_to_market）

| ID | 項目 | 狀態 |
|----|------|------|
| TD-CCU-01 | 尚未 Fork `校園美食地圖_v2` 程式碼 | **已關**（2026-06-26） |
| TD-CCU-02 | 無 `places_cache.public.json` | **已關**（631 家，2026-06-26） |
| TD-CCU-03 | 無 Streamlit 公開 URL | 開（待 push + Cloud） |
| TD-CCU-04 | 未跑真實 Google Places fetch 煙測 | **已關** |

## P1

| ID | 項目 |
|----|------|
| TD-CCU-10 | 核心 bugfix 需手動從 `food_map_niu_v2` cherry-pick |
| TD-CCU-11 | `food_group_overrides.json` 人工校正未完成 |
| TD-CCU-12 | 轉盤 pin（`user_favorites.json`）未設定 |

## P2 / v1.1

- 嘉義市次中心點
- 抽 `foodmap-core` 共用 package
