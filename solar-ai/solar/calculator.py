def calculate(data):
    bill = int(data["monthly_bill"])
    unit_rate = 8

    units = bill / unit_rate
    system_kw = round(units / 30 / 5, 1)

    base_cost = system_kw * 55000
    subsidy = base_cost * 0.4
    final = base_cost - subsidy

    return {
        "system_kw": system_kw,
        "base_cost": base_cost,
        "subsidy": subsidy,
        "final_cost": final
    }
