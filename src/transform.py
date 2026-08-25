import json

def shipments_by_status(shipments):
    delivery_status={}
    for row in shipments:
        delivery_status[row['status']]=delivery_status.get(row['status'],0)+1
    return delivery_status 

def best_carrier(shipments):
    carriers={}
    delivered={}
    delivery_rates={}
    for row in shipments:
        carriers[row['carrier']]=carriers.get(row['carrier'],0)+1
        if row['status'] == 'delivered':
            delivered[row['carrier']]=delivered.get(row['carrier'],0)+1
    for e in carriers:
        delivery_rates[e] = delivered.get(e,0)/carriers[e]
    best_carrier_list = sorted(delivery_rates.items(),key=lambda item: item[1],reverse=True)
    name, rate = best_carrier_list[0]
    return name

def top_routes(shipments):
    total_routes={}
    for row in shipments:
        total_routes[row['origin'],row['destination']] = total_routes.get((row['origin'],row['destination']),0)+1
    top_routes_list = sorted(total_routes.items(), key=lambda item: item[1], reverse=True)
    return [f"{route[0]} → {route[1]}" for route,frecuency in top_routes_list[:3]]
    

def avg_weight_by_carrier(shipments):
    weight_by_carrier = {}
    avg_by_carrier={}
    for row in shipments:
        weight_by_carrier.setdefault(row['carrier'], []).append(float(row['weight_kg']))
    for e in weight_by_carrier:
        avg_by_carrier[e]=round((sum(weight_by_carrier[e])/len(weight_by_carrier[e])),2)
    return avg_by_carrier
        
        
def write_json(summary,output):
    with open(output,'w', encoding='utf-8') as json_hanler:
        json.dump(summary,json_hanler, indent=2, ensure_ascii=False)

def build_summary(shipments): 
    return {
        "shipments_by_status": shipments_by_status(shipments),
        "best_carrier": best_carrier(shipments),
        "top_routes": top_routes(shipments),
        "avg_weight_by_carrier": avg_weight_by_carrier(shipments)
    }
