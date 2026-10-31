# Ordered visual review gates

Use this sequence for coloring plus animation-layer work. A coloring-only task ends at A; a layer-only task starts from the user's supplied colored master, reviewing disputed source interpretation at A when needed. Keep the three comparison pairs distinct. Review is an assessment with a result, not merely the act of opening an image.

## Establish the references

- Original drawing: anatomy, pose, expression, ink, screentones and material boundaries.
- Palette/style reference: design colors and rendering treatment, not permission to change the drawing.
- Approved colored master: the visible appearance that the separated layers must reproduce at rest.
- Output: actual exported layer assembly, not a convenient earlier preview.

For public demonstrations, label the original drawing, pre-separation colored master, and exported static assembly separately. Show the actual colored master as the coloring result; do not replace it with the layer composite. Retain that master as an independent downloadable file.

Record approved exceptions such as a chosen iris treatment or prop-color correction. Freeze the reviewed colored master before judging layer fidelity. A preferred old PSD is a construction starting point; it does not override the drawing or colored master. If a later material decision changes the coloring, correct/review the master first and then compare the rebuilt layers against that corrected master. Do not silently change color only inside the separated output.

## A. Coloring: drawing versus colored image

Compare the same canvas and crop at normal viewing size and native-resolution detail. Use the palette reference to judge color, the drawing to judge structure.

Inspect facial proportions, gaze/expression, jaw and neck, hands and finger contacts, joints, costume folds, hair tips, held props and ornaments. Trace ambiguous boundaries through the original ink before assigning skin, hair, cloth or object material. Gray shading alone is not a material label. Check hue spilling across those boundaries and loss of hatching, screentones or ink weight.

Pass only when unwanted structural/style changes and disputed color ownership have been resolved. If the colored master itself has a known error, record A as failed; do not use that error as the excuse for a different unreviewed layer result.

## B. Separation: colored master versus STATIC exported assembly

**Finish this gate before running motion acceptance.** Render the real PSD/PNG stack at its default pose, layer order, opacity and blending. Match canvas/crop and matte backgrounds. Global crop registration may normalize presentation, but do not nonrigidly warp a review image to conceal drift.

Place master and output side by side; use an overlay or blink comparison as an additional aid. Inspect both the full figure and enlarged crops. Look explicitly for:

- Missing or extra visible pixels/parts and altered exterior silhouettes.
- Displaced hands, joints, sleeves, facial features or props; changed proportions, pose or grip.
- Changed skin/cloth/hair/prop colors, shadows or material ownership; incorrect contact shading.
- Changed strand direction, duplicated contours, lost or invented folds, texture and ink changes.
- Exposure of inferred backing at rest, registration drift and patch seams.

Keep a short difference ledger: **region — master appearance — output difference — owning layer — correction — recheck result**. An assertion that an old layer is unchanged does not answer whether that layer matches the colored master. Quantitative differences can locate candidates, but neither zero global error nor a small sampled-region error proves the entire assembly is correct.

Static fidelity is perceptual unless the user explicitly requires pixel identity. Necessary underlap and edge repairs must respect the approved pose, expression, silhouette and strand direction; perceptual tolerance does not authorize unrequested rerouting or redesign. Assess the assembled likeness, materials and contact rather than automatically restoring old pixels. Record meaningful differences. Do not optimize an equality assertion by clipping completed parts back into disconnected visible fragments, retaining old ink on a fixed neighbor, or adding unnecessary depth planes. If the useful independent movement does not justify the boundary cost, keep the part continuous or merge the unreliable split.

### Isolated surfaces are also part of static review

Use visibility toggles on the exported stack: inspect every major layer solo, then hide foreground hair, hide eyes/mouth, and hide individual eye subparts. Inspect enlarged crops of brows/eyes, both ears, neck/headphones, hair roots/tips and mouth backing. Hide each occluder and inspect the underlying part on white, gray and black. Check complete material, shadow and linework across cut boundaries, sufficient underlap, natural contours, residual fragments and alpha holes. Diagnose gray bands/halos using both RGB and alpha before repainting; intended opaque skin is not fixed by changing its hue while leaving it translucent.

Inspect layer opacity and pixel alpha separately. For opaque artwork, set layer/fill opacity to 100% and verify solid material interiors are opaque; transparent background, actual apertures and a narrow antialiased contour are expected. Audit connected components on each intended continuous movable part, but judge anatomy and material visually: a thin artificial bridge does not repair a broken painted surface, and legitimate separate facial marks are not necessarily errors. Repair missing joins with real material or revise grouping, rather than labeling disconnected scraps as one part.

Rear completion must be a coherent rear surface, not another copy of the bangs, cheek curls or their tip outlines. Its hidden strand flow may differ from the front, while its actually visible locks still match the colored master. Removing duplicated front locks is not a pass if the exposed rear silhouette is now wrong. Do not use alpha expansion, foreground-shaped clipping or pasted visible scraps as a substitute for painted hidden continuity.

A merged layer can retain its old seam, misplaced joint or wrong color: inspect the merged artwork itself. When reusing an approved completion, compare its repair crop against the same crop from the exported isolated layer. If the intermediate is correct but delivery is wrong, inspect compositing order, source-restoration masks, crop bounds and stale output paths before regenerating artwork. Prefer source-preserving extraction/local redraw for visible regions. Reject registration that bends a rigid prop, melts strands or distorts anatomy; an attractive whole-part redraw can still have changed the source pose.

For eyes, use [facial-parts.md](facial-parts.md#toggle-inspection-and-functional-eye-coverage): check complete brows, sclera coverage, iris aperture/matte and skin-free movable lid contours. Record blink support separately from gaze. For rear hair, check exposed-lock coverage against the traced master silhouette, not just whether the new back plate looks plausible. A clean flattened assembly cannot excuse broken isolated material or a feature that hides a defective base.

Pass B only after major visible differences and hidden-surface defects are corrected, with remaining agreed exceptions stated explicitly. If B fails, record C as **not run / pending static correction**, rather than using an existing animation as evidence of success.

## C. Motion: accepted static layers versus small intended movements

After B passes, test the actual requested motion at a small agreed range and a modest margin. Check each moving part separately, then combined and opposing motions. Do not move everything identically, which can hide doubled hair or attachment defects. Do not reduce the range just to conceal a discovered problem.

Inspect revealed strips around boundaries for gaps, transparent wedges, doubled tips, wrong material, abrupt shading, detached fragments, slipping joints or a broken grip. Stable roots and fixed parts must remain attached; rigid objects must retain their shape. A static match does not prove hidden parts are ready for motion.

Tip-only deformation does not validate a cap/face or accessory attachment boundary. When the intended shot permits relative root motion, also translate/rotate the relevant whole part slightly against its neighbor, independently and in opposition. Inspect backing layers for retained foreground ink, cast-shadow triangles, old feature copies and duplicated recognizable strand contours. State root constraints separately from free-tip limits. At a supposedly continuous junction, inspect actual material width and painted flow relative to the deformation; a large lock connected only by a hair-thin thread can pass a component-count test and still be unusable.

Repair findings, rerun B for the changed artwork, then retest C. A coloring/material change returns to A first. Distinguish a raster deformation preview, a parenting/import script and an actual AE/Cubism rig test; do not claim a runtime that was not used.

## Record the result honestly

Report A, B and C separately as **passed, failed, or not checked**, with concrete findings and evidence paths. PSD parsing, dimensions, layer presence, script syntax and numeric checks are a separate technical category. “Reviewed”, “reopened” and “preview generated” are not synonyms for passed visual review. Historical previews do not certify a later revision. Keep intermediate material internal unless the user requests it; deliver a concise summary of actual findings and unresolved limits.

When the user reports a remaining defect, reopen the associated gate and record the unresolved feedback. Do not keep citing its earlier pass or promote the attempted repair into a successful example. Reusable cleanup methods belong in the skill; whether the latest artwork actually satisfies them remains a separate assessment. See [backing-cleanup.md](backing-cleanup.md) for the diagnostic/repair sequence.
