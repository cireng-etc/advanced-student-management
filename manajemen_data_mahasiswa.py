import tkinter as tk
from tkinter import messagebox, filedialog
import re
import csv
import openpyxl

# Class Mahasiswa
class Mahasiswa:
    def __init__(self, nim, nama, jurusan, email):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.email = email

    def __str__(self):
        return f"{self.nim} - {self.nama} - {self.jurusan} - {self.email}"

# Class DataManager untuk mengelola data mahasiswa
class DataManager:
    def __init__(self):
        self.mahasiswa_list = []

    # Tambahkan mahasiswa
    def add_mahasiswa(...