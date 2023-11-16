
import customtkinter
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from helper import Equation


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("920x600")
        self.resizable(False, False)

        self.title("Построение графиков")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.initialize_ui()

        self.scale = self.entry.get()


    def initialize_ui(self):
        self.entry_frame = customtkinter.CTkFrame(self)
        self.entry_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.plot_frame = customtkinter.CTkFrame(self, corner_radius=10, width=400, height=420)
        self.plot_frame.grid(row=0, column=1, sticky="e")

        self.entry_label = customtkinter.CTkLabel(
            self.entry_frame, text="Значения", fg_color="#F2E7DE", corner_radius=10
        )
        self.entry_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")


        self.dependancy = customtkinter.CTkLabel(self.entry_frame, text="f(x)=")
        self.dependancy.grid(row=1, column=0, padx=5, pady=(10, 0), sticky="e")

        self.func_entry = customtkinter.CTkEntry(self.entry_frame, placeholder_text="Функция")
        self.func_entry.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="nsw")

        self.entry = customtkinter.CTkEntry(self.entry_frame, placeholder_text="Масштаб")
        self.entry.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="nsw")
        
        self.button = customtkinter.CTkButton(self, text="Построить график", command=self.plot)
        self.button.grid(row=10, column=0, padx=20, pady=20, sticky="swn")


    def _get_entry_data(self, scale: int, func: str):
        if self.scale == "":
            scale = int(self.entry.get())
        else:
            scale = 20
        if not func == "":
            self.eq = Equation(func=func)

        return scale, self.eq.convert()

    def plot(self):
        matplotlib.pyplot.close()
        scale, func = self._get_entry_data(scale=self.entry.get(), func=self.func_entry.get())
        fig, ax = plt.subplots()

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.get_tk_widget().grid(row=0, column=0)

        ax.set_title(f"График функции {self.eq._func}")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        x = np.linspace(-scale, scale, 10000)

        ax.axis([-scale, scale, -scale, scale])
        ax.arrow(-scale, 0, scale * 2, 0)
        ax.arrow(0, -scale, 0, scale * 2)

        ax.plot(x, func(x))
        
        canvas.draw()


if __name__ == "__main__":
    matplotlib.use("TkAgg")
    app = App()
    app.mainloop()
    exit(0)
