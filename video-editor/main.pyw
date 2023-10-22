import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np

class VideoEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Editor")
        self.video_path = ""
        self.cap = None
        self.playing = False

        self.viewer_width = 640
        self.viewer_height = 480

        self.canvas = tk.Canvas(self.root, width=self.viewer_width, height=self.viewer_height)
        self.canvas.pack()

        self.load_button = tk.Button(self.root, text="Load Video", command=self.load_video)
        self.load_button.pack()

        self.play_pause_button = tk.Button(self.root, text="Play", command=self.toggle_play_pause)
        self.play_pause_button.pack()

        self.seek_scale = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, label="Seek")
        self.seek_scale.pack()

        self.seek_scale.bind("<ButtonRelease-1>", self.seek)

    def load_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
        if file_path:
            self.video_path = file_path
            self.cap = cv2.VideoCapture(self.video_path)
            self.seek_scale.config(to=self.cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1)
            self.play_video()

    def play_video(self):
        if self.cap:
            self.playing = True
            self.play_pause_button.config(text="Pause")
            self.play_frame()

    def pause_video(self):
        self.playing = False
        self.play_pause_button.config(text="Play")

    def toggle_play_pause(self):
        if self.playing:
            self.pause_video()
        else:
            self.play_video()

    def seek(self, event):
        if self.cap:
            frame_number = int(self.seek_scale.get())
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    def play_frame(self):
        if self.playing and self.cap:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, _ = frame.shape
                aspect_ratio = w / h
                
                if w > h:
                    new_w = self.viewer_width
                    new_h = int(self.viewer_width / aspect_ratio)
                else:
                    new_h = self.viewer_height
                    new_w = int(self.viewer_height * aspect_ratio)

                resized_frame = cv2.resize(frame, (new_w, new_h))

                self.photo = tk.PhotoImage(data=cv2.imencode('.png', resized_frame)[1].tobytes())
                self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
                self.root.after(10, self.play_frame)
            else:
                self.playing = False
                self.play_pause_button.config(text="Play")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoEditorApp(root)
    root.mainloop()
