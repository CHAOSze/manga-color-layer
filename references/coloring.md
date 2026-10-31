# Reference-faithful manga coloring

## Inputs and invariants

Identify a structure source (black-and-white panel or approved colored master) and a color/style reference. Ask for a missing edit target rather than substituting an earlier version. Inspect both at actual size. Record a short palette/material map: hair base and shadows, skin, iris, costume, metal trim and props. Reference colors are affected by its lighting: transfer design colors without copying unrelated firelight or glow unless requested.

Preserve face proportions, eye direction, mouth contour and teeth, gesture, foreshortening, silhouette, line weight, hatching, screentone dot spacing and intentional paper texture. Keep original black ink dark. Fine screen patterns should survive at native resolution; avoid unnecessary resizing or sharpening that creates moiré.

## Editing prompt pattern

“Image A is the exact drawing to color; image B supplies only palette and rendering style. Keep A's composition, anatomy, face, expression, perspective, linework, hatching and printed screentones unchanged. Color the existing drawing with B's [specific palette/materials]. Use B's limited shadow shapes and ink-based contrast. Do not add smooth airbrushed gradients, glossy 3D surfaces, bloom, rim lighting, extra eyelashes, ornamental details or invented textures. Keep [named prop] [specified color/material]. Change only color, preserving the original drawing.”

Avoid relying on “less AI-looking” alone: name the actual visual features. If the reference itself uses watercolor or gradients, preserve those instead of imposing universal flat shading. Use focused revisions for a prop color or a background rather than regenerating the entire image.

## Review and preservation

Compare the result against the structure source with alignment/overlay where available. Check the eyes, fingers, teeth, hair tips and costume ornaments individually. Distinguish approved new color from unwanted line changes. If registration is good, retaining the original ink/screentone as a separate top layer can protect texture; do not blindly multiply white pixels or heavy gray tone over already dark color.

For a green-screen request, use an even green absent from the character's palette. For animation delivery, prefer real alpha and inspect edge contamination against white, gray and black. Do not globally remove all green if eyes, jewelry or clothing also use green. Keep natural holes between hair strands transparent.

For exact preservation demands, use localized color layers/masks or another user-authorized deterministic workflow when available; explain any generative drift. Image editing is not a guarantee of lossless colorization. Do not change resolution or erase comic texture merely to make the image look cleaner.

Before prop recoloring, inspect the original line art at close zoom and map skin, nails, object, ink and shadow boundaries. Color similarity or shape alone does not establish material ownership. If an interpretation is disputed, retrieve original attachments rather than repeating a prior generated interpretation. Check the corrected material at enlarged and normal size and again after layer reconstruction. Apply Gate A in [review-gates.md](review-gates.md) before freezing the colored master. Separation then compares against that master at Gate B, not against a previous separation; see artist-redraw.md for completion techniques.

## Preserve an approved eye-color treatment

When the user prefers an earlier eye treatment, retrieve that actual approved artwork and reuse its iris pixels or a tightly registered eye crop. Do not replace it with a newly generated approximation while repairing unrelated anatomy, clothing or hair. Keep an approved feature ledger for the current asset: expression/gaze, iris treatment, material assignments and required independent controls. Carry these decisions through subsequent rebuilds.

For reference art with luminous, detailed manga irises, a useful treatment is a dark upper iris under the lid, a more saturated/lighter lower arc, a clear pupil and outer rim, restrained radial tonal facets, and a small coherent group of sharp highlights. Derive hue, contrast and highlight shape from the reference or approved result. Keep whites neutral, lid ink crisp and nearby manga texture intact. This is conditional styling, not a default for every character; flat or muted reference eyes should remain flat or muted. Avoid spreading iris colors into skin, lashes or hair, and avoid applying glossy rendering to the whole face.

Example focused prompt: “Change only the iris coloration to match the approved eye reference: [upper shadow], [lower accent], [pupil/rim], [highlight grouping]. Preserve the approved perspective, eye opening, gaze and lash ink. Do not recolor sclera, skin, hair or costume. Preserve the surrounding printed texture.” Once accepted, reuse that artwork for layer extraction. A requested approval of richer iris rendering takes precedence over a generic preference for flatter shading.
