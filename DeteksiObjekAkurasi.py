from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput

# Inisialisasi model deteksi
net = detectNet("ssd-mobilenet-v2", threshold=0.5)

# Inisialisasi sumber video
camera = videoSource("In_1.jpg")      # '/dev/video0' for V4L2

# Inisialisasi tampilan video
display = videoOutput("Out_1.jpg") # 'my_video.mp4' for file

# Inisialisasi hitungan objek manusia
jumlah_objek_manusia = 0
selain_manusia = 0

while display.IsStreaming():
    img = camera.Capture()

    if img is None: # capture timeout
        continue

    # Lakukan deteksi objek
    detections = net.Detect(img)
    
    # Hitung jumlah objek manusia
    for detection in detections:
        if detection.ClassID == 1:  # ID kelas untuk manusia (Anda perlu memeriksa ID kelas yang benar)
            jumlah_objek_manusia += 1
        
        if detetcion.ClassID == 0:
            selain_manusia +=1
    
    # Tampilkan hasil deteksi
    display.Render(img)
    display.SetStatus("Jumlah Objek Manusia: {}, Jumlah Objek Selain Manusia{}".format(jumlah_objek_manusia, selain_manusia))

# Hentikan tampilan video
display.Close()