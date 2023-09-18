from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput
import time

net = detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = videoSource("/dev/video0")      # '/dev/video0' for V4L2
display = videoOutput("display://0") # 'my_video.mp4' for file

# Setel waktu berapa lama program akan berjalan (15 detik)
run_time = 15  # Detik

fps_data = []  # Untuk menyimpan data FPS

start_time = time.time()

while (time.time() - start_time) < run_time:
    img = camera.Capture()

    if img is None: # capture timeout
        continue

    detections = net.Detect(img)
    
    display.Render(img)
    
    # Dapatkan dan catat FPS
    fps = net.GetNetworkFPS()
    fps_data.append(fps)

    display.SetStatus("FPS: {:.2f}".format(fps))

# Buat file notepad dan catat data FPS
with open("fps_data.txt", "w") as file:
    for fps in fps_data:
        file.write("{:.2f}\n".format(fps))
        
# Hentikan tampilan video
display.Close()