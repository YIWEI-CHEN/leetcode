import re
from ipaddress import ip_address, IPv6Address


class WrongSolution:
    # "01.01.01.01" should be Neither, but the library said IPv4
    # "2001:0db8:85a3::8A2E:0370:7334" should be Neither, but library said it IPv6
    def validIPAddress(self, IP: str) -> str:
        try:
            return "IPv6" if type(ip_address(IP)) is IPv6Address else "IPv4"
        except ValueError:
            return "Neither"


class PlainSolution:
    def validIPAddress(self, IP: str) -> str:
        if IP.count('.') == 3:
            parts = IP.split('.')
            for part in parts:
                if len(part) == 0 or len(part) > 3:
                    return "Neither"
                if part[0] == '0' and len(part) >= 2 or not part.isdigit() or int(part) > 255:
                    return "Neither"
            return "IPv4"
        if IP.count(':') == 7:
            hexdigits = '0123456789abcdefABCDEF'
            parts = IP.split(':')
            for part in parts:
                if len(part) == 0 or len(part) > 4 or not all(c in hexdigits for c in part):
                    return "Neither"
            return "IPv6"
        return "Neither"


class RegexSolution:
    def validIPAddress(self, IP: str) -> str:
        # () --> group match
        chunk_ipv4 = r'([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][1-9]|25[0-5])'
        pattern_ipv4 = re.compile(r'^(' + chunk_ipv4 + r'\.){3}' + chunk_ipv4 + r'$')

        chunk_ipv6 = r'([0-9a-fA-F]{1,4})'
        pattern_ipv6 = re.compile(r'^(' + chunk_ipv6 + r'\:){7}' + chunk_ipv6 + r'$')

        if pattern_ipv4.match(IP):
            return "IPv4"
        if pattern_ipv6.match(IP):
            return "IPv6"
        return "Neither"


if __name__ == '__main__':
    for IP, e in (
        ("20EE:FGb8:85a3:0:0:8A2E:0370:7334", "Neither"),
        ("0.0.0.-0", "Neither"),
        ("2001:0db8:85a3:0:0:8A2E:0370:7334", "IPv6"),
        ("256.256.256.256", "Neither"),
        ("01.01.01.01", "Neither"),
        ("2001:db8:85a3:0:0:8A2E:0370:7334", "IPv6"),
        ("2001:0db8:85a3::8A2E:0370:7334", "Neither"),
        ("ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", "IPv6"),
        ("1e1.4.5.6", "Neither"),
    ):
        o = RegexSolution().validIPAddress(IP)
        # print(o)
        print(e == o)
