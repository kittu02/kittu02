# lab 20
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sg

# # Task 1:  Sine wave
# freq = 2
# amp = 2
# t = np.linspace(0,2,1000)
# sig_sine = amp*np.sin(2*np.pi*freq*t)
# plt.figure(figsize = (10,8)) # set the size of figure
# plt.title('Sine Wave',fontsize=20)
# plt.plot(t,sig_sine, linewidth=3,label= 'x(t) = sin(wt)')
# plt.xlabel('time',fontsize=15)
# plt.ylabel('Amplitude',fontsize=15)
# plt.legend(loc='upper right')
# plt.grid()
# plt.show()

# # Task 2: Square Wave

# freq = 2
# amp = 2
# t = np.linspace(0,2,1000)
# sig_square = amp*sg.square(2*np.pi*freq*t, duty=0.3)
# plt.figure(figsize = (10,4)) # set the size of figure
# plt.title('Square Wave',fontsize=20)
# plt.plot(t,sig_square, linewidth=10,label= 'x(t) = Square')
# plt.xlabel('time',fontsize=15)
# plt.ylabel('Amplitude',fontsize=15)
# plt.legend(loc='upper right')
# plt.grid()
# plt.show()


# # Task 3:  Triangle wave
# freq = 2
# amp = 2
# t = np.linspace(0,2,1000)
# sig_triangle = amp*sg.sawtooth(2*np.pi*freq*t, width = 0.5)
# plt.figure(figsize = (10,4)) # set the size of figure
# plt.title('Triangle Wave',fontsize=20)
# plt.plot(t,sig_triangle, linewidth=2,label= 'x(t) = tri(wt)')
# plt.xlabel('time',fontsize=15)
# plt.ylabel('Amplitude',fontsize=15)
# plt.legend(loc='upper right')
# plt.grid()
# plt.show()

# # Task 4: Sinc Function
# # t1 = np.arange(-2*np.pi, 2*np.pi,0.01)
# t1 = np.linspace(-8,8,1000)
# sig_sinc = np.sinc(t1)
# # plt.figure(figsize=(10,4)) # set the size of figure
# plt.title('Sine Function',fontsize=20)
# plt.plot(t1,sig_sinc,'--g',linewidth=1, label='x(t) = sinc(t)')
# plt.xlabel('time',fontsize=15)
# plt.ylabel('Amplitude',fontsize=15)
# plt.legend(loc='upper right')
# # Highlights axis at x=0 and y=0 
# plt.axhline(y=0, color='k')
# plt.axvline(x=0, color='k')
# plt.grid()
# plt.show()



# # Task 5: basic function
# def p(t):
#     """Basic rectangular pulse"""
#     return 1 * (abs(t) < 0.5)

# def pt(t):
#     """ Basic triangular pulse"""
#     return (1 - abs(t)) * (abs(t) < 1)

# def sgn(t):
#     """Sign function"""
#     return 1 * (t >= 0) - 1 * (t < 0)

# def u(t):
#     """Unit step function"""
#     return 1 * (t >= 0)

# functions = [p, pt, sgn, u]

# t = np.linspace(-2, 2, 1000)

# plt.figure()
# for i, function in enumerate(functions, start=1):
#     plt.subplot(2, 2, i)
#     plt.plot(t, function(t), '-b')
#     plt.ylim((-1.1, 1.1))
#     plt.title(function.__doc__)
# plt.tight_layout()
# plt.show()

# u(t)
# u(t+1)
# u(t-2)
# u(t-1)


############### posst lab 
# def u1(t):
#     """Unit step function u(t+1)"""
#     return 1 * ((t+1) >= 0)
# def u2(t):
#     """Unit step function u(t-1)"""
#     return 1 * ((t-1) >= 0)
# def u3(t):
#     """Unit step function u(t-2)"""
#     return 1 * ((t-2) >= 0)
# def u4(t):
#     """Unit step function u(-t+1)"""
#     return 1 * ((-t+1) >= 0)
# functions = [u1, u2, u3, u4]

# t = np.linspace(-4, 4, 1000)

# plt.figure()
# for i, function in enumerate(functions, start=1):
#     plt.subplot(2, 2, i)
#     plt.plot(t, function(t), '-b')
#     plt.xlim((-4,4))
#     plt.ylim((-1.1, 1.1))
#     plt.title(function.__doc__)
# plt.tight_layout()
# plt.show()

# Task 1: Plot Discrete-time signals
# Sine wave
n = np.linspace(0, 10, 100)
amp = 5 # Amplitude
f = 50
x = amp * np.sin(2 * np.pi * f * n)

# Exponential Signal
x_ = amp * np.exp(-n)
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.stem(n, x, 'yo', label='Sine wave')

plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 2)
plt.stem(n, x_, 'yo', label='Exponential Signal')

plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')
plt.show()