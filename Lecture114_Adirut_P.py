def package_info():
    print("1. Value Package: Snorkeling at Similan Islands (Phang Nga)")
    print("2. Adventure Package: Scuba Fun Dive at Koh Tao (Surat Thani)")
    print("3. Private Charter Package: Inner & Outer Zones Snorkeling at Koh Lipe (Satun)")
    print("4. Premium VIP Package: Sunset Yacht Cruise at Phi Phi Islands (Krabi)")
    print("------------------------------------------------")

    while True:
        Choice = input("Please select a package by entering the corresponding number (1-4): ")
        if Choice in ['1', '2', '3', '4']:
            print(f"You have selected package {Choice}.")
            print("------------------------------------------------")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    return Choice

def show_package_detail(choice_info, user_country):
    country_key = user_country.strip().upper()
    
    currency_map = {
        "USA": "USD", "AMERICA": "USD", "UNITED STATES": "USD", "US": "USD",
        "CANADA": "CAD", "MEXICO": "MXN",
        "FRANCE": "EUR", "GERMANY": "EUR", "ITALY": "EUR", "SPAIN": "EUR", 
        "NETHERLANDS": "EUR", "BELGIUM": "EUR", "AUSTRIA": "EUR", "GREECE": "EUR", 
        "PORTUGAL": "EUR", "FINLAND": "EUR", "IRELAND": "EUR", "EUROPE": "EUR",
        "UK": "GBP", "ENGLAND": "GBP", "UNITED KINGDOM": "GBP", "BRITAIN": "GBP",
        "SWITZERLAND": "CHF", "SWEDEN": "SEK", "NORWAY": "NOK", 
        "DENMARK": "DKK", "CZECH": "CZK", "POLAND": "PLN", 
        "HUNGARY": "HUF", "ROMANIA": "RON", "ICELAND": "ISK",
        "JAPAN": "JPY", "CHINA": "CNY", "HONG KONG": "HKD", 
        "KOREA": "KRW", "SOUTH KOREA": "KRW", "INDIA": "INR", 
        "INDONESIA": "IDR", "MALAYSIA": "MYR", "PHILIPPINES": "PHP", 
        "SINGAPORE": "SGD", "THAILAND": "THB",
        "AUSTRALIA": "AUD", "NEW ZEALAND": "NZD", 
        "BRAZIL": "BRL", "SOUTH AFRICA": "ZAR", "TURKEY": "TRY", "ISRAEL": "ILS"
    }

    target_currency = currency_map.get(country_key, "USD")
    
    rate = 1 
    if target_currency != "THB":
        print(f"\n[System] Checking exchange rates for {target_currency}...")
        try:
            from forex_python.converter import CurrencyRates
            c = CurrencyRates()
            rate = c.get_rate(target_currency, 'THB') 
        except Exception:
            print("[System] Network error or unsupported currency. Using THB instead.")
            target_currency = "THB"
            rate = 1

    if choice_info == '1':
        base_price = 2800
        final_price = base_price / rate 
        
        print("Trip Type: One Day Trip (Speedboat) - Join-in Group")
        
        if target_currency != "THB":
            print(f"(Current Exchange Rate: 1 {target_currency} = {rate:,.2f} THB)")
            
        print(f"Price: {final_price:,.2f} {target_currency} / Person") 
        print("Capacity: Max 40 persons / boat")
        print("Locations: Island 8, Island 9, Island 7, Island 4")
        print("Details & Food: 2 snorkeling spots by speedboat. (Price includes a seafood buffet lunch)")
        print("Special Promo: Come 4 Pay 3")
        print("--------------------------------------------------")
        
        if PartySize.isdigit() and int(PartySize) >= 4:
            print("Special Promo Applied: Come 4 Pay 3")
            print("--------------------------------------------------")
            discounted_people = int(PartySize) - 1
            total_price = discounted_people * final_price
            print(f"Total Price for {PartySize} people: {total_price:,.2f} {target_currency}")
        elif PartySize.isdigit():
            total_price = int(PartySize) * final_price
            print(f"Total Price for {PartySize} people: {total_price:,.2f} {target_currency}")

    elif choice_info == '2':
        base_price = 2500
        final_price = base_price / rate
        
        print("Trip Type: Half Day Trip (Big Boat) - Small Group")
        if target_currency != "THB":
            print(f"(Current Exchange Rate: 1 {target_currency} = {rate:,.2f} THB)")
        print(f"Price: {final_price:,.2f} {target_currency} / Person")
        print("Capacity: 4 persons per 1 Divemaster")
        print("Locations: Chumphon Pinnacle, Sail Rock")
        print("Details & Food: 2 deep dives. (Price includes standard lunch box)")
        print("--------------------------------------------------")
        
        if PartySize.isdigit():
            total_price = int(PartySize) * final_price
            print(f"Total Price for {PartySize} people: {total_price:,.2f} {target_currency}")

    elif choice_info == '3':
        base_price = 3000
        final_boat_price = base_price / rate
        addon_price_thb = 500
        final_addon = addon_price_thb / rate
        
        print("Trip Type: One Day Trip (Private Longtail Boat)")
        if target_currency != "THB":
            print(f"(Current Exchange Rate: 1 {target_currency} = {rate:,.2f} THB)")
        print(f"Price: {final_boat_price:,.2f} {target_currency} / Boat (Charter Price)")
        print("Capacity: 1 - 8 persons")
        print("Locations: Jabang Channel, Koh Hin Ngam, Koh Rok Roy")
        print("Details & Food: Flexible schedule.")
        print(f"Add-on option: BBQ buffet for {final_addon:,.2f} {target_currency} / Person")
        print("Special Promo: Full Boat Discount (500 THB off if you have 8 persons)")
        print("--------------------------------------------------")
        
        if PartySize.isdigit():
            pax = int(PartySize)
            
            if pax == 8:
                discount = 500 / rate
                final_boat_price -= discount
                print("Special Promo Applied: Full Boat Discount (-500 THB)")
            
            want_addon = input("Do you want to add the BBQ buffet? (Y/N): ").strip().upper()
            if want_addon == 'Y':
                total_price = final_boat_price + (pax * final_addon)
                print(f"BBQ Buffet added for {pax} people.")
            else:
                total_price = final_boat_price
                
            print("--------------------------------------------------")
            print(f"Total Price for {pax} people: {total_price:,.2f} {target_currency}")

    elif choice_info == '4':
        base_price = 5500
        final_price = base_price / rate
        overnight_thb = 3500
        final_overnight = overnight_thb / rate
        
        print("Trip Type: Flexible Trip (Day Trip & Overnight available)")
        if target_currency != "THB":
            print(f"(Current Exchange Rate: 1 {target_currency} = {rate:,.2f} THB)")
        print(f"Price: {final_price:,.2f} {target_currency} / Person")
        print("Capacity: 15 - 20 persons / boat")
        print("Locations: Maya Bay, Pileh Lagoon, Viking Cave")
        print("Details & Food: Luxury catamaran cruise. (Includes international buffet lunch)")
        print(f"Overnight Option: Add {final_overnight:,.2f} {target_currency} / Person")
        print("--------------------------------------------------")
        
        if PartySize.isdigit():
            pax = int(PartySize)
            
            want_overnight = input("Do you want to upgrade to Overnight? (Y/N): ").strip().upper()
            if want_overnight == 'Y':
                price_per_person = final_price + final_overnight
                print("Overnight upgrade added.")
            else:
                price_per_person = final_price
                
            total_price = pax * price_per_person
            print("--------------------------------------------------")
            print(f"Total Price for {pax} people: {total_price:,.2f} {target_currency}")

    else:
        print("Invalid package choice.")


print("Hello All tourists!")
print("Welcome to Mixercat's diving tour company.")
print("------------------------------------------------")
print("May I know your name and which country you are from?")
print("And how many people are in your party?")
Name = input("Your name: ")
Country = input("Your country: ")
PartySize = input("Number of people in your party: ")
print("------------------------------------------------")
print("Hello " + Name + "! Nice to meet you!")
print("From " + Country + ", huh? That's interesting!")
print("Great! We can accommodate a party of " + PartySize + " people.")
print("------------------------------------------------")
print("Today, we also have a package that includes snorkeling and island sightseeing.")
selected_choice = package_info()
show_package_detail(selected_choice, Country)
print("Have a wonderful trip!")
print("------------------------------------------------")