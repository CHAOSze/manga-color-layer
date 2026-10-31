# Optional backend checks

Select a backend for the current input and required output. Record repository/model revisions, input dimensions, crop/padding transforms, inference resolution and any resampling. Script defaults are starting values, not quality requirements or tested guarantees for a new subject. Inspect current upstream documentation when executing a backend; do not assume one historical environment is required.

- Check nonempty alpha in required classes. A missing class cannot be repaired by naming an empty layer. Use a suitable complete part or reconstruct the missing surface according to the motion plan.
- Check fused or misplaced semantic parts against original contours. Automatic anatomical categories do not establish useful animation groups or correct stacking.
- Restore source texture only within reviewed material ownership regions. Unmasked copying can introduce duplicate features, transferred ornaments or contaminated edges.
- Reverse recorded padding and scaling consistently across PSD layers, PNG canvases and metadata; do not stretch a square inference image to the original aspect ratio.
- Reopen the PSD and inspect metadata separately. A successful image save does not guarantee metadata serialization succeeded. If NumPy scalar serialization fails, a narrow conversion using np.generic.item() may be appropriate; inspect the actual exception before patching.
- For exporter changes, use a small synthetic stack to check ordering, offsets, transparency and unpadding, then visually inspect the real output. This tests packaging, not artistic completeness or rig behavior.

Compare local and cloud edits on the same relevant crop and criteria when that comparison helps resolve defects. Neither backend is inherently guaranteed to preserve identity, materials or manga texture. Select the better result by observed fidelity and completion, and record what actually ran. Approximate previews never certify a target application's deformation solver.
