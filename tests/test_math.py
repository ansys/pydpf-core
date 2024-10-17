import numpy as np

import ansys.dpf.core as dpf


def test_math_matrix_inverse_3d():
    dim = 3
    real_field = dpf.fields_factory.create_matrix_field(
        num_entities=1,
        num_lines=dim,
        num_col=dim,
    )
    real_field.unit = "m"
    values = [1.0, 1.0, 1.0,
              4.0, 0.0, 0.0,
              1.0, 1.0, 1.0]
    real_field.append(values, 1)

    img_field = dpf.fields_factory.create_matrix_field(
        num_entities=1,
        num_lines=dim,
        num_col=dim,
    )
    img_field.unit = "m"
    values = [0.3, 0.0, 0.0,
              1.0, 1.0, 2.0,
              0.0, 0.0, 0.1]
    img_field.append(values, 1)

    fc_in = dpf.fields_container_factory.over_time_freq_complex_fields_container(
        real_fields={1.0: real_field}, imaginary_fields={1.0: img_field}, time_freq_unit="s"
    )

    fc_out = dpf.operators.math.matrix_inverse(fields_container=fc_in).eval()

    print(fc_out)
    print(fc_out[0])
    assert fc_out[0].unit == "m^-1"
    real_inverse_values = [1.4551, 0.1564, -1.5642,
                           -5.1946, -0.6584, 6.5842,
                           4.3652, 0.4693, -4.6926]
    assert np.allclose(fc_out[0].data, real_inverse_values, atol=0.0001)

    print(fc_out[1])
    assert fc_out[1].unit == "m^-1"
    img_inverse_values = [-1.2477, -0.1091, 1.0913,
                          -5.4456, 0.3896, 6.1040,
                          6.2568, -0.3274, -6.7261]
    assert np.allclose(fc_out[1].data, img_inverse_values, atol=0.0001)


def test_math_matrix_inverse_2d():
    dim = 2
    real_field = dpf.fields_factory.create_matrix_field(
        num_entities=1,
        num_lines=dim,
        num_col=dim,
    )
    real_field.unit = "m"
    values = [0.0, 1.0,
              2.0, 3.0]
    real_field.append(values, 1)

    img_field = dpf.fields_factory.create_matrix_field(
        num_entities=1,
        num_lines=dim,
        num_col=dim,
    )
    img_field.unit = "m"
    values = [1.0, 1.0,
              1.0, 1.0]
    img_field.append(values, 1)

    fc_in = dpf.fields_container_factory.over_time_freq_complex_fields_container(
        real_fields={1.0: real_field}, imaginary_fields={1.0: img_field}, time_freq_unit="s"
    )

    fc_out = dpf.operators.math.matrix_inverse(fields_container=fc_in).eval()

    print(fc_out)
    print(fc_out[0])
    assert fc_out[0].unit == "m^-1"
    real_inverse_values = [-1.5, 0.5, 1.0, 0.0]
    assert np.allclose(fc_out[0].data, real_inverse_values, atol=0.0001)

    print(fc_out[1])
    assert fc_out[1].unit == "m^-1"
    img_inverse_values = [-0.5, 0.5,  0.5, -0.5]
    assert np.allclose(fc_out[1].data, img_inverse_values, atol=0.0001)
