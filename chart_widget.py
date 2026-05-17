import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QWidget, QVBoxLayout

class MatplotlibWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.figure, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(6, 8))
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

    def update_charts(self, df):
        self.ax1.clear()
        self.ax2.clear()

        if not df.empty:
            sales_by_product = df.groupby('Product line')['Sales'].sum()
            self.ax1.bar(sales_by_product.index, sales_by_product.values, color='#4CAF50')
            self.ax1.set_title('Total Penjualan per Kategori', fontsize=12, fontweight='bold', pad=10)
            self.ax1.set_ylabel('Total ($)', fontsize=10)
            
            self.ax1.tick_params(axis='x', rotation=35, labelsize=9) 

            qty_by_product = df.groupby('Product line')['Quantity'].sum()
            self.ax2.pie(qty_by_product.values, labels=qty_by_product.index, 
                         autopct='%1.1f%%', startangle=90, 
                         textprops={'fontsize': 9}) 
            self.ax2.set_title('Proporsi Kuantitas Terjual', fontsize=12, fontweight='bold', pad=10)

        self.figure.tight_layout(pad=2.0, h_pad=3.0) 
        self.canvas.draw()

    def export_to_png(self):
        self.figure.savefig('dashboard_charts.png', dpi=300)