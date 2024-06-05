from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt") 

# Use the model
model.train(data="coco128.yaml", epochs=3)  
metrics = model.val()  
results = model("https://ultralytics.com/images/bus.jpg")  
path = model.export(format="onnx") 

