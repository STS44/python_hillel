# import block
import json
import random
from argparse import ArgumentParser

# functions block

def read_data_from_config_and_state():
    with open("config.json", "r") as config_json:
        data = json.load(config_json)
    with open("state.json", "r") as state_json:
        new_data = json.load(state_json)
    return [data, new_data]

def change_rate_and_write_state():
    config_data = read_data_from_config_and_state()[0]
    state_data = read_data_from_config_and_state()[1]
    if "new_rate" not in state_data:
        min_price = config_data["rate"] - config_data["delta"]
        max_price = config_data["rate"] + config_data["delta"]
    else:
        min_price = state_data["new_rate"] - config_data["delta"]
        max_price = state_data["new_rate"] + config_data["delta"]
    new_price = round(random.uniform(min_price, max_price), 2)
    with open("state.json", "w") as state_json:
        state_data["new_rate"] = new_price
        json.dump(state_data, state_json, indent=1)
    return state_data

def get_current_rate():
    config_data = read_data_from_config_and_state()[0]
    state_data = read_data_from_config_and_state()[1]
    if "new_rate" not in state_data:
        current_rate = config_data["rate"]
    else:
        current_rate = round(state_data["new_rate"], 2)
    print(f"{current_rate}")

# ----------------------------------------buy usd functions-----------------------------------------------------------

def get_available_uah_balance():
    config_data = read_data_from_config_and_state()[0]
    state_data = read_data_from_config_and_state()[1]
    if "new_uah_balance" not in state_data:
        available_uah_balance = config_data["uah_balance"]
    else:
        available_uah_balance = state_data["new_uah_balance"]
    return available_uah_balance

def calculate_required_uah_balance(usd_amount):
    config_data = read_data_from_config_and_state()[0]
    state_data = read_data_from_config_and_state()[1]
    if "new_rate" not in state_data:
        required_uah_balance = round(usd_amount * config_data["rate"], 2)
    else:
        required_uah_balance = round(usd_amount * state_data["new_rate"], 2)
    return required_uah_balance

def calculate_new_usd_balance_after_purchase(usd_amount):
    config_data = read_data_from_config_and_state()[0]
    state_data = read_data_from_config_and_state()[1]
    if "new_uah_balance" not in state_data:
        new_usd_balance = round(config_data["usd_balance"] + usd_amount, 2)
    else:
        new_usd_balance = round(state_data["new_usd_balance"] + usd_amount, 2)
    return new_usd_balance

def calculate_new_uah_balance_after_purchase(usd_amount):
    config_data = read_data_from_config_and_state()[0]
    state_data = read_data_from_config_and_state()[1]
    if "new_uah_balance" not in state_data and "new_rate" not in state_data:
        new_uah_balance = round(config_data["uah_balance"] - usd_amount * config_data["rate"], 2)
    elif "new_uah_balance" not in state_data and "new_rate" in state_data:
        new_uah_balance = round(config_data["uah_balance"] - usd_amount * state_data["new_rate"], 2)
    elif "new_uah_balance" in state_data and "new_rate" not in state_data:
        new_uah_balance = round(state_data["new_uah_balance"] - usd_amount * config_data["rate"], 2)
    elif "new_uah_balance" in state_data and "new_rate" in state_data:
        new_uah_balance = round(state_data["new_uah_balance"] - usd_amount * state_data["new_rate"], 2)
    return new_uah_balance

def buy_usd_and_write_state(usd_amount):
    state_data = read_data_from_config_and_state()[1]
    available_uah_balance = get_available_uah_balance()
    required_uah_balance = calculate_required_uah_balance(usd_amount)
    if available_uah_balance < required_uah_balance:
        print(f"UNAVAILABLE, REQUIRED BALANCE UAH {required_uah_balance}, AVAILABLE {available_uah_balance}")
    else:
        new_usd_balance = calculate_new_usd_balance_after_purchase(usd_amount)
        new_uah_balance = calculate_new_uah_balance_after_purchase(usd_amount)
        with open("state.json", "w") as state_json:
            state_data["new_usd_balance"] = new_usd_balance
            state_data["new_uah_balance"] = new_uah_balance
            json.dump(state_data, state_json, indent=1)
    return state_data

# -----------------------------------------sell usd functions---------------------------------------------------------

def get_available_usd_balance():
    state_data = read_data_from_config_and_state()[1]
    if "new_usd_balance" not in state_data:
        available_usd_balance = 0.00
    else:
        available_usd_balance = state_data["new_usd_balance"]
    return available_usd_balance

def calculate_new_usd_balance_after_sale(usd_amount):
    state_data = read_data_from_config_and_state()[1]
    if "new_usd_balance" not in state_data:
        new_usd_balance = 0.00
    else:
        new_usd_balance = round(state_data["new_usd_balance"] - usd_amount, 2)
    return new_usd_balance

def calculate_new_uah_balance_after_sale(usd_amount):
    config_data = read_data_from_config_and_state()[0]
    state_data = read_data_from_config_and_state()[1]
    if "new_usd_balance" not in state_data:
        new_uah_balance = config_data["uah_balance"]
    elif "new_usd_balance" in state_data and "new_rate" not in state_data:
        new_uah_balance = round(state_data["new_uah_balance"] + usd_amount * config_data["rate"], 2)
    elif "new_usd_balance" in state_data and "new_rate" in state_data:
        new_uah_balance = round(state_data["new_uah_balance"] + usd_amount * state_data["new_rate"], 2)
    return new_uah_balance

def sell_usd_and_write_state(usd_amount):
    state_data = read_data_from_config_and_state()[1]
    available_usd_balance = get_available_usd_balance()
    if available_usd_balance < usd_amount:
        print(f"UNAVAILABLE, REQUIRED BALANCE USD {usd_amount}, AVAILABLE {available_usd_balance}")
    else:
        new_usd_balance = calculate_new_usd_balance_after_sale(usd_amount)
        new_uah_balance = calculate_new_uah_balance_after_sale(usd_amount)
        with open("state.json", "w") as state_json:
            state_data["new_usd_balance"] = new_usd_balance
            state_data["new_uah_balance"] = new_uah_balance
            json.dump(state_data, state_json, indent=1)
    return state_data

# --------------------------------------buy and sell all usd functions------------------------------------------------

def buy_all_and_write_state():
    config_data = read_data_from_config_and_state()[0]
    state_data = read_data_from_config_and_state()[1]
    if "new_uah_balance" not in state_data and "new_rate" not in state_data:
        new_usd_balance = round(config_data["usd_balance"] + config_data["uah_balance"] / config_data["rate"], 2)
        new_uah_balance = 0.00
    elif "new_uah_balance" not in state_data and "new_rate" in state_data:
        new_usd_balance = round(config_data["usd_balance"] + config_data["uah_balance"] / state_data["new_rate"], 2)
        new_uah_balance = 0.00
    elif "new_uah_balance" in state_data and "new_rate" not in state_data:
        new_usd_balance = round(state_data["new_usd_balance"] + state_data["new_uah_balance"] /
                                config_data["rate"], 2)
        new_uah_balance = 0.00
    else:
        new_usd_balance = round(state_data["new_usd_balance"] + state_data["new_uah_balance"] /
                                state_data["new_rate"], 2)
        new_uah_balance = 0.00
    with open("state.json", "w") as state_json:
        state_data["new_uah_balance"] = new_uah_balance
        state_data["new_usd_balance"] = new_usd_balance
        json.dump(state_data, state_json, indent=1)
    return state_data

def sell_all_and_write_state():
    config_data = read_data_from_config_and_state()[0]
    state_data = read_data_from_config_and_state()[1]
    if "new_usd_balance" not in state_data and "new_rate" not in state_data:
        new_uah_balance = round(config_data["uah_balance"] + config_data["usd_balance"] * config_data["rate"], 2)
        new_usd_balance = 0.00
    elif "new_usd_balance" not in state_data and "new_rate" in state_data:
        new_uah_balance = round(config_data["uah_balance"] + config_data["usd_balance"] * state_data["new_rate"], 2)
        new_usd_balance = 0.00
    elif "new_usd_balance" in state_data and "new_rate" not in state_data:
        new_uah_balance = round(state_data["new_uah_balance"] + state_data["new_usd_balance"] *
                                config_data["rate"], 2)
        new_usd_balance = 0.00
    else:
        new_uah_balance = round(state_data["new_uah_balance"] + state_data["new_usd_balance"] *
                                state_data["new_rate"], 2)
        new_usd_balance = 0.00
    with open("state.json", "w") as state_json:
        state_data["new_uah_balance"] = new_uah_balance
        state_data["new_usd_balance"] = new_usd_balance
        json.dump(state_data, state_json, indent=1)
    return state_data

# --------------------------------------get balances and clear state.json---------------------------------------------

def get_balances():
    config_data = read_data_from_config_and_state()[0]
    state_data = read_data_from_config_and_state()[1]
    if "new_uah_balance" in state_data and "new_usd_balance" in state_data:
        current_uah_balance = round(state_data["new_uah_balance"], 2)
        current_usd_balance = round(state_data["new_usd_balance"], 2)
    else:
        current_uah_balance = round(config_data["uah_balance"], 2)
        current_usd_balance = round(config_data["usd_balance"], 2)
    print(f"USD {current_usd_balance} UAH {current_uah_balance}")

def clear_state():
    state_data = {}
    with open("state.json", "w") as state_json:
        json.dump(state_data, state_json, indent=1)
    return state_data

# functions call block

# CLI

args = ArgumentParser()
args.add_argument("action", nargs="?", type=str)
args.add_argument("count", nargs="?", type=str)
args = vars(args.parse_args())

if args["action"] == "RATE":
    get_current_rate()
elif args["action"] == "NEXT":
    change_rate_and_write_state()
elif args["action"] == "BUY":
    if args["count"] == "ALL":
        buy_all_and_write_state()
    else:
        usd_amount = float(args["count"])
        buy_usd_and_write_state(usd_amount)
elif args["action"] == "SELL":
    if args["count"] == "ALL":
        sell_all_and_write_state()
    else:
        usd_amount = float(args["count"])
        sell_usd_and_write_state(usd_amount)
elif args["action"] == "AVAILABLE":
    get_balances()
elif args["action"] == "RESTART":
    clear_state()

