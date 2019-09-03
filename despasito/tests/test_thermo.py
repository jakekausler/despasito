"""
Unit and regression test for the despasito package.
"""

# Import package, test suite, and other packages as needed
import despasito.thermodynamics.calc as calc
import despasito.thermodynamics as thermo
import despasito.equations_of_state
import pytest
import sys
import numpy as np

Tlist = [323.2]
xilist = [[0.89885627, 0.10114373]]
yilist = [[0.9883095246375379, 0.011690475362462203]]
rho_co2_h2o = np.array([19986.78358869])
P = np.array([4099056.163132072])

beads_co2_h2o = ['CO2', 'H2O']
nui_co2_h2o = np.array([[1., 0.],[0., 1.]])
beadlibrary_co2_h2o = {'CO2': {'epsilon': 207.89, 'l_a': 5.055, 'l_r': 26.408, 'sigma': 3.05e-10, 'Sk': 0.8468, 'Vks': 2, 'mass': 0.04401, 'NkH': 1, 'Nka1': 1},'H2O': {'epsilon': 266.68, 'l_a': 6.0, 'l_r': 17.02, 'sigma': 3.0063e-10, 'Sk': 1.0, 'Vks': 1, 'mass': 0.018015, 'NkH': 2, 'Nke1': 2, 'epsilonHe1': 1985.4, 'KHe1': 1.0169e-28}}
crosslibrary_co2_h2o = {'CO2': {'H2O': {'epsilon': 226.38, 'epsilonHe1': 2200.0, 'KHe1': 9.1419e-29}}}
sitenames_co2_h2o = ['H', 'e1', 'a1'] 
epsilonHB_co2_h2o = np.array([[[[   0.,     0.,     0. ], \
                       [   0.,     0.,     0. ], \
                       [   0.,     0.,     0. ]], \
                      [[   0.,  2200.,     0. ], \
                       [   0.,     0.,     0. ], \
                       [   0.,     0.,     0. ]]], \
                     [[[   0.,     0.,     0. ], \
                       [2200.,     0.,     0. ], \
                       [   0.,     0.,     0. ]], \
                      [[   0.,  1985.4,    0. ], \
                       [1985.4,    0.,     0. ], \
                       [   0.,     0.,     0. ]]]])
eos_co2_h2o = despasito.equations_of_state.eos("saft.gamma_mie",xi=np.array(xilist[0]),beads=beads_co2_h2o,nui=nui_co2_h2o,beadlibrary=beadlibrary_co2_h2o,crosslibrary=crosslibrary_co2_h2o,sitenames=sitenames_co2_h2o)

def test_thermo_import():
#    """Sample test, will always pass so long as import statement worked"""
    assert "despasito.thermodynamics" in sys.modules

def test_calc_types(eos=eos_co2_h2o,Tlist=Tlist,xilist=xilist):

    calcs = ["phase_xiT","phase_yiT","sat_props","liquid_properties","vapor_properties"]
    thermo_dict = [{"Tlist":Tlist,"xilist":xilist},{"Tlist":Tlist,"yilist":yilist},{"Tlist":Tlist},{"Tlist":Tlist,"xilist":xilist},{"Tlist":Tlist,"yilist":yilist}]
    calctest = []
    for i in range(len(calcs)):
        try:
            thermo.thermo(calcs[i],eos,thermo_dict[i])
        except:
            calctest.append(False)
        else:
            calctest.append(True)
        
    assert calctest.all() == True

def test_calc_Psat(T=Tlist[0],xi=[0.0,1.0],eos=eos_co2_h2o):

    Psat, rhov, rhol = calc.calc_Psat(T, xi, eos)

    assert ([ Psat, rhov, rhol]==[]).all()

    