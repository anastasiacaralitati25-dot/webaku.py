import streamlit as st
st.sidebar.title(" Navigasi")
menu = st.sidebar.selectbox("Pilih Halaman:", ["Profil Singkat", "Hubungi Saya"])
if menu == "Profil Singkat":
    st.title("Web Biodata Saya")
    st.write("Selamat datang di website profil saya!")
    # --- Kode untuk menampilkan foto profil ---
    # tamppilan foto profil
    st.image("foto_profil.jpeg", width=250)

    st.divider()

    # Membuat sub-judul
    st.header(" Profil Singkat")
    
    # Menampilkan informasi biodata
    st.write("**Nama Lengkap:** Anastasia Chalarita Lodang")
    st.write("**Jurusan:** Teknik Informatika")
    st.write("**Universitas:** Universitas Nusa Putra")

    st.divider()
elif menu == "Hubungi Saya":
    st.header("Hubungi Saya")
    kolom1, kolom2 = st.columns(2)

    with kolom1:
        st.write("*Email:* anastasia.caralita_ti25@nusaputra.ac.id")
    with kolom2:
        st.write("*GitHub:* github.com/anastasiacaralita")

    #st.title("Hubungi Saya")
    st.divider()

    st.subheader("Kirim pesan interaktif")
    nama = st.text_input("nama anda:")
    pesan = st.text_area("pesan anda")

    if st.button("kirim pesan"):
        if nama and pesan:
            st.success(f"Terkirim! Terima kasih {nama}, pesan anda berhasil diproses")
        else:
            st.warning("mohon isi nama dan pesan anda terlebih dahulu ya besti!")


