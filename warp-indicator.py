#!/usr/bin/env python3
"""
WARP Indicator - Native GTK AppIndicator for Cloudflare WARP
"""

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk, AppIndicator3, GLib
import subprocess
import requests
import os


class WARPIndicator:
    """Main WARP Indicator application"""

    def __init__(self):
        self.app_name = "warp-indicator"
        self.version = "1.1.0"

        # -------------------------
        # Paths
        # -------------------------

        self.base_dir = os.path.dirname(os.path.abspath(__file__))

        self.connected_icon = os.path.join(
            self.base_dir,
            "assets/icons/connected.svg"
        )

        self.disconnected_icon = os.path.join(
            self.base_dir,
            "assets/icons/disconnected.svg"
        )

        # -------------------------
        # Create Indicator
        # -------------------------

        self.indicator = AppIndicator3.Indicator.new(
            self.app_name,
            self.disconnected_icon,
            AppIndicator3.IndicatorCategory.SYSTEM_SERVICES
        )

        self.indicator.set_status(
            AppIndicator3.IndicatorStatus.ACTIVE
        )

        # -------------------------
        # Menu
        # -------------------------

        self.menu = Gtk.Menu()

        # Status label
        self.status_item = Gtk.MenuItem(label="Checking status...")
        self.status_item.set_sensitive(False)
        self.menu.append(self.status_item)

        # IP label
        self.ip_item = Gtk.MenuItem(label="IP: Fetching...")
        self.ip_item.set_sensitive(False)
        self.menu.append(self.ip_item)

        # Separator
        self.menu.append(Gtk.SeparatorMenuItem())

        # Toggle button
        self.toggle_item = Gtk.MenuItem(label="Connect")
        self.toggle_item.connect("activate", self.toggle_warp)
        self.menu.append(self.toggle_item)

        # Separator
        self.menu.append(Gtk.SeparatorMenuItem())

        # About button
        about_item = Gtk.MenuItem(label="About")
        about_item.connect("activate", self.show_about)
        self.menu.append(about_item)

        # Quit button
        quit_item = Gtk.MenuItem(label="Quit")
        quit_item.connect("activate", self.quit_app)
        self.menu.append(quit_item)

        self.menu.show_all()
        self.indicator.set_menu(self.menu)

        # -------------------------
        # Start Updates
        # -------------------------

        self.update_ui()

        GLib.timeout_add_seconds(
            5,
            self.update_ui
        )

    # -------------------------
    # WARP Status
    # -------------------------

    def get_warp_status(self):
        """Get WARP connection status"""

        try:
            result = subprocess.run(
                ['warp-cli', 'status'],
                capture_output=True,
                text=True,
                timeout=5
            )

            output = result.stdout.lower()

            if "status update: connected" in output:
                return True

            if "status update: disconnected" in output:
                return False

            return None

        except Exception:
            return None

    # -------------------------
    # Public IP
    # -------------------------

    def get_public_ip(self):
        """Fetch public IP"""

        try:
            response = requests.get(
                "https://api.ipify.org",
                timeout=5
            )

            return response.text.strip()

        except Exception:
            return "Unavailable"

    # -------------------------
    # Toggle Connection
    # -------------------------

    def toggle_warp(self, widget):
        """Connect or disconnect WARP"""

        try:
            status = self.get_warp_status()

            if status:
                subprocess.run(
                    ['warp-cli', 'disconnect'],
                    check=False
                )
            else:
                subprocess.run(
                    ['warp-cli', 'connect'],
                    check=False
                )

            GLib.timeout_add_seconds(
                2,
                self.update_ui
            )

        except Exception as e:
            print(f"Toggle error: {e}")

    # -------------------------
    # Update UI
    # -------------------------

    def update_ui(self):
        """Update indicator UI"""

        status = self.get_warp_status()

        # -------------------------
        # Connected
        # -------------------------

        if status is True:

            ip = self.get_public_ip()

            self.status_item.set_label(
                "Status: Connected ✓"
            )

            self.ip_item.set_label(
                f"IP: {ip}"
            )

            self.toggle_item.set_label(
                "Disconnect"
            )

            self.indicator.set_icon_full(
                self.connected_icon,
                "Connected"
            )

        # -------------------------
        # Disconnected
        # -------------------------

        elif status is False:

            self.status_item.set_label(
                "Status: Disconnected"
            )

            self.ip_item.set_label(
                "IP: Not Connected"
            )

            self.toggle_item.set_label(
                "Connect"
            )

            self.indicator.set_icon_full(
                self.disconnected_icon,
                "Disconnected"
            )

        # -------------------------
        # Unknown State
        # -------------------------

        else:

            self.status_item.set_label(
                "Status: Unknown"
            )

            self.ip_item.set_label(
                "IP: Unknown"
            )

            self.toggle_item.set_label(
                "Retry"
            )

        return True

    # -------------------------
    # About Dialog
    # -------------------------

    def show_about(self, widget):
        """Show About dialog"""

        dialog = Gtk.AboutDialog()

        dialog.set_program_name(
            "WARP Indicator"
        )

        dialog.set_version(
            self.version
        )

        dialog.set_comments(
            "Native GTK AppIndicator for Cloudflare WARP"
        )

        dialog.set_website(
            "https://github.com/CoderAni34/warp-indicator"
        )

        dialog.set_authors(
            ["CoderAni34"]
        )

        dialog.set_license_type(
            Gtk.License.MIT_X11
        )

        dialog.run()
        dialog.destroy()

    # -------------------------
    # Quit
    # -------------------------

    def quit_app(self, widget):
        Gtk.main_quit()


# -------------------------
# Main Entry
# -------------------------

def main():

    WARPIndicator()

    Gtk.main()


if __name__ == "__main__":
    main()