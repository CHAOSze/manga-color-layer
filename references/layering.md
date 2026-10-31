# Semantic decomposition and occlusion completion

## Project selection

- [See-through](https://github.com/shitagaki-lab/see-through): generates semantic transparent layers with occluded regions and estimates depth/draw order. Inspect its current README and actual command help before setup. Source reviewed for this workflow: `df019de5129d6c4b406587a14c3501669441a783`.
- [PSD2Live](https://github.com/tsunehimatoi/psd2live): consumes prepared PSDs and provides mesh/deformer generation, editing and animation/export. It is not a replacement for recovering hidden artwork from a flattened panel. Review its [PSD naming guide](https://github.com/tsunehimatoi/psd2live/blob/master/docs/zh/spec/PSD_LAYER_SPEC.md) if a PSD2Live project is requested. Semantic names include front hair, back hair, face, irides, eyebrow, eyewhite, eyelash, ears, mouth, neck, topwear, handwear and objects. Do not promise automatic rigging quality for strongly foreshortened/non-upright poses.
- [ComfyUI-See-through](https://github.com/jtydhr88/ComfyUI-See-through): an alternative integration when a compatible ComfyUI environment is already available. Do not upgrade the user's environment globally just to run one image.

## Execution

Use an isolated environment or task-local dependency directory. Inspect GPU, compatible Python/PyTorch and disk space first. Keep model caches inside an approved workspace. Pin and record repository/model revisions. Download weights only from the actual model links in the reviewed upstream documentation. Resolve required network permissions; do not bypass blocked approval or disable TLS verification.

At the reviewed revision, the main entry point is `inference/scripts/inference_psd.py`, run with repository root as working directory. Its important options include `--srcp`, `--save_dir`, `--save_to_psd`, `--resolution`, `--resolution_depth`, `--seed`, `--tblr_split`, and `--group_offload`. The two model stages use LayerDiff3D and Marigold. Head detail decomposition is a separate pass after body decomposition. Use supported offloading when VRAM is tight, and release the first pipeline before loading depth when needed. Test imports before downloading unnecessary optional UI/training/annotation stacks.

## Registration and correction

The included `scripts/run_backend.py` wraps these stages with explicit paths and releases the first model before depth inference. Run its `--stage check` before inference, and inspect `--help`. It assumes models are already downloaded and does not install dependencies. `scripts/export_ae.py` converts the resulting square-padded PSD into registered rectangular PSD/PNGs and an AE import script; pass original `--width` and `--height`. It preserves draw order but does not choose a rig hierarchy or create Puppet pins. Review the actual output and configure hierarchy for the pose.

Read [backend-checks.md](backend-checks.md) for compatibility checks and failure diagnosis. Backend settings and outputs must be evaluated for the current input.

The backend square-pads inputs. Record original dimensions and the exact padding/scale; invert them when exporting to the original canvas. Do not independently center each PNG or stretch square output into a rectangular canvas. Layer canvases, pivot coordinates and PSD positions must use the same transform.

Inspect raw results before selecting layers. Empty classes should not become meaningful parts. Split fused limbs only when supported by the visible pose. Keep a prop with its hand unless independent motion is requested. Correct automatic depth ordering by visual evidence. Do not use the full generated head and its component face/eye/mouth layers simultaneously, creating duplicates.

Specifically check whether the `face` alpha is empty even when `head` and the eye/mouth layers exist. For an AE head puppet, a complete head plate can be preferable to rebuilding a full facial rig. If the user requests independent facial layers or facial animation, complete a blank skin base and inspect every feature join. Do not copy original pupils into the eye-white layer or hair into the face layer while restoring texture. If repair degrades the approved expression, revise the reconstruction. A complete head is a fallback only when it still supports the requested motion; otherwise describe the unresolved limitation.

Preserve generated completion outside the visible masks. Replacing visible pixels with the registered source may help protect the comic style, but must not remove hidden surfaces or leave mixed fragments. Avoid independently regenerating every part with unconstrained positioning: their joins and scale can diverge.

## Motion QA

Inspect head/neck under front and back hair, hand/cuff, sleeve/torso and costume overlaps. Move hair tips slightly, translate or rotate head a few degrees, and shift the hand/arm modestly, checking revealed surfaces and contact seams. Save a preview or diagnostic poses. A backend may change the style or misclassify a foreshortened hand: repair or report that instead of calling the result complete.

Use a real PSD parser to reopen the export, check canvas and nonempty layers, and compare the composite. Preserve one pixel coordinate system in AE. Automatic parent assignment does not add a Puppet mesh or animation keyframes; describe precisely what the import script does.
