from TroyanoData import Troyano_data
# importar librerias necesarias 
import uvicorn
from fastapi import FastAPI
import numpy as np
import pickle
import pandas as pd
from sklearn import preprocessing 

# Crear objeto de FastAPI 
app = FastAPI()

# Crear las rutas y funciones para los servicios 
@app.get('/')
def index():
    return {'Mensaje': 'Sistema de Clasificacion'}

@app.post('/predecir/tree')
def predecirTree(data: Troyano_data):
    data = data.dict()
    number = preprocessing.LabelEncoder()
    
    Flow_id = data['Flow_id']  
    Source_ip = data['Source_ip']
    Source_port = data['Source_port']  
    Destination_ip = data['Destination_ip']
    Destination_port = data['Destination_port']   
    Protocol = data['Protocol']  
    Timestamp = data['Timestamp'] 
    Flow_duration = data['Flow_duration']  
    Total_fwd_packets = data['Total_fwd_packets']   
    Total_backward_packets = data['Total_backward_packets']           
    Total_length_of_fwd_packets = data['Total_length_of_fwd_packets']   
    Fwd_packet_length_max = data['Fwd_packet_length_max']  
    Fwd_packet_length_min = data['Fwd_packet_length_min']  
    Fwd_IAT_total = data['Fwd_IAT_total']   
    Bwd_IAT_total = data['Bwd_IAT_total']  
    Min_packet_length = data['Min_packet_length']   
    Max_packet_length = data['Max_packet_length']   
    FIN_flag_count = data['FIN_flag_count']  
    SYN_flag_count = data['SYN_flag_count']   
    PSH_flag_count = data['PSH_flag_count']  
    ACK_flag_count = data['ACK_flag_count']  
    URG_flag_count = data['URG_flag_count']   
    Down_up_ratio = data['Down_up_ratio']  
    Init_Win_bytes_backward = data['Init_Win_bytes_backward']   
    act_data_pkt_fwd = data['act_data_pkt_fwd']    
    min_seg_size_forward = data['min_seg_size_forward']  
    Active_max = data['Active_max']   
    Active_min = data['Active_min']   
    Idle_max = data['Idle_max']    
    Idle_min = data['Idle_min'] 
    
    # Se transforman variables string a numericas 
    # flow_id = number.fit_transform('121.14.255.84')  
    # source_ip = number.fit_transform(Source_ip)
    # destination_ip = number.fit_transform(Destination_ip)  
    # timestamp = number.fit_transform(Timestamp) 
    
    xin = np.array([Flow_id, Source_ip, Source_port, Destination_ip, Destination_port, Protocol, 
                    Timestamp, Flow_duration, Total_fwd_packets, Total_backward_packets, 
                    Total_length_of_fwd_packets, Fwd_packet_length_max, Fwd_packet_length_min,
                    Fwd_IAT_total, Bwd_IAT_total, Min_packet_length, Max_packet_length,
                    FIN_flag_count, SYN_flag_count, PSH_flag_count, ACK_flag_count, URG_flag_count,
                    Down_up_ratio, Init_Win_bytes_backward, act_data_pkt_fwd, min_seg_size_forward,
                    Active_max, Active_min, Idle_max, Idle_min]).reshape(1,30)
    yout = model.predict(xin)
    mensaje = ''
    for y_out in yout:
        mensaje = mensaje + 'El trafico de red ' + labels[y_out] + ' contiene troyano\n'
    
    return mensaje


# Cargar modelo
pkl_filename = 'modelTroyano_tree.pkl'
with open(pkl_filename, 'rb') as file:
    model = pickle.load(file)
    
labels = ['No', 'SI'] # Etiquetas de datos

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)