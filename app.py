import streamlit as st

# Main Title
st.markdown(
    "<h1 style='color: #CF9FFF;'>🔄 Advanced Unit Converter</h1>",
    unsafe_allow_html=True
)

# Sidebar for Selecting Unit Type
unit_type = st.sidebar.radio("Select Conversion Type:", ["Length Converter", "Weight Converter"])

# Length Converter
if unit_type == "Length Converter":
    st.markdown("<h2 style='color: #FFA500;'>📏 Length Converter</h2>", unsafe_allow_html=True)

    length_units = {
        "Kilometre": 1000,
        "Metre": 1,
        "Centimetre": 0.01,
        "Millimetre": 0.001,
        "Micrometre": 0.000001,
        "Nanometre": 0.000000001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
        "Nautical Mile": 1852
    }

    amount = st.number_input("Enter length:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From (Length):", list(length_units.keys()))
    to_unit = st.selectbox("To (Length):", list(length_units.keys()))

    if st.button("Convert Length"):
        result = amount * (length_units[to_unit] / length_units[from_unit])
        st.success(f"{amount} {from_unit} = {result:.4f} {to_unit}")

# Weight Converter
elif unit_type == "Weight Converter":
    st.markdown("<h2 style='color: #FF5733;'>⚖️ Weight Converter</h2>", unsafe_allow_html=True)

    weight_units = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    }

    amount = st.number_input("Enter weight:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From (Weight):", list(weight_units.keys()))
    to_unit = st.selectbox("To (Weight):", list(weight_units.keys()))

    if st.button("Convert Weight"):
        result = amount * (weight_units[to_unit] / weight_units[from_unit])
        st.success(f"{amount} {from_unit} = {result:.4f} {to_unit}")
