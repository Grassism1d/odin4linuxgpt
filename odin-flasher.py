import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import os
import time
import threading

class OdinFlasherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Samsung Odin & ADB/Fastboot Tool")
        self.root.geometry("700x700")
        self.root.configure(bg='#2e2e2e')  # Default dark background
        self.root.resizable(False, False)
        
        self.is_dark_mode = True
        self.setup_styles()
        self.create_tabs()
        self.device_thread = threading.Thread(target=self.check_device, daemon=True)
        self.device_thread.start()
    
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", font=("Roboto", 12), borderwidth=2)
        self.style.configure("TLabel", font=("Roboto", 12), padding=6)
        self.style.configure("Rounded.TFrame", background="#2e2e2e", relief="groove", borderwidth=3)
    
    def create_tabs(self):
        notebook = ttk.Notebook(self.root)
        self.odin_frame = ttk.Frame(notebook, style="Rounded.TFrame")
        self.adb_frame = ttk.Frame(notebook, style="Rounded.TFrame")
        
        notebook.add(self.odin_frame, text="Odin Flasher")
        notebook.add(self.adb_frame, text="ADB & Fastboot")
        notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        self.create_odin_tab()
        self.create_adb_tab()
    
    def create_odin_tab(self):
        tk.Label(self.odin_frame, text="Samsung Odin Flasher", font=("Roboto", 18)).pack(pady=10)
        
        self.create_partition_buttons()
        self.flash_button = ttk.Button(self.odin_frame, text="Start Flashing", command=self.start_flashing)
        self.flash_button.pack(pady=20)
        
        self.device_label = tk.Label(self.odin_frame, text="Device Not Connected", font=("Roboto", 12))
        self.device_label.pack(pady=10)
    
    def create_partition_buttons(self):
        self.partition_buttons = {}
        partitions = ["AP", "BL", "CP", "CSC", "HOME_CSC"]
        
        for partition in partitions:
            btn = ttk.Button(self.odin_frame, text=f"Select {partition} File", command=lambda p=partition: self.select_file(p))
            btn.pack(pady=5)
            self.partition_buttons[partition] = btn
    
    def create_adb_tab(self):
        tk.Label(self.adb_frame, text="ADB & Fastboot Tools", font=("Roboto", 18)).pack(pady=10)
        
        ttk.Button(self.adb_frame, text="Check Device", command=self.check_adb_device).pack(pady=5)
        ttk.Button(self.adb_frame, text="Reboot to Bootloader", command=self.reboot_to_bootloader).pack(pady=5)
        ttk.Button(self.adb_frame, text="Reboot to Recovery", command=self.reboot_to_recovery).pack(pady=5)
        ttk.Button(self.adb_frame, text="Sideload Zip", command=self.sideload_zip).pack(pady=5)
    
    def check_device(self):
        while True:
            device_id = self.get_connected_device_id()
            self.device_label.config(text=f"Device: {device_id}" if device_id else "Device Not Connected")
            time.sleep(5)
    
    def get_connected_device_id(self):
        try:
            result = subprocess.run("adb devices", shell=True, capture_output=True, text=True)
            devices = result.stdout.splitlines()
            if len(devices) > 1:
                return devices[1].split()[0]
        except:
            return None
    
    def select_file(self, partition):
        file_path = filedialog.askopenfilename(title=f"Select {partition} File")
        if file_path:
            self.partition_buttons[partition].config(text=f"{partition}: {os.path.basename(file_path)}")
    
    def start_flashing(self):
        messagebox.showinfo("Flash", "Flashing process would start here.")
    
    def check_adb_device(self):
        result = subprocess.run("adb devices", shell=True, capture_output=True, text=True)
        messagebox.showinfo("ADB Devices", result.stdout)
    
    def reboot_to_bootloader(self):
        subprocess.run("adb reboot bootloader", shell=True)
        messagebox.showinfo("Reboot", "Rebooting to bootloader...")
    
    def reboot_to_recovery(self):
        subprocess.run("adb reboot recovery", shell=True)
        messagebox.showinfo("Reboot", "Rebooting to recovery...")
    
    def sideload_zip(self):
        zip_file = filedialog.askopenfilename(title="Select Zip File")
        if zip_file:
            subprocess.run(f"adb sideload {zip_file}", shell=True)
            messagebox.showinfo("Sideload", "Zip sideload initiated.")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = OdinFlasherApp(root)
    root.mainloop()
