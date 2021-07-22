from neuron import h # step 1

try: 
    from neuron.units import ms, mV
except ModuleNotFoundError:
    ms = 1
    mV = 1

h.load_file("stdrun.hoc")

import matplotlib.pyplot as plt # step 8


soma = h.Section(name='soma') # step 2

soma.L = 20 # step 3
soma.diam = 20 # step 3

soma.insert('hh') # step 4

iclamp = h.IClamp(soma(0.5)) # step 5

iclamp.delay = 2 # step 5
iclamp.dur = 0.1 # step 5
iclamp.amp = 0.9 # step 5

v = h.Vector().record(soma(0.5)._ref_v)             # Membrane potential vector step 6
t = h.Vector().record(h._ref_t)                     # Time stamp vector step 6
h.finitialize(-65 * mV)
h.continuerun(40 * ms)



f1 = plt.figure()
plt.xlabel('t (ms)')
plt.ylabel('v (mV)')
plt.plot(t, soma_v, linewidth=2)
plt.show(f1)

f = plt.figure()
plt.xlabel('t (ms)')
plt.ylabel('v (mV)')
amps = [0.075 * i for i in range(1, 5)]
colors = ['green', 'blue', 'red', 'black']
for amp, color in zip(amps, colors):
    stim.amp = amp
    for my_cell.dend.nseg, width in [(1, 2), (101, 1)]:
        h.finitialize(-65)
        h.continuerun(25)
        plt.plot(t, list(soma_v),
               linewidth=width,
               label='amp=%g' % amp if my_cell.dend.nseg == 1 else None,
               color=color)
        plt.plot(t, list(dend_v), '--',
               linewidth=width,
               color=color)
plt.legend()
plt.show(f)
