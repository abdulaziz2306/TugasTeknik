from jetson_inference import detectNet # Library Jetson Inference menyediakan model SSD MobilenetV2, dicloning dari Github 
from jetson_utils import videoSource, videoOutput # Library Jetson Utils untuk Display dengan CUDA dari Jetson nano, dicloning dari Github

# Inisialisasi mo el deteksi dengan batas threshold 0.5 atau 50%
net = detectNet("ssd-mobilenet-v2", threshold=0.5)

# Inisialisasi sumber video
camera = videoSource("2.jpeg") #file gambar diletakan difolder .py ini.

# Inisialisasi tampilan video
display = videoOutput("Out_3.jpg") #file gambar akan disimpan pada folder .py ini

# Inisialisasi hitungan objek manusia dan bukan manusia diawali nilai 0
jumlah_objek_manusia = 0
selain_manusia = 0

#Perintah eksekusi running
while display.IsStreaming():
    img = camera.Capture()

    if img is None: # capture timeout
        continue

    # Lakukan deteksi objek
    detections = net.Detect(img)
    
    # Hitung jumlah objek manusia
    for detection in detections:
        if detection.ClassID == 1:  # ID Class manusia pada no 1 pada file ClassID.txt
            jumlah_objek_manusia += 1
    #up
    
    # Tampilkan hasil deteksi
    display.Render(img)
    display.SetStatus("Jumlah Objek Manusia: {}, Jumlah Objek Selain Manusia{}".format(jumlah_objek_manusia, selain_manusia))

# Hentikan tampilan video
display.Close()