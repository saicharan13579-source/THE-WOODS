# The Woods drawing portal · notes for continuing work

Live: https://saicharan13579-source.github.io/THE-WOODS/ (villa portal) and /site.html (site portal).
A private Claude artifact mirrors it (built from the same template, downloads point to the GitHub site).

## How the site is built
- `tools/app_template.html` is the single source. Edit it, then run `python3 tools/gen.py`.
  That writes `index.html` (villa portal), `site.html` (site portal) and `tools/artifact.html` (for the Claude artifact).
- `tools/plots.json`: 53 plots (no, sq.m, sq.yd, facing E/W/N, hit box in pixels of `img/site-layout.jpg`, the Ankura site layout rendered at 200 dpi). Areas are from the architect key plan.
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
- 21-10-2026 GFC site plan added as ST-01 (pdf 31 MB, too big for the artifact: F flag 1 makes the artifact read it from GitHub) + CAD-18 DWG. CAD-01 kept for spot levels.
- Structural: S16 now = 1625E set 05-10-2026 (SD-01/03 R02, SD-02 R01); S12 = 1215E R01 07-10; new S6W (1625W R01) and S2W (1215W R01). Old revisions kept as S16-0x-Rxx / S12-0x-R0 (Superseded). All structural DWGs in the 22-10 transfer were 0 bytes.

## Villa types
- Saving happens in the Claude artifact: its db doc `villa/types` ({plots:{"31":{"type":"custom","note":"..."}}, updatedAt}) is authoritative there; the owner picks a type and it saves instantly.
- The GitHub site is read-only for types: it reads `data/villa-types.json`. Sync = read the artifact db (ArtifactData get villa/types) -> write the json -> push. No regenerate needed.
- Each plot record also has `status` (booked/registered/blocked; absent = available) and `label` (e.g. Sales office) from Ankura's sales layout; `_asof` holds the status date. Blocked plots (except Plot 30, the model villa) show no villa drawings. Master layout colours follow status.
- Plots 01-05, 08, 23, 28 are North facing (sales layout); they show the East set as typical reference with a warning.
- type is "1625", "1215" or "custom" (client custom floor plan: no standard sets shown; add its drawings via PLOT_INFO extra).

## Revision archive
- `SUP` in the template maps each superseded code to [current code, date replaced]. Superseded sheets never show on plot tabs or in the register; they appear only under Drawing register → Revision archive, and the viewer shows "Old revs (n)" on the current sheet. When a new revision arrives: add the new sheet, keep the old row (status "super"), add it to SUP.

## Site progress & RFIs (per villa "Site" tab, plus the Progress page)
- Claude artifact db: `progress/<plot>` {stages:{setout|excav|pcc|footing|plinth|walls|roof|services|finish|land:{st:""|"wip"|"done",date,remark,photos:[{id,url}]}},updatedAt,by}; `rfi/<id>` {plot,sheet,rev,sheetTitle,q,photos,status:open|answered|closed,at,by,replies:[{by,at,text}]}. Photos via the assets capability.
- Who can write: owner + people invited by email as Editor. `villa/types` is owner-only (rule). The GitHub site cannot store anything: its Site tab offers WhatsApp messages (wa.me) with plot and drawing filled in, plus a link to the Claude version.
- Artifact capabilities: db rules [{path:"",read:"view",write:"admin"},{path:"villa",read:"view",write:"owner"}], user {scopes:["profile"]}, assets {}.
