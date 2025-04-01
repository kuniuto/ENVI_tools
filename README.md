# ENVI tools

## Introduction

This project provides simple tools to deal with reflectance ENVI files.
Currently, the following tools (functions) are available.

- Sampling reflectance of RoIs.
- Color enhancement.

---
## Sampling reflectance of RoIs. (`sample_rois` function)
1. **Installing necesary dependencies**
   - Install necessary dependencies by referring to `envi_tool.py` and `envi_tool_demo_sample_rois.py`.
     
2. **Running code**
   - Specify `envi_fname` in `envi_tool_demo_sample_rois.py`, then run the following command:
```bash
python envi_tool_demo_sample_rois.py
```

3. **Selecting RoIs**
   - Select RoIs. After each selection, type `space` key. To finish selection, type `esc`.

**Seelction of RoIs (bboxes)**:
![RoI selection](asset/RoIs_selection.png)

4. **Reflectance plot**
   - Averaged reflectances of RoIs shows up.

**Averaged reflectances of RoIs**:
![RoI selection](asset/RoIs_reflectance.png)

---
## Color enhancement. (`color_enhancement` function)
In general, inteinsities of leaf areas in color images generated from reflectance hyperspecral data is low.
This is because leaf reflectance is low.
This function makes plants brighter by maximizing intensity in RoI.

1. **Installing necesary dependencies**
   - Install necessary dependencies by referring to `envi_tool.py` and `envi_tool_demo_color_enhanncement.py`.
     
2. **Running code**
   - Specify `envi_fname` in `envi_tool_demo_color_enhancement.py`, then run the following command:
```bash
python envi_tool_demo_color_enhancement.py
```

3. **Selecting RoI**
   - Select RoI. Type `space` key and, then, type `Enter`.

4. **Display of original and enhance color images**
   - Original and enhance color images show up.

**Video of operation**:
![Color enhancement](asset/color_enhancement_video.mp4)
