from ansys.dpf import core as dpf
from ansys.dpf.core.changelog import Changelog
from ansys.dpf.core.custom_operator import CustomOperatorBase
from ansys.dpf.core.operator_specification import CustomSpecification, SpecificationProperties, \
    PinSpecification


class CustomOperator(CustomOperatorBase):
    @property
    def name(self):
        """Return the scripting name of the operator in Snake Case."""
        return "my_custom_operator"

    @property
    def specification(self) -> CustomSpecification:
        """Create the specification of the custom operator.

        The specification declares:
            - the description of the operator
            - the inputs of the operator
            - the outputs of the operator
            - the properties of the operator (a username, a category, a required license)
            - the changelog of the operator (starting with DPF 2026 R1)
        """
        # Instantiate the custom specification
        spec = CustomSpecification()
        # Set the description of the operator
        spec.description = "What the Operator does. You can use MarkDown and LaTeX in descriptions."
        # Define the inputs of the operator if any
        spec.inputs = {
            0: PinSpecification(name="input_0", type_names=[dpf.Field, dpf.FieldsContainer],
                                document="Describe input pin 0."),
        }
        # Define the outputs of the operator if any
        spec.outputs = {
            0: PinSpecification(name="output_0", type_names=[dpf.Field], document="Describe output pin 0."),
        }
        # Define the properties of the operator if any
        spec.properties = SpecificationProperties(
            user_name="my custom operator",  # Optional, defaults to the scripting name with spaces
            category="my_category",  # Optional, defaults to 'other'
            license="my_license",  # Optional, defaults to None
        )
        # Set the changelog of the operator to track changes
        spec.set_changelog(Changelog()
                           .patch_bump("Describe a patch bump.")
                           .major_bump("Describe a major bump.")
                           .minor_bump("Describe a minor bump.")
                           .expect_version("1.1.0")  # Checks the resulting version is as expected
        )
        return spec

    def run(self):
        """Run the operator and execute the logic implemented here.

        This method defines the behavior of the operator.

        Request the inputs with the method ``get_input``,
        perform operations on the data,
        then set the outputs with the method ``set_output``,
        and finally call ``set_succeeded``.

        In this example, the operator changes the name of a Field.

        """
        # First get the field in input by calling get_input for the different types supported
        # # Try requesting the input as a Field
        field: dpf.Field = self.get_input(0, dpf.Field)
        # # If function returns None, there is no Field connected to this input
        if field is None:
            # # Try requesting the input as a FieldsContainer
            field: dpf.FieldsContainer = self.get_input(0, dpf.FieldsContainer).get_field(0)
        # # If the input is optional, set its default value
        # # If the input is not optional and empty, raise an error
        if field is None:
            raise ValueError("my_custom_operator: mandatory input 'input_0' is empty or of an unsupported type.")

        # Perform some operations on the data
        field.name = "new_field_name"

        # Set the output of the operator
        self.set_output(0, field)

        # And declare the operator run a success
        self.set_succeeded()


def load_operators(*args):
    from ansys.dpf.core.custom_operator import record_operator
    record_operator(CustomOperator, *args)
