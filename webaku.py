import streamlit as st
import pandas as pd

st.set_page_config(page_title="Biodata Anastasia", layout="wide")

st.title("Web Biodata Profesional")

# 1. Menggunakan Layout Columns
col1, col2 = st.columns([1, 2])

with col1:
    # Asumsikan foto sudah di-upload di GitHub
    st.image("foto_profil.jpeg", caption="Anastasia Chalarita Lodang", width=250)

with col2:
    st.header("Profil Singkat")
    st.write("Mahasiswa Teknik Informatika yang tertarik pada pengembangan web dan algoritma.")
    st.info("Saat ini sedang mendalami Python dan Streamlit.")

st.divider()

# 2. Menggunakan Looping untuk Daftar Keahlian
st.subheader("Keahlian Pemrograman")
# 2. Struktur Data & Looping (Menunjukkan kemampuan logika)
st.subheader("Peta Pembelajaran Saya")
skills = {
    "Python": 70,      # Sedang dalam proses belajar intensif
    "HTML/CSS": 40,    # Dasar-dasar web
    "Java": 30,        # Baru mulai mengenal
    "SQL": 20          # Dasar basis data
}

# Menampilkan dengan Progress Bar
for skill, level in skills.items():
    st.write(f"*{skill}*")
    st.progress(level / 100)

# Menampilkan dengan Progress Bar (Looping)
for skill, level in skills.items():
    st.write(f"*{skill}*")
    st.progress(level / 100)

# 3. Menambahkan Visualisasi Data (Grafik)
st.subheader("Statistik Penguasaan Skill")
chart_data = pd.DataFrame.from_dict(skills, orient='index', columns=['Persentase'])
st.bar_chart(chart_data)

# 4. Form Kontak (Interaktivitas)
st.divider()
st.subheader("Hubungi Saya")
with st.form("contact_form"):
    email = st.text_input("Email Anda")
    pesan = st.text_area("Pesan untuk saya")
    submit = st.form_submit_button("Kirim")
    if submit:
        st.success(f"Terima kasih {email}, pesan telah diterima!")