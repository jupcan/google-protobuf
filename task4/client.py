#!/usr/bin/python3
#-*- coding:utf-8-*-
import sys
import Ice
Ice.loadSlice('cristian.ice')
import ssdd
from time import time

class Client(Ice.Application):
	def run(self, argv):
		broker = self.communicator()
		cprx = broker.propertyToProxy("Cristian")
		cristian_prx = ssdd.CristianPrx.checkedCast(cprx)
		sprx = broker.propertyToProxy("SyncReport")
		syncReport_prx = ssdd.SyncReportPrx.checkedCast(sprx)

		if not cristian_prx:
			raise RuntimeError('invalid cristian proxy')
		if not syncReport_prx:
			raise RuntimeError('invalid sync proxy')

		dni = '71229899A'
		fullname = 'Juan Perea Campos'
		tc1 = time()
		t = cristian_prx.getServerTime(dni, tc1)
		tc2 = time()
		err = (tc2-tc1)/2
		t_new = t + err

		syncReport_prx.notifyTime(dni, fullname, t_new, err, tc2)
		self.shutdownOnInterrupt()
		broker.waitForShutdown()
		return 0

if __name__ == "__main__":
	client = Client()
	sys.exit(client.main(sys.argv))
