import tkinter as tk 
from tkinter import ttk
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,GRU
from pandas_market_calendars import get_calendar
import plotly.express as px
from tkinter import messagebox

class StockPredictionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Stock Prediction App")

        # Etiqueta y caja de texto para ingresar el símbolo de la acción
        self.label = ttk.Label(master, text="Ingrese el símbolo de la acción:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.entry = ttk.Entry(master)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        # Botón para mostrar el gráfico
        self.button = ttk.Button(master, text="Mostrar Gráfico", command=self.mostrar_grafico)
        self.button.grid(row=1, column=0, columnspan=2, pady=10)

    def mostrar_grafico(self):
        # Obtener el símbolo de la acción desde la caja de texto
        symbol = self.entry.get()
        messagebox.showinfo("Mensaje", symbol)
        # Descargar datos históricos de una acción específica
        #Descargar datos históricos de una acción específica
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="1y")
        step = 60
        train_data = hist[:-step]
        test_data = hist[-step:]
        #Separar data
        training_set = train_data['Close'].values
        test_set = test_data['Close'].values
        #Normalizar los datos
        scaler = MinMaxScaler(feature_range=(0,1))
        scaled_data_train = scaler.fit_transform(training_set.reshape(-1,1))#scaler.fit_transform requiere 1 dimension
        
        
        #Separacion de datos de entrenamiento
        prediction_days = 60

        x_train = []
        y_train = []
        
        for x in range(prediction_days,len(scaled_data_train)):
            x_train.append(scaled_data_train[x-prediction_days:x,0])
            y_train.append(scaled_data_train[x,0])

        x_train, y_train = np.array(x_train), np.array(y_train)
        x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))
        model = Sequential()

        model.add(GRU(units=50,return_sequences = True, input_shape=(x_train.shape[1],1)))
        model.add(Dropout(0.2))
        model.add(GRU(units=50,return_sequences = True))
        model.add(Dropout(0.2))
        model.add(GRU(units=50))
        model.add(Dropout(0.1))
        model.add(Dense(units=1))

        model.compile(optimizer='adam', loss='mean_squared_error')

        model.fit(x_train,y_train,epochs=20,batch_size=32)

        HIST = hist.loc[:,"Close"]
        inputs = HIST[len(HIST) - len(test_set) - prediction_days :].values
        inputs = inputs.reshape(-1, 1)
        #scaling
        scaled_data_test = scaler.transform(inputs)

        x_test = []
        y_test = []
        for x in range(prediction_days,len(scaled_data_test)):
            x_test.append(scaled_data_test[x-prediction_days:x,0])
            y_test.append(scaled_data_test[x,0])
        x_test, y_test = np.array(x_test), np.array(y_test)
        x_test = np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))
        
        
#CA_ini_data_pred_fut"""
        data_fut_ini = scaled_data_test[prediction_days:]
        data_fut_add = scaler.transform(test_set.reshape(-1,1))
        data_pred_fut = np.vstack([data_fut_ini,data_fut_add])
        
        x_test_fut = []
        for x in range(prediction_days,len(data_pred_fut)):
            x_test_fut.append(data_pred_fut[x-prediction_days:x,0])

        x_test_fut = np.array(x_test_fut)
        x_test_fut = np.reshape(x_test_fut,(x_test_fut.shape[0],x_test_fut.shape[1],1))
#CA_fini"""


        #prediction
        predicted_stock_price = model.predict(x_test)
        #inverse transform the values
        predicted_stock_price = scaler.inverse_transform(predicted_stock_price)


#CA_ini Prediction for future
        predicted_stock_price_fut = model.predict(x_test_fut)
        #inverse transform the values
        predicted_stock_price_fut = scaler.inverse_transform(predicted_stock_price_fut)
#Concatening
        predicted_stock_price = np.concatenate((predicted_stock_price, predicted_stock_price_fut))
#CA_fini

        nyse = get_calendar("XNYS")

        start_date = train_data.index[-1]+ pd.Timedelta(days=1)
        tz_start_date = start_date.tz
        #Crea un rango de fechas para predicted_stock_price descartando las fechas que no abre la bolsa
        date_range = []
        current_date = start_date
        while len(date_range) < 120:
            if any(nyse.valid_days(current_date, current_date, tz=tz_start_date)):
                date_range.append(current_date)
            current_date += pd.DateOffset(days=1)
        # Datagrame para la data predecida
        
        predicted_data = pd.DataFrame(predicted_stock_price, index=date_range, columns=['Close'])
        #print(predicted_data)

        fig = px.line(train_data, x=train_data.index, y='Close', labels={'Close': 'Close Price'},
              title='Real Price VS Prediccion',
              width=900, height=400, color_discrete_sequence=['blue'])
        # Añade las líneas de prueba con un color diferente
        fig.add_scatter(x=test_data.index, y=test_data['Close'], mode='lines', name='Test', line=dict(color='orange'))
        fig.add_scatter(x=predicted_data.index, y=predicted_data['Close'], mode='lines', name='Predicción', line=dict(color='green'))
        fig.show()
    def onpick(self, event):
        # Función llamada cuando se hace clic en una línea
        thisline = event.artist
        label = thisline.get_label()

        if label == 'train':
            thisline.set_visible(not thisline.get_visible())
        elif label == 'test':
            thisline.set_visible(not thisline.get_visible())
        elif label == 'Predicción':
            thisline.set_visible(not thisline.get_visible())

        # Volver a dibujar la figura
        event.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = StockPredictionApp(root)
    root.mainloop()
