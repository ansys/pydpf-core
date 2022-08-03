.. _contributing:

============
Contributing
============
We absolutely welcome any code contributions and we hope that this
guide will facilitate an understanding of the DPF-Core code
repository. It is important to note that while the DPF-Core software
package is maintained by Ansys and any submissions will be reviewed
thoroughly before merging, we still seek to foster a community that
can support user questions and develop new features to make this
software a useful tool for all users.  As such, we welcome and
encourage any questions or submissions to this repository.


Cloning the Source Repository
-----------------------------

You can clone the source repository from `DPF-Core
GitHub <https://https://github.com/pyansys/DPF-Core>`_
and install the latest version in development mode by running:

.. include:: pydpf-core_clone_install.rst


Questions
---------
For general or technical questions about the project, its
applications, or about software usage, please create an issue at
`DPF-Core Issues <https://github.com/pyansys/DPF-Core/issues>`_ where the
community or DPF-Core developers can collectively address your
questions. To reach the project support team, 
email `pyansys.support@ansys.com <pyansys.support@ansys.com>`_.

By posting on the issues page, your question can be addressed by
community members with the needed expertise and the knowledge gained
will remain available on the issues page for other users.


Reporting Bugs
--------------
If you encounter any bugs or crashes while using DPF-Core, please
report it at `DPF-Core Issues <https://github.com/pyansys/DPF-Core/issues>`_
with an appropriate label so we can promptly address it.  When
reporting an issue, please be overly descriptive so that we may
reproduce it. Whenever possible, please provide tracebacks,
screenshots, and sample files to help us address the issue.


Feature Requests
----------------
We encourage users to submit ideas for improvements to DPF-Core!
Please create an issue on the `DPF-Core Issues <https://github.com/pyansys/DPF-Core/issues>`_
with a **Feature Request** label to suggest an improvement.
Please use a descriptive title and provide ample background information to help
the community implement that functionality. For example, if you would like a
reader for a specific file format, please provide a link to documentation of
that file format and possibly provide some sample files with screenshots to work
with. We will use the issue thread as a place to discuss and provide feedback.


Contributing New Code
---------------------
If you have an idea for how to improve DPF-Core, consider first
creating an issue as a feature request which we can use as a
discussion thread to work through how to implement the contribution.

Once you are ready to start coding, please see the `Development
Practices <#development-practices>`__ section for more details.


Licensing
---------
All contributed code will be licensed under The MIT License found in
the repository. If you did not write the code yourself, it is your
responsibility to ensure that the existing license is compatible and
included in the contributed files or you can obtain permission from
the original author to relicense the code.

--------------

Development Practices
---------------------
This section provides a guide to how we conduct development in the
DPF-Core repository. Please follow the practices outlined here when
contributing directly to this repository.

Guidelines
~~~~~~~~~~

Consider the following general coding paradigms when contributing:

1. Follow the `Zen of Python <https://www.python.org/dev/peps/pep-0020/>`__. As
   silly as the core Python developers are sometimes, there's much to
   be gained by following the basic guidelines listed in PEP 20.
   Without repeating them here, focus on making your additions
   intuitive, novel, and helpful for DPF-Core and its users.

   When in doubt, ``import this``

2. **Document it**. Include a docstring for any function, method, or
   class added.  Follow the `numpydocs docstring
   <https://numpydoc.readthedocs.io/en/latest/format.html>`_
   guidelines, and always provide a for simple use cases for the new
   features.

3. **Test it**. Since Python is an interperted language, if it's not
   tested, it's probably broken.  At the minimum, include unit tests
   for each new feature within the ``tests`` directory.  Ensure that
   each new method, class, or function has reasonable (>90%) coverage.

Additionally, please do not include any data sets for which a license
is not available or commercial use is prohibited.

Finally, please take a look at our `Code of Conduct <https://github.com/pyansys/DPF-Core/blob/master/CODE_OF_CONDUCT.md>`_


Contributing to DPF-Core through GitHub
---------------------------------------
To submit new code to DPF-Core, first fork the `DPF-Core GitHub Repo
<https://github.com/pyansys/DPF-Core>`_ and then clone the forked
repository to your computer.  Next, create a new branch based on the
`Branch Naming Conventions Section <#branch-naming-conventions>`__ in
your local repository.

Next, add your new feature and commit it locally. Be sure to commit
often as it is often helpful to revert to past commits, especially if
your change is complex. Also, be sure to test often. See the `Testing
Section <#testing>`__ below for automating testing.

When you are ready to submit your code, create a pull request by
following the steps in the `Creating a New Pull Request
section <#creating-a-new-pull-request>`__.


Creating a New Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Once you have tested your branch locally, create a pull request on
`DPF-Core <https://github.com/pyansys/DPF-Core>`_ and target your
merge to `master`.  This will automatically run continuous
integration (CI) testing and verify your changes will work across all
supported platforms.

For code verification, someone from the pyansys developers team will
review your code to verify your code meets our our standards.  Once
approved, if you have write permission you may merge the branch.  If
you don't have write permission, the reviewer or someone else with
write permission will merge the branch and delete the PR branch.

Since it may be necessary to merge your branch with the current
release branch (see below), please do not delete your branch if it
is a ``fix/`` branch.


Branch Naming Conventions
~~~~~~~~~~~~~~~~~~~~~~~~~
To streamline development, we have the following requirements for
naming branches. These requirements help the core developers know what
kind of changes any given branch is introducing before looking at the
code.

-  ``fix/``: any bug fixes, patches, or experimental changes that are
   minor
-  ``feat/``: any changes that introduce a new feature or significant
   addition
-  ``junk/``: for any experimental changes that can be deleted if gone
   stale
-  ``maint/``: for general maintenance of the repository or CI routines
-  ``doc/``: for any changes only pertaining to documentation
-  ``no-ci/``: for low impact activity that should NOT trigger the CI
   routines
-  ``testing/``: improvements or changes to testing
-  ``release/``: releases (see below)

Testing
~~~~~~~
Periodically when making changes, be sure to test locally before
creating a pull request. The following tests will be executed after
any commit or pull request, so we ask that you perform the following
sequence locally to track down any new issues from your changes.

To test the core API, be sure to have ANSYS 2021R1 or newer
installed.  Next, install the testing requirements with:

.. code::

    pip install -r requirements/requirements_test.txt

Run the primary test suite and generate a coverage report with:

.. code::

    pytest -v --cov ansys-dpf-core

If you do not have DPF-Core installed locally, setup the following
environment variables to connect to a remote server.

.. code::

   export DPF_START_SERVER=False
   export DPF_PORT=50054
   export DPF_IP=<XXX.XXX.XXX.XXX>

Or on windows:

.. code::

   set DPF_START_SERVER=False
   set DPF_PORT=50054
   set DPF_IP=<XXX.XXX.XXX.XXX>

This will tell `ansys.dpf.core` to attempt to connect to the existing
DPF service by default rather than launching a new service.


Spelling and Code Style
~~~~~~~~~~~~~~~~~~~~~~~

If you are using Linux or Mac OS, run check spelling and coding style
with:

.. code::

   make

Any misspelled words will be reported.  You can add words to be
ignored to ``ignore_words.txt``


Documentation
-------------
Documentation for DPF-Core is generated from three sources:

- Docstrings from the classes, functions, and modules of ``ansys.dpf.core`` using `sphinx.ext.autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_.
- Restructured test from `docs/`
- Examples from `examples/`

General usage and API descriptions should be placed within `docs/` and
the docstrings.  Full examples should be placed in `examples`.


Documentation Style and Organization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Docstrings should follow the `numpydocs docstring
<https://numpydoc.readthedocs.io/en/latest/format.html>`_ guidelines.
Documentation from `docs` use reStructuredText format.  Examples
within the `examples/` directory should be PEP8 compliant and will be
compiled dynamically during the build process; ensure they run
properly locally as they will be verified through the continuous
integration performed on GitHub Actions.


Building the Documentation Locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Documentation for DPF-Core is hosted at docs.pyansys.com and is
automatically built and deployed using the GitHub Actions.  You can
build and verify the html documentation locally by install ``sphinx``
and the other documentation build dependencies by running the
following from the DPF-Core source directory:

.. code::

   pip install -r requirements/requirements_docs.txt


Next, if running Linux/Mac OS, build the documentation with 

.. code::

    make -C docs html

Otherwise, if running Windows, build the documentation by running

.. code::

   cd docs
   make.bat html

Upon the successful build of the documentation, you can open the local
build by opening ``index.html`` at ``docs/build/html/`` with
your browser.

If you are running DPF remotely or through docker, see the `Testing Section <#testing>`__ for setting up the correct environment variables.


Continuous Integration and Continuous Delivery
----------------------------------------------
The DPF-Core project uses continuous integration and delivery (CI/CD)
to automate the building, testing, and deployment tasks.  The CI
Pipeline is deployed on both GitHub Actions and Azure Pipelines and
performs following tasks:

- Module wheel build
- Core API testing
- Spelling and style verification
- Documentation build


Branching Model
~~~~~~~~~~~~~~~
This project has a branching model that enables rapid development of
features without sacrificing stability, and closely follows the 
`Trunk Based Development <https://trunkbaseddevelopment.com/>`_ approach.

The main features of our branching model are:

- The `master` branch is the main development branch.  All features,
  patches, and other branches should be merged here.  While all PRs
  should pass all applicable CI checks, this branch may be
  functionally unstable as changes might have introduced unintended
  side-effects or bugs that were not caught through unit testing.
- There will be one or many `release/` branches based on minor
  releases (for example `release/0.2`) which contain a stable version
  of the code base that is also reflected on PyPi/.  Hotfixes from
  `fix/` branches should be merged both to master and to these
  branches.  When necessary to create a new patch release these
  release branches will have their `__version__.py` updated and be
  tagged with a patched semantic version (e.g. `0.2.1`).  This
  triggers CI to push to PyPi, and allow us to rapidly push hotfixes
  for past versions of ``ansys.dpf.core`` without having to worry about
  untested features.
- When a minor release candidate is ready, a new `release` branch will
  be created from `master` with the next incremented minor version
  (e.g. `release/0.2`), which will be thoroughly tested.  When deemed
  stable, the release branch will be tagged with the version (`0.2.0`
  in this case), and if necessary merged with master if any changes
  were pushed to it.  Feature development then continues on `master`
  and any hotfixes will now be merged with this release.  Older
  release branches should not be deleted so they can be patched as
  needed.


Minor Release Steps
~~~~~~~~~~~~~~~~~~~
Minor releases are feature and bug releases that improve the
functionality and stability of ``DPF-Core``.  Before a minor release is
created the following will occur:

1.  Create a new branch from the ``master`` branch with name
    ``release/MAJOR.MINOR`` (e.g. `release/0.2`).

2. Locally run all tests as outlined in the `Testing Section <#testing>`__
and ensure all are passing.

3. Locally test and build the documentation with link checking to make sure
no links are outdated. Be sure to run `make clean` to ensure no results are
cached.

    .. code::

        cd docs
        make clean  # deletes the sphinx-gallery cache
        make html -b linkcheck

4. After building the documentation, open the local build and examine
   the examples gallery for any obvious issues.

5. Update the version numbers in ``ansys/dpf/core/_version.py`` and commit it.
   Push the branch to GitHub and create a new PR for this release that
   merges it to master.  Development to master should be limited at
   this point while effort is focused on the release.

6. It is now the responsibility of the `DPF-Core` community and
   developers to functionally test the new release.  It is best to
   locally install this branch and use it in production.  Any bugs
   identified should have their hotfixes pushed to this release
   branch.

7. When the branch is deemed as stable for public release, the PR will
   be merged to master and the `master` branch will be tagged with a
   `MAJOR.MINOR.0` release.  The release branch will not be deleted.
   Tag the release with:

    .. code::

	git tag <MAJOR.MINOR.0>
        git push origin --tags


8. Create a list of all changes for the release. It is often helpful
   to leverage `GitHub's compare feature
   <https://github.com/pyansys/DPF-Core/compare>`_ to see the
   differences from the last tag and the `master` branch.  Be sure to
   acknowledge new contributors by their GitHub username and place
   mentions where appropriate if a specific contributor is to thank
   for a new feature.

9. Place your release notes from step 8 in the description within
   `DPF-Core Releases <https://github.com/pyansys/mapdl/releases/new>`_


Patch Release Steps
~~~~~~~~~~~~~~~~~~~
Patch releases are for critical and important bugfixes that can not or
should not wait until a minor release.  The steps for a patch release

1. Push the necessary bugfix(es) to the applicable release branch.
   This will generally be the latest release branch
   (e.g. `release/0.2`).

2. Update `__version__.py` with the next patch increment
   (e.g. `0.2.1`), commit it, and open a PR that merge with the
   release branch.  This gives the `DPF-Core` developers and community
   a chance to validate and approve the bugfix release.  Any
   additional hotfixes should be outside of this PR.

3. When approved, merge with the release branch, but not `master` as
   there is no reason to increment the version of the `master` branch.
   Then create a tag from the release branch with the applicable
   version number (see above for the correct steps).

4. If deemed necessary a release notes page.
