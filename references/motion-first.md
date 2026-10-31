# Motion-first layer design

## Sources and scope

Reviewed official sources:
- [Live2D illustration preparation](https://docs.live2d.com/en/cubism-editor-tutorials/psd/): separate necessary parts and complete concealed regions.
- [Live2D material separation](https://docs.live2d.com/en/cubism-editor-manual/divide-the-material/): material preparation for modeling.
- [Live2D skinning](https://docs.live2d.com/en/cubism-editor-manual/skinning/): root-to-tip deformation paths.
- [Adobe Puppet documentation](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/animate-with-puppet-tools/animating-puppet-tools.html): alpha-derived meshes, local deformation, stiffness and overlap; Legacy/Advanced pin behavior differs.

The workflow below is our application of those principles, not a claim that the manuals prescribe these exact partitions.

## Decide what needs its own layer

Start with the user's actual animation: cinematic breathing/sway, facial expression animation, or substantial pose changes. Ask once when this changes the design. If already answered, carry it forward. Document relative motion, not just anatomical categories.

For every region decide:
- **Fixed:** image-boundary anchors/background or material with no independent motion.
- **Inherited rigid:** face preserving expression, held prop/fist, or a hair cap following a head transform. "Not independently moving" does not mean frozen in screen space.
- **Continuous flexible:** one continuous hair sheet with anchored roots and movable tips; cloth with a fixed base and deforming upper portion. Do not cut each control region into its own image merely to place different Puppet pins.
- **Attachment bridge:** neck from head to chest, sleeve from wrist to sleeve base. Endpoints must follow their neighbors, not independently rotate with a single null.
- **Independent overlap:** a separate depth order or a motion that exposes underlying material warrants a separate layer, including disjoint hair pieces with different roots.

Split only when relative motion, depth ordering, independent replacement, clipping, or topology requires it. Keep fixed-expression eyes/brows/mouth on a rigid head plate only when independent feature layers are not requested. If they are requested, preserve the starting expression through separate registered parts and a completed face base; use [facial-parts.md](facial-parts.md). Keep a grip and prop together if the user does not need fingers or prop to move independently. Fine feature separation is conditional on requested controls. A completed face base is required wherever separated features can reveal the surface beneath them; layer count is not a quality gate.

Name the intended rigid area, flexible area, attachment points, parent motion and exposed backing for each moving part. Start with a modest action appropriate to the image, then validate at that range plus a margin. Do not lower amplitude merely to hide defects discovered during testing.

## Algorithm adapter

`scripts/compile_motion_parts.py` is a local postprocessor for regrouping reviewed layers. It takes a flat, visible, normal-blend PSD plus a reviewed plan, and exports motion-oriented PSD/PNGs. It does not infer the user's motion, train a model, generate missing anatomy or create a Cubism/AE rig.

Usage: `python compile_motion_parts.py --src reviewed.psd --plan motion_plan.json --output motion_output`

Plan keys: `intent`, optional `canvas: [width,height]`, optional `controls`, and `parts`. Each part has `id`, `name`, `sources` (zero-based indices in bottom-to-top PSD order), `mode` (`fixed`, `rigid`, `bend`, `bridge`, `breath`), `reason`, `parent`, `pivot`, and `pins` (`xy`, `role`) for deformable parts. Pin roles are descriptive metadata for the chosen rig and preview.

Bundles must partition the original stack in order. The adapter rejects crossing over an intervening occluder, unassigned/reused layers, absent motion reasons, unsupported blending and deformable parts without attachment plans. It checks premultiplied rest-composition error and reopens the PSD. This avoids the common mistake of merging all head-related classes across clothing that should lie in front of them.

Optional `rigid_root_region: {target, rect}` moves a reviewed non-deforming patch into a rigid region with the same parent. Rest-composition checks still apply. Optional `hidden_root_rect` promotes existing low-alpha root pixels only when upper art fully hides them; it is not a general inpainting algorithm. If no suitable hidden pixels exist, do not claim that promotion repaired the connection. Reclassify a static fragment or complete the needed root instead.

`scripts/motion_fields.py` supplies a smooth pin-field preview and premultiplied-alpha transforms. Its mobility field is separate from alpha: protected pixels remain in the same part rather than being cut out. This approximates local deformation for QA; it is not AE's Puppet solver. Test parent-child attachment constraints and alpha topology, not just rigid rotations.

## Checks that matter

Inspect significant connected components at multiple alpha thresholds. Disconnected art can mean multiple meshes, while a very faint connection can yield a weak root. A root marker outside opaque artwork is not a usable pin: reposition it deliberately and record the final coordinates. A rigid plate may legitimately contain disconnected hidden fragments, because it is not being bent as one mesh.

Verify the fixed expression remains rigid (e.g. landmark distance invariants), the held prop does not slip, the sleeve/hand and head/neck contacts remain overlapped, and frame-edge anchors stay fixed. Test breathing, head, hair and arm individually before the combined loop. Save a guide explaining fixed/inherited/flexible areas as well as the final PSD and previews. Numeric overlap area helps diagnose contact loss; it is not proof of good drawing.

For AE delivery, a parenting/import script alone does not implement neck/sleeve bridging or Puppet pins. Supply clear pin guides; distinguish a transform-only control preview from the local deformation QA. Never present either as an actual AE/Cubism run unless it was executed there.
