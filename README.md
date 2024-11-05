# Aquaculture Installation Volume Calculator

## Overview

This repository provides code for visualizing and calculating the volume of aquaculture installations (it tested for seaweed and mussels) using processed data from a multibeam ecosounder sensor.

If you have any question, don't hesitate to contact me: samira.lashkari@gmail.com

## Data Requirements

The uploaded data should have the following six columns in this specific order: 'x', 'y', 'z', 'intensity', 'ping_number', 'beam' and be .txt or .csv format. Please ensure that there are no indices for the columns.

You can find sample data [here](https://drive.google.com/file/d/15rBiuT27kIJQX5pq0yL5JK0sN9E-XCw0/view?usp=drive_link) to process with the developed GUI.

## Requirements

It is important to set the exact version of libraries and python version. You can download anaconda here which makes it easier to set the desired version of python and libraries:
[here](https://www.anaconda.com/download). 


- **Python 3.9.20**: Please install Python 3.9.20 in your environment, as the open3d library is not compatible with more recent versions of Python.

Open Anaconda powershell prompt and write the command below. You give any name to your environment and replace my_env in command below. 
```bash
conda create -n my_env python=3.9.20
conda activate my_env
```
  
- **Dependencies**:
  - `open3d==0.17.0`
  - `hdbscan==0.8.33`
  - `pandas==1.5.3`
  - `numpy==1.24.3`
  - `scikit-learn==1.3.0`
  - `matplotlib==3.7.2`

## Installation and running GUI automatically

After setting up your environment with the specified Python version, you can install the `CloudVolume-multibeam` library along with its dependencies by running:

```bash
pip install CloudVolume-multibeam
```
Once installed, you can launch the GUI by running the following command:

```bash
CloudVolume
```
This will launch the application’s GUI.

## Installation and running GUI manually

If you prefer to install the required libraries manually, you can do so by running:

```bash
pip install -r requirements.txt
```

To launch the graphical user interface (GUI), execute the following command in your terminal:

```bash
python CloudVolume.py
```
![GUI-image](https://github.com/SamiraLashkari/CloudVolume_multibeam/blob/main/GUI_CloudVolume.jpg)

## Part 1: uploading data
**Data Upload**:
   - Upload data in .csv or .txt format with columns X, Y, Z, intensity, ping_number, and beam.
   - After upload, view intensity histogram.

**Default Values**:
   - Choose species to set default parameter values.
     
## Part 2: Filtering (red)
**Remove Noise**:
   - Visualize beam number histogram to identify noise.
   - Remove noise using 'Remove Most Frequent'.
   - Adjust bottom data removal ratio for profile noise.

**Setting Threshold**:
   - Adjust threshold if necessary and filter.

**Statistical Outlier Removal**:
   - Set number of neighbors and standard ratio for outlier removal.

**Radius Outlier Removal**:
   - Define minimum points and radius for outlier removal.
## Part3: Clustering (green)
**K-Means Clustering**:
   - Automatically group similar points.
   - Choose number of clusters.

**GMM Clustering**:
   - Identify hidden patterns with less rigid clusters.
   - Choose number of clusters.

**Hdbscan Clustering**:
   - Identify clusters based on data point density.
   - Set minimum cluster size and samples.

**Drawing Clusters**:
    - Manually draw cluster boundaries if needed.
    
## Part4: Volume calculation (yellow)
**Result Section**:
    - Edit, add, remove, and merge clusters to the filnal result
    - Update and check result by clicking on the choosen cluster to add, remove or merge into result.

**Interpolation**:
    - Estimate points between known data points in point cloud of each volume (you can choose any cluster to process the rest).

**Voxelization**:
    - Convert point cloud to voxel grid.
    - Define thresholds for voxelization.
    - Set upper and lower thresholds for weighted voxelization.
    - Calculate voxel weights based on point counts.

**Calculate Result Volume**:
    - Add cluster volumes to total volume. 
