import time
import json
import subprocess

def get_location():
    # Termux API kullanarak GPS konumunu alma
    result = subprocess.run(['termux-location', '--request', 'once', '--provider', 'gps'], stdout=subprocess.PIPE)
    location = json.loads(result.stdout)
    latitude = location['latitude']
    longitude = location['longitude']
    return latitude, longitude

if __name__ == "__main__":
    while True:
        try:
            latitude, longitude = get_location()
            google_maps_url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
            print(f"Telefonun konumu: {latitude}, {longitude}")
            print(f"Google Haritalar URL: {google_maps_url}")
        except Exception as e:
            print(f"Konum alınırken hata oluştu: {e}")
        
        time.sleep(15)  # Her 15 saniyede bir konumu al ve yazdır
