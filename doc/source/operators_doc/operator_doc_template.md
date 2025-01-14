# {{ operator_name }}

## Description

{{ operator_description }}

## Inputs

{% for input in inputs %}
- **Pin {{ input.pin_number }}** {{ input.name }} (type: {{ input.types }}) (optional: {{ input.optional }}): {{ input.document }}
{% endfor %}

## Outputs

{% for output in outputs %}
- **Pin {{ output.pin_number }}** {{ output.name }} (type: {{ output.types }}): {{ output.document }}
{% endfor %}

## Configurations

{% for configuration in configurations %}
- **{{ configuration.name }}** (type: {{ configuration.types }}) (default: {{ configuration.default_value }}): {{ configuration.document }}
{% endfor %}

## Scripting

- **category**: {{ scripting_info.category }}
- **plugin**: {{ scripting_info.plugin }}
- **scripting name**: {{ scripting_info.scripting_name }}
- **full name**: {{ scripting_info.full_name }}
- **internal name**: {{ scripting_info.internal_name }}