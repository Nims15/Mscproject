import streamlit as st
import numpy as np
from PyAstronomy import pyasl
import matplotlib.pylab as plt
from PyAstronomy.pyasl import planck
from PIL import Image
st.title("MSc PHYSICS PROJECT")
st.title("Evaluate Planck’s radiation law.")

st.image("img_3.png", use_column_width=True)





st.header("BLACK BODY RADIATION")
st.write("A black-body is an idealised object which absorbs and emits all radiation frequencies. Near thermodynamic equilibrium, the emitted radiation is closely described by Planck's law and because of its dependence on temperature, Planck radiation is said to be thermal radiation, such that the higher the temperature of a body the more radiation it emits at every wavelength")
st.header("PLANCKS RADIATION LAW")
st.write(" Planck's law (also Planck radiation law) describes the spectral density of electromagnetic radiation emitted by a black body in thermal equilibrium at a given temperature T, when there is no net flow of matter or energy between the body and its environment")
st.write("Formula - ")
st.image("img_4.png", use_column_width=True)
st.write("Max Planck was awarded the nobel prize in 1918 for quanta of light")
# Define wavelength in meters
lam = np.arange(1000.0 * 1e-10, 20000. * 1e-10, 20e-10)
T1 = st.slider('Temperature1', min_value=0, max_value=10000, value=7000)
st.write('Temperature1 =', T1)
T2 = st.slider('Temperature2', min_value=0, max_value=10000, value=5000)
st.write('Temperature2 =', T2)
T3 = st.slider('Temperature3', min_value=0, max_value=10000, value=9000)
st.write('Temperature3 =', T3)
# Get the Planck spectrum in [W/(m**2 m)] for a temperature of 7000 K
s7 = planck(T1, lam=lam)
# Get the Planck spectrum in [W/(m**2 m)] for a temperature of 5000 K
s5 = planck(T2, lam=lam)
# Get the Planck spectrum in [W/(m**2 m)] for a temperature of 9000 K
s9 = planck(T3, lam=lam)

# Convert into erg/(cm**2 * A * s)
s5erg = s5 * 1e-7
s7erg = s7 * 1e-7
s9erg = s9 * 1e-7
# Integrate the spectrum and compare with Stefan-Boltzmann law
i5 = np.sum(s5) * (lam[1] - lam[0])
i7 = np.sum(s7) * (lam[1] - lam[0])
i9 = np.sum(s9) * (lam[1] - lam[0])
print("5000 K integral: %.3e W/m**2 (Stefan-Boltzmann predicts %.3e W/m**2)" % (i5, (5.67e-8 * 5000. ** 4)))
print("7000 K integral: %.3e W/m**2 (Stefan-Boltzmann predicts %.3e W/m**2)" % (i7, (5.67e-8 * 7000. ** 4)))
print("7000 K integral: %.3e W/m**2 (Stefan-Boltzmann predicts %.3e W/m**2)" % (i9, (5.67e-8 * 9000. ** 4)))
fig1, ax = plt.subplots()
ax.set_xlabel("Wavelength [$\AA$]")
ax.set_ylabel("Flux = [erg / cm^2 / A / s]")
ax.plot(lam * 1e10, s5erg, 'r-')
ax.plot(lam * 1e10, s7erg, 'b-')
ax.plot(lam * 1e10, s9erg, 'c-')
# plt.show()
st.pyplot(fig1)
