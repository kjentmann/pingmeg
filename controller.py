from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER 
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0
from ryu.lib.packet import packet, ipv4, arp, icmp, ethernet
from ryu.ofproto import ofproto_v1_3

print("starting up Controller...")
class L2Switch(app_manager.RyuApp):
	OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]
	print("1")	
	def __init__(self ,*args, **kwargs):
		super(L2Switch, self).__init__(*args, **kwargs)
	print("2")	
	@set_ev_cls (ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)

	#This function is called for every packet received by the controller

	def packet_in_handler(self, ev):
		print("packet!")
		msg = ev.msg
		dp = msg.datapath
		ofp = dp.ofproto
	        ofp_parser = dp.ofproto_parser
		pkt = packet.Packet(msg.data)
		
		#This variable is true if the arrived pacet is an ICMP packet, false elswise
		isICMP = pkt.get_protocol(icmp.icmp)
		
		#check if packet is ICMP and it is a ICMP request
		
		
		#check if the ICMP packet is an echo request
		if (isICMP != None and isICMP.type == icmp.ICMP_ECHO_REQUEST):
			#retrieve the ipv4 packet
			incomming_request = pkt.get_protocol(ipv4.ipv4)

			#check if the ICMP request is sent to H1 
			if(incomming_request.dst == "172.31.1.1"):
				print("ping request sendt towards H1!")
				
				print("packet dropped")
				return

		#other packets not dropped by the filter above is flooded to the rest of the network
		actions = [ofp_parser.OFPActionOutput(ofp.OFPP_FLOOD)]
		out = ofp_parser.OFPPacketOut(datapath=dp, buffer_id=msg.buffer_id, in_port=msg.in_port, actions=actions)
		dp.send_msg(out)
 
