
import tkinter as tk
from tkinter import ttk, messagebox
import math

class FinanceCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Financeira")
        self.root.geometry("600x400")
        
        # Criar notebook para abas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=5)
        
        # Aba de Juros Compostos
        self.compound_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.compound_frame, text='Juros Compostos')
        self.setup_compound_interest()
        
        # Aba de Investimentos
        self.investment_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.investment_frame, text='Investimentos')
        self.setup_investment()
        
        # Aba de Empréstimos
        self.loan_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.loan_frame, text='Empréstimos')
        self.setup_loan()

    def setup_compound_interest(self):
        # Campos para juros compostos
        ttk.Label(self.compound_frame, text="Principal (R$):").grid(row=0, column=0, padx=5, pady=5)
        self.principal = ttk.Entry(self.compound_frame)
        self.principal.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.compound_frame, text="Taxa de Juros (%):").grid(row=1, column=0, padx=5, pady=5)
        self.rate = ttk.Entry(self.compound_frame)
        self.rate.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self.compound_frame, text="Tempo (anos):").grid(row=2, column=0, padx=5, pady=5)
        self.time = ttk.Entry(self.compound_frame)
        self.time.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(self.compound_frame, text="Calcular", 
                  command=self.calculate_compound).grid(row=3, column=0, columnspan=2, pady=20)
        
        self.compound_result = ttk.Label(self.compound_frame, text="")
        self.compound_result.grid(row=4, column=0, columnspan=2)

    def setup_investment(self):
        ttk.Label(self.investment_frame, text="Investimento Mensal (R$):").grid(row=0, column=0, padx=5, pady=5)
        self.monthly_invest = ttk.Entry(self.investment_frame)
        self.monthly_invest.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.investment_frame, text="Taxa de Retorno Anual (%):").grid(row=1, column=0, padx=5, pady=5)
        self.return_rate = ttk.Entry(self.investment_frame)
        self.return_rate.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self.investment_frame, text="Período (anos):").grid(row=2, column=0, padx=5, pady=5)
        self.invest_period = ttk.Entry(self.investment_frame)
        self.invest_period.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(self.investment_frame, text="Calcular", 
                  command=self.calculate_investment).grid(row=3, column=0, columnspan=2, pady=20)
        
        self.investment_result = ttk.Label(self.investment_frame, text="")
        self.investment_result.grid(row=4, column=0, columnspan=2)

    def setup_loan(self):
        ttk.Label(self.loan_frame, text="Valor do Empréstimo (R$):").grid(row=0, column=0, padx=5, pady=5)
        self.loan_amount = ttk.Entry(self.loan_frame)
        self.loan_amount.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.loan_frame, text="Taxa de Juros Anual (%):").grid(row=1, column=0, padx=5, pady=5)
        self.loan_rate = ttk.Entry(self.loan_frame)
        self.loan_rate.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self.loan_frame, text="Prazo (meses):").grid(row=2, column=0, padx=5, pady=5)
        self.loan_term = ttk.Entry(self.loan_frame)
        self.loan_term.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(self.loan_frame, text="Calcular", 
                  command=self.calculate_loan).grid(row=3, column=0, columnspan=2, pady=20)
        
        self.loan_result = ttk.Label(self.loan_frame, text="")
        self.loan_result.grid(row=4, column=0, columnspan=2)

    def calculate_compound(self):
        try:
            p = float(self.principal.get())
            r = float(self.rate.get()) / 100
            t = float(self.time.get())
            
            amount = p * (1 + r) ** t
            interest = amount - p
            
            result = f"Montante Final: R${amount:.2f}\n"
            result += f"Juros Ganhos: R${interest:.2f}"
            self.compound_result.config(text=result)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def calculate_investment(self):
        try:
            pmt = float(self.monthly_invest.get())
            r = float(self.return_rate.get()) / 100 / 12
            t = float(self.invest_period.get()) * 12
            
            fv = pmt * ((1 + r)**t - 1) / r
            total_invested = pmt * t
            gains = fv - total_invested
            
            result = f"Valor Final: R${fv:.2f}\n"
            result += f"Total Investido: R${total_invested:.2f}\n"
            result += f"Rendimento: R${gains:.2f}"
            self.investment_result.config(text=result)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def calculate_loan(self):
        try:
            pv = float(self.loan_amount.get())
            r = float(self.loan_rate.get()) / 100 / 12
            n = float(self.loan_term.get())
            
            pmt = pv * (r * (1 + r)**n) / ((1 + r)**n - 1)
            total = pmt * n
            interest = total - pv
            
            result = f"Parcela Mensal: R${pmt:.2f}\n"
            result += f"Total a Pagar: R${total:.2f}\n"
            result += f"Total de Juros: R${interest:.2f}"
            self.loan_result.config(text=result)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

def main():
    root = tk.Tk()
    app = FinanceCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
