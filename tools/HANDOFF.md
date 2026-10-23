# The Woods drawing portal · notes for continuing work

Live: https://saicharan13579-source.github.io/THE-WOODS/ (villa portal) and /site.html (site portal).
A private Claude artifact mirrors it (built from the same template, downloads point to the GitHub site).

## How the site is built
- `tools/app_template.html` is the single source. Edit it, then run `python3 tools/gen.py`.
  That writes `index.html` (villa portal), `site.html` (site portal) and `tools/artifact.html` (for the Claude artifact).
- `tools/plots.json`: 53 plots from the architect's key plan (no, sq.m, sq.yd, facing E/W, hit box on `img/master-plan.png`).
- Drawing data inside the template: `F` (PDF files), `S` (sheets, codes AR-/S16-/S12-/LA-/TP-/RD-), `CAD` (DWG/Excel downloads, codes CAD-/MEP-), `SITE_G` (site portal groups), `plotSet()` (which drawings each plot shows per villa type).
- `PLOT_INFO` in the template: per-plot record. `type` "1625"/"1215" once confirmed (only Plot 30 confirmed = 1625 East), `note`, `extra` plot-specific drawings.
- Files: `pdf/` + `thumb/` (sheet previews, `<pdfname>_p<page>.jpg`, made with pdftoppm -r 40), `cad/`, `mep/`.

## Next step (pending)
Vamsi will send a folder with all drawings. Sort by plot, villa type (1625/1215), facing and discipline;
add new sheets, mark old revisions Superseded, link plot-specific drawings via PLOT_INFO.extra,
put whole-layout drawings in SITE_G, regenerate, push, and republish the artifact.
Do not build or use a DWG converter (Vamsi asked not to). DWG and Excel files stay as downloads.

## 23-10-2026 update
- Added Plot 30 landscape set LA-07 to LA-19 (conceptual, marking MP-01, levels LIP-01, irrigation, lighting, sections LS-001 to .4, storm water SWDO-01). LA-01/LA-02 (05-10) marked Superseded.
- Added streetscape set SS-01 to SS-06 (22-10-2026) to the site portal. All six carry the same dwg no. LLA-TW-LC-01.
- Added typical landscape conceptual plans LA-20 to LA-23 (1625 E/W LC-10 20-09-2026, 1215 E/W LC-04 22-10-2026), shown on every plot by villa type and facing.
- Material plan PDFs in the Plot 30 folder were identical to the ones already published; lighting fixture PNGs are already on LA-13, so they were not added separately.
- 21-10-2026 GFC reissue: AR-14 (1625E floor plan) and AR-15 (opening schedule) replace AR-09/AR-13; AW-01 = first 1625 West GFC floor plan (TP-02 superseded). CAD-14..17 added; CAD-09/CAD-12 marked old.
  The other sheets in the 2026-10-22 transfer (elevations, sections, centre line, excavation, footing, framing, East and West) were 0-byte files. Add them when re-sent.
