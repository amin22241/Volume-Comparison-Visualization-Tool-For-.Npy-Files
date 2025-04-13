# Volume-Comparison-Visualization-Tool-For-.Npy-Files
A Python script for comparing 3D/4D volumetric datasets (`.npy` files) 
 # Volume Comparison & Visualization Tool For .Npy Files


## Table of Contents
- [Description](## Description)
- [Features](## Features )
- [Outputs](**Outputs**)
- [Example](#examples are provided in the folder)
- [License](#mohammadamin)

## Description
A Python script for comparing 3D/4D volumetric datasets (`.npy` files) that:
1. Computes voxel-wise overlap and differences
2. Generates quantitative metrics
3. Provides interactive visualization using Napari

## Features
- **Data Handling**
  - Loads multiple `.npy` files
  - Auto-crops to smallest common dimensions
- **Analysis**
  - Overlap mask (intersection of all volumes)
  - Difference map (absolute difference between volumes)
- **Outputs**
  - Binary overlap array (`.npy`)
  - Difference array (`.npy`)
  - JSON metadata with statistics
  - Screenshot of visualization
- **Visualization**
  - Multi-volume blending in Napari
  - Adjustable opacity/colormaps

## Installation
```bash
cd volume-comparison-tool
pip install -r requirements.txt  # numpy napari imageio

##p.s I have used the breakly university open data to compare 5 FMRI subject data
