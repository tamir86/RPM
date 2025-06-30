# 📘 Nike SB RPM Digital Archive — Project Log

**Date:** 2025-06-20

---

## ✅ SYSTEM SETUP OVERVIEW

### Tools in Use
- **ChatGPT** – Strategy, code generation, system logic
- **VS Code** – Coding, file management, archive control
- **Python** – Automation scripts for photo metadata extraction
- **.csv** – Structured metadata storage (`master_metadata.csv`)
- **.md** – Documentation, changelogs, research logs

---

## 🏗️ CURRENT WORKING STRUCTURE

```
Nike_SB_RPM_Archive/
├── 02_Models/
│   ├── BA2037-089/
│   │   └── Photos/
│   │       └── BA2037-089_front_1_ebay.jpg
│   ├── ...
│
├── master_metadata.csv
└── Daily Archiving Notes.md
```

---

## 📸 FILE NAMING FORMAT

```
BA####-###_[viewtype]_[sequence][_source].ext
```

Examples:
- `BA2037-089_front_1.jpg`
- `BA2037-089_back_2_ebay.jpg`

---

## 🧠 KEY METADATA FIELDS IN `master_metadata.csv`

| Field             | Description                          |
|------------------|--------------------------------------|
| filename          | Photo filename                      |
| style_code        | Nike SB RPM model code              |
| view_type         | front / back / tag / etc.           |
| sequence          | Sequential number per view type     |
| date_saved        | Date image was logged               |
| source_url        | Link to source (e.g. eBay)          |
| context_notes     | Optional context, visual insights   |
| confidence_level  | Manual flag for authenticity        |
| seller_name       | eBay or third-party seller          |

---

## 🔁 WORKFLOW STATUS

- ✅ File naming rules finalized and enforced
- ✅ Dual-format naming supports `_ebay`, `_stockx`, etc.
- ✅ Python script built to:
  - Scan folders for images
  - Parse structured filenames
  - Prompt for seller info if `_ebay` present
  - Append to `master_metadata.csv`

---

## 🧾 KEY MILESTONES LOG

- 2025-06-16: Metadata script first tested and validated
- 2025-06-17: Clean, strict naming format enforced (no spaces, lowercase)
- 2025-06-19: eBay photo collection begins in structured format
- 2025-06-20: Script upgraded to prompt for `seller_name`, `source_url`, `context_notes`
- 2025-06-20: Markdown and Obsidian documentation plan formalized

---

## 🔧 NEXT STEPS

- [ ] Begin logging seller metadata for existing `_ebay` images
- [ ] Backfill missing `source_url` + context in `master_metadata.csv`
- [ ] Add Obsidian vault structure for advanced tagging + queries
- [ ] Document rare model case studies (e.g. Floral Camo, Tiger Camo)

---

