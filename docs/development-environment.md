# Development environment

This describe a typical development environment and the toolbox that is in use.

The current scripting uses _Bash_ which assumes a Linux development environment.

## General tools

- An IDE like Visual Studio Code ([link](https://code.visualstudio.com/))
  - Helpful plug-ins
    - Debugging Tools (https://code.visualstudio.com/docs/editor/debugging)
- If you are on an Equinor Windows PC, then Git can be installed from Equinor Applications (apply through AccessIT)
- ssh-keygen - We recommend using SSH for authentication with Github.com. Information on how to generate and install keys are available on the [github docs](https://docs.github.com/en/enterprise-server@2.19/github/authenticating-to-github/connecting-to-github-with-ssh). Remember that SSH keys that will be used against Equinor repositories will have to be enabled for SSO (in the same page where you add the key to your github account)
- SSH

## Windows-Specific Tools

- Git Bash (comes with the Git for Windows installation) is ok for git and SSH, but not so for real _bashing_ in windows.

Tools like GitBash and VSCode for Windows can be installed using Equinor Application Store on Windows 10.

## General

Tools can be downloaded and installed manually or by your preferred package management systems. Some of the tools are available in [Access IT](https://accessit.equinor.com/) for Managed Equinor Windows computers.

* based on https://github.com/equinor/oc-iaas-iac-course
