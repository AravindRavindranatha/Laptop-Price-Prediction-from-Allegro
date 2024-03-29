# Project Title: Laptop Price Prediction Model using Machine Learning.

**Description:** Developed a machine learning model to predict the price of laptops based on their attributes. The goal was to minimize the Root Mean Squared Error (RMSE) measure when testing and comparing different models.

**Role:** Sole developer responsible for defining, training, and evaluating the machine learning models.

**Technologies Used:**
  - Python
  - Jupyter Notebook
  - Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
    
**Challenges and Solutions:**
  - Challenge: Selecting the most suitable machine learning algorithms for the task.
  - Solution: Conducted research and experimentation to identify the algorithms that performed best for predicting laptop prices.
  - Challenge: Ensuring the model generalizes well to unseen data and doesn't overfit.
  - Solution: Implemented cross-validation techniques and evaluated model performance on a separate test dataset to mitigate overfitting.

**Approaches Tested:**
  - Linear Regression
  - Decision Tree Regression
  - Random Forest Regression
  - Gradient Boosting Regression
    
**Results:**
- Linear Regression:
  - RMSE 0.18408866223145284 
  - R2 score 0.8391841000697197
  - MAE 0.13505841373778849
- Ridge Regression:
  - RMSE 0.18694424747997215
  - R2 score 0.8341562483171016
  - MAE 0.13682326245648682
- Lasso Regression
  - RMSE 0.19078282513076833
  - R2 score 0.8272756953058719
  - MAE 0.13907383981690896
- K Nearest Neigbour
  - RMSE 0.175673172043473
  - R2 score 0.8535512098006105
  - MAE 0.12509611553357758
- Decision Tree
  - RMSE 0.18014282010898716
  - R2 score 0.8405597148432071
  - MAE 0.13496884551134025
- Random Forest
  - RMSE 0.1367438601579829
  - R2 score 0.9112658950637865
  - MAE 0.0958890112055825
 
**Final Model:**
- Selected [Random Forest], achieving the R2 Score of [0.9112658950637865].
Model trained using the training dataset and evaluated on the test dataset to ensure generalization.

**Thought Process:**

- Explored and preprocessed the dataset to handle missing values, categorical variables, and feature scaling.
- Experimented with different machine learning algorithms and hyperparameters to find the best-performing model.
- Visualized the performance of each model using appropriate metrics and visualizations.
- Documented all steps, insights, and decisions in the Jupyter Notebook to provide transparency and reproducibility.

**Notebook: Provide a link to the Jupyter Notebook containing the code, analysis, and results.**
