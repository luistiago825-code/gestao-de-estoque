import sys
import sqlite3
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                               QTableWidget, QTableWidgetItem, QTabWidget, 
                               QFormLayout, QMessageBox, QHeaderView)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor

# ==========================================
# CONFIGURAÇÃO DO BANCO DE DADOS (SQLite)
# ==========================================
def inicializar_banco():
    conn = sqlite3.connect("gestao_comercial.db")
    cursor = conn.cursor()
    # Tabela de Produtos (Estoque)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            marca TEXT,
            modelo TEXT,
            armazenamento TEXT,
            ram TEXT,
            preco REAL,
            quantidade INTEGER
        )
    ''')
# ==========================================
# INTERFACE PRINCIPAL (PySide6)
# ==========================================
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gestão - Assistência e Vendas")
        self.resize(900, 600)
        self.aplicar_estilo()

        # Widget Central e Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Cabeçalho
        lbl_titulo = QLabel("Painel de Controle Comercial")
        lbl_titulo.setFont(QFont("Segoe UI", 20, QFont.Bold))
        lbl_titulo.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(lbl_titulo)

        # Criação das Abas
        self.abas = QTabWidget()
        self.abas.setFont(QFont("Segoe UI", 12))
        main_layout.addWidget(self.abas)

        # Adicionando os Módulos às Abas
        self.setup_aba_estoque()
        self.setup_aba_pdv()
        self.setup_aba_clientes()
        self.setup_aba_os()

    def aplicar_estilo(self):
        # Estilo CSS (QSS) para deixar o visual moderno e sério
        self.setStyleSheet("""
            QMainWindow { background-color: #f4f6f9; }
            QLabel { color: #333; }
            QTabWidget::pane { border: 1px solid #ccc; background: white; border-radius: 5px; }
            QTabBar::tab { background: #e0e0e0; padding: 10px 20px; margin-right: 2px; border-top-left-radius: 4px; border-top-right-radius: 4px; }
            QTabBar::tab:selected { background: #2c3e50; color: white; font-weight: bold; }
            QPushButton { background-color: #3498db; color: white; border: none; padding: 8px 15px; border-radius: 4px; font-weight: bold; }
            QPushButton:hover { background-color: #2980b9; }
            QLineEdit { padding: 6px; border: 1px solid #ccc; border-radius: 4px; }
            QTableWidget { gridline-color: #ddd; border: none; }
            QHeaderView::section { background-color: #2c3e50; color: white; padding: 5px; font-weight: bold; }
        """)

    # ------------------------------------------
    # MÓDULO 1: ESTOQUE (Funcional)
    # ------------------------------------------
    def setup_aba_estoque(self):
        aba_estoque = QWidget()
        layout_estoque = QVBoxLayout(aba_estoque)

        # Formulário de Cadastro
        form_layout = QFormLayout()
        self.input_marca = QLineEdit()
        self.input_modelo = QLineEdit()
        self.input_armazenamento = QLineEdit()
        self.input_ram = QLineEdit()
        self.input_preco = QLineEdit()
        self.input_qtd = QLineEdit()

        form_layout.addRow("Marca:", self.input_marca)
        form_layout.addRow("Modelo:", self.input_modelo)
        form_layout.addRow("Armazenamento (GB):", self.input_armazenamento)
        form_layout.addRow("RAM (GB):", self.input_ram)
        form_layout.addRow("Preço (R$):", self.input_preco)
        form_layout.addRow("Quantidade:", self.input_qtd)

        btn_salvar = QPushButton("Cadastrar Produto")
        btn_salvar.clicked.connect(self.salvar_produto)

        layout_estoque.addLayout(form_layout)
        layout_estoque.addWidget(btn_salvar)

        # Tabela de Visualização
        self.tabela_estoque = QTableWidget()
        self.tabela_estoque.setColumnCount(7)
        self.tabela_estoque.setHorizontalHeaderLabels(["ID", "Marca", "Modelo", "Armaz.", "RAM", "Preço", "Qtd"])
        self.tabela_estoque.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout_estoque.addWidget(self.tabela_estoque)

        self.abas.addTab(aba_estoque, "Gerenciamento de Estoque")
        self.carregar_produtos() # Carrega os dados iniciais do banco

    def salvar_produto(self):
        marca = self.input_marca.text()
        modelo = self.input_modelo.text()
        armaz = self.input_armazenamento.text()
        ram = self.input_ram.text()
        try:
            preco = float(self.input_preco.text().replace(',', '.'))
            qtd = int(self.input_qtd.text())
        except ValueError:
            QMessageBox.warning(self, "Erro", "Preço e Quantidade devem ser números válidos.")
            return

        if not marca or not modelo:
            QMessageBox.warning(self, "Erro", "Marca e Modelo são obrigatórios.")
            return

        conn = sqlite3.connect("gestao_comercial.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (marca, modelo, armazenamento, ram, preco, quantidade) VALUES (?, ?, ?, ?, ?, ?)",
                       (marca, modelo, armaz, ram, preco, qtd))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Sucesso", "Produto cadastrado no estoque!")
        
        # Limpa os campos
        for input_field in [self.input_marca, self.input_modelo, self.input_armazenamento, self.input_ram, self.input_preco, self.input_qtd]:
            input_field.clear()
            
        self.carregar_produtos()

    def carregar_produtos(self):
        conn = sqlite3.connect("gestao_de_estoque.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        conn.close()

        self.tabela_estoque.setRowCount(0)
        for row_number, row_data in enumerate(produtos):
            self.tabela_estoque.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled) # Somente leitura
                self.tabela_estoque.setItem(row_number, column_number, item)

# ==========================================
# EXECUÇÃO DO APLICATIVO
# ==========================================
if __name__ == "__main__":
    # 1. Inicializa o banco de dados e as tabelas
    inicializar_banco()
    
    # 2. Roda a interface gráfica
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())