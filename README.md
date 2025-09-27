# Pi Local Radio

A **Raspberry Pi–friendly local radio station** where users can create customizable stations, upload their own music, and listen in a browser. Designed for **localhost use**, no extra hardware required.  

![Pi Local Radio](https://user-images.githubusercontent.com/yourusername/pi-local-radio/demo.png)  
*(Optional: add a screenshot of your app)*

---

## Features

- Create **custom stations** on your Raspberry Pi.
- Upload **MP3 or WAV files** per station.
- **Playlists** with shuffle, loop, and continuous play.
- Accessible in a **browser via localhost** or on your local network (`http://<Pi-IP>:5000`).
- Lightweight and optimized for **Raspberry Pi 4**.
- Folder structure persists — uploaded files stay after restarts.
- Ready to be shared as an **open-source project**.

---

## Requirements

- Raspberry Pi 4 (or any Pi with Python 3)
- Python 3
- Flask (`pip3 install Flask`)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/pi-local-radio.git
cd pi-local-radio
