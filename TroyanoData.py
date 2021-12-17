from pydantic import BaseModel

class Troyano_data(BaseModel):
    
    Source_port: int
    Destination_port: int 
    Protocol: int
    Timestamp: str
    Flow_duration: int
    Total_fwd_packets: int 
    Total_backward_packets: int
    Total_length_of_fwd_packets: float 
    Fwd_packet_length_max: float
    Fwd_packet_length_min: float
    Fwd_IAT_total: float 
    Bwd_IAT_total: float
    Min_packet_length: float 
    Max_packet_length: float 
    FIN_flag_count: int
    SYN_flag_count: int 
    PSH_flag_count: int 
    ACK_flag_count: int
    URG_flag_count: int 
    Down_up_ratio: float 
    Init_Win_bytes_backward: int 
    act_data_pkt_fwd: int  
    min_seg_size_forward: int  
    Active_max: float 
    Active_min: float  
    Idle_max: float  
    Idle_min: float 