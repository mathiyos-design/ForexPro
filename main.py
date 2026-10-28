def risk_calculator():
    print("\n--- RISK CALCULATOR ---")
    try:
        balance = float(input("Account balance ($): "))
        risk_percent = float(input("Risk percentage (%): "))
        if balance <= 0 or not 0 < risk_percent <= 100:
            print("Please enter valid values.")
            return
        print(f"Planned risk: ${balance * risk_percent / 100:.2f}")
    except ValueError:
        print("Please enter numbers only.")


def lot_size_calculator():
    print("\n--- LOT SIZE CALCULATOR ---")
    try:
        balance = float(input("Account balance ($): "))
        risk_percent = float(input("Risk percentage (%): "))
        stop_loss = float(input("Stop Loss (pips): "))
        pip_value = float(input("Pip value per 1.00 lot ($): "))
        if balance <= 0 or not 0 < risk_percent <= 100:
            print("Invalid balance or risk percentage.")
            return
        if stop_loss <= 0 or pip_value <= 0:
            print("Stop Loss and pip value must be positive.")
            return
        risk_amount = balance * risk_percent / 100
        lot_size = risk_amount / (stop_loss * pip_value)
        print(f"Planned risk: ${risk_amount:.2f}")
        print(f"Estimated lot size: {lot_size:.4f}")
        print("Verify pip value and contract specifications with your broker.")
    except ValueError:
        print("Please enter numbers only.")


def risk_to_reward_calculator():
    print("\n--- RISK-TO-REWARD CALCULATOR ---")
    try:
        entry = float(input("Entry price: "))
        stop_loss = float(input("Stop Loss price: "))
        take_profit = float(input("Take Profit price: "))
        risk = abs(entry - stop_loss)
        reward = abs(take_profit - entry)
        if risk == 0 or reward == 0:
            print("Prices must be different.")
            return
        print(f"Risk distance: {risk:.5f}")
        print(f"Reward distance: {reward:.5f}")
        print(f"Risk-to-Reward: 1:{reward / risk:.2f}")
    except ValueError:
        print("Please enter valid numbers.")


def chart_analysis_helper():
    print("\n--- CHART ANALYSIS HELPER ---")
    symbol = input("Currency pair (e.g. EURUSD): ").upper().strip()
    timeframe = input("Timeframe (e.g. H4, H1, M15): ").upper().strip()
    trend = input("Trend (Uptrend/Downtrend/Sideways/Unsure): ").strip()
    support_text = input("Support level (optional): ").strip()
    resistance_text = input("Resistance level (optional): ").strip()

    print("\nEnter trade levels to calculate risk-to-reward.")
    try:
        entry_text = input("Entry price (optional): ").strip()
        sl_text = input("Stop Loss price (optional): ").strip()
        tp_text = input("Take Profit price (optional): ").strip()

        print("\n--- YOUR CHART NOTES ---")
        print(f"Pair: {symbol or 'Not entered'}")
        print(f"Timeframe: {timeframe or 'Not entered'}")
        print(f"Trend: {trend or 'Not entered'}")
        print(f"Support: {support_text or 'Not entered'}")
        print(f"Resistance: {resistance_text or 'Not entered'}")

        if entry_text and sl_text and tp_text:
            entry = float(entry_text)
            sl = float(sl_text)
            tp = float(tp_text)
            risk = abs(entry - sl)
            reward = abs(tp - entry)
            if risk > 0 and reward > 0:
                print(f"Risk distance: {risk:.5f}")
                print(f"Reward distance: {reward:.5f}")
                print(f"Risk-to-Reward: 1:{reward / risk:.2f}")
            else:
                print("Risk and reward prices must be different.")
        else:
            print("Risk-to-reward not calculated; one or more prices were left blank.")

        print("\nThese are your observations, not a trade signal.")
        print("This tool does not fetch live market data.")
    except ValueError:
        print("Invalid price entered. Use numbers such as 1.08500.")


def main():
    while True:
        print("\n" + "=" * 30)
        print("         FOREX PRO")
        print("=" * 30)
        print("1. Risk Calculator")
        print("2. Lot Size Calculator")
        print("3. Risk-to-Reward Calculator")
        print("4. Chart Analysis Helper")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()
        if choice == "1":
            risk_calculator()
        elif choice == "2":
            lot_size_calculator()
        elif choice == "3":
            risk_to_reward_calculator()
        elif choice == "4":
            chart_analysis_helper()
        elif choice == "5":
            print("Thank you for using Forex Pro!")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
