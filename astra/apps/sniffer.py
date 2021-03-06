from ..framework.application import Application


class SnifferApplication(Application):
    """
    Listen for traffic on a wired interface.
    """
    interface = None
    promiscuous = None

    @staticmethod
    def help(parser):
        parser.add_argument('-i', '--interface', help='The name or IP of the interface to listen on.', default=None,
                            action='store')
        parser.add_argument('-p', '--promiscuous', help='Listen in promiscuous mode.', action='store_true',
                            default=False)

    def run(self):
        socket = self.services.socket.raw_icmp(self.interface, self.promiscuous)

        try:
            socket.raw_listen(self.handle_packet)
        finally:
            socket.close()

    @staticmethod
    def handle_packet(packet):
        print(packet)
