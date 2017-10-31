#!usr/bin/python
from mininet.net import Mininet
from mininet.node import Controller,RemoteController,OVSController
from mininet.node import CPULimitedHost,Host
from mininet.node import OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel,info
from mininet.link import TCLink,Intf

def MandagsTopo():
    net=Mininet(topo=None,build=False,link=TCLink)
    info('AddingHardcoreController\n')
    ryuController=net.addController(name='ryuController', controller=RemoteController,ip='127.0.0.1',port=6633)
    info('NowAddingSwitches\n')
    sw1=net.addSwitch('sw1')
    info('AddingHosts\n')
    h1=net.addHost(name='h1',ip='172.31.1.1')
    h2=net.addHost(name='h2',ip='172.31.1.2')
    h3=net.addHost(name='h3',ip='172.31.1.3')
    h4=net.addHost(name='h4',ip='172.31.1.4')

    info('AddingLinks\n')
    net.addLink(h1,sw1,100)
    net.addLink(h2,sw1,100)
    net.addLink(h3,sw1,100)
    net.addLink(h4,sw1,100)

    #buildingandstartingthemininetnetwork
    net.build()
    net.start()
    #startthemininetterminal
    CLI(net)
    #finallystopmininet
    net.stop()	
if __name__=='__main__':
	setLogLevel('info')
	MandagsTopo()
