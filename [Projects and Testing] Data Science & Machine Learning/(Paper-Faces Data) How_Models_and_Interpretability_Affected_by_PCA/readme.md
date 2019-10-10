### Datasource: https://cs.nyu.edu/~roweis/data.html  
- In the dataset, there are images of 40 people with 10 different poses e.g. smiling and angry faces etc. Therefore, there are total 400 samples.  
- The images size is (64, 64), which is stored as features of size 4096

### Goal:  
- For optimizing XGM model by exploring the important features.
- For the better accuracy-wall time trade-off, find out the best number of componenents of PCA with quantitative measures and human intervention.
- Explore how the classification/prediction will be affected by XGB models with different PCA components.  
- Figure out by interpretability: What the different features between these images which were always predicted wrongly by training all models with different number of PCA componenents.

-------------------------
For the better visualization of experiments result, please download the .ipynb file, or check by https://nbviewer.jupyter.org/github/ziweifan177/Data_Science_Pilot/blob/master/%5BProjects%20and%20Testing%5D%20Data%20Science%20%26%20Machine%20Learning/%28Paper-Faces%20Data%29%20How_Models_and_Interpretability_Affected_by_PCA/Image_Interpretability_Affected_by_PCA%20%28Faces%20Data%29.ipynb.
- But for nbviewer, the final comparison image could not be displayed.
- For the final comparison image, please direct to 'Output' Folder.
