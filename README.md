## Create Conda Environment, Clone the YOLOv9 repository and installation
Create conda environment python 3.8 <br/><br/>
conda create -n yolov9 python=3.8 -y<br/>
git clone https://github.com/carlosfab/yolov9.git <br/>
cd yolov9 <br/>
pip install -r requirements.txt -q <br/>
python download_weights_for_yolov9.py <br/>
Install pytorch cuda <br/>
https://pytorch.org/get-started/locally/
## Training CLI
python train.py --batch 16 --epochs 20 --img 640 --device 0 --data data.yaml --weights weights/gelan-c.pt --cfg models/detect/gelan-c.yaml <br/>
or <br/>
python train.py --batch 16 --epochs 20 --img 640 --device 0 --data data.yaml --weights weights/yolov9-c.pt --cfg models/detect/yolov9-c.yaml <br/>
or <br/>
pair of weight and config files in CLI as below<br/>
gelan-e.pt , gelan-e.yaml<br/>
yolov9-e.pt , yolov9-e.yaml<br/>
## yolov9 referrence link
https://sigmoidal.ai/en/how-to-train-yolov9-on-custom-dataset-a-complete-tutorial/
