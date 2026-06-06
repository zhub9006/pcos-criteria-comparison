# PCOS Diagnostic Criteria Comparison

A visual comparison of the three main Polycystic Ovary Syndrome (PCOS) diagnostic criteria sets:

| Criteria | Year | Issuing Body | Rule |
|----------|------|-------------|------|
| **NIH 1990** | 1990 | National Institutes of Health | Both features required |
| **Rotterdam 2003** | 2003 | ESHRE / ASRM | 2 of 3 required |
| **AES 2006** | 2006 | Androgen Excess Society | HA required + either OD or PCO |

## Feature Requirements

| Feature | NIH 1990 | Rotterdam 2003 | AES 2006 |
|---------|----------|----------------|----------|
| Oligo-/Anovulation | ✅ Required | 🔵 One of three | 🟡 Either/Or (if HA present) |
| Clinical Hyperandrogenism | ✅ Required | 🔵 One of three | ✅ Required |
| Biochemical Hyperandrogenism | ✅ Required | 🔵 One of three | ✅ Required |
| Polycystic Ovaries (US) | ⬜ Not considered | 🔵 One of three | 🟡 Either/Or (if HA present) |
| Exclusion of Other Disorders | ✅ Required | ✅ Required | ✅ Required |

## Rotterdam Phenotypes Captured

| Phenotype | Features | NIH 1990 | Rotterdam 2003 | AES 2006 |
|-----------|----------|----------|----------------|----------|
| **A** (Classic) | HA + OD + PCO | ✅ | ✅ | ✅ |
| **B** (HA + Anovulatory) | HA + OD | ✅ | ✅ | ✅ |
| **C** (Ovulatory HA) | HA + PCO | ❌ | ✅ | ✅ |
| **D** (Normo-androgenic) | OD + PCO | ❌ | ✅ | ❌ |

## Key Differences

- **NIH 1990** is the narrowest definition, capturing only the metabolically-loaded classic phenotype (~6–10% prevalence). Does not include polycystic ovarian morphology as a criterion.
- **Rotterdam 2003** is the most widely used, broadest phenotype capture, and source of the four-phenotype classification (~10–15% prevalence). Requires any 2 of 3 features.
- **AES 2006** frames PCOS as fundamentally hyperandrogenic, excluding normo-androgenic Phenotype D (~8–12% prevalence). Hyperandrogenism is mandatory.

## Files

| File | Description |
|------|-------------|
| `pcos_criteria_comparison.py` | Python script that generates the comparison chart (PNG + SVG) |
| `pcos_criteria_comparison_chart.svg` | Presentation-ready comparison chart (SVG, viewable in browsers & PowerPoint) |
| `pcos_criteria_comparison.png` | Generated locally by running the script (200 DPI, presentation-ready) |

## Usage

```bash
pip install matplotlib numpy
python pcos_criteria_comparison.py
```

This generates both:
- `pcos_criteria_comparison.png` — high-resolution PNG for presentations
- `pcos_criteria_comparison_chart.svg` — scalable vector graphic

## Chart Legend

| Color | Meaning |
|-------|---------|
| 🔴 Deep Red | **Required** — must be present for diagnosis |
| 🟡 Amber | **Either / Or** — counts toward a multi-criteria threshold |
| ⬜ Light Grey | **Not Required** — not part of this criteria set |

## Sources

- Zawadzki & Dunaif, NIH 1990 working definition
- Rotterdam ESHRE/ASRM 2003 consensus (Fertility & Sterility, 2004)
- Azziz et al., AE-PCOS Society 2006 position statement (J Clin Endocrinol Metab)
- International Evidence-Based PCOS Guideline 2023 (Teede et al.)
- Clinical reference: [endocrinologyindia/nie2](https://github.com/endocrinologyindia/nie2) — PCOS diagnostic criteria notes

## License

MIT
