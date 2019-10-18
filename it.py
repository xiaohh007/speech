import numpy as np
import math,librosa
import sys


y, sr = librosa.load(sys.argv[1], sr=16000)
frame_size = 256
frmae_shift = 128
mfccs = librosa.feature.mfcc(y, sr, n_mfcc=12, hop_length=frmae_shift, n_fft=frame_size)
print(mfccs)
