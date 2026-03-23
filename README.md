# WARP Indicator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Release](https://img.shields.io/badge/release-1.0-brightgreen.svg)](https://github.com/CoderAni34/warp-indicator/releases)

A lightweight, professional system tray indicator for Cloudflare WARP VPN on Linux. Monitor your VPN connection status directly from your system taskbar with a clean, intuitive interface.

## 🌟 Features

- **Real-time Status Monitor** - See your WARP connection status at a glance with dynamic updates
- **Quick Toggle** - Enable/disable WARP directly from the system tray with a single click
- **Lightweight** - Minimal system resource usage with pure Python implementation
- **Debian/Ubuntu Support** - Professional Debian packaging with easy installation
- **Native Integration** - System tray integration using AppIndicator3 for seamless desktop experience
- **About & Settings** - Quick access to settings and application information
- **Cross-platform Linux** - Works on all major Linux distributions with GTK 3.0+

## 📋 Requirements

- **OS:** Linux (Ubuntu, Debian, Fedora, Arch, etc.)
- **Python:** 3.6 or higher
- **Cloudflare WARP:** Must be installed and available as `warp-cli`
- **Dependencies:**
  - GTK 3.0+ 
  - libappindicator3
  - PyGObject (Python GObject bindings)

## 📦 Installation

### From Pre-built Debian Package (Recommended for Ubuntu/Debian)

The repository includes a pre-built .deb package for easy installation:

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install -y python3 python3-gi gir1.2-appindicator3-0.1 gir1.2-gtk-3.0 cloudflare-warp

# Clone and install
git clone https://github.com/CoderAni34/warp-indicator.git
cd warp-indicator
sudo dpkg -i warp-indicator_1.0-1.deb
```

**Or directly download and install:**

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install -y python3 python3-gi gir1.2-appindicator3-0.1 gir1.2-gtk-3.0 cloudflare-warp

# Download the latest .deb from the repository
wget https://github.com/CoderAni34/warp-indicator/raw/master/warp-indicator_1.0-1.deb
sudo dpkg -i warp-indicator_1.0-1.deb
```

### Build Debian Package (For Development)

To build your own Debian package from source:

```bash
git clone https://github.com/CoderAni34/warp-indicator.git
cd warp-indicator

# Install build dependencies
sudo apt-get install -y python3 python3-gi gir1.2-appindicator3-0.1 gir1.2-gtk-3.0 cloudflare-warp dh-python debhelper

# Build the package
chmod +x build.sh
./build.sh

# Install the generated .deb file
sudo dpkg -i build/warp-indicator_1.0-1_all.deb
```

## 🚀 Usage

### Command Line

```bash
warp-indicator
```

Or directly:
```bash
python3 warp-indicator.py
```

### System Startup

The application will integrate with your system tray. Look for the WARP Indicator icon:

- **View Status** - Click the indicator to see current connection status
- **Quick Toggle** - Click "Connect" or "Disconnect" to toggle VPN
- **Settings** - Access Cloudflare WARP settings panel
- **About** - View application information
- **Quit** - Exit the application

## 🏗️ Project Structure

```
warp-indicator/
├── warp-indicator.py       # Main application code
├── setup.py                # Python package setup
├── requirements.txt        # Python dependencies
├── build.sh               # Build script for Debian packaging
├── LICENSE                # MIT License
├── README.md              # This file
└── debian/                # Debian packaging files
    ├── control            # Package metadata
    ├── rules              # Build rules
    ├── changelog          # Version history
    └── compat             # Debhelper compatibility
```

## 🔧 Configuration

The application works out of the box with no configuration required. It communicates directly with `warp-cli` to control your WARP connection.

## 📝 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Bug Reports & Feature Requests

Found a bug or have a feature request? Please open an [issue](https://github.com/CoderAni34/warp-indicator/issues) on GitHub.

## 📧 Support

For questions and support, please open an [issue](https://github.com/CoderAni34/warp-indicator/issues) on GitHub or contact the maintainer.

## 🙏 Acknowledgments

- [Cloudflare WARP](https://warp.com/) - VPN service
- [GNOME Project](https://www.gnome.org/) - GTK and AppIndicator libraries
- [Python](https://www.python.org/) - Programming language

---

Made with ❤️ by [CoderAni34](https://github.com/CoderAni34)