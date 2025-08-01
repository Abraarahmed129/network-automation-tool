from flask import Flask, render_template, request
from network_functions import get_device_info, configure_vlan

app = Flask(__name__)

DEVICE_CREDENTIALS = {
    'device_type': 'cisco_ios_telnet',
    'ip':   'sandbox-iosxe-latest-1.cisco.com',
    'username': 'developer',
    'password': 'C1sco12345',
}

@app.route('/', methods=['GET', 'POST'])
def index():
    config_output = ""
    if request.method == 'POST':
        vlan_id_from_form = request.form['vlan_id']
        vlan_name_from_form = request.form['vlan_name']
        config_output = configure_vlan(DEVICE_CREDENTIALS, vlan_id_from_form, vlan_name_from_form)

    device_info = get_device_info(DEVICE_CREDENTIALS)
    return render_template('index.html', device_info=device_info, config_output=config_output)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)