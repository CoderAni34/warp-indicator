# WARP Indicator

A lightweight system tray indicator for Cloudflare WARP VPN on Linux. Monitor your VPN connection status directly from your system taskbar with a clean, intuitive interface.

## 🌟 Features

- **Real-time Status Monitor** - See your WARP connection status at a glance
- **Quick Toggle** - Enable/disable WARP directly from the system tray
- **Lightweight** - Minimal system resource usage with Python-based implementation
- **Debian/Ubuntu Support** - Easy installation on Debian-based systems
- **Clean UI** - Native system tray integration for a seamless experience

## 📦 Installation

### Prerequisites

- Python 3.6+
- Cloudflare WARP installed on your system
- GTK 3.0+ and associated Python bindings

### From Source

```bash
git clone https://github.com/CoderAni34/warp-indicator.git
cd warp-indicator
./build.sh
```

### Debian/Ubuntu

The project includes Debian packaging for easy installation:

```bash
cd debian/
# Follow the packaging instructions to build and install the .deb package
```

## 🚀 Usage

Run the indicator:

```bash
python3 warp-indicator.py
```

The application will appear in your system tray. Click to expand options:
- View current WARP status (Connected/Disconnected)
- Toggle VPN connection on/off
- Access quick settings

## 🔧 Configuration

Configuration files are typically stored in `~/.config/warp-indicator/`

## 📝 License

This project is licensed under the terms specified in the LICENSE file.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

Made with ❤️ for Linux users