
class CalculadoraHorasExtras ( ):
    """Calculadora para sacar horas extras"""
    def __init__(self, salario_base, horas_laboradas, porcentaje=1):
        self.salario_base = salario_base
        self.porcentaje = porcentaje
        self.horas_laboradas = horas_laboradas
    
    def valor_hora_diurna_ordinaria(self):
        """Calculo de 1 hora diurna ordinaria"""
        hora_diurna_ordinaria = self.salario_base/self.horas_laboradas
        return round(hora_diurna_ordinaria, 2)
    
    def valor_con_porcentaje(self):
        """calculo 1 hora extra diurna"""
        hora_extra = float(self.valor_hora_diurna_ordinaria())*self.porcentaje
        return round(hora_extra, 2)
    
    
class CalculadoraHorasExtasColombia(CalculadoraHorasExtras):
    
    def __init__(self, salario_base, horas_laboradas, porcentaje=1):
        super().__init__(salario_base, horas_laboradas, porcentaje)
    
    def valor_hora_ordinaria_diurna (self):
        """Muestra el valor de la hora ordinaria"""
        print(f"valor hora ordinaria diurna: {self.valor_hora_diurna_ordinaria()}")
    
    def valor_hora_ordinaria_nocturna (self):
        """calcula el valor de la hora extra diurna en colombia"""
        self.porcentaje = 0.25
        hora_ordinaria_nocturna = self.valor_hora_diurna_ordinaria()+(self.valor_hora_diurna_ordinaria()*0.35)
        print(f"valor hora ordinaria nocturna {round(hora_ordinaria_nocturna, 2)}")
    
    def valor_hora_extra_diurna (self):
        """calcula el valor de la hora extra diurna en colombia"""
        self.porcentaje = 0.25
        hora_extra_diurna = self.valor_hora_diurna_ordinaria()+self.valor_con_porcentaje()
        print(f"valor hora extra diurna {round(hora_extra_diurna, 2)}")
        
    def valor_hora_extra_nocturna (self):
        """calcula el valor de la hora extra nocturna en colombia"""
        self.porcentaje = 0.75
        hora_extra_nocturna = self.valor_con_porcentaje()+self.valor_hora_diurna_ordinaria()
        print(f"valor hora extra nocturna {round(hora_extra_nocturna, 2)}")
    
    def valor_hora_extra_diurna_dominical_festiva (self):
        """calcula el valor de la hora extra diurna_dominical en colombia"""
        self.porcentaje = 1.00
        hora_extra_diurna_dominical = self.valor_con_porcentaje()+self.valor_hora_diurna_ordinaria()
        print(f"valor hora extra dominical/Festiva diurna {round(hora_extra_diurna_dominical, 2)}")
        
    def valor_hora_extra_nocturna_dominical_festiva (self):
        """calcula el valor de la hora extra diurna_dominical en colombia"""
        self.porcentaje = 1.50
        hora_extra_diurna_dominical = self.valor_con_porcentaje()+self.valor_hora_diurna_ordinaria()
        print(f"valor hora extra dominical/Festiva nocturna {round(hora_extra_diurna_dominical, 2)}")
    

