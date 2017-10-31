#!usr/bin/python
from mininet.net import Mininet
from mininet.node import Controller,RemoteController,OVSController
from mininet.node import CPULimitedHost,Host
from mininet.node import OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel,info
from mininet.link import TCLink,Intf

def MyTopo():
    net=Mininet(topo=None,build=False,link=TCLink)
    info('AddingController1')
    ryuController=net.addController(name='ryuController', controller=RemoteController,ip='127.0.0.1',port=6633)
    info('NowAddingSwitches')
    switch1=net.addSwitch('switch1')
    switch2=net.addSwitch('switch2')
    info('AddingHosts')
    host1=net.addHost('h1')
    host2=net.addHost('h2')
    host3=net.addHost('h3')
    host4=net.addHost('h4')
    info('AddingLinks')
    net.addLink(switch1,switch2)
    net.addLink(host1,switch1)
    net.addLink(host2,switch1)
    net.addLink(host3,switch2)
    net.addLink(host4,switch2)
    #buildingandstartingthemininetnetwork
    net.build()
    net.start()
    #startthemininetterminal
    CLI(net)
    #finallystopmininet
    net.stop()	
if __name__=='__main__':
	setLogLevel('info')
	MyTopo()
