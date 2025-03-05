import streamlit as st  # Import Streamlit for creating the web-based UI

st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    div.stButton > button {
        background-color: #ff4b4b;
        color: white;
        font-size: 16px;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #ff0000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def convert_units(value, unit_from, unit_to):

    conversions ={
        "meters_kilometers": 0.001, # 1 meter = 0.001 kilometer
        "kilometers_meters": 1000, # 1 kilometer = 1000 meter
        "grams_kilograms": 0.001,  # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000,  # 1 kilogram = 1000 grams
        "Meter_centimeter": 100, # 1 meter = 100 centimeter
    }

    key = f"{unit_from}_{unit_to}"  # Generate a key based on input and output units
    if key in conversions:
        conversion = conversions[key]
        # If the conversion is a function (e.g., temperature conversion), call it
        return (
            conversion(value) if callable(conversion) else value * conversion
        )  # Otherwise, multiply by the conversion factor
    else:
        return "Conversion not supported"  # Return message if conversion is not defined


# Streamlit UI setup
st.title("Unit Converter")  # Set title for the web app

# User input: numerical value to convert
value = st.number_input("Enter value:", min_value=1.0, step=1.0)

# Dropdown to select unit to convert from
unit_from = st.selectbox(
    "Convert from:", ["meters", "kilometers", "grams", "kilograms", "Meter", "centimeter" ]
)

# Dropdown to select unit to convert to
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms","Meter", "centimeter" ])

# Button to trigger conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)  # Call the conversion function
    st.write(f"Converted Value: {result}")  # Display the result
     