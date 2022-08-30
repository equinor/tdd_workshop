# Development environment

This describe a typical development environment and the toolbox that is in use.

## Codespace

[Codespaces](https://docs.github.com/en/codespaces) creates an environment in the cloud for which the user can run and debug their project within their browser. This project has a pre-made configuration including all necessary requirements for the user once it has been made.

### Create and use

To create a codespace please first fork the repository and create the codespace from the fork (we do this in order for the user to have access to push their changes to the repository).

While visiting your fork in the browser, select the _<>Code_ dropdown box and choose Codespaces. Codespaces requires Single-sign-on (SSO), and you will be prompted if you have not yet enabled it. Please enable and continue. Single-sign-on within your organisations requires you to sign in using your Equinor account.

You should now be able to create a new codespace (or choose one, if you have one already). Or if you want to use one that is already made, click the options (three vertical dots) at the codespace you want to use.

Codespace within a browser runs in a vscode plugin and you should have close to all features available, be able to run and debug your code and use git to push changes back to your repository.

### Remote connection in local application

Please note that it is also possible to use a local Visual Studio Code application and connect to any codespace you have created. You need the Github Codespaces extension to do so (please make sure you update vscode and extensions - some features are not available on older versions). After install and sign-in you should be able to chose any codespace from the "remote explorer" (in sidebar) after selecting "GitHub Codespaces" in the drop down.

After setting up the environment please verify that you are able to install and run the tests.

## Local

### Interpreter

This workshop is run using Python for any code development, and hence local work must include a python interpreter. There are different ways to set up an interpreter, even within each operating system. We strongly encourage participants to do this before participating in the workshop. Some operating systems have python included already. Python is available in the Microsoft Store for participants on a managed Equinor laptop, at the time of writing this documentation.

We strongly recommend at least Python 3.6, preferably higher. Please note that it is good practice to use a [virtual environment](https://docs.python.org/3/library/venv.html) to install your own as well as third party packages.

After setting up the environment please verify that you are able to install and run the tests.

### Integrated Development Environment (IDE)

You are free to use whatever editor you please, but we recommend using one that is suited for python development. Typically Jetbrains Pycharm and [Visual Studio Code](https://code.visualstudio.com/) are good alternatives. While Pycharm is a python specific IDE, vscode is made for any language and requires the user to install extensions in order to properly integrate with project. Please check out the documentation for how to setup your IDE ([vscode Debugging Tools](https://code.visualstudio.com/docs/editor/debugging))

### Git

Typically Git is included with osx or unix operating systems. If you are on an Equinor Windows PC, then Git can be installed from Equinor Applications (apply through AccessIT).

### SSH

We recommend using SSH for authentication with Github.com. Information on how to generate and install keys are available on the [github docs](https://docs.github.com/en/enterprise-server@2.19/github/authenticating-to-github/connecting-to-github-with-ssh). Remember that SSH keys that will be used against Equinor repositories will have to be enabled for SSO (in the same page where you add the key to your github account).

## Windows-Specific Tools

Git Bash (comes with the Git for Windows installation) is ok for git and SSH, but not so for real _bashing_ in windows.

Tools like GitBash and VSCode for Windows can be installed using Equinor Application Store on Windows 10.

## General

Tools can be downloaded and installed manually or by your preferred package management systems. Some of the tools are available in [Access IT](https://accessit.equinor.com/) for Managed Equinor Windows computers.

* based on https://github.com/equinor/oc-iaas-iac-course
