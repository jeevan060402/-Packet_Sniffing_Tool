import React, { useState } from 'react';

const PacketSniffer = () => {
  const [packets, setPackets] = useState([]);

  const startSniffing = async () => {
    const response = await fetch('http://127.0.0.1:5000/start_sniffing');
    const data = await response.json();
    setPackets(data.packets);
  };

  return (
    <div>
      <h1>Packet Sniffer</h1>
      <button onClick={startSniffing}>Start Sniffing</button>
      <ul>
        {packets.map((packet, index) => (
          <li key={index}>
            Source: {packet.src}, Destination: {packet.dst}, EtherType: {packet.ether_type}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PacketSniffer;
