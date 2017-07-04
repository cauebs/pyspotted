import tkinter as tk
from tkinter import filedialog, messagebox
from threading import Thread
from os import path


class Application(tk.Frame):
    def __init__(self):
        super().__init__()
        self.master.title('Spotted UFSC')
        self.master.resizable(width=False, height=False)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        padding = {'padx': 5, 'pady': 10}
        sticky = {'sticky': tk.W + tk.E + tk.N + tk.S}
        style = {**padding, **sticky}

        self.input_field = tk.Entry(self)
        self.input_field.grid(row=0, column=0, columnspan=2, **style)

        self.input_button = tk.Button(self)
        self.input_button['text'] = 'Selecionar arquivo de entrada'
        self.input_button['command'] = self.select_input
        self.input_button.grid(row=0, column=2, **style)

        self.output_field = tk.Entry(self)
        self.output_field.grid(row=1, column=0, columnspan=2, **style)

        self.output_button = tk.Button(self)
        self.output_button['text'] = 'Selecionar diretório de saída'
        self.output_button['command'] = self.select_output
        self.output_button.grid(row=1, column=2, **style)

        self.label_starting_id = tk.Label(self, text='Número inicial:')
        self.label_starting_id.grid(row=2, column=0, **style)

        self.starting_id = tk.Entry(self)
        self.starting_id.grid(row=2, column=1, **style)

        self.start_button = tk.Button(self)
        self.start_button['text'] = 'Iniciar'
        self.start_button['command'] = self.start
        self.start_button.grid(row=2, column=2, columnspan=3, **style)

    def select_input(self):
        file_types = [('Arquivos do Microsoft Office Excel', '*.xlsx'),
                      ('Arquivos do Microsoft Office Excel', '*.xls'),
                      ('Valores separados por vírgula', '*.csv')]
        file_path = filedialog.askopenfilename(filetypes=file_types)

        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, file_path)

    def select_output(self):
        dir_path = filedialog.askdirectory()
        self.output_field.delete(0, tk.END)
        self.output_field.insert(0, dir_path)

    def check_fields(self):
        if not path.isfile(self.input_field.get()):
            raise Exception('O arquivo de entrada é inválido!')

        elif not path.isdir(self.output_field.get()):
            raise Exception('O diretório de saída é inválido!')

        elif not self.starting_id.get().isdigit():
            raise Exception('O número inicial é inválido!')

    def disable_fields(self):
        self.input_button.config(state='disabled')
        self.input_field.config(state='disabled')
        self.output_button.config(state='disabled')
        self.output_field.config(state='disabled')
        self.starting_id.config(state='disabled')
        self.start_button.config(state='disabled')

    def enable_fields(self):
        self.input_button.config(state='normal')
        self.input_field.config(state='normal')
        self.output_button.config(state='normal')
        self.output_field.config(state='normal')
        self.starting_id.config(state='normal')
        self.start_button.config(state='normal')

    def start(self):
        thread = Thread(target=self.generate_images)
        thread.start()

    def generate_images(self):
        try:
            self.disable_fields()
            self.check_fields()
            # do something

        except Exception as e:
            messagebox.showerror('Erro!', str(e))

        else:
            messagebox.showinfo('Processamento finalizado!',
                                'As imagens já estão disponíveis na pasta.')

        finally:
            self.enable_fields()


if __name__ == '__main__':
    Application().mainloop()
