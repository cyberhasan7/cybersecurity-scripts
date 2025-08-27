import socket
import struct

def sniff_packets():
    print("🌐 Network Traffic Sniffer")
    print("-" * 40)

    # Raw socket create
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    host = socket.gethostbyname(socket.gethostname())

    conn.bind((host, 0))
    conn.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    try:
        while True:
            raw_data, addr = conn.recvfrom(65535)
            ip_header = raw_data[:20]
            iph = struct.unpack("!BBHHHBBH4s4s", ip_header)

            version_ihl = iph[0]
            version = version_ihl >> 4
            ihl = version_ihl & 0xF
            ttl = iph[5]
            proto = iph[6]
            src_ip = socket.inet_ntoa(iph[8])
            dst_ip = socket.inet_ntoa(iph[9])

            print(f"Protocol: {proto} | Src: {src_ip} -> Dst: {dst_ip}")

    except KeyboardInterrupt:
        print("\n❌ Sniffer stopped by user")
        conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == "__main__":
    sniff_packets()
