import requests
import json
from tabulate import tabulate

# DEFINING APIs INTERFACE
def define_api_interface():
    """demonstarte defining an api interface"""
    print("\n-------DEFINING APIs INTERFACE-------")
    api_url = "https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=5bf2a5f18c0877b10038045f2cdaac77"
    supported_methods = ["GET"]
    print(f"API ENDPOINT : {api_url}")
    print(f"SUPPORTED METHODS : {supported_methods}")

# Remote API Examples with error handling
def remote_api_example():
    print("\n-------REMOTE API EXAMPLES-------")
    # Example 1: OpenWeatherMap API (Get Current Weather Data)
    url_age = "https://disease.sh/v3/covid-19/all"
    try:
        response = requests.get(url_age)
        response.raise_for_status()
        data = response.json()
        print("Agnify API Responsege(Predict Age):")
        print(tabulate(data.items(), headers=['Field', 'Value']))
    except requests. exceptions.RequestException as e:
        print("Error fetching data from Agnify API:", e)
    #Example 2 : coingecko API (Get Cryptocurrency Prices)
    url_crypto = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&x_cg_demo_api_key=CG-hJ7L8TqbnRMNsHQjqczWAnUL"
    try:
        response = requests.get(url_crypto)
        response.raise_for_status()
        crypto_data = response.json()
        print("\nCoingecko API response (Bitcoin Price USD):")
        print(tabulate(crypto_data.items(),headers=["currency","price"]))
    except requests.exceptions.RequestException as e:
        print("Error fetching data from Coingecko API:", e)
    # Example 3: COVID-19 API (Global statistics)
    url_covid = "https://disease.sh/v3/covid-19/all"
    try:
        response = requests.get(url_covid)
        response.raise_for_status()
        covid_data = response.json()
        print(f"\nCOVID_19 Global Cases: {covid_data['cases']:,},Deaths: {covid_data['deaths']:}")
    except requests.exceptions.RequestException as e:
        print("Error fetching data from COVID-19 API:", e)
def api_from_command_line():
        print("\n-------API FROM COMMAND LINE-------")
        try:
            post_id = input("Enter Post ID (1-100):")
            url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
            response = requests.get(url)
            response.raise_for_status()
            post = response.json()
            print("\nPost Details:")
            print(tabulate(post.items(), headers=["Field", "Value"]))
        except requests.exceptions.RequestException as e:
            print("Error fetching post data:", e)
        except ValueError:
            print("Invalid input. Please enter a numeric Post ID.")
def api_limits_example():
    print("\n-------API LIMITS EXAMPLE-------")
    max_requests_per_minute = 5
    current_requests = 3
    print(f"Max requests allowed per minute: {max_requests_per_minute}")
    if current_requests < max_requests_per_minute:
        print("You can make more requests.")
    else:
        print("request limit reached, please wait.")
def api_for_js_spa():
    print("\n-------API FOR JS SPA-------")
    example_js_code = """
    fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&x_cg_demo_api_key=CG-hJ7L8TqbnRMNsHQjqczWAnUL')
        .then(response => response.json())
        .then(data => console.log('Bitcoin Price in USD:', data))
        .catch(error => console.error(error));
    """
    print("Example javascript code to fetch API data for SPA:")
def api_on_action_js_spa():
    print("\n--------API ON ACTION JS SPA--------")

#HTML + JAVASCRIPT TEMPLATE
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>SPA API DEMO</title>
    </head>
    <body>
    <h2>BITCOIN PRICE IN USD(via API)</h2>
    <div id="price">Loading...</div>
    <script>
        fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&x_cg_demo_api_key=CG-hJ7L8TqbnRMNsHQjqczWAnUL')
            .then(response => response.json())
                .then(data => {
                    document.getElementById('price').innerText = 'Bitcoin Price in USD: ' + data.bitcoin.usd;
                })
                .catch(error => {
                    document.getElementById('price').innerText = 'Error fetching data.';
                    console.error(error);
                });
        </script>
</body>
</html>
 """
#Save HTML File
file_name = "spa_api_demo.html"
with open(file_name, "w") as f:
    f.write(html_content)
    print(f"spa demo html file created: {file_name}")
    print("open this file in a web browser to see live API data in action.")
    #MAIN PROGRAM
if __name__ == "__main__":
    """Entry point of the script
    executes all steps sequentially"""
    print("\n=======ENHANCED REAl-TIME API INTEGRATION DEMO=======")
    define_api_interface()
    remote_api_example()
    api_from_command_line()
    api_limits_example()
    api_for_js_spa()
    api_on_action_js_spa()
    print("\n=======END OF DEMO=======")