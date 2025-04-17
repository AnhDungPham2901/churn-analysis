import os

# Define the project root directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define data paths
DATA_DIR = os.path.join(ROOT_DIR, 'data')
TRAIN_DATA_PATH = os.path.join(DATA_DIR, 'club_churn_train.xlsx')
TEST_DATA_PATH = os.path.join(DATA_DIR, 'club_churn_test.xlsx')

# Other directories
NOTEBOOKS_DIR = os.path.join(ROOT_DIR, 'notebooks')
UTILS_DIR = os.path.join(ROOT_DIR, 'utils')