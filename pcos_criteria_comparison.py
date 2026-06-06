"""
PCOS Diagnostic Criteria Comparison Chart
==========================================
Compares the three main PCOS diagnostic criteria sets:
  - NIH 1990 (National Institutes of Health)
  - Rotterdam 2003 (Rotterdam ESHRE/ASRM)
  - AES 2006 (Androgen Excess Society)

Generates a professional comparison chart saved as a PNG image
suitable for presentations.

Data sourced from:
  - Zawadzki & Dunaif, NIH 1990 working definition
  - Rotterdam ESHRE/ASRM 2003 consensus (Fertility & Sterility)
  - AE-PCOS Society 2006 position statement
  - International Evidence-Based PCOS Guideline 2023 (Teede et al.)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ──────────────────────────────────────────────
# 1. Define the diagnostic features and criteria
# ──────────────────────────────────────────────

features = [
    "Oligo-anovulation",
    "Clinical Hyperandrogenism\n(hirsutism, acne, alopecia)",
    "Biochemical Hyperandrogenism\n(elevated androgens)",
    "Polycystic Ovaries\n(ultrasound morphology)",
    "Exclusion of Other\nAndrogen-Excess Disorders",
]

# Requirement levels:
#   2 = Required (must be present)
#   1 = Either/or (one of multiple options counts)
#   0 = Not required / not part of criteria

# NIH 1990: BOTH oligo-anovulation AND clinical/biochemical hyperandrogenism required
#   PCOM is NOT part of the criteria; exclusion of other causes is implied
nih_1990 = [2, 2, 2, 0, 2]

# Rotterdam 2003: ANY 2 out of 3 (oligo-anovulation, hyperandrogenism, PCOM)
#   Clinical and biochemical HA are grouped; exclusion of other causes implied
rotterdam_2003 = [1, 1, 1, 1, 2]

# AES 2006: Hyperandrogenism REQUIRED + ovarian dysfunction (oligo-anovulation OR PCOM)
#   Exclusion of other androgen-excess disorders is mandatory
aes_2006 = [1, 2, 2, 1, 2]

criteria_data = {
    "NIH 1990":       nih_1990,
    "Rotterdam 2003": rotterdam_2003,
    "AES 2006":       aes_2006,
}

# ──────────────────────────────────────────────
# 2. Build the figure
# ──────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(16, 9))
fig.patch.set_facecolor("#FAFAFA")
ax.set_facecolor("#FAFAFA")

n_features = len(features)
n_criteria = len(criteria_data)

# Cell dimensions
cell_w = 3.2
cell_h = 1.3
header_h = 1.1
label_w = 5.2
gap = 0.12

# Colors
color_required   = "#C62828"   # deep red
color_either     = "#F9A825"   # amber
color_not_req    = "#E0E0E0"   # light grey
color_header_bg  = "#1565C0"   # deep blue
color_label_bg   = "#E3F2FD"   # light blue
text_color_dark  = "#212121"
text_color_light = "#FFFFFF"

def requirement_label(val):
    if val == 2:
        return "Required"
    elif val == 1:
        return "Either / Or"
    else:
        return "Not Required"

def requirement_color(val):
    if val == 2:
        return color_required
    elif val == 1:
        return color_either
    else:
        return color_not_req

def requirement_text_color(val):
    if val == 2:
        return text_color_light
    elif val == 1:
        return text_color_dark
    else:
        return "#9E9E9E"

# ── Title ──
fig.text(0.5, 0.96,
         "PCOS Diagnostic Criteria Comparison",
         ha="center", va="top",
         fontsize=22, fontweight="bold", color="#0D47A1",
         fontfamily="sans-serif")
fig.text(0.5, 0.925,
         "NIH 1990  \u00b7  Rotterdam 2003  \u00b7  AES 2006",
         ha="center", va="top",
         fontsize=13, color="#546E7A", fontfamily="sans-serif")

# ── Column headers ──
x_start = label_w + gap
for j, (crit_name, _) in enumerate(criteria_data.items()):
    x = x_start + j * (cell_w + gap)
    rect = mpatches.FancyBboxPatch(
        (x, n_features * (cell_h + gap) + gap),
        cell_w, header_h,
        boxstyle="round,pad=0.1",
        facecolor=color_header_bg, edgecolor="none"
    )
    ax.add_patch(rect)
    ax.text(x + cell_w / 2,
            n_features * (cell_h + gap) + gap + header_h / 2,
            crit_name,
            ha="center", va="center",
            fontsize=13, fontweight="bold",
            color=text_color_light, fontfamily="sans-serif")

# ── Row labels + cells ──
for i, feat in enumerate(features):
    y = (n_features - 1 - i) * (cell_h + gap)
    # Label cell
    rect = mpatches.FancyBboxPatch(
        (0, y), label_w, cell_h,
        boxstyle="round,pad=0.1",
        facecolor=color_label_bg, edgecolor="#90CAF9", linewidth=0.8
    )
    ax.add_patch(rect)
    ax.text(label_w / 2, y + cell_h / 2,
            feat,
            ha="center", va="center",
            fontsize=10.5, fontweight="semibold",
            color=text_color_dark, fontfamily="sans-serif",
            linespacing=1.3)

    # Data cells
    for j, (_, row) in enumerate(criteria_data.items()):
        val = row[i]
        x = x_start + j * (cell_w + gap)
        bg = requirement_color(val)
        tc = requirement_text_color(val)
        rect = mpatches.FancyBboxPatch(
            (x, y), cell_w, cell_h,
            boxstyle="round,pad=0.1",
            facecolor=bg, edgecolor="none"
        )
        ax.add_patch(rect)
        # Symbol
        symbol = "\u2714" if val == 2 else ("\u25d0" if val == 1 else "\u2014")
        ax.text(x + cell_w / 2, y + cell_h * 0.62,
                symbol,
                ha="center", va="center",
                fontsize=20, color=tc, fontfamily="sans-serif")
        ax.text(x + cell_w / 2, y + cell_h * 0.28,
                requirement_label(val),
                ha="center", va="center",
                fontsize=9, fontweight="bold",
                color=tc, fontfamily="sans-serif")

# ── Legend ──
legend_y = -1.4
legend_items = [
    (color_required,   "Required \u2014 must be present for diagnosis"),
    (color_either,     "Either / Or \u2014 counts toward a multi-criteria threshold"),
    (color_not_req,    "Not Required \u2014 not part of this criteria set"),
]
for k, (col, desc) in enumerate(legend_items):
    lx = 0.5 + k * 7.5
    rect = mpatches.FancyBboxPatch(
        (lx, legend_y), 0.5, 0.5,
        boxstyle="round,pad=0.05",
        facecolor=col, edgecolor="none"
    )
    ax.add_patch(rect)
    ax.text(lx + 0.8, legend_y + 0.25,
            desc,
            ha="left", va="center",
            fontsize=9, color=text_color_dark, fontfamily="sans-serif")

# ── Key diagnostic rules annotation ──
note_y = -2.3
notes = [
    "NIH 1990: Requires BOTH oligo-anovulation + hyperandrogenism (clinical or biochemical). PCOM not included.",
    "Rotterdam 2003: Requires ANY 2 of 3 \u2014 oligo-anovulation, hyperandrogenism, or polycystic ovaries.",
    "AES 2006: Requires hyperandrogenism + ovarian dysfunction (oligo-anovulation and/or PCOM). Exclusion mandatory.",
]
for n_idx, note in enumerate(notes):
    ax.text(0.5, note_y - n_idx * 0.55,
            f"\u25b8 {note}",
            ha="left", va="center",
            fontsize=8.8, color="#37474F", fontfamily="sans-serif",
            style="italic")

# ── Source citation ──
ax.text(0.5, note_y - 3 * 0.55 - 0.15,
        "Sources: Zawadzki & Dunaif (1992); Rotterdam ESHRE/ASRM (2004); Azziz et al. (2006)",
        ha="left", va="center",
        fontsize=7.5, color="#78909C", fontfamily="sans-serif")

# ── Axes off & limits ──
ax.set_xlim(-0.5, x_start + n_criteria * (cell_w + gap) + 0.5)
ax.set_ylim(note_y - 3 * 0.55 - 0.6, n_features * (cell_h + gap) + header_h + gap + 0.3)
ax.axis("off")

# ── Save ──
output_path = "pcos_criteria_comparison.png"
plt.savefig(output_path, dpi=200, bbox_inches="tight",
            facecolor=fig.get_facecolor(), edgecolor="none")
plt.close()
print(f"Chart saved to: {output_path}")
