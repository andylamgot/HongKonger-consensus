#HongKongerConsensus
from __future__ import print_function

class HongKongConsensusBuilder:
    def __init__(self):
        self._subject = ''
        self._oppose = ''
        self._motto = ''
        
    def will(self):
        self._oppose = 'Fugitive Offenders Ordinance Amendment Bill 2019'
        return self
        
    def always(self):
        self._subject = 'The vast majority of HongKonger'
        return self
        
    def believe(self):
        self._motto = 'HongKonger consensus'
        return self
        
    def __str__(self):
        return ('Hong Kong absolutely will not accept "{0}".\n\r' +
                '{1} absolutely oppose "{0}".\n\r' +
                'This is the "{2}".').format(self._oppose,
                                            self._subject,
                                            self._motto)
                            
if __name__ == '__main__':
    HK = HongKongConsensusBuilder()
    
    print(HK.will().always().believe())
                    
