# simpan file ini sebagai semangat.py
import streamlit as st

# Judul elegan
st.title("Pesan Semangat untuk Kamu")

# Masukkan nama teman
nama = st.text_input("Masukkan nama kamu disini:")

# Tombol untuk menampilkan pesan
if st.button("Dapatkan Pesan Semangat"):
    if nama:
        st.success(f"Halo {nama}, tetap percaya diri dan semangat buat menjalani hari yang tidak mudah ini!")
    else:
        st.warning("Masukkan nama kamu disini 🙂")
