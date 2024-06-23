# Step 1: Install Kaggle API
!pip install Kaggle
# Step 2: Upload the kaggle.json file
from google.colab import files
files.upload()  # This will prompt you to upload the kaggle.json file
!mkdir -p ~/.kaggle
!mv kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!kaggle datasets download -d nikhilpandey360/chest-xray-masks-and-labels
# Step 5: Unzip the dataset (if necessary)
!unzip chest-xray-masks-and-labels.zip
