def tampilkan_status():
    print("Kondisi penyimpanan biji kopi baik")

    for i, data in enumerate(data_sensor, 1):
        print("Data ke-", i)
        print("Suhu:", data["suhu"], "°C")
        print("Kelembapan:", data["kelembapan"], "%")
