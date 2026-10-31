# Blonde maid animation layers

The two movable foreground layers are bangs_middle (one complete long strip, rounded root and tapered tips) and bangs_sides (left/right hair combined into one continuous crown and side-lock plate). The side locks intentionally stay together: separate controls caused unstable boundaries without useful extra motion. The full painted under-center hairline is baked into bangs_sides itself; there is no separate crown/scalp/root layer. Hiding bangs_middle shows that same complete side plate, not an independently truncated backing.

The 17 other original layers retain their artwork, including face/body/arms/toy rifle, posterior hair, brows, eyes, eyelashes, forward gaze and mouth. Four blink replacement drawings are hidden at rest; both irises retain PSD clipping. All layer opacities are 100%; material interiors are opaque.

Use blonde-maid-import-to-ae.jsx for aligned PNG import and BANGS_MIDDLE_CTRL / BANGS_SIDES_CTRL parents. Keep side roots fixed near y100 and the middle attachment near y120 and deform the free lengths. blonde-maid-puppet-pins.json supplies suggestions. Local raster checks cover independent and opposing center/combined-side movements: center free tips +/-3px horizontal and +/-1px vertical, sides +/-4px and +/-1.5px. Whole center translation +/-3px and +/-1px is also a diagnostic. These are local previews, not an actual After Effects run or an unrestricted motion guarantee.

The central leaf follows the original registered root and tips; the concealed under-center surface is an inferred redraw. expression and overall hairstyle are compared against the accepted colored master. A full reference-PSD strip, rather than its cropped visible region, guided the construction.

The cloud-painted quiet under-center surface is retained intact inside bangs_sides. The original central leaf is isolated from its actual parting, rather than exposing the trial strip's oversized hidden root over the crown. No extra head-top plate is exported. Strong downscaling uses area prefiltering before registration to preserve fine line continuity. reviews includes rest comparison, complete solo strip, middle-hidden saved-PSD inspection and small-motion extremes.

The corrected side-hair plate retains the complete earlier cloud-painted flow. Its repaired region is composited above the superseded extraction, so old center-edge ink cannot reappear over the completion. The accepted middle plate is unchanged.
