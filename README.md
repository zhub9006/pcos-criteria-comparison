# PCOS Diagnostic Criteria Comparison

A visual comparison of the three main Polycystic Ovary Syndrome (PCOS) diagnostic criteria sets:

| Criteria | Year | Issuing Body | Rule |
|----------|------|-------------|------|
| **NIH 1990** | 1990 | National Institutes of Health | Both features required |
| **Rotterdam 2003** | 2003 | ESHRE / ASRM | 2 of 3 required |
| **AE-PCOS 2006** | 2006 | Androgen Excess and PCOS Society | HA required + either OD or PCO |

## Feature Requirements

| Feature | NIH 1990 | Rotterdam 2003 | AE-PCOS 2006 |
|---------|----------|----------------|--------------|
| Oligo-/Anovulation | ✅ Required | 🔵 One of three | 🟡 Optional (if HA present) |
| Hyperandrogenism | ✅ Required | 🔵 One of three | ✅ Required |
| Polycystic Ovaries (US) | ⬜ Not considered | 🔵 One of three | 🟡 Optional (if HA present) |

## Rotterdam Phenotypes Captured

| Phenotype | Features | NIH 1990 | Rotterdam 2003 | AE-PCOS 2006 |
|-----------|----------|----------|----------------|--------------|
| **A** (Classic) | HA + OD + PCO | ✅ | ✅ | ✅ |
| **B** (HA + Anovulatory) | HA + OD | ✅ | ✅ | ✅ |
| **C** (Ovulatory HA) | HA + PCO | ❌ | ✅ | ✅ |
| **D** (Normo-androgenic) | OD + PCO | ❌ | ✅ | ❌ |

## Key Differences

- **NIH 1990** is the narrowest definition, capturing only the metabolically-loaded classic phenotype (~6–10% prevalence).
- **Rotterdam 2003** is the most widely used, broadest phenotype capture, and source of the four-phenotype classification (~10–15% prevalence).
- **AE-PCOS 2006** frames PCOS as fundamentally hyperandrogenic, excluding normo-androgenic Phenotype D (~8–12% prevalence).

## Files

- `pcos_criteria_comparison.py` — Python script that generates the comparison chart
- `pcos_criteria_comparison.png` — Presentation-ready comparison chart (200 DPI)

## Usage

```bash
pip install matplotlib numpy
python pcos_criteria_comparison.py
```

## Sources

- Zawadzki & Dunaif, NIH 1990 working definition
- Rotterdam ESHRE/ASRM 2003 consensus (Fertility & Sterility)
- AE-PCOS Society 2006 position statement
- International Evidence-Based PCOS Guideline 2023 (Teede et al.)
- Curated data: [rrmadmin/rrm-academy-cf](https://github.com/rrmadmin/rrm-academy-cf) `src/data/pcos.json`

## License

MIT
