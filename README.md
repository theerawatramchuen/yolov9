# yolov9
https://sigmoidal.ai/en/how-to-train-yolov9-on-custom-dataset-a-complete-tutorial/

## Clone the YOLOv9 repository and installation
git clone https://github.com/carlosfab/yolov9.git <br/>
cd yolov9 <br/>
pip install -r requirements.txt -q <br/>
python download_weights_for_yolov9.py <br/>
## Training CLI
python train.py --batch 16 --epochs 20 --img 640 --device 0 --data data.yaml --weights weights/gelan-c.pt --cfg models/detect/gelan-c.yaml <br/>
