def tampilkan_laporan(data_sensor):
    print("\n--- LAPORAN DATA SENSOR ---")

    for i, data in enumerate(data_sensor, 1):
        print("Data ke-", i)
        print("Suhu:", data["suhu"], "°C")
        print("Kelembapan:", data["kelembapan"], "%")
