#!/usr/bin/env python3
"""
WARP Indicator - System tray indicator for Cloudflare WARP VPN
"""

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk, AppIndicator3, GLib
import subprocess
import os
import sys


class WARPIndicator:
    """Main WARP Indicator application class"""
    
    def __init__(self):
        self.app_name = "warp-indicator"
        self.app_version = "1.0.0"
        
        # Create indicator
        icon_path = os.path.dirname(os.path.abspath(__file__))
        self.indicator = AppIndicator3.Indicator.new(
            self.app_name,
            "network-wireless",
            AppIndicator3.IndicatorCategory.SYSTEM_SERVICES
        )
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        
        # Create menu
        self.menu = Gtk.Menu()
        self.update_menu()
        self.indicator.set_menu(self.menu)
        
        # Update status periodically
        GLib.timeout_add_seconds(5, self.update_status)
    
    def get_warp_status(self):
        """Get current WARP connection status"""
        try:
            result = subprocess.run(
                ['warp-cli', 'status'],
                capture_output=True,
                text=True,
                timeout=5
            )
            return 'Connected' in result.stdout
        except Exception:
            return None
    
    def toggle_warp(self, widget):
        """Toggle WARP connection on/off"""
        try:
            status = self.get_warp_status()
            if status:
                subprocess.run(['warp-cli', 'disconnect'], check=False)
            else:
                subprocess.run(['warp-cli', 'connect'], check=False)
            self.update_menu()
        except Exception as e:
            print(f"Error toggling WARP: {e}")
    
    def update_menu(self):
        """Update menu items based on current status"""
        # Clear existing menu
        for item in self.menu.get_children():
            self.menu.remove(item)
        
        # Get current status
        status = self.get_warp_status()
        
        if status is None:
            status_text = "Status: Unknown"
        elif status:
            status_text = "Status: Connected ✓"
        else:
            status_text = "Status: Disconnected"
        
        # Status item
        status_item = Gtk.MenuItem(label=status_text)
        status_item.set_sensitive(False)
        self.menu.append(status_item)
        
        # Separator
        sep1 = Gtk.SeparatorMenuItem()
        self.menu.append(sep1)
        
        # Toggle button
        toggle_text = "Disconnect" if status else "Connect"
        toggle_item = Gtk.MenuItem(label=toggle_text)
        toggle_item.connect("activate", self.toggle_warp)
        self.menu.append(toggle_item)
        
        # Separator
        sep2 = Gtk.SeparatorMenuItem()
        self.menu.append(sep2)
        
        # Settings item
        settings_item = Gtk.MenuItem(label="Settings")
        settings_item.connect("activate", self.open_settings)
        self.menu.append(settings_item)
        
        # About item
        about_item = Gtk.MenuItem(label="About")
        about_item.connect("activate", self.show_about)
        self.menu.append(about_item)
        
        # Quit item
        quit_item = Gtk.MenuItem(label="Quit")
        quit_item.connect("activate", self.quit_app)
        self.menu.append(quit_item)
        
        self.menu.show_all()
    
    def update_status(self):
        """Periodically update menu status"""
        self.update_menu()
        return True
    
    def open_settings(self, widget):
        """Open WARP settings"""
        try:
            subprocess.Popen(['warp-cli', 'settings'])
        except Exception as e:
            print(f"Error opening settings: {e}")
    
    def show_about(self, widget):
        """Show about dialog"""
        dialog = Gtk.AboutDialog()
        dialog.set_program_name("WARP Indicator")
        dialog.set_version(self.app_version)
        dialog.set_comments("System tray indicator for Cloudflare WARP VPN")
        dialog.set_website("https://github.com/CoderAni34/warp-indicator")
        dialog.set_authors(["CoderAni34"])
        dialog.set_license_type(Gtk.License.MIT)
        dialog.run()
        dialog.destroy()
    
    def quit_app(self, widget):
        """Quit the application"""
        Gtk.main_quit()


def main():
    """Main entry point"""
    app = WARPIndicator()
    Gtk.main()


if __name__ == "__main__":
    main()
