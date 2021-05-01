import threading
import tkinter as tk

class AppWindow:
    def __init__(self, master):
        self.w = master

        self.w.title('Sample Systray')
        self.w.rowconfigure(0, weight=1)
        self.w.columnconfigure(0, weight=1)

        frame = tk.Frame(self.w, name="sample_systray")
        frame.grid(sticky=tk.NSEW)
        frame.columnconfigure(1, weight=1)

        self.thing_label = tk.Label(frame)
        self.thing_label.grid(row=1, column=0, sticky=tk.W)
        self.thing_label['text'] = 'We have a systray! And some more text to make the window a bit bigger.'

        self.w.protocol("WM_DELETE_WINDOW", self.onexit)

        # System Tray icon
        from infi.systray import SysTrayIcon

        def open_window(systray) -> None:
            self.w.deiconify()

        menu_options = (('Open', None, open_window),)
        self.systray = SysTrayIcon(None, "Sample Systray", menu_options, on_quit=self.exit_tray)
        self.systray.start()

    def exit_tray(self, systray) -> None:
        exit_thread = threading.Thread(target=self.onexit)
        exit_thread.setDaemon(True)
        exit_thread.start()

    def onexit(self, event=None):
        shutdown_thread = threading.Thread(target=self.systray.shutdown)
        shutdown_thread.setDaemon(True)
        shutdown_thread.start()

        self.w.destroy()

    def _destroy(self):
        self.destroy()

def main():
    root = tk.Tk(className='sample_systray')

    app = AppWindow(root)

    root.mainloop()

if __name__ == '__main__':
    main()
