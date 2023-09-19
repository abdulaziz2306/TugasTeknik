from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput

net = detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = videoSource("file://In_1.jpg")      # '/dev/video0' for V4L2
display = videoOutput("file://Out_1.jpg") # 'my_video.mp4' for file

while display.IsStreaming():
    img = camera.Capture()

    if img is None: # capture timeout
        continue

    detections = net.Detect(img)
    
    display.Render(img)
    display.SetStatus("FPS".format(net.GetNetworkFPS()))