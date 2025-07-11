---
category: {{ scripting_info.category }}
plugin: {{ scripting_info.plugin }}
license: {{ scripting_info.license }}
---

# {{ operator_name }}

**Version: {{ scripting_info.version }}**

## Description

{{ operator_description }}

{%- if show_supported_file_types %}

## Supported file types

{%- for namespace, extensions in namespace_map|dictsort %}
- {{namespace}}: {{extensions}}
{%- endfor %}

{%- endif %}

## Inputs

| Input | Name | Expected type(s) | Description |
|-------|-------|------------------|-------------|
{%- for input in inputs %}
| {% if not input.optional %}<strong>Pin {{ input.pin_number }}</strong> <br><span style="background-color:#d93025; color:white; padding:2px 6px; border-radius:3px; font-size:0.75em;">Required</span>{% else %}<strong>Pin {{ input.pin_number }}</strong>{% endif %}|  {{ input.name }} |
{%- for t in input.types -%}{% if "::" in t %}{{ t }}{% elif t == "int32" or t == "bool" or t == char or t == "double" or t == "string" or t == "uint32" or t == "uint64" or t == "vector<int32>" or t == "vector<bool>" or t == "vector<char>" or t == "vector<double>" or t == "vector<string>" or t == "vector<float>" %}[`{{ t }}`](../../core-concepts/dpf-types.md#standard-types}}){% elif t.startswith("abstract_") %}[`{{ t }}`](../../core-concepts/dpf-types.md#{{ t | replace("abstract_", "") | replace("_", "-") | replace (" ", "-") | lower}}){% else %}[`{{ t }}`](../../core-concepts/dpf-types.md#{{ t | replace("_", "-") | replace(" ", "-") | lower}}){% endif %}{% if not loop.last %}, {% endif %}{%- endfor %} | {{ input.document | replace("\n", "<br>") }} |
{%- endfor %}

## Outputs

| Output |  Name | Expected type(s) | Description |
|-------|------|------------------|-------------|
{%- for output in outputs %}
|  **Pin {{ output.pin_number }}**| {{ output.name }} |
{%- for t in output.types -%}{% if "::" in t %}{{ t }}{% elif t == "int32" or t == "bool" or t == char or t == "double" or t == "string" or t == "uint32" or t == "uint64" or t == "vector<int32>" or t == "vector<bool>" or t == "vector<char>" or t == "vector<double>" or t == "vector<string>" or t == "vector<float>" %}[`{{ t }}`](../../core-concepts/dpf-types.md#standard-types}}){% elif t.startswith("abstract_") %}[`{{ t }}`](../../core-concepts/dpf-types.md#{{ t | replace("abstract_", "") | replace("_", "-") | replace (" ", "-") | lower}}){% else %}[`{{ t }}`](../../core-concepts/dpf-types.md#{{ t | replace("_", "-") | replace(" ", "-") | lower}}){% endif %}{% if not loop.last %}, {% endif %}{%- endfor %} | {{ output.document }} |
{%- endfor %}

## Configurations

| Name| Expected type(s) | Default value | Description |
|-----|------|----------|-------------|
{%- for configuration in configurations %}
| **{{ configuration.name }}** |
{%- for t in configuration.types -%}{% if "::" in t %}{{ t }}{% elif t == "int32" or t == "bool" or t == char or t == "double" or t == "string" or t == "uint32" or t == "uint64" or t == "vector<int32>" or t == "vector<bool>" or t == "vector<char>" or t == "vector<double>" or t == "vector<string>" or t == "vector<float>" %}[`{{ t }}`](../../core-concepts/dpf-types.md#standard-types}}){% elif t.startswith("abstract_") %}[`{{ t }}`](../../core-concepts/dpf-types.md#{{ t | replace("abstract_", "") | replace("_", "-") | replace (" ", "-") | lower}}){% else %}[`{{ t }}`](../../core-concepts/dpf-types.md#{{ t | replace("_", "-") | replace(" ", "-") | lower}}){% endif %}{% if not loop.last %}, {% endif %}{%- endfor %} | {{ configuration.default_value }} | {{ configuration.document }} |
{%- endfor %}

## Scripting

 **Category**: {{ scripting_info.category }}

 **Plugin**: {{ scripting_info.plugin }}

 **Scripting name**: {{ scripting_info.scripting_name }}

 **Full name**: {{ scripting_info.full_name }}

 **Internal name**: {{ scripting_info.internal_name }}

 **License**: {{ scripting_info.license }}


## Changelog

{%- for entry in scripting_info.changelog %}

- {{ entry }}
{%- endfor %}
