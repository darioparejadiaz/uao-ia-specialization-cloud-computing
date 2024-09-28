# *******************************************
# *******************************************

import streamlit as st
import requests
import json
import os

# *******************************************
# *******************************************

API_URL = os.getenv(
    "API_URL", "http://172.169.59.91:80/api/v1/service/dp-house-endpoint/score"
)
print("API_URL", API_URL)

# *******************************************
# *******************************************


def llamar_api_model(
    bedrooms,
    bathrooms,
    sqft_living,
    sqft_lot,
    floors,
    waterfront,
    view,
    condition,
    sqft_above,
    sqft_basement,
    yr_built,
    yr_renovated,
    city,
    statezip,
):
    url = f"{API_URL}"

    payload = json.dumps(
        {
            "Inputs": {
                "WebServiceInput0": [
                    {
                        "date": "",
                        "price": 0,
                        "bedrooms": bedrooms,
                        "bathrooms": bathrooms,
                        "sqft_living": sqft_living,
                        "sqft_lot": sqft_lot,
                        "floors": floors,
                        "waterfront": waterfront,
                        "view": view,
                        "condition": condition,
                        "sqft_above": sqft_above,
                        "sqft_basement": sqft_basement,
                        "yr_built": yr_built,
                        "yr_renovated": yr_renovated,
                        "street": "",
                        "city": city,
                        "statezip": statezip,
                        "country": "",
                    }
                ]
            },
            "GlobalParameters": {},
        }
    )
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer fkK467mrlg8CsYsp33PWoQDvHkHvy8Do",
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    parsed_response = f"Precio predecido de la casa: USD :blue[${int(response.json()["Results"]["WebServiceOutput0"][0]["Scored Labels"])}]"
    return parsed_response


# *******************************************
# *******************************************


def crear_modelo_predict():
    st.subheader("Ingrese los datos de la casa:", divider=True)

    bedrooms = st.number_input("Dormitorios", min_value=0.0, max_value=10.0, value=3.0)
    bathrooms = st.number_input("Baños", min_value=0.0, max_value=10.0, value=2.0)
    sqft_living = st.number_input(
        "Pies cuadrados construidos", min_value=0, max_value=10000, value=1340
    )
    sqft_lot = st.number_input(
        "Pies cuadrados lote", min_value=0, max_value=10000, value=7912
    )
    floors = st.number_input("Cantidad de pisos", min_value=0, max_value=10, value=2)
    waterfront = st.number_input("Frente al Mar", min_value=0, max_value=1, value=0)
    view = st.number_input("Vista", min_value=0, max_value=1, value=0)
    condition = st.number_input("Condición", min_value=0, max_value=10, value=3)
    sqft_above = st.number_input(
        "Pies Cuadrados altillo", min_value=0, max_value=10000, value=1340
    )
    sqft_basement = st.number_input(
        "Pies cuadrados Sotano", min_value=0, max_value=10000, value=0
    )
    yr_built = st.number_input(
        "Año de la contrucción", min_value=1920, max_value=3000, value=1955
    )
    yr_renovated = st.number_input(
        "Año de renovación", min_value=1920, max_value=3000, value=2005
    )
    city = st.text_input("Ciudad", value="Shoreline")
    statezip = st.text_input("Estado", value="WA 98133")

    is_clicked = st.button("Predecir")
    if is_clicked:
        with st.spinner("Predicting..."):
            json_result = llamar_api_model(
                bedrooms,
                bathrooms,
                sqft_living,
                sqft_lot,
                floors,
                waterfront,
                view,
                condition,
                sqft_above,
                sqft_basement,
                yr_built,
                yr_renovated,
                city,
                statezip,
            )
        st.title(json_result)
        st.balloons()
        
# *******************************************
# *******************************************


def app():
    st.set_page_config(
        page_title="Home Page",
        page_icon=":bar_chart:",
        layout="centered",
        initial_sidebar_state="auto",
    )

    st.title(":blue[House Pricing Prediction] :house::dollar:")
    st.write(
        "Powered by Carlos Gutiérrez, Dario Pareja, Juan Andrade, Andres Rojas, Fernando Salazar"
    )

    option_selected = st.selectbox("Modelo Seleccionado", ["house-pricing"])

    if option_selected == "house-pricing":
        crear_modelo_predict()
    else:
        print("Se presento un error")

# *******************************************
# *******************************************


if __name__ == "__main__":
    app()
