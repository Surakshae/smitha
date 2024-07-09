import shodan

# Setup Shodan API
SHODAN_API_KEY = "ETONYgf4Vlis51LqfUpeIoMWKDG4JjQr"
api = Shodan.Shodan(SHODAN_API_KEY)

# Search for live camera devices
try:
    results = api.search('port:554 webcam')
    # Process the results
    for result in results['matches']:
        print('IP: {}'.format(result['ip_str']))
        print('Port: {}'.format(result['port']))
        print(result['data'])
        print('')
except Exception as e:
    print('Error: {}'.format(e))
