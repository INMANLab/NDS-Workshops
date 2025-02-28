# Neural Data Science Workshops

This repository holds a series of tutorials created for the **INMAN Lab** designed to provide a hands-on introduction to basic neural data analysis. 

The tutorials are implemented within `.ipynb` notebooks for use with [Google Colab](https://colab.google). This allows anyone to access the content via a web browser runtime and requires no local Python installation. All required Data for the tutorials is located in `/Data/`, which can be downloaded separately from Google Drive [here](https://drive.google.com/drive/folders/1ApD9cu3gtnUNT-zSg6OzQBV8wKWnUoep?usp=sharing).

These tutorials use functions from common Python libraries (e.g., `pandas`, `numpy`) as well as some open-source packages (e.g., `MNE`). These are installed within the notebook virtual environment. Detailed documentation for the functions used can be found online.

For a more detailed review of the material, check out Mike X Cohen's YouTube playlists on [Analyzing Neural Time Series Data](https://www.youtube.com/channel/UCUR_LsXk7IYyueSnXcNextQ)

<br>

# Accessing the Tutorials

The recommended approach is to simply clone the `NDS-Workshops` GitHub repository. Alternatively, you can just download the specific files you need.  

To run the code, simply move the `.ipynb` file to somewhere on your Google Drive. Next, open a web browser, navigate to your Google Drive, and double-click the `.ipynb` file; it should automatically render as a Google Colab notebook that you can interact with. If it launches in a separate code editor, try right-clicking the file and selecting *Open-with: Google Colaboratory*. Finally, if that option is not available, navigate to the [Google Colab website](https://colab.research.google.com) and upload the `.ipynb` file manually.

<br>

# Content

1. **Fundamentals of Neural Signal Processing**

    This tutorial provides a general overview of the different types of analyses used with neural recordings (e.g., time-domain vs. frequency-domain). Much of the tutorial concerns neural signal processing, specifically the common preprocessing steps used: re-referencing, identification of bad channels and artifacts, downsampling, filtering, etc.

2. **Event-Related Analyses**

    This tutorial will focus on using event information to create trial epochs, visualize epoched data, extract features, and perform statistical comparisons. The dataset used is from an experiment with intracranial recordings in human that used single-pulse electrical stimulation (SPES) to elicit cortico-cortical evoked potentials (CCEPs).

3. **Data Visualization**

    This tutorial reviews general principles and best practices for data vizualization, including: figure construction and design, how to maximize information density, the use of different color palettes, and Python-based plotting libraries (e.g., `matplotlib`, `seaborn`). 
