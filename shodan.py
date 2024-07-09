import shodan

# Setup Shodan API
SHODAN_API_KEY = "ETONYgf4Vlis51LqfUpeIoMWKDG4JjQr"
api = shodan.Shodan(SHODAN_API_KEY)

# Search for maritime-related devices
try:
    results = api.search('port:"554" maritime')
    # Process the results
    for result in results['matches']:
        print('IP: {}'.format(result['ip_str']))
        print('Port: {}'.format(result['port']))
        print(result['data'])
        print('')
except Exception as e:
    print('Error: {}'.format(e))


import shodan

# Set up Shodan API
SHODAN_API_KEY = ETONYgf4Vlis51LqfUpeIoMWKDG4JjQr
api = shodan.Shodan(SHODAN_API_KEY)

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




local Shodan = require "shodan"

local api_key = ETONYgf4Vlis51LqfUpeIoMWKDG4JjQr
local query = "port:554 webcam"

action = function(host, port)
    local client = shodan.client(api_key)
    local result = client:host(host.ip)
    if result then
        return result['data']
    end
end
