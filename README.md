# ENVI tools

## Introduction

This project provides simple tools to deal with reflectance ENVI files.
Currently, the following tools (functions) are available.

- Sampling reflectance of RoIs.
- Color enhancement.

## Sampling reflectance of RoIs.
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
