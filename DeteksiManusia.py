from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput
import cv2

# Inisialisasi model deteksi dengan threshold 0.5 atau 50%
net = detectNet("ssd-mobilenet-v2", threshold=0.5)

# Inisialisasi sumber video
camera = videoSource("/path/to/your/image.jpg")  # Ganti dengan path gambar Anda

# Inisialisasi tampilan video (output gambar)
display = videoOutput("Out_3.jpg")  # File gambar akan disimpan pada folder .py ini

# Inisialisasi hitungan objek manusia dan objek selain manusia
jumlah_objek_manusia = 0
selain_manusia = 0

# Perintah eksekusi running
while display.IsStreaming():
    img = camera.Capture()

    if img is None:  # capture timeout
        continue

    # Lakukan deteksi objek
    detections = net.Detect(img)

    # Hitung jumlah objek manusia dan selain manusia
    for detection in detections:
        if detection.ClassID == 1:  # ID Class manusia pada nomor 1 pada file ClassID.txt
            jumlah_objek_manusia += 1
        else:
            selain_manusia += 1

    # Tampilkan hasil deteksi
    display.Render(img)
    display.SetStatus("Jumlah Objek Manusia: {}, Jumlah Objek Selain Manusia: {}".format(jumlah_objek_manusia, selain_manusia))

# Hentikan tampilan video
display.Close()
