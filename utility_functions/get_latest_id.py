# Utility Function
def get_latest_id(data):
    try: 
        return data["tasks"][-1]["id"]
    except Exception as e:
        return 0