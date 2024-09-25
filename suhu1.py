import streamlit as st

# Input suhu dan satuan
x = st.number_input("Masukkan suhu")
sx = st.text_input("Satuan asal (c/f/k)", "c").lower()
st.write("Anda menginput suhu ", x, " dengan satuan ", sx)
sy = st.text_input("Konversi ke satuan (c/f/k)", "c").lower()

# Fungsi konversi suhu
def convert_temperature(temp, from_unit, to_unit):
    if from_unit == to_unit:
        return temp
    if from_unit == "c":
        if to_unit == "f":
            return (temp * 9/5) + 32
        elif to_unit == "k":
            return temp + 273.15
    elif from_unit == "f":
        if to_unit == "c":
            return (temp - 32) * 5/9
        elif to_unit == "k":
            return (temp - 32) * 5/9 + 273.15
    elif from_unit == "k":
        if to_unit == "c":
            return temp - 273.15
        elif to_unit == "f":
            return (temp - 273.15) * 9/5 + 32
    return None

# Konversi suhu
hasil = convert_temperature(x, sx, sy)

# Tampilkan hasil konversi
if hasil is not None:
    st.write(f"Hasil konversi dari {x} {sx.upper()} adalah {hasil:.2f} {sy.upper()}")
else:
    st.write("Satuan tidak valid.")
