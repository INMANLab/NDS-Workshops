# Neural Data Science Workshops

This repository holds a series of tutorials created for the **INMAN Lab** designed to provide a hands-on introduction to basic neural data analysis. 

The tutorials are implemented within `.ipynb` notebooks for use with [Google Colab](https://colab.google). This allows anyone to access the content via a web brower runtime and requires no local Python installation. All required Data for the tutorials is located in `./Sample Data/`.

These tutorials use functions from common Python libraries (e.g., `pandas`, `numpy`) as well as some open-source packages (e.g., `MNE`, `neurodsp`). These are installed within the notebook virtual environment. Detailed documentation for the functions used can be found online.

For a more detailed review of the material, check out Mike X Cohen's YouTube playlists on [Analyzing Neural Time Series Data](https://www.youtube.com/channel/UCUR_LsXk7IYyueSnXcNextQ)

<br>

# Accessing the Tutorials

The recommended approach is to simply clone the `NDS Workshops` GitHub repository. Alternatively, you can just download the specific files you need. Instructions for both approaches can be found [here](https://www.gitkraken.com/learn/git/github-download#:~:text=Click%20on%20the%20file%20you,the%20file%2C%20and%20select%20Save%20).


<br>


# Content

1. **Fundamentals of NSP**

    This tutorial provides a general overview of the different types of analyses used with neural recordings (e.g., time-domain vs. frequency-domain). Much of the tutorial concerns neural signal processing, specifically the common preprocessing steps used: re-referencing, identification of bad channels and artifacts, downsampling, filtering, etc.

2. **Event-Related Analyses (under dev.)**

    This tutorial will focus on using event information to create trial epochs, extract features from ERPs, and perform appropriate time-frequency analyses. The dataset used is from an experiment with intracranial recordings in human that used single-pulse electrical stimulation (SPES) to elicit cortico-cortical evoked potentials (CCEPs).

3. **???**