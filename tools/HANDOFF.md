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
