

## **Chapter 1: Introduction**
### **1. What is the Internet?**
- **Nuts and bolts view**: 
  - Billions of connected devices (hosts/end systems).
  - Packet switches (routers, switches) forward data.
  - Communication links (fiber, copper, radio, satellite).
  - Networks managed by organizations (ISPs, enterprises, etc.).
- **Services view**:
  - Infrastructure for applications (web, email, streaming).
  - Provides programming interface (APIs) for apps.

### **2. What is a Protocol?**
- Rules governing communication between network entities.
- **Human analogy**: "What’s the time?" → "2:00".
- **Network protocols**: Define message format, order, actions (e.g., HTTP, TCP/IP).

### **3. Network Edge vs. Core**
- **Edge**: Hosts (clients/servers), access networks (DSL, FTTH, WiFi, 4G/5G).
- **Core**: Interconnected routers, packet/circuit switching.
  - **Packet switching**: Data split into packets, forwarded independently (efficient for bursty traffic).
  - **Circuit switching**: Dedicated path (e.g., telephone networks).

### **4. Performance Metrics**
- **Delay**: 
  - Processing, queueing, transmission (`L/R`), propagation (`d/s`).
  - Total delay = `d_proc + d_queue + d_trans + d_prop`.
- **Throughput**: Rate of data transfer (min of bottleneck links).
- **Packet loss**: Due to buffer overflow.

### **5. Protocol Layers**
- **OSI Model**: 7 layers (Physical, Data Link, Network, Transport, Session, Presentation, Application).
- **Internet Stack**: 5 layers (Physical, Link, Network, Transport, Application).
- **Encapsulation**: Data wrapped with headers at each layer (e.g., HTTP → TCP → IP → Ethernet).

---

## **Chapter 2: Application Layer**
### **1. Application Architectures**
- **Client-Server**: Clients request services from always-on servers (e.g., HTTP, SMTP).
- **P2P**: Peers act as both clients and servers (e.g., BitTorrent).

### **2. HTTP (HyperText Transfer Protocol)**
- **Stateless**: No memory of past requests.
- **Methods**: GET (fetch), POST (upload), HEAD (headers only), PUT (upload file).
- **Persistent vs. Non-persistent**:
  - Non-persistent: New TCP connection per object (slow).
  - Persistent: Single TCP connection for multiple objects (faster).
- **Cookies**: Maintain state (e.g., shopping carts, login sessions).

### **3. DNS (Domain Name System)**
- **Purpose**: Maps hostnames to IP addresses.
- **Hierarchical structure**: 
  - Root DNS → TLD (e.g., `.com`) → Authoritative (e.g., `google.com`).
- **Caching**: Reduces lookup time.

### **4. Email Protocols**
- **SMTP**: Push protocol for sending email (uses TCP, port 25).
- **IMAP**: Retrieve/store email on server (port 143).
- **POP3**: Download email to local device (port 110).

### **5. P2P & CDNs**
- **P2P**: Scalable file sharing (e.g., BitTorrent).
- **CDNs**: Distribute content geographically (e.g., Netflix, Akamai).

---

## **Chapter 3: Transport Layer**
### **1. UDP vs. TCP**
| Feature          | UDP                          | TCP                          |
|------------------|------------------------------|------------------------------|
| **Connection**   | Connectionless               | Connection-oriented          |
| **Reliability**  | Unreliable                   | Reliable                     |
| **Flow Control** | No                           | Yes (sliding window)         |
| **Congestion Control** | No                   | Yes (AIMD, CUBIC)            |
| **Use Cases**    | DNS, VoIP, streaming         | Web, email, file transfer    |

### **2. TCP Features**
- **3-Way Handshake**: SYN → SYN-ACK → ACK.
- **Reliable Data Transfer**:
  - Sequence numbers, acknowledgments (ACKs), retransmissions (timeout/fast retransmit).
- **Flow Control**: Receiver advertises window size (`rwnd`) to prevent overflow.
- **Congestion Control**:
  - **AIMD**: Additive Increase (slow start), Multiplicative Decrease (on loss).
  - **CUBIC**: Faster probing for bandwidth.

### **3. Principles of Reliable Data Transfer**
- **Stop-and-Wait**: Send 1 packet, wait for ACK (inefficient).
- **Pipelining**: Send multiple packets (Go-Back-N, Selective Repeat).
  - **GBN**: Retransmit all packets after lost packet.
  - **Selective Repeat**: Retransmit only lost packets.

### **4. Congestion Control**
- **Causes**: Too many senders → packet loss/delay.
- **Approaches**:
  - **End-to-End**: TCP infers congestion from loss/delay.
  - **Network-Assisted**: Routers signal congestion (e.g., ECN).

----


### Key Concepts from Chapter 4: Network Layer (Data Plane)

#### **1. Network Layer Overview**
- **Data Plane**: Handles local, per-router functions like forwarding packets from input to output ports based on header values.
- **Control Plane**: Manages network-wide logic (e.g., routing algorithms) to determine paths. Approaches:
  - **Traditional**: Distributed algorithms in routers (e.g., OSPF, BGP).
  - **SDN (Software-Defined Networking)**: Centralized control via remote servers.

#### **2. Router Architecture**
- **Components**:
  - **Input Ports**: Perform lookup/forwarding using tables (e.g., longest prefix matching).
  - **Switching Fabric**: Transfers packets between ports (methods: memory, bus, interconnection networks).
  - **Output Ports**: Manage buffering and scheduling (FIFO, priority, round-robin, WFQ).
- **Buffering**: Required to handle congestion; RFC 3439 recommends buffer size = RTT × link capacity.

#### **3. IP (Internet Protocol)**
- **IPv4 Datagram Format**: 20-byte header with fields like TTL, checksum, and source/destination addresses.
- **Fragmentation**: Handled by endpoints, not routers (unlike IPv4, IPv6 avoids fragmentation).
- **Addressing**:
  - **Classes**: A (0-127), B (128-191), C (192-223), D (multicast), E (experimental).
  - **CIDR (Classless Inter-Domain Routing)**: Flexible subnet masks (e.g., `200.23.16.0/20`).
  - **Subnets**: Isolated networks with common high-order bits (e.g., `223.1.1.0/24`).

#### **4. DHCP (Dynamic Host Configuration Protocol)**
- Dynamically assigns IP addresses to hosts:
  1. Discover → Offer → Request → Acknowledge.
- Provides additional info: subnet mask, default gateway, DNS server.

#### **5. NAT (Network Address Translation)**
- Allows multiple devices to share a single public IP:
  - Maps private IPs (e.g., `10.0.0.0/8`) to public IP + unique port.
  - Controversial (violates end-to-end principle) but widely used.

#### **6. IPv6**
- **Motivation**: Larger address space (128-bit), simplified header (fixed 40 bytes), no fragmentation.
- **Transition**: Tunneling (IPv6 over IPv4) enables gradual adoption.

#### **7. Middleboxes**
- Devices performing non-standard IP functions (e.g., firewalls, NAT, load balancers).
- **Trend**: Shift to SDN/NFV (Network Functions Virtualization) for programmable networks.

#### **8. Key Principles**
- **Hierarchical Addressing**: Enables route aggregation (e.g., `200.23.16.0/20` summarizes smaller subnets).
- **Best-Effort Service**: No guarantees on delivery, order, or bandwidth (simplicity drives scalability).

---

### Example: Longest Prefix Matching
- **Forwarding Table**:
  | Destination Range          | Interface |
  |----------------------------|-----------|
  | `11001000 00010111 00010*** *******` | 0         |
  | `11001000 00010111 00011000 *******` | 1         |
  | `11001000 00010111 00011*** *******` | 2         |
- **Packet to `11001000 00010111 00010110 10100001`**: Matches first entry (prefix length 21) → Interface 0.

### Summary
The data plane focuses on efficient packet forwarding using IP, switching fabrics, and QoS mechanisms, while the control plane manages routing. Key technologies like CIDR, DHCP, NAT, and IPv6 address scalability and deployment challenges. Middleboxes and SDN reflect evolving network architectures.

---

## **Key Formulas & Concepts**
1. **Delay**: 
   - Transmission delay = `L / R` (packet size / link rate).
   - Propagation delay = `d / s` (distance / speed).
2. **Throughput**: 
   - Per-connection throughput = min(`R_c`, `R_s`, `R/N`) for `N` connections.
3. **TCP Throughput**: 
   - `cwnd / RTT` (window size / round-trip time).

---

## **Exam Tips**
1. **Understand Layering**: Know how data moves through layers (encapsulation).
2. **TCP vs. UDP**: When to use each and why.
3. **HTTP & DNS**: Statelessness, caching, persistent connections.
4. **Reliable Transfer**: How TCP ensures reliability (ACKs, retransmissions).
5. **Congestion Control**: AIMD, CUBIC, fairness.

**Good luck!** Focus on these key points, and you’ll do great! 🚀