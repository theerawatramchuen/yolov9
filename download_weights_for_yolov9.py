# Imports the necessary libraries
import sys
import os
import requests
from tqdm.notebook import tqdm
from pathlib import Path
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
from IPython.display import display, Image
from PIL import Image as PILImage


# Configures the directories for code and data
CODE_FOLDER = Path(".").resolve()  # Code directory
WEIGHTS_FOLDER = CODE_FOLDER / "weights"  # Directory for model weights
DATA_FOLDER = CODE_FOLDER / "data"  # Directory for data

# Creates the directories for weights and data, if they don't exist
WEIGHTS_FOLDER.mkdir(exist_ok=True, parents=True)
DATA_FOLDER.mkdir(exist_ok=True, parents=True)

# Adds the code directory to the Python path for importing modules
sys.path.append(str(CODE_FOLDER))

# URLs of weight files
weight_files = [
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c.pt",
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-e.pt",
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-c.pt",
    "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-e.pt"
]

# Iterate over the list of URLs to download the weight files
for i, url in enumerate(weight_files, start=1):
    filename = url.split('/')[-1]
    response = requests.get(url, stream=True)
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kilobyte
    with open(WEIGHTS_FOLDER / filename, 'wb') as file:
        for data in response.iter_content(block_size):
            file.write(data)


""" 
Training CLI:
python train.py --batch 16 --epochs 20 --img 640 --device 0 --data data.yaml --weights weights/gelan-c.pt --cfg models/detect/gelan-c.yaml 
"""