import streamlit as st

#App Title
st.title("🌍Unit Convertor")

#Conversion Units
conversion_types = ["Length","Weight","Temperature","Volume","Time","Speed"]

#Making the user select an Conversion
conversion_choice = st.selectbox("Choose Conversion Type:",conversion_types)

#Length Conversion
if conversion_choice == "Length":
    length_units = ["Meters","Kilometers","Feet","Inches","Centimeters"]
    input_value = st.number_input("Enter length value:",min_value=0.0, format = "%.2f")
    from_unit = st.selectbox("From Unit:",length_units)
    to_unit = st.selectbox("To Unit:",length_units)

    #Conversion Dictionaries
    length_conversion = {
        "Meters":1,
        "Kilometers":1000,
        "Feet":0.3048,
        "Inches":0.0254,
        "Centimeters":0.01
    } 
    #Conversion Logic
    if st.button("Convert"):
        result = input_value * (length_conversion[from_unit] / length_conversion[to_unit])
        st.success(f"{input_value} {from_unit} = {result:.2f} {to_unit}")

#Weight Conversion
elif conversion_choice == "Weight":
    weight_units = ["Kilograms","Grams","Pounds","Ounces"]
    input_value = st.number_input("Enter weight value:",min_value=0.0, format = "%.2f")
    from_unit = st.selectbox("From Unit:",weight_units)
    to_unit = st.selectbox("To Unit:",weight_units)
    
    #Conversion Dictionaries
    weight_conversion = {
        "Kilograms":1,
        "Grams":0.001,       
        "Pounds":0.453592,
        "Ounces":0.0283495
    }
    #Conversion Logic
    if st.button("Convert"):
        result = input_value * (weight_conversion[from_unit] / weight_conversion[to_unit])
        st.success(f"{input_value} {from_unit} = {result:.2f} {to_unit}")

#Temperature Conversion
elif conversion_choice == "Temperature":
    temperature_units = ["Celsius","Fahrenheit","Kelvin"]
    input_value = st.number_input("Enter temperature value:",min_value=0.0, format = "%.2f")
    from_unit = st.selectbox("From Unit:",temperature_units)
    to_unit = st.selectbox("To Unit:",temperature_units)

    #Conversion Dictionaries
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == "Celsius":
            if to_unit == "Fahrenhit":
                return (value * 9/5) + 32 
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenhit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celcius":
                return value - 273.15
            elif to_unit == "Fahrenhit":
                return (value - 273.15) * 9/5 + 32
        return value
    
    #Conversion Logic
    if st.button("Convert"):
        result = convert_temperature(input_value, from_unit, to_unit)
        st.success(f"{input_value:.2f} {from_unit} = {result:.2f} {to_unit}")

#Volume Conversion
if conversion_choice == "Volume":
    volume_units = ["Liters","Milliliters","Gallons","Quarts","Pints","Cups"]
    input_value = st.number_input("Enter volume value:",min_value=0.0, format = "%.2f")
    from_unit = st.selectbox("From Unit:",volume_units)
    to_unit = st.selectbox("To Unit:",volume_units)

    #Conversion Dictionaries
    volume_conversion = {
        "Liters":1,
        "Milliliters":1000,
        "Gallons":0.264172,
        "Quarts":1.05669,
        "Pints":2.11338,
        "Cups":4.16667
    } 
    #Conversion Logic
    if st.button("Convert"):
        result = input_value * (volume_conversion[from_unit] / volume_conversion[to_unit])
        st.success(f"{input_value} {from_unit} = {result:.2f} {to_unit}")

#Time Conversion
if conversion_choice == "Time":
    time_units = ["Seconds","Minutes","Hours","Days"]
    input_value = st.number_input("Enter time value:",min_value=0.0, format = "%.2f")
    from_unit = st.selectbox("From Unit:",time_units)
    to_unit = st.selectbox("To Unit:",time_units)

    #Conversion Dictionaries
    time_conversion = {
        "Seconds":1,
        "Minutes":1/60,
        "Hours":1/3600,
        "Days":1/86400
    } 
    #Conversion Logic
    if st.button("Convert"):
        result = input_value * (time_conversion[from_unit] / time_conversion[to_unit])
        st.success(f"{input_value} {from_unit} = {result:.2f} {to_unit}")

#Speed Conversion
if conversion_choice == "Speed":
    speed_units = ["Meters per second","Kilometers per hour","Miles per hour","Feet per second"]
    input_value = st.number_input("Enter speed value:",min_value=0.0, format = "%.2f")
    from_unit = st.selectbox("From Unit:",speed_units)
    to_unit = st.selectbox("To Unit:",speed_units)

    #Conversion Dictionaries
    speed_conversion = {
        "Meters per second":1,
        "Kilometers per hour":3.6,
        "Miles per hour":2.23694,
        "Feet per second":3.28084
    } 
    #Conversion Logic
    if st.button("Convert"):
        result = input_value * (speed_conversion[from_unit] / speed_conversion[to_unit])
        st.success(f"{input_value} {from_unit} = {result:.2f} {to_unit}")
