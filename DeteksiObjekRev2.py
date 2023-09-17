from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput

net = detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = videoSource(640, 480, "/dev/video1")      # '/dev/video0' for V4L2
display = jetson.utils.glDisplay() # 'my_video.mp4' for file

while display.IsOpen():
    img, width, height = cameraCaptureRGBA()
    detetctions = net.Detect(img, width, height)
    display.RenderOnce(img, width, height)
    display.SetTitle("FPS : ". format(net.GetNetworkFPS()))