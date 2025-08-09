from psychopy import visual, core, monitors, plugins
import numpy as np
import scipy.io as sio
import time
import random
stim_info = dict()

# set information
save_path = ''#
stim_info['n_trials'] = 300
stim_info['stimulus_duration'] = 2
stim_info['isi'] = 4
stim_info['sz'] = 20

# prepare stuff
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

stim_info = dict()
x_pool = np.arange(-1, 1, 5)
y_pool = np.arange(-1, 1, 5)

stim_info['x_pos'] = random.sample(x_pool, stim_info['n_trials'])
stim_info['y_pos'] = random.sample(y_pool, stim_info['n_trials'])
sio.savemat(save_path, stim_info) # work on this...

# start experiment
clock = core.Clock()
ct=0
# calculate frames here
n_frames = int(stim_info['stimulus_duration'] * win.monitorFramePeriod)
for nt in range(stim_info['n_trials']):
    # choose  a position
    gabor.pos = (stim_info['y_pos'], stim_info['x_pos'])
    t_start = clock.getTime()
    for frame_n in range(n_frames):
        gabor.setPhase(2 * clock.getTime() - t_start) # drift at 2hz
        gabor.setOri((0 + (clock.getTime() - t_start) * 180)%360)
        gabor.draw(win)
        win.flip()
    win.flip() # gray screen 
    time.sleep(stim_info['isi'])
    ct+=1