# Independent eyes and mouth

Use this route when independent facial parts are requested, even if the starting pose must retain its expression. Preserving the initial expression does not mean permanently baking features into the face. Adapt the plan to the subject's anatomy, perspective, style and motion; do not assume two visible eyes, bilateral symmetry or human lips.

An eye-separation requirement remains active across revisions of the same asset. Put it in the part plan before export and verify the exported layer list; a generic “fixed expression” decision must not silently remove already requested eye controls. For an actually closed eye, separate the visible lid/lash region without inventing open-eye geometry unless opening it is requested. For an approved iris treatment, reuse the accepted artwork; see [coloring.md](coloring.md#preserve-an-approved-eye-color-treatment).

## Choose a useful level of separation

| Requested control | Artwork preparation | Limit |
| --- | --- | --- |
| Independent feature adjustment or gentle local deformation | Clean face base plus each visible eye region and mouth region as separate parts | Region plates alone do not establish blinking, gaze or lip sync |
| Gaze | Eye whites/backing and iris/pupil units, with lid/lash occlusion; highlights separate only if their motion needs it | Complete material hidden behind lids and at gaze extremes; pupils must remain clipped to the eye opening |
| Blink or wink | Independently controllable upper/lower lids or reviewed open/half/closed replacement drawings, plus eye interior backing | Squashing an entire eye plate also squashes its pupil and lashes; it is not a verified blink |
| Mouth opening or speech | Lip/contour controls, cavity backing and visible teeth/tongue separated where their motion requires it, or a reviewed mouth-shape set | A single open-mouth image cannot supply all closed-mouth or phoneme geometry |
| Brow/expression movement | Separate brows and expression-dependent creases/shadows when needed | Do not leave duplicate brow ink or fixed creases on the face base |

When the request only says “separate eyes and mouth,” begin with independently addressable visible eye regions and a mouth region; label this level honestly. Use more detailed components only when the requested motion benefits from them. Record left/right naming convention (viewer or character) explicitly. Each feature inherits head motion while retaining its own local controls.

## Build the face base and feature artwork

1. Inspect the source at native scale. Identify feature contours, adjacent skin, expression creases, hair occlusion and shared shadows. Use anatomical/ink evidence rather than color thresholds. Preserve perspective and natural asymmetry; do not mirror the better-exposed eye automatically.
2. Keep an untouched reference outside the visible animation stack. Plan ownership for every movable mark: eyelid lines, lashes, brows, lip borders, corner shadows and highlights. Fixed nose/face contour can remain on the base unless the requested motion involves them.
3. Construct a continuous face base beneath removed features, with consistent skin color, shading and texture. Remove the movable feature AND its residual ink/shadows from that base. Reconstruct only the regions that can be exposed by the intended movement; do not flatten the whole face or erase fixed expression marks indiscriminately.
4. Extract trustworthy original feature artwork or redraw the complete feature using the source as a structural guide. Preserve eye shape, gaze, lash weight, mouth contour, teeth arrangement, cavity proportions and screentones. Include narrowly controlled stationary skin support where necessary, but do not move a broad skin-bearing frame as an eyelid: it drags the cheek and creates a sticker seam. Separate contour/lash ink from skin support when lid movement is required; any lid drawing must own only the material it actually moves.
5. Complete hidden feature areas and backing according to occlusion. An eye under hair needs enough extension for the planned relative motion, not an invented full symmetric eye by default. A mouth cavity must remain covered by lips/contours and any applicable masks. Hair, lids and facial features must retain the pose's actual draw order.
6. Blend transitions in skin tone and texture without blurring defining ink. Completion can precede or follow extraction; choose the route that yields coherent surfaces. Do not fill base holes by covering them with an intact original face layer, and do not keep duplicate eyes/mouth under the new parts.
7. Register all parts to a shared canvas and record pivots, parent relationships, masks and layer order. If clipping or replacement logic is not implemented by the export/import tool, provide the required guide and state that limitation instead of claiming the rig is complete.

## Separating iris/pupil units for gaze

When the user asks to separate the eyeball, establish whether they mean the visible iris/pupil/highlight unit or the whole eye interior. For a small gaze-control step, keeping iris, pupil and attached highlights together preserves their relationship. Keep the original shape and asymmetry; do not redraw or mirror a small iris unnecessarily.

Prepare a continuous sclera backing and remove the original iris plus its colored fringe from it. Place the iris above that backing and below the eyelid/lash occluder. Keep the completed iris as reusable material, but clip its rendered visibility to the actual eye-opening aperture at every tested gaze and lid state. A surrounding frame is not an infinite mask: its finite skin coverage can fail during movement. Export and verify an explicit aperture/matte when needed; do not assume PSD order alone implements clipping. Review aperture edges against ink and shading, not just a coarse ellipse. Do not cut eyelid ink into the movable iris.

Audit the actual solo iris, not just the assembled eye: a circular crop of a composite eye can still contain a lash cap, tear strip or skin fragment. Complete the iris's own material and keep those occluders on the frame. After changing foreground artwork, recheck facial parts for cuts inherited from the old hair mask; old alpha is not anatomical evidence. Restore the complete eye corner or mouth contour rather than retaining an obsolete source-ownership polygon. Preserve trusted visible feature paint where possible, without copying foreign alpha or occlusion marks into the completed unit.

Keep all subparts under one eye-region parent, which inherits head motion, while the iris retains local movement. Independent iris layers alone do not implement blinking. Test rest composition, iris-hidden backing, horizontal/vertical extremes and any planned simultaneous eye/head movement. Set the tested range from geometry and user intent, not from a previous example's pixel values.

## Registration and patch boundaries

A generated backing may change head size, outline or landmark positions despite preservation prompts. Inspect those changes before using it. When the original silhouette is sound, retain its alpha, nose, ears and fixed anatomy; register the generated backing and use only the needed completed surface. A bounding-box transform can be a starting estimate, but verify with landmarks and review the assembled result.

Keep defining feature ink at full opacity. Place any feathering in a narrow surrounding skin support region, and extend the backing beyond that region by the planned movement margin. Avoid blurring through lashes or lip contours. Match backing color using nearby clean material, excluding ink and highlights; numerical matching still needs visual review for gradient seams and texture changes. Check both signs of translation/rotation and any planned scale change, including simultaneous parent and occluder motion.

## Required review

- Hide every eye and mouth part: the base must contain continuous skin, with no duplicate feature ink, transparent holes or obvious patch boundaries in exposed areas.
- Solo each feature against opaque light/dark/gray backgrounds: inspect clipped lashes, corners, teeth, alpha fringe and unrelated skin/hair fragments.
- Reassemble at the original pose: compare eye spacing, gaze, expression, mouth corners, teeth, distinctive linework and overall likeness against the source. Check after registration, not just at generation size.
- Move each feature independently through the intended range, then combine with head/hair motion. Inspect all newly exposed boundaries and ensure feature controls inherit the head transform without slipping.
- For gaze, inspect all planned gaze extremes and lid containment. For blink, inspect open/intermediate/closed states and corner continuity. For mouth motion, inspect each supported shape and transitions for exposed cavity edges, floating teeth and broken lip corners. Run only the claims the artwork and test actually support.
- Fix defects before delivery. Report the supported control level, inferred regions and remaining limitations. Separate PNGs, a successful PSD reopen, or a local preview is not proof of a functional facial rig in AE/Cubism.

## Reusable edit prompt structure

“Prepare [specific facial part/base] from the supplied approved source for [specified motion]. Preserve its perspective, asymmetry, initial expression, proportions, palette, ink weight and texture. Change only [named region]. Complete [named hidden surfaces] to support [relative movement]. Remove [owned movable marks] from the backing; preserve [fixed anatomy/shading]. Keep the original canvas alignment and transparent exterior where applicable. Do not add extra facial features or change the character design.”

Request distinct assets separately when that gives more reliable alignment and review than a generated contact sheet. Use the available image-editing tool for actual drawing changes, and deterministic packaging tools for the reviewed layers.

Reference: [Live2D material separation](https://docs.live2d.com/en/cubism-editor-manual/divide-the-material/) explains separating illustration features such as eyelashes and eyeballs. The control levels and review procedure above are workflow choices, not a claim that every model needs the same parts.

## Toggle inspection and functional eye coverage

Inspect the actual exported stack by toggling visibility, not just a flattened preview. Hide foreground hair to inspect brows, lids, ears and temples; hide each eye subpart in turn, then all features. A brow must read as one intentional complete brow, without dotted duplicates, old fringe strokes or hair-shadow fragments. Keep approved expression and natural perspective; repair extraction loss without mirroring facial anatomy mechanically.

For gaze, the iris-hidden sclera must cover the entire intended eye opening through horizontal, vertical and diagonal extremes, including any lid motion. Review its reveal margin on the actual scale and transforms. Moving the iris must reveal eye white rather than face skin, transparency or a painted copy of the old iris. A complete circular iris is useful backing artwork; an unclipped visible circular iris is not a finished gaze control. Provide or implement the eye-opening mask in the target workflow and verify it after import; a mask guide alone is a pending runtime setup, not a working rig.

For blinking, prepare independently deformable upper/lower lid artwork or approved open/half/closed drawings; check eye corners, lash continuity and complete disappearance of the iris at closure. If only gaze or feature adjustment was requested, do not silently expand scope to a blink rig, but explicitly state that blink is unsupported. If blinking is requested, a skin ring named frame or squashed open eye is insufficient.

Hide the mouth and inspect its surrounding backing as well as the removed mouth plate. Restore consistent local skin gradient, blush and texture across the support area; avoid a pale/dark island, rectangular patch or leftover lip/shadow. Compare mouth-on and mouth-off crops on the same background. A feature that conceals a bad base at rest has not passed review.

## Preserve gaze and fine eyelash identity through extraction

A gaze correction is a relational check: compare pupil/iris position, visible iris proportions, upper-lid overlap, upper/lower sclera exposure, eye-corner slope and head perspective against the approved reference. Do not infer gaze from an absolute pupil coordinate alone. Register eyelids, aperture and iris together; vertically compressing the lid drawing while reusing an iris from another revision can change the apparent viewing direction. Keep an existing complete iris as hidden support only when its visible artwork and default placement do not match the current approved eye.

Extract fine lashes and crease strokes from the highest trustworthy source resolution before reduction. A component-size filter suitable for large hair or body plates can erase legitimate small lash tips and branching strokes; a tight aperture ring can truncate their reach. Retain those strokes without importing a cheek patch or eyelid ink into the iris. Inspect the saved rest assembly at normal size for expression, then enlarged for line identity, before testing gaze extremes and blink replacements again.
