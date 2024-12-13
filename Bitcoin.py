ticker = "X:BTCUSD"
multiplier = 1
timespan = "day"
start_date = "2024-01-09"
end_date = "2024-12-10"

url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{start_date}/{end_date}?apiKey={API_Key}"

#print(url)

response = requests.get(url)
data = response.json()

if "results" in data:
    df = pd.DataFrame(data["results"])

    df['t'] = pd.to_datetime(df['t'], unit='ms')

    df.rename(columns={'t': 'Date', 'o': 'Open', 'h': 'High', 'l': 'Low', 'c': 'Close', 'v': 'Volume'}, inplace=True)

    print(df.head())
else:
    print("Error fetching data:", data)