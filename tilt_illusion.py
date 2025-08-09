from psychopy import visual, core, monitors, plugins
import numpy as np
import scipy.io as sio
import time
import random
stim_info = dict()

save_path = ''# your save path here
stim_info['n_trials'] = 300
stim_info['stimulus_duration'] = 2
stim_info['isi'] = 4
stim_info['sz'] = 100

# generate stuff
monitor = monitors.Monitor('experiment_calibrated') # figure out here monitor
win = visual.Window(monitor.getSizePix(), screen=1, allowStencil=True, monitor=monitor, fullscr=False)

center = visual.GratingStim(win=win,
                              mask='circle',
                              units='deg',
                              sf=0.04,
                              contrast=1,
                              ori=0,
                              pos=(0, 0),
                              size=(stim_info['sz'], stim_info['sz']),
                              tex='sin',
                              texRes=512,
                              name='gabor'
                              )

surround = visual.GratingStim(win=win,
                              mask='circle',
                              units='deg',
                              sf=0.04,
                              contrast=1,
                              ori=0,
                              pos=(0, 0),
                              size=(stim_info['sz'], stim_info['sz']),
                              tex='sin',
                              texRes=512,
                              name='gabor'
                              )

surround_shift = [-20, -15, -10, -5, 0, 5, 10, 15, 20, -45, 45, -90, 90]
orientation_pool = 0
stim_info['center_ori'] = random.sample(orientation_pool, stim_info['n_trials']) # this needs to be saved
stim_info['surround_shift'] = random.sample(surround_shift, stim_info['n_trials']) # this needs to be saved
contrast_pool = 1
stim_info['contrast'] = random.sample(contrast_pool, stim_info['n_trials'])

# save the stim info
sio.savemat(save_path, stim_info) # work on this...

# start the presentation
clock = core.Clock()
ct=0

# calculate frames here
n_frames = int(stim_info['stimulus_duration'] * win.monitorFramePeriod)
for nt in range(stim_info['n_trials']):
    center.setOri(stim_info['orientation'][nt])
    surround.set_ori(stim_info['orientation'][nt] + stim_info['surround_shift'])
    
    # kill one stimulus by setting contrast to 0
    t_start = clock.getTime()
    for frame_n in range(n_frames):
        center.draw(win)
        surround.draw(win)
        win.flip()

    time.sleep(stim_info['isi'])
    ct+=1