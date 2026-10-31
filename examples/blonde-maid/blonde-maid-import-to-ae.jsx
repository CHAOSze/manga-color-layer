(function () {
    app.beginUndoGroup("Import blonde maid");
    try {
        if (!app.project) app.newProject();
        var base = new File($.fileName).parent;
        var data = {"width": 1056, "height": 1490, "stack": "bottom-to-top", "source_resolution": [1056, 1490], "color_generation_resolution": [1056, 1490], "layout_box": [0, 0, 1056, 1490], "layers": [{"id": "rear_hair", "name": "Posterior hair", "file": "layers/blonde-maid-01_rear_hair.png", "mode": "hair", "parent": "ROOT_CTRL", "pivot": [430, 380], "notes": "Continuous posterior flow; visible extent registered from supplied reference."}, {"id": "head_body", "name": "Head neck body arms and toy rifle", "file": "layers/blonde-maid-02_head_body.png", "mode": "fixed", "parent": "ROOT_CTRL", "pivot": [530, 900], "notes": "Continuous opaque backing; corrected ear/neck/headphones; face free of old hair and feature fragments."}, {"id": "brow_viewer_left", "name": "Continuous eyebrow", "file": "layers/blonde-maid-03_brow_viewer_left.png", "mode": "fixed", "parent": "ROOT_CTRL", "pivot": [368, 231], "notes": "Continuous gold brow, separate from clean face backing."}, {"id": "eye_viewer_left_white", "name": "white", "file": "layers/blonde-maid-04_eye_viewer_left_white.png", "mode": "fixed", "parent": "EYE_VIEWER_LEFT_CTRL", "pivot": [368, 276], "notes": "Viewer-based naming. Iris clipped to white eye-opening alpha; lids own ink/tear material, not a cheek ring.", "eye": "viewer_left", "blink_state": "open"}, {"id": "eye_viewer_left_iris", "name": "iris", "file": "layers/blonde-maid-05_eye_viewer_left_iris.png", "mode": "iris", "parent": "EYE_VIEWER_LEFT_CTRL", "pivot": [368, 276], "notes": "Viewer-based naming. Iris clipped to white eye-opening alpha; lids own ink/tear material, not a cheek ring.", "clip_to": "eye_viewer_left_white", "eye": "viewer_left", "blink_state": "open"}, {"id": "eye_viewer_left_upper_lid", "name": "upper_lid", "file": "layers/blonde-maid-06_eye_viewer_left_upper_lid.png", "mode": "fixed", "parent": "EYE_VIEWER_LEFT_CTRL", "pivot": [368, 276], "notes": "Viewer-based naming. Iris clipped to white eye-opening alpha; lids own ink/tear material, not a cheek ring.", "eye": "viewer_left", "blink_state": "open"}, {"id": "eye_viewer_left_lower_lid_tears", "name": "lower_lid_tears", "file": "layers/blonde-maid-07_eye_viewer_left_lower_lid_tears.png", "mode": "fixed", "parent": "EYE_VIEWER_LEFT_CTRL", "pivot": [368, 276], "notes": "Viewer-based naming. Iris clipped to white eye-opening alpha; lids own ink/tear material, not a cheek ring.", "eye": "viewer_left", "blink_state": "open"}, {"id": "eye_viewer_left_half", "name": "Blink half", "file": "layers/blonde-maid-08_eye_viewer_left_half.png", "mode": "fixed", "parent": "EYE_VIEWER_LEFT_CTRL", "pivot": [368, 276], "notes": "Aligned eyelid replacement drawing; hidden at rest.", "eye": "viewer_left", "blink_state": "half", "visible": false}, {"id": "eye_viewer_left_closed", "name": "Blink closed", "file": "layers/blonde-maid-09_eye_viewer_left_closed.png", "mode": "fixed", "parent": "EYE_VIEWER_LEFT_CTRL", "pivot": [368, 276], "notes": "Aligned eyelid replacement drawing; hidden at rest.", "eye": "viewer_left", "blink_state": "closed", "visible": false}, {"id": "brow_viewer_right", "name": "Continuous eyebrow", "file": "layers/blonde-maid-10_brow_viewer_right.png", "mode": "fixed", "parent": "ROOT_CTRL", "pivot": [495, 213], "notes": "Continuous gold brow, separate from clean face backing."}, {"id": "eye_viewer_right_white", "name": "white", "file": "layers/blonde-maid-11_eye_viewer_right_white.png", "mode": "fixed", "parent": "EYE_VIEWER_RIGHT_CTRL", "pivot": [495, 258], "notes": "Viewer-based naming. Iris clipped to white eye-opening alpha; lids own ink/tear material, not a cheek ring.", "eye": "viewer_right", "blink_state": "open"}, {"id": "eye_viewer_right_iris", "name": "iris", "file": "layers/blonde-maid-12_eye_viewer_right_iris.png", "mode": "iris", "parent": "EYE_VIEWER_RIGHT_CTRL", "pivot": [495, 258], "notes": "Viewer-based naming. Iris clipped to white eye-opening alpha; lids own ink/tear material, not a cheek ring.", "clip_to": "eye_viewer_right_white", "eye": "viewer_right", "blink_state": "open"}, {"id": "eye_viewer_right_upper_lid", "name": "upper_lid", "file": "layers/blonde-maid-13_eye_viewer_right_upper_lid.png", "mode": "fixed", "parent": "EYE_VIEWER_RIGHT_CTRL", "pivot": [495, 258], "notes": "Viewer-based naming. Iris clipped to white eye-opening alpha; lids own ink/tear material, not a cheek ring.", "eye": "viewer_right", "blink_state": "open"}, {"id": "eye_viewer_right_lower_lid_tears", "name": "lower_lid_tears", "file": "layers/blonde-maid-14_eye_viewer_right_lower_lid_tears.png", "mode": "fixed", "parent": "EYE_VIEWER_RIGHT_CTRL", "pivot": [495, 258], "notes": "Viewer-based naming. Iris clipped to white eye-opening alpha; lids own ink/tear material, not a cheek ring.", "eye": "viewer_right", "blink_state": "open"}, {"id": "eye_viewer_right_half", "name": "Blink half", "file": "layers/blonde-maid-15_eye_viewer_right_half.png", "mode": "fixed", "parent": "EYE_VIEWER_RIGHT_CTRL", "pivot": [495, 258], "notes": "Aligned eyelid replacement drawing; hidden at rest.", "eye": "viewer_right", "blink_state": "half", "visible": false}, {"id": "eye_viewer_right_closed", "name": "Blink closed", "file": "layers/blonde-maid-16_eye_viewer_right_closed.png", "mode": "fixed", "parent": "EYE_VIEWER_RIGHT_CTRL", "pivot": [495, 258], "notes": "Aligned eyelid replacement drawing; hidden at rest.", "eye": "viewer_right", "blink_state": "closed", "visible": false}, {"id": "mouth", "name": "Mouth", "file": "layers/blonde-maid-17_mouth.png", "mode": "fixed", "parent": "ROOT_CTRL", "pivot": [445, 366], "notes": "Tight original mouth contour; no broad skin support."}, {"id": "bangs_sides", "name": "bangs sides", "file": "layers/blonde-maid-18_bangs_sides.png", "mode": "hair", "parent": "BANGS_SIDES_CTRL", "pivot": [430, 85], "notes": "Complete central strip or combined left/right foreground. Side locks and their completed hidden material form one continuous plate. Painted under-center hair is integral to the side plate, with no separate crown layer.", "root_fixed_until_y": 100, "tested_tip_motion": [4, 1.5]}, {"id": "bangs_middle", "name": "bangs middle", "file": "layers/blonde-maid-19_bangs_middle.png", "mode": "hair", "parent": "BANGS_MIDDLE_CTRL", "pivot": [432, 117], "notes": "Complete central strip or combined left/right foreground. Side locks and their completed hidden material form one continuous plate. Painted under-center hair is integral to the side plate, with no separate crown layer.", "root_fixed_until_y": 120, "tested_tip_motion": [3, 1]}], "controls": {"ROOT_CTRL": [528, 1192], "EYE_VIEWER_LEFT_CTRL": [368, 276], "EYE_VIEWER_RIGHT_CTRL": [495, 258], "BANGS_SIDES_CTRL": [430, 85], "BANGS_MIDDLE_CTRL": [432, 117]}};
        var folder = app.project.items.addFolder("Blonde maid");
        var comp = app.project.items.addComp("Blonde maid", data.width, data.height, 1, 5, 24);
        comp.parentFolder = folder;
        var controls = {}, layers = {};
        for (var name in data.controls) {
            var control = comp.layers.addNull(5);
            control.name = name;
            control.property("ADBE Transform Group").property("ADBE Position").setValue(data.controls[name]);
            controls[name] = control;
            if (name.indexOf("EYE_") === 0) {
                var blink = control.property("ADBE Effect Parade").addProperty("ADBE Slider Control");
                blink.name = "Blink";
                blink.property(1).setValue(0);
                var gaze = control.property("ADBE Effect Parade").addProperty("ADBE Point Control");
                gaze.name = "Gaze";
                gaze.property(1).setValue([0, 0]);
            }
        }
        for (var name in controls) if (name !== "ROOT_CTRL") controls[name].parent = controls.ROOT_CTRL;
        for (var i = 0; i < data.layers.length; i++) {
            var e = data.layers[i];
            var options = new ImportOptions(new File(base.fsName + "/" + e.file));
            options.sequence = false;
            var footage = app.project.importFile(options);
            footage.parentFolder = folder;
            var layer = comp.layers.add(footage);
            layer.name = e.id;
            var transform = layer.property("ADBE Transform Group");
            transform.property("ADBE Anchor Point").setValue(e.pivot);
            transform.property("ADBE Position").setValue(e.pivot);
            layer.parent = controls[e.parent];
            layer.comment = e.notes;
            layers[e.id] = layer;
            if (e.blink_state) {
                var state = e.blink_state === "open" ? 0 : e.blink_state === "half" ? 1 : 2;
                transform.property("ADBE Opacity").expression =
                    'var b=thisComp.layer("' + e.parent + '").effect("Blink")(1);' +
                    'var s=b<25?0:(b<75?1:2);s===' + state + '?100:0;';
            }
            if (e.mode === "iris") {
                transform.property("ADBE Position").expression =
                    'value+thisComp.layer("' + e.parent + '").effect("Gaze")(1);';
            }
        }
        for (var i = 0; i < data.layers.length; i++) {
            var e = data.layers[i];
            if (!e.clip_to) continue;
            var iris = layers[e.id];
            var matte = layers[e.clip_to].duplicate();
            matte.name = e.id + "_aperture_matte";
            var opacity = matte.property("ADBE Transform Group").property("ADBE Opacity");
            opacity.expression = "";
            opacity.setValue(100);
            matte.moveBefore(iris);
            if (typeof iris.setTrackMatte === "function") iris.setTrackMatte(matte, TrackMatteType.ALPHA);
            else iris.trackMatteType = TrackMatteType.ALPHA;
        }
        for (var name in controls) controls[name].moveToBeginning();
        comp.openInViewer();
    } catch (error) {
        alert(error.toString());
    } finally {
        app.endUndoGroup();
    }
})();
