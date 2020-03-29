""" Modul untuk menghitung GLB

Modul ini berfungsi untuk menghitung beberapa parameter dalam gerak lurus beraturan
"""

def glb_v(x, t):
    """
    Mengembalikan nilai kecepatan v dari gerak lurus beraturan dengan jarak x dan waktu t
    """
    return (x/t)

def glb_x(v, t):
    """
    Mengembalikan nilai kecepatan v dari gerak lurus beraturan dengan jarak x dan waktu t
    """
    return (v*t)

def glb_t(v, x):
    """
    Mengembalikan nilai kecepatan v dari gerak lurus beraturan dengan jarak x dan waktu t
    """
    return (x/v)
