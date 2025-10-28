import tkinter as tk
from tkinter import messagebox
import ast
import operator

# Évaluateur sûr pour +, -, *, /, parenthèses et nombres
_ops = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

def _safe_eval(node):
    if isinstance(node, ast.Expression):
        return _safe_eval(node.body)
    elif isinstance(node, ast.BinOp) and type(node.op) in _ops:
        left = _safe_eval(node.left)
        right = _safe_eval(node.right)
        return _ops[type(node.op)](left, right)
    elif isinstance(node, ast.UnaryOp) and type(node.op) in _ops:
        operand = _safe_eval(node.operand)
        return _ops[type(node.op)](operand)
    elif isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    elif isinstance(node, ast.Num):  # compat ancien Python
        return node.n
    elif isinstance(node, ast.Call) or isinstance(node, ast.Name):
        raise ValueError("Fonctions et variables interdites.")
    elif isinstance(node, ast.Subscript) or isinstance(node, ast.Attribute):
        raise ValueError("Syntaxe non autorisée.")
    elif isinstance(node, ast.Paren) or isinstance(node, ast.Tuple) or isinstance(node, ast.List):
        raise ValueError("Collections non autorisées.")
    else:
        raise ValueError("Expression non prise en charge.")

def eval_safe_expr(expr: str) -> float:
    # Remplacements visuels × ÷ → * /
    expr = expr.replace("×", "*").replace("÷", "/")
    # Autoriser uniquement chiffres, opérateurs de base, points et parenthèses
    allowed = "0123456789+-*/.() "
    if any(ch not in allowed for ch in expr):
        raise ValueError("Caractère non autorisé.")
    # Parser puis évaluer
    tree = ast.parse(expr, mode="eval")
    return _safe_eval(tree)

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculatrice")
        self.root.resizable(False, False)
        self.expr_var = tk.StringVar(value="")

        # Affichage
        self.entry = tk.Entry(root, textvariable=self.expr_var, font=("Arial", 18), justify="right", bd=8, relief="groove")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=8, pady=8)
        self.entry.focus_set()

        # Grille responsive
        for r in range(1, 6):
            root.rowconfigure(r, weight=1, minsize=60)
        for c in range(4):
            root.columnconfigure(c, weight=1, minsize=60)

        # Boutons
        buttons = [
            ("C",  1, 0), ("(",  1, 1), (")",  1, 2), ("Del", 1, 3),
            ("7",  2, 0), ("8",  2, 1), ("9",  2, 2), ("÷",   2, 3),
            ("4",  3, 0), ("5",  3, 1), ("6",  3, 2), ("×",   3, 3),
            ("1",  4, 0), ("2",  4, 1), ("3",  4, 2), ("-",   4, 3),
            ("0",  5, 0), (".",  5, 1), ("=",  5, 2), ("+",   5, 3),
        ]

        for (txt, r, c) in buttons:
            cmd = (lambda t=txt: self.on_press(t))
            btn = tk.Button(root, text=txt, command=cmd, font=("Arial", 14), bd=4)
            btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

        # Raccourcis clavier
        root.bind("<Return>", lambda e: self.on_press("="))
        root.bind("<KP_Enter>", lambda e: self.on_press("="))
        root.bind("<Escape>", lambda e: self.clear_all())
        root.bind("<BackSpace>", lambda e: self.delete_last())
        # Entrée directe clavier : on laisse Tkinter gérer, mais on garde l’affichage cohérent
        for key in "0123456789+-*/().":
            root.bind(key, self._insert_char)

    def _insert_char(self, event):
        # Insère le caractère dans l’Entry à la position du curseur
        self.entry.insert(tk.INSERT, event.char)
        return "break"

    def on_press(self, key: str):
        if key == "C":
            self.clear_all()
        elif key == "Del":
            self.delete_last()
        elif key == "=":
            self.calculate()
        else:
            # Append du symbole
            self.entry.insert(tk.INSERT, key)

    def clear_all(self):
        self.expr_var.set("")

    def delete_last(self):
        cur = self.expr_var.get()
        if cur:
            self.expr_var.set(cur[:-1])

    def calculate(self):
        expr = self.expr_var.get().strip()
        if not expr:
            return
        try:
            result = eval_safe_expr(expr)
            # Afficher résultat et permettre de continuer à calculer
            self.expr_var.set(str(result))
            # Mettre le curseur à la fin
            self.entry.icursor(tk.END)
        except ZeroDivisionError:
            messagebox.showwarning("Attention", "Division par zéro.")
        except Exception as e:
            messagebox.showwarning("Attention", f"Expression invalide.\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()