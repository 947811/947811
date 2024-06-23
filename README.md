Pneumonia Detection using UNet

Project Overview:
- This project uses a UNet model to detect pneumonia from chest X-ray images.

Dataset:
- Chest X-ray images and corresponding lung masks from Kaggle.

Data Preparation:
1. Install Kaggle API and upload `kaggle.json` for authentication.
2. Download and unzip the dataset.
3. Load images and masks, ensuring a 1-to-1 correspondence.

Model Architecture:
- UNet model with encoding path, bottleneck, and decoding path.

Loss Function and Metrics:
- Dice Coefficient Loss
- Dice Coefficient, Binary Accuracy

Training:
1. Split the dataset into training, validation, and testing sets.
2. Compile the model with Adam optimizer.
3. Train the model with checkpointing, early stopping, and learning rate reduction callbacks.

Evaluation:
- Metrics: Accuracy, F1 Score, Precision, Recall



Model Saving:
- The trained model is saved as `pneumonia.h5`.

