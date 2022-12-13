<div align="center">
   
  <h1>nih-box 📦</h1>
  
  **_Archive projects, metadata, and files at Box@NIH_**

  [![tests](https://github.com/OpenOmics/nih-box/workflows/tests/badge.svg)](https://github.com/OpenOmics/bx/actions/workflows/main.yaml) [![docs](https://github.com/OpenOmics/nih-box/workflows/docs/badge.svg)](https://github.com/OpenOmics/nih-box/actions/workflows/docs.yml) [![GitHub issues](https://img.shields.io/github/issues/OpenOmics/nih-box?color=brightgreen)](https://github.com/OpenOmics/nih-box/issues)  [![GitHub license](https://img.shields.io/github/license/OpenOmics/nih-box)](https://github.com/OpenOmics/nih-box/blob/main/LICENSE) 
  
  <i>
    This is the home of the [Box@NIH](https://nih.box.com/) command-line tool, [bx](https://github.com/OpenOmics/nih-box). Its long-term goals: to enable [FAIR<sup>1</sup>](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4792175/) scientific research, to archive and share project data, and to create a unified tool that makes using Box easier than ever before!
  </i>
</div>

## Overview
Welcome to bx! Before getting started, we highly recommend reading through [bx's documentation](https://openomics.github.io/nih-box/).

The **`./bx`** command-line tool is composed several inter-related sub commands to explore and archive data across the NIH's Box storage system. Each of the available sub commands perform different functions: 

 * [<code>bx <b>ls</b></code>](usage/ls.md): Change Box working directories.
 * [<code>bx <b>cd</b></code>](usage/cd.md): List Box directory contents.
 * [<code>bx <b>cp</b></code>](usage/cp.md): Copy files and directories to/from Box.
 * [<code>bx <b>mkdir</b></code>](usage/mkdir.md): Make a new directory on Box.
 * [<code>bx <b>rm</b></code>](usage/rm.md): Remove files or directories on Box.

**bx** is a command-line tool that make using Box easier than ever before! It leverages [Box's python-sdk](http://opensource.box.com/box-python-sdk/) to make it easy to manage your [Box@NIH](https://nih.box.com/) account. Users who are familiar with unix-like environments will love its easy to remember set of commands. 

Before getting started, we highly recommend reading through the [usage](usage/ls.md) section of each available sub command.

For more information about issues or trouble-shooting a problem, please checkout our [FAQ](faq/questions.md) prior to [opening an issue on Github](https://github.com/OpenOmics/nih-box/issues).

## Dependencies
**Requires:** `python>=3.8`  

At the current moment, the only dependency is python! Please install a version of python greater than or equal to _3.8_. Any missing python requirements can be installed with the _requirements.txt_.

## Contribute 
This site is a living document, created for and by members like you. **bx** is maintained by the members of OpenOmics and is improved by continous feedback! We encourage you to contribute new content and make improvements to existing content via pull request to our [GitHub repository](https://github.com/OpenOmics/nih-box).

## References
<sup>**1.**  Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., Blomberg, N., Boiten, J. W., da Silva Santos, L. B., Bourne, P. E., Bouwman, J., Brookes, A. J., Clark, T., Crosas, M., Dillo, I., Dumon, O., Edmunds, S., Evelo, C. T., Finkers, R., Gonzalez-Beltran, A., … Mons, B. (2016). The FAIR Guiding Principles for scientific data management and stewardship. Scientific data, 3, 160018. https://doi.org/10.1038/sdata.2016.18</sup>  

