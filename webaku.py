import streamlit as st
import pandas as pd

st.set_page_config(page_title="Biodata Anastasia", layout="wide")

st.title("Web Biodata Profesional")

# 1. Menggunakan Layout Columns
col1, col2 = st.columns([1, 2])

with col1:
    st.image("foto_profil.jpeg", caption="Anastasia Chalarita Lodang", width=250)

with col2:
    st.header("Profil Singkat")
    st.write("Mahasiswa Teknik Informatika yang tertarik pada pengembangan web dan algoritma.")
    st.info("Saat ini sedang mendalami Python dan Streamlit.")

st.divider()

# 2. Struktur Data & Looping
st.subheader("Peta Pembelajaran Saya")
skills = {
    "Python": 70,
    "HTML/CSS": 40,
    "Java": 30,
    "SQL": 20
}

for skill, level in skills.items():
    st.write(f"*{skill}*")
    st.progress(level / 100)

# 3. Visualisasi Data
st.subheader("Statistik Penguasaan Skill")
chart_data = pd.DataFrame.from_dict(skills, orient='index', columns=['Persentase'])
st.bar_chart(chart_data)

st.divider()
st.subheader("Hubungi Saya")
st.write("Silakan hubungi saya melalui:")
st.write("- *Email:* [Masukkan email kamu di sini]")
st.write("- *GitHub:* [github.com/anastasiacaralitati25-dot](https://github.com/anastasiacaralitati25-dot)")

