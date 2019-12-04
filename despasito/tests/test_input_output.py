"""
Regression tests for the despasito input/output package.

The following functions are not tested because they require importing a file:
    file2paramdict, extract_calc_data, process_commandline, make_xi_matrix

The following functions are not tested because they require exporting a file:
    write_EOSparameters

The following functions are tested:
    process_bead_data
"""

# Import package, test suite, and other packages as needed
import despasito.input_output.readwrite_input as d_io
import pytest
import numpy as np

# Not Used because we shouldn't reference an external file
@pytest.mark.parametrize('data', [([[0.8, [['CH4_2', 1]]], [0.2, [['eCH3', 2]]]])])
def test_process_bead_data(data):
    """Test extraction of system component information"""

    xi, beads, nui = d_io.process_bead_data(data)

    errors = []
    if not all(xi == np.array([0.8,0.2])):
        errors.append("xi: %s is not %s" % (str(xi),str(np.array([0.8,0.2]))))
    elif not set(beads) == set(['CH4_2', 'eCH3']):
        errors.append("beads: %s is not %s" % (str(beads),str(['CH4_2', 'eCH3'])))
    elif not np.array_equal(nui,np.array([[1.,0.],[0.,2.]])):
        errors.append("nui: %s is not %s" % (str(nui),str(np.array([[1.,0.],[0.,2.]]))))

    assert not errors, "errors occured:\n{}".format("\n".join(errors))

# Not Used because we shouldn't reference an external file
#@pytest.mark.parametrize('key, answer', [("rhoinc",2.0),("minrhofrac",2.5e-06)])
#def test_file2paramdict(key,answer):
#    """Test conversion of txt file to dictionary"""
#    rho_dict = d_io.file2paramdict("example/dens_params.txt")
#    print(rho_dict)
#    assert rho_dict[key] == pytest.approx(answer,abs=1e-7)
