# Aquaculture Installation Volume Calculator

## Overview

This repository provides code for visualizing and calculating the volume of segmented parts of point cloud data using processed data from a multibeam echosounder. Despite being developed for multibeam water column data on mussels and seaweed, it can be used for any point cloud file where clustering is desired.

If you have any question, don't hesitate to contact me: samira.lashkari@gmail.com

## Data Requirements

The uploaded data must have the following four columns in this specific order: 'x', 'y', 'z' and 'intensity' and be in .txt or .csv format. If you wish to use all functionalities of CloudVolume, 'ping_number' and 'beam' should be added to the files as well. Please ensure that there are no indices for the columns.

You can find sample data [here](https://drive.google.com/file/d/15rBiuT27kIJQX5pq0yL5JK0sN9E-XCw0/view?usp=drive_link) to process with the developed GUI.

## Requirements

It is important to set the exact version of libraries and python. You can download anaconda here which makes it easier to set the desired version of python and libraries:
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

To clone this repository, follow these steps:

1. Open **Git Bash**.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command:

```bash
git clone https://github.com/SamiraLashkari/CloudVolume_multibeam
```
You can download the repository from website as well. 

Then, you can install all dependencies in your environment by running the following command. First, navigate to the `CloudVolume_multibeam` folder in your system:

```bash
cd CloudVolume_multibeam
pip install -r requirements.txt
```

To launch the graphical user interface (GUI), execute the following command in your terminal:

```bash
python CloudVolume/CloudVolume.py
```
![GUI-image](https://github.com/SamiraLashkari/CloudVolume_multibeam/blob/main/GUI_CloudVolume.jpg)

## Uploading data
**Data Upload**:
   - Upload data in .csv or .txt format with columns X, Y, Z, intensity and optionally ping_number, and beam.
   - After upload, view the intensity histogram.

**Default Values**:
   - Choose species to set default parameter values for these species (values based on learning dataset) or define your own values.
     
## 🔴 Filtering

**Remove Noise**:
   - Visualize beam number histogram to identify noise.
   - Remove the most frequently occurring bin by using  **Remove Most Frequent**.
   - Adjust bottom data removal ratio to delete the seafloor interference bands. This step removes a percentage (from the bottom up) of the data.

**Setting Threshold**:
   - Adjust the thresholds if necessary (or keep the default values) and filter.

**Statistical Outlier Removal**:
   - Set number of neighbours and standard ratio for outlier removal.

**Radius Outlier Removal**:
   - Define minimum amount of points and radius for outlier removal.

## 	🔵 Saving Data as Point Cloud or DataFrame 

At any point in the process before clustering, you can save the data either as a **point cloud** (.pcd)  or a **dataframe** (.csv):

- **Saving as DataFrame**:  
  This allows you to load the saved data later directly from the GUI, enabling you to continue processing from where you left off.

- **Saving as Point Cloud**:  
  Point cloud data can be loaded into platforms like **CloudCompare** for visualization and analysis.

Before saving, you can verify the point cloud size by checking the fields **Size of Current Point Cloud** and **Size of Previous Point Cloud** to ensure you are saving the correct version.

This flexibility ensures you can choose the format that best suits your workflow, whether for further processing or visualization.

## 🟢 Clustering 
**K-Means Clustering**: groups datapoints into a predefined amount of clusters based on proximity

**GMM Clustering**: identifies hidden patterns and groups data less rigidly into a predefined amount of clusters 

**Hdbscan (Hierarchical Density-Based Spatial Clustering of Applications with Noise) Clustering**: identifies clusters based on data point density. A minimum cluster size and amount of samples within each cluster needs to be specified.

**Drawing Clusters**:
      
  If the clustering algorithms do not yield satisfactory results—especially in cases of close entanglement—you can manually define boundaries. To do so:

  1. Press the **Start** button next to **Drawing the  border**. This will open another GUI window.
  2. To begin drawing lines between clusters, click the **Draw Curve** button. Each click will allow you to place points and connect them, forming boundaries.
  3. Once you’ve finished drawing borders for one cluster, press **Assign Labels** to label it. This will close the polygon and assign the data points into a single cluster.
  4. Continue the previous step until all points belong to a cluster.
  5. When finished, press the **Finish** button.
  6. Return to the main GUI and click **Get Clusters**. All manually created clusters are now added to the clusters-database.

This will help to refine clusters manually, especially in challenging cases.
![GUI-image](https://github.com/SamiraLashkari/CloudVolume_multibeam/blob/main/Drawing_clusters.jpg)

## 🟣 Result section 

- **Refining and Managing Result**:

  After completing the initial clustering step, you can add these clusters to the result by pressing the **Add Clusters** button. The cluster numbering will be updated based on their size. If clusters are added, the numbering is adapted based on the new size distribution. Be aware of this: cluster 4 may not be called clusters 4 again after clusters have been deleted and/or added. Always check the new numbers by pressing “Update clusters”. Clusters can be merged as well. To delete/add/merge (a) cluster(s), select them in the panel and click on the desired action.

  To reset or start over, use the following options:
  
  - **Empty Result**: Clears all clusters from the result.
    
  - **Convert All to Pointcloud**: Merges all points back into a single point cloud, allowing you to start the clustering process from the beginning.

    
## 🟡 Volume calculation 

**Interpolation**:
- In certain cases, the distance between datapoints may be too large, especially for multibeam data points. To reduce the gap, interpolation can be performed to generate data points between existing data ones. Choose the desired amount of interpolations and perform the step by clicking **start**.

**Voxelization**:
Converts the point cloud data into a voxel grid with a predefined voxel size. Upper and lower thresholds for weighted voxelization can be defined. Weighted voxelization calculates the amount of data points within each voxel and considers voxels as a whole if above the upper threshold and disregards them if below the lower threshold. In between, voxels are considered percentage-wise. The default value for upper and lower threshold is d10 (10th percentile) and d25 (25th percentile).
The volume is calculated without and with weighted voxelization applied and added to the **volume results** section.  


## 🟠 Saving results     

Select the desired clusters by checking the box next to them and click  the **Add Chosen Cluster** button. These clusters will be added to the table in the bottom-right, with their volumes calculated before **Volume** and after **Customized volume** weighted voxelization and interpolation.

You can remove the last cluster from the list by clicking the **Remove Last Cluster** button. 

When all desired clusters are in the list, click **Save Clusters and Volume**. This action will save:

- A `.csv` file containing all volume information for the selected clusters.
- Individual clusters as `.pcd` files (point cloud format).

This ensures that both volume calculations and cluster geometries are preserved for further analysis.
    
