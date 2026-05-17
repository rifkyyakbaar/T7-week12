# Nama  : RIFKY AKBAR UTOMO PUTRA
# NIM   : F1D02310149
# Kelas : D

import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QTableWidget, QTableWidgetItem, QLabel, 
                               QComboBox, QPushButton, QMessageBox, QHeaderView)
from data_loader import DataLoader
from chart_widget import MatplotlibWidget

class DashboardApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Supermarket Sales Dashboard - Tugas 7 Week 12")
        self.resize(1100, 700)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #F4F7F6;
            }
            QTableWidget {
                background-color: white;
                alternate-background-color: #F8F9F9;
                border: 1px solid #E0E0E0;
                border-radius: 8px;
                gridline-color: #EEEEEE;
                selection-background-color: #4CAF50;
            }
            QHeaderView::section {
                background-color: #2C3E50;
                color: white;
                padding: 6px;
                font-weight: bold;
                border: none;
            }
            QPushButton {
                background-color: #3498DB;
                color: white;
                border: none;
                padding: 8px 15px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
            QComboBox {
                padding: 5px;
                border: 1px solid #BDC3C7;
                border-radius: 4px;
                background-color: white;
            }
            QLabel {
                color: #2C3E50;
            }
        """)

        self.data_loader = DataLoader()
        
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.layout = QVBoxLayout(main_widget)

        self.summary_label = QLabel("Loading data...")
        self.summary_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px; background-color: #e0f7fa;")
        self.layout.addWidget(self.summary_label)

        control_layout = QHBoxLayout()
        self.filter_combo = QComboBox()
        self.filter_combo.addItem("All")

        if not self.data_loader.df.empty:
            branches = sorted(self.data_loader.df['Branch'].unique().tolist())
            self.filter_combo.addItems(branches)
        self.filter_combo.currentTextChanged.connect(self.refresh_dashboard)
        
        self.btn_refresh = QPushButton("🔄 Refresh Data")
        self.btn_refresh.clicked.connect(self.refresh_dashboard)
        
        self.btn_export = QPushButton("💾 Export Chart (PNG)")
        self.btn_export.clicked.connect(self.export_chart)

        control_layout.addWidget(QLabel("Filter Cabang (Branch):"))
        control_layout.addWidget(self.filter_combo)
        control_layout.addStretch()
        control_layout.addWidget(self.btn_refresh)
        control_layout.addWidget(self.btn_export)
        self.layout.addLayout(control_layout)

        content_layout = QHBoxLayout()
        self.table = QTableWidget()
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False) 
        content_layout.addWidget(self.table, stretch=1)
        
        self.chart_widget = MatplotlibWidget()
        content_layout.addWidget(self.chart_widget, stretch=1)
        
        self.layout.addLayout(content_layout)
        self.refresh_dashboard()

    def refresh_dashboard(self):
        current_branch = self.filter_combo.currentText()
        df = self.data_loader.get_data(current_branch)

        if df.empty:
            self.summary_label.setText("Data tidak ditemukan! Pastikan file supermarket_sales.csv ada di folder ini.")
            return

        total_sales = df['Sales'].sum()
        total_trx = len(df)
        self.summary_label.setText(f"Cabang: {current_branch} | Total Penjualan: ${total_sales:,.2f} | Total Transaksi: {total_trx}")

        df_display = df.head(50) 
        self.table.clear()
        self.table.setColumnCount(len(df_display.columns))
        self.table.setRowCount(len(df_display))
        self.table.setHorizontalHeaderLabels(df_display.columns)
        
        for row_idx, row in enumerate(df_display.values):
            for col_idx, value in enumerate(row):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        self.chart_widget.update_charts(df)

    def export_chart(self):
        self.chart_widget.export_to_png()
        QMessageBox.information(self, "Sukses", "Chart diexport ke dashboard_charts.png")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DashboardApp()
    window.show()
    sys.exit(app.exec())