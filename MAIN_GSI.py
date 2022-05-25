import exfoCTRL, time, DBCtrl
from time import sleep

filter_Alice_1 = exfoCTRL.filter('192.168.2.201')
filter_Alice_2 = exfoCTRL.filter('192.168.2.202')

filter_Bob_1 = exfoCTRL.filter('192.168.2.203')
filter_Bob_2 = exfoCTRL.filter('192.168.2.204')

bandwidth = 0.100
start_wl = 1535
res = 0.1

filter_Alice_1.setBandwidth(bandwidth)
filter_Alice_2.setBandwidth(bandwidth)

filter_Bob_1.setBandwidth(bandwidth)
filter_Bob_2.setBandwidth(bandwidth)

for wl_1 in range(21):
    wavelength_1 = start_wl+wl_1*res

    filter_Alice_1.setWavelength(wavelength_1)

    filter_Bob_2.setWavelength(wavelength_1)

    for wl_2 in range(21):
        wavelength_2 = start_wl+wl_2*res

        filter_Alice_2.setWavelength(wavelength_2)

        filter_Bob_1.setWavelength(wavelength_2)

        #WLA1 = filter_Alice_1.getWavelength()
        #BWA1 = filter_Alice_1.getBandwidth()

        #WLA2 = filter_Alice_2.getWavelength()
        #BWA2 = filter_Alice_2.getBandwidth()

        #WLB1 = filter_Bob_1.getWavelength()
        #BWB1 = filter_Bob_1.getBandwidth()

        #WLB2 = filter_Bob_2.getWavelength()
        #BWB2 = filter_Bob_2.getBandwidth()

        DBCtrl.recFilter(wavelength_1, bandwidth, wavelength_1, bandwidth, wavelength_2, bandwidth, wavelength_2, bandwidth)

        sleep(2)
