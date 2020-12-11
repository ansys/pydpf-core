from ansys import dpf
import os


class PinSpecification:
    def __init__(self, name = None, type_names = None, optional = None, document = None, ellipsis = None):
        self.name = name
        self.type_names = type_names
        self.document = document
        setattr(self, "optional", optional)
        setattr(self, "ellipsis", ellipsis)
      
def _loadOperators():
    """Will be available in 21.2 release."""
    database_path = os.getcwd()
    database_path += '/../ansys/dpf/operators'
    generator = dpf.Operator("python_generator")
    generator.inputs.dll_source_path.connect("Ans.Dpf.Native.dll")
    generator.inputs.output_path.connect(database_path)
    generator.run()
    generator.inputs.dll_source_path.connect("Ans.Dpf.FEMUtils.dll")
    generator.inputs.output_path.connect(database_path)
    generator.inputs.overwrite_existing_files.connect(False)
    generator.run()
    generator.inputs.dll_source_path.connect("mapdlOperatorsCore.dll")
    generator.inputs.output_path.connect(database_path)
    generator.inputs.overwrite_existing_files.connect(False)
    generator.run()
    generator.inputs.dll_source_path.connect("meshOperatorsCore.dll")
    generator.inputs.output_path.connect(database_path)
    generator.inputs.overwrite_existing_files.connect(False)
    generator.run()
    