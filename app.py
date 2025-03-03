import streamlit as st
import time
import google.generativeai as genai

# Main Title
st.markdown(
    "<h1 style='color: #CF9FFF;'>🔄 Advanced Unit Converter</h1>",
    unsafe_allow_html=True
)

# Sidebar for Selecting Unit Type
unit_type = st.sidebar.radio("Select Conversion Type:", [
    "📏 Length Converter",
    "⚖️ Weight Converter",
    "🌡️ Temperature Converter",
    "💧 Liquid Converter",
    "⏳ Time Converter",
    "📐 Area Converter",
    "🤖 Offline AI Chatbot"
])

# Conversion Dictionaries
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

weight_units = {
    "Kilogram": 1,
    "Gram": 0.001,
    "Pound": 0.453592,
    "Ounce": 0.0283495
}

temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]

liquid_units = {
    "Litre": 1,
    "Millilitre": 0.001,
    "Gallon": 3.78541,
    "Pint": 0.473176,
    "Quart": 0.946353,
    "Cup": 0.24,
    "Fluid Ounce": 0.0295735
}

time_units = {
    "Second": 1,
    "Minute": 60,
    "Hour": 3600,
    "Day": 86400,
    "Month": 2628000,
    "Year": 31536000
}

area_units = {
    "Square Metre": 1,
    "Square Kilometre": 1000000,
    "Square Centimetre": 0.0001,
    "Square Millimetre": 0.000001,
    "Hectare": 10000,
    "Acre": 4046.86
}

# Conversion Logic
if unit_type == "📏 Length Converter":
    st.markdown("<h2 style='color: #FFA500;'>📏 Length Converter</h2>", unsafe_allow_html=True)
    amount = st.number_input("Enter length:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From (Length):", list(length_units.keys()))
    to_unit = st.selectbox("To (Length):", list(length_units.keys()))
    if st.button("Convert Length", key="btn_length", help="Convert Length", args=None, kwargs=None):
        result = amount * (length_units[to_unit] / length_units[from_unit])
        st.success(f"{amount} {from_unit} = {result:.4f} {to_unit}")

elif unit_type == "⚖️ Weight Converter":
    st.markdown("<h2 style='color: #FF5733;'>⚖️ Weight Converter</h2>", unsafe_allow_html=True)
    amount = st.number_input("Enter weight:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From (Weight):", list(weight_units.keys()))
    to_unit = st.selectbox("To (Weight):", list(weight_units.keys()))
    if st.button("Convert Weight", key="btn_weight", help="Convert Weight", args=None, kwargs=None):
        result = amount * (weight_units[to_unit] / weight_units[from_unit])
        st.success(f"{amount} {from_unit} = {result:.4f} {to_unit}")

elif unit_type == "🌡️ Temperature Converter":
    st.markdown("<h2 style='color: #1E90FF;'>🌡️ Temperature Converter</h2>", unsafe_allow_html=True)
    amount = st.number_input("Enter temperature:", format="%.2f")
    from_unit = st.selectbox("From (Temperature):", temperature_units)
    to_unit = st.selectbox("To (Temperature):", temperature_units)
    if st.button("Convert Temperature"):
        if from_unit == to_unit:
            result = amount
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (amount * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = amount + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (amount - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (amount - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = amount - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (amount - 273.15) * 9/5 + 32
        st.success(f"{amount} {from_unit} = {result:.2f} {to_unit}")

elif unit_type == "💧 Liquid Converter":
    st.markdown("<h2 style='color: #00CED1;'>💧 Liquid Converter</h2>", unsafe_allow_html=True)
    amount = st.number_input("Enter volume:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From (Liquid):", list(liquid_units.keys()))
    to_unit = st.selectbox("To (Liquid):", list(liquid_units.keys()))
    if st.button("Convert Liquid"):
        result = amount * (liquid_units[to_unit] / liquid_units[from_unit])
        st.success(f"{amount} {from_unit} = {result:.4f} {to_unit}")

elif unit_type == "📐 Area Converter":
    st.markdown("<h2 style='color: #8A2BE2;'>📐 Area Converter</h2>", unsafe_allow_html=True)
    amount = st.number_input("Enter area:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From (Area):", list(area_units.keys()))
    to_unit = st.selectbox("To (Area):", list(area_units.keys()))
    if st.button("Convert Area"):
        result = amount * (area_units[to_unit] / area_units[from_unit])
        st.success(f"{amount} {from_unit} = {result:.4f} {to_unit}")

elif unit_type == "⏳ Time Converter":
    st.markdown("<h2 style='color: #FFD700;'>⏳ Time Converter</h2>", unsafe_allow_html=True)
    amount = st.number_input("Enter time:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From (Time):", list(time_units.keys()))
    to_unit = st.selectbox("To (Time):", list(time_units.keys()))
    if st.button("Convert Time"):
        result = amount * (time_units[to_unit] / time_units[from_unit])
        st.success(f"{amount} {from_unit} = {result:.4f} {to_unit}")

elif unit_type == "🤖 Offline AI Chatbot":
    genai.configure(api_key="AIzaSyAjMHUKa0kRSCFtoClkY9HlIPd0p9fvjv8")
    model = genai.GenerativeModel("gemini-1.5-pro-latest")

    st.title("🤖 Offline AI Chatbot")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display Chat messages from history on app rerun
    for m in st.session_state.messages:  # Use 'm' instead  of 'message'
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    # React to user input
    prompt = st.chat_input("Ask me anything...")        
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user",   "content": prompt})

        chat_history = [
            {"role": m["role"], "parts": [m["content"]]}    for m in st.session_state.messages
        ]

        response = model.generate_content(chat_history)

        full_response = response.text 

        with st.chat_message("assistant"):
            st.markdown(full_response)

        st.session_state.messages.append({"role":   "assistant", "content":   full_response})              

    # Clear History Button
    if st.button("🗑️ Clear History"):
        st.session_state.messages = []
        st.rerun()


# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; color: gray;'>© 2025 Advanced Unit Converter | Developed with ❤️ by Areeba Zafar</p>
""", unsafe_allow_html=True)