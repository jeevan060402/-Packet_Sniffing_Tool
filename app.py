from flask import Flask, render_template, jsonify
from scapy.all import sniff, Ether, conf
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/start_sniffing": {"origins": "http://localhost:3000"}}, expose_headers="X-Content-Type-Options", supports_credentials=True, allow_headers=["Content-Type", "Authorization"])


captured_packets = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_sniffing')
def start_sniffing():
    print("started Sniffing")
    global captured_packets
    captured_packets = []

    def packet_callback(packet):
        ether_type = packet[Ether].type if Ether in packet else None
        obj = {
            'src': packet.src,
            'dst': packet.dst,
            'ether_type': ether_type,
        }
        print(obj)
        captured_packets.append(obj)


    sniff(prn=packet_callback, store=0, count=10, iface=conf.iface)
    return jsonify({'status': 'success', 'packets': captured_packets})

if __name__ == '__main__':
    app.run(debug=True)
