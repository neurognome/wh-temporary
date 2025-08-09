from psychopy import visual, core, monitors, plugins
import numpy as np
import scipy.io as sio
import time
import random
stim_info = dict()

save_path = ''# your save path here
stim_info['n_trials'] = 300
stim_info['stimulus_duration'] = 1
stim_info['isi'] = 3
stim_info['sz'] = 100

# generate stuff
monitor = monitors.Monitor('experiment_calibrated') # figure out here monitor
win = visual.Window(monitor.getSizePix(), screen=1, allowStencil=True, monitor=monitor, fullscr=False)

gabor = visual.GratingStim(win=win,
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

orientation_pool = np.arange(0, 330, 30) # set the orientations here
stim_info['orientation'] = random.sample(orientation_pool, stim_info['n_trials']) # this needs to be saved
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
    gabor.setOri(stim_info['orientation'][nt])
    gabor.setOpacity(stim_info['contrasts'][nt])
    
    # kill one stimulus by setting contrast to 0
    t_start = clock.getTime()
    for frame_n in range(n_frames):
        gabor.setPhase(2 * clock.getTime() - t_start) # drift at 2hz

        gabor.draw(win)
        win.flip()
    # while (clock.getTime() - t_start) < (stimulus_duration + isi):
    #     pass # just wait

    ct+=1