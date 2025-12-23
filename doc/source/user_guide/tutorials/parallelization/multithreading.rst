.. _ref_tutorial_multithreading:

============================================
Multithreading with Operator Configurations
============================================

This tutorial demonstrates how to use the `num_threads` and `mutex` configuration options of DPF operators to control parallel execution and thread safety.

Overview
--------

Many DPF operators support parallel execution to speed up computations.
The `num_threads` configuration option allows you to specify the number of threads used by an operator.
The `mutex` option can be used to ensure thread safety when required.

Setting Up
----------

.. jupyter-execute::

    from ansys.dpf import core as dpf
    from ansys.dpf.core import operators as op
    from ansys.dpf.core import examples
    import numpy as np

    # Load a result file and create a Model
    model = dpf.Model(examples.find_simple_bar())
    fields_container = model.results.displacement.on_all_time_freqs.eval()

Using num_threads
-----------------

You can control the number of threads used by an operator by setting the `num_threads` option in its configuration.

Below, we compare the execution time of the norm operator with the default configuration (single-threaded) and with `num_threads=2`.

.. jupyter-execute::

    import time

    # Run with default configuration (single-threaded)
    norm_op_default = op.math.norm_fc()
    norm_op_default.inputs.fields_container.connect(fields_container)
    start = time.time()
    result_fc_default = norm_op_default.outputs.fields_container()
    elapsed_default = time.time() - start
    print(f"Norm (default config): {len(result_fc_default)} fields, time: {elapsed_default:.4f} s")

    # Run with num_threads=2
    config = op.math.norm_fc.default_config()
    config.options["num_threads"] = 2
    norm_op_mt = op.math.norm_fc(config=config)
    norm_op_mt.inputs.fields_container.connect(fields_container)
    start = time.time()
    result_fc_mt = norm_op_mt.outputs.fields_container()
    elapsed_mt = time.time() - start
    print(f"Norm (num_threads=2): {len(result_fc_mt)} fields, time: {elapsed_mt:.4f} s")

    print(f"Speedup: {elapsed_default/elapsed_mt:.2f}x (if >1, multithreading is faster)")

Using mutex for Thread Safety
----------------------------

The `mutex` option can be set to `true` to ensure that the operator executes in a thread-safe manner. This is useful if you are running multiple operators in parallel and want to avoid race conditions.

Below, we demonstrate a potential race condition by running two norm operators in parallel threads,
first without mutex (which may cause inconsistent results), and then with mutex enabled (which ensures thread safety).

.. jupyter-execute::

    import threading
    import copy

    # Function to run a norm operator and collect the result
    def run_norm_op(fc, config, results, idx):
        op = op.math.norm_fc(config=config)
        op.inputs.fields_container.connect(fc)
        results[idx] = op.outputs.fields_container()[0].data.copy()

    # Prepare results containers
    results_no_mutex = [None, None]
    results_mutex = [None, None]

    # Run two norm operators in parallel WITHOUT mutex
    config_no_mutex = op.math.norm_fc.default_config()
    config_no_mutex.options["num_threads"] = 2
    config_no_mutex.options["mutex"] = "false"
    threads = [
        threading.Thread(target=run_norm_op, args=(fields_container, config_no_mutex, results_no_mutex, 0)),
        threading.Thread(target=run_norm_op, args=(fields_container, config_no_mutex, results_no_mutex, 1)),
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Results without mutex:")
    print("Thread 0 result:", results_no_mutex[0])
    print("Thread 1 result:", results_no_mutex[1])
    print("Equal results?", np.allclose(results_no_mutex[0], results_no_mutex[1]))

    # Run two norm operators in parallel WITH mutex
    config_mutex = op.math.norm_fc.default_config()
    config_mutex.options["num_threads"] = 2
    config_mutex.options["mutex"] = "true"
    threads = [
        threading.Thread(target=run_norm_op, args=(fields_container, config_mutex, results_mutex, 0)),
        threading.Thread(target=run_norm_op, args=(fields_container, config_mutex, results_mutex, 1)),
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("\nResults with mutex:")
    print("Thread 0 result:", results_mutex[0])
    print("Thread 1 result:", results_mutex[1])
    print("Equal results?", np.allclose(results_mutex[0], results_mutex[1]))

    # Note: Without mutex, results may differ due to race conditions. With mutex, results should always match.

Summary
-------

- Use `num_threads` to control the number of threads for operator execution.
- Use `mutex` to ensure thread safety when running operators in parallel.
- These options can help you optimize performance and reliability in parallel DPF workflows.
