import ansys.dpf.core as dpf


def test_label_space_(server_type):
    reference = {"test": 1, "various": 2}
    ls = dpf.LabelSpace(label_space=reference)
    assert dict(ls) == reference
    assert str(ls)
    reference = {"test": 1, "various": 2}
    ls.fill(label_space=reference)
    print(ls)
