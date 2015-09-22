"""
This module contains links to audio files you can use for test purposes.

September 2015
@author: Amine SEHILI <amine.sehili@gmail.com>
"""

import os

__all__ = ["one_to_six_arabic_16000_mono_bc_noise", "was_der_mensch_saet_mono_44100_lead_tail_silence"]

_current_dir = os.path.dirname(os.path.realpath(__file__))

one_to_six_arabic_16000_mono_bc_noise = "{cd}{sep}data{sep}1to6arabic_\
16000_mono_bc_noise.wav".format(cd=_current_dir, sep=os.path.sep)


was_der_mensch_saet_mono_44100_lead_tail_silence = "{cd}{sep}data{sep}was_\
der_mensch_saet_das_wird_er_vielfach_ernten_44100Hz_mono_lead_tail_\
silence.wav".format(cd=_current_dir, sep=os.path.sep)
