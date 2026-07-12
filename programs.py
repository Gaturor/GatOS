import calc

class Program:
    program_list = []

    def __init__(self, name, logo, version, launch_prog):
        self.name = name
        self.logo = logo
        self.version = version
        self.launch_prog = launch_prog
        self.program_list.append(name)
    def show_logo(self):
        print(f"{self.logo}")
    def launch(self):
        self.launch_prog()
    def show_all_programs(self):
        print(self.program_list) 

# Программы:
calcul = Program("Калькулятор","test","V0.12", calc.calc)