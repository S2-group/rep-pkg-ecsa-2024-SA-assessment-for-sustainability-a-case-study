# Software Architecture Assessment for Sustainability: A Case Study


This repository contains the supplementary material to support the paper published at the International Conference on Software Architecture (ECSA) 2024 titled, "Software Architecture Assessment for Sustainability: A Case Study". 
This repository can be used to replicate the study and carry out a Software Architecture Evaluation of other software systems. 

## Repository Structure
This is the root directory of the repository. The directory is structured as follows:

    rep-pkg-sustainable-canvas
     .
     |
     |--- src/		Source code to generate SIS
     |
     |--- docs/		Architecture documentation
     |
     |--- data/		Data used in the paper including templates, input and output data of intermediary steps, and results
           
### Getting started
Here, we provide step-by-step instructions on using this repository, including requirements, and installation/script execution steps.

#### Pre-requisites
- Clone the repository to use it for your project or replication of steps using,
   `git clone https://github.com/iffatfatima/rep-pkg-sustainable-canvas`
- Prioritize QAs
- Document the design decisions using the [DD_Template](data/DD_Template.xlsx), assign QAs to each design option (DO)
- Create a DMatrix for each design option (see [DMatrix](data/dmatrix.xlsx) for example). Detailed instructions are provided in the paper. 

#### Generating a Sustainability Impact Score (SIS)
- Run the following command in [src](src/) folder for all design concerns

  	`python score.py "../data/dmatrix.xlsx" <option-prefix>`

	For example, to get the Sustainability Impact Score (SIS) for all design options for design concern DC-5, use the option prefix "O-5."
	Example command:

	`python score.py "../data/dmatrix.xlsx" "O-5."`

	This will provide the SIS for all options of DC-5 based on the DMatrix.

	Example output:
 
	![screenshot](data/SIS-DC-5.png)
- Document the SISs as provided in [results][data/results.xlsx] for observing trade-offs

### How to cite this work
```
@inproceedings{ecsa-2024-SA-assess-sus,
  title={{Software Architecture Assessment for Sustainability: A Case Study}},
  author={Iffat Fatima and Patricia Lago},
  booktitle={Software Architecture},
  publisher={Springer Nature Switzerland},
  year={2024}
}
```
