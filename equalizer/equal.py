import tkinter as tk
import tkinter.filedialog as filedialog
import pygame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        # Add Track Information Frame
        track_frame = tk.Frame(self.root)
        track_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.track_name = tk.Label(track_frame, text="No track selected")
        self.track_name.pack(side=tk.LEFT)
        load_button = tk.Button(track_frame, text="Load", command=self.load_music)
        load_button.pack(side=tk.RIGHT)

        # Add Control Frame
        control_frame = tk.Frame(self.root)
        control_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        play_button = tk.Button(control_frame, text="Play", command=self.play_music)
        play_button.grid(row=0, column=0, padx=5)
        stop_button = tk.Button(control_frame, text="Stop", command=self.stop_music)
        stop_button.grid(row=0, column=1, padx=5)

        # Add Volume Frame
        volume_frame = tk.Frame(self.root)
        volume_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        tk.Label(volume_frame, text="Volume").pack(side=tk.LEFT)
        self.volume = tk.Scale(volume_frame, from_=0, to=1, orient=tk.HORIZONTAL, resolution=0.01)
        self.volume.set(0.5)
        self.volume.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.volume.bind("<ButtonRelease-1>", self.set_volume)

        # Add Equalizer Frame
        equalizer_frame = tk.Frame(self.root)
        equalizer_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        tk.Label(equalizer_frame, text="Bass").grid(row=0, column=0, sticky=tk.W)
        self.bass = tk.Scale(equalizer_frame, from_=-10, to=10, orient=tk.HORIZONTAL, resolution=0.1)
        self.bass.set(0)
        self.bass.grid(row=0, column=1)
        self.bass.bind("<ButtonRelease-1>", self.set_equalizer)
        tk.Label(equalizer_frame, text="Mid").grid(row=1, column=0, sticky=tk.W)
        self.mid = tk.Scale(equalizer_frame, from_=-10, to=10, orient=tk.HORIZONTAL, resolution=0.1)
        self.mid.set(0)
        self.mid.grid(row=1, column=1)
        self.mid.bind("<ButtonRelease-1>", self.set_equalizer)
        tk.Label(equalizer_frame, text="Treble").grid(row=2, column=0, sticky=tk.W)
        self.treble = tk.Scale(equalizer_frame, from_=-10, to=10, orient=tk.HORIZONTAL, resolution=0.1)
        self.treble.set(0)
        self.treble.grid(row=2, column=1)
        self.treble.bind("<ButtonRelease-1>", self.set_equalizer)

        # Add Spectrum Visualization Frame
        spectrum_frame = tk.Frame(self.root)
        spectrum_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5, expand=True)
        self.spectrum_figure = plt.Figure(figsize=(5,5), dpi=100)
        self.spectrum_plot = self.spectrum_figure.add_subplot(111)
        self.spectrum_canvas = FigureCanvasTkAgg(self.spectrum_figure, master=spectrum_frame)
        self.spectrum_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.spectrum_canvas.draw()

        # Set up Pygame Mixer
        pygame.mixer.init()

    def load_music(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg")])
        pygame.mixer.music.load( file_path)
        self.track_name.config(text=file_path)

    def play_music(self):
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def set_volume(self, event):
        volume = self.volume.get()
        pygame.mixer.music.set_volume(volume)

    def set_equalizer(self, event):
        bass = self.bass.get()
        mid = self.mid.get()
        treble = self.treble.get()
        # Apply equalizer effect to audio
        # Implementation of equalizer effect left as an exercise to the reader

    def update_spectrum(self):
        # Get audio data and update spectrum visualization
        # Implementation of audio data extraction and visualization left as an exercise to the reader
        self.spectrum_canvas.draw()
        self.root.after(50, self.update_spectrum)

    def run(self):
        self.root.after(50, self.update_spectrum)
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    player.run()




