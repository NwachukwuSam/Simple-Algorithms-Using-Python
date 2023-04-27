def return_on_investment(amount, years):
    for year in range(1, years+1):
        roi = amount + amount*0.05
        print(f"Year {year} Return on investment == {roi}")
        amount=roi


how_much = int(input("How much are you investing: "))
how_many_years = int(input("How many years are you investing: "))
return_on_investment(how_much, how_many_years)