import math
def solution(fees, records):
    dic = {}
    result_dic = {}
    
    for r in records:
        # 05:34 5961 IN
        time, car_number, in_out_type = r.split()
        minute = int(time.split(':')[0]) * 60 + int(time.split(':')[1])
        
        if in_out_type == 'IN':
            dic[car_number] = minute
            
        else: # 'OUT'
            parking_time = minute - dic[car_number]
            if result_dic.get(car_number) is None:
                result_dic[car_number] = parking_time
            else:
                result_dic[car_number] += parking_time
            dic.pop(car_number)
    
    # 남아있는 dic 23:59로 처리
    for car_number in dic:
        parking_time = 23*60+59 - dic[car_number]
        if result_dic.get(car_number) is None:
            result_dic[car_number] = parking_time
        else:
            result_dic[car_number] += parking_time
    
    result_array = []
    for car_number in sorted(result_dic.keys()):
        result_array.append(calculate_fee(fees, result_dic[car_number]))
    
    return result_array

def calculate_fee(fees, parking_time):
    basic_time, basic_fee, add_time, add_fee = fees
    
    result = basic_fee
    parking_time -= basic_time
    
    if parking_time > 0:
        result += math.ceil(parking_time / add_time) * add_fee
    
    return result