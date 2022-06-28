> A tool for calculating carbon emissions associated from organisational mileage claim data developed by the Sustainability Team at [Kent Community Health NHS Foundation Trust](https://www.kentcht.nhs.uk/) in collaboration with [Dr Steven Firth](https://github.com/stevenkfirth) at [Loughborough University](https://www.lboro.ac.uk/departments/abce/).

<h1 align="center">
  <br>
  <img src="https://github.com/danwrisar/COVE_ContextOfVehicleEmissionsTool/blob/main/img/covelogo.png" alt="COVE Tool" width="200">
  <br>
  Context of Vehicle Emissions (COVE) Tool v1.0
  <br>
</h1>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a> •
  <a href="#example-report">Example report</a> •
  <a href="#change-log">Change log</a>
</p>

## Key features

* Pull outputs from the [UK Department for Transport's Vehicle Enquiry Service API](https://developer-portal.driver-vehicle-licensing.api.gov.uk/apis/vehicle-enquiry-service/vehicle-enquiry-service-description.html#vehicle-enquiry-service-api) into your mileage claim data including:
    - Vehicle carbon emissions (CO<sub>2</sub>/km)
    - Year of manufacture
    - Fuel type
    - Vehicle colour
    - Wheelplan
    - Cylinder capacity

* Cacluate emissions associated with mileage claimed by:
    - Fuel type
    - Organisation
    - Journey reason

* Calculate mileage completed by:
    - Fuel type
    - Organisation
    - Journey reason

## How to use

The files can be downloaded by navigating to the parent folder 'cove-project' and choosing the 'Download ZIP' option from the 'Code' button. Alternatively, the repository can be forked and/or cloned using [Git](https://git-scm.com).

Each module has an individual README for guidance on how to implement via the command line or through a notebook environment:

* Module One: VES API cache creation
* Module Two: Mileage data analysis
* ~~Module Three: Create graphs to visualise the mileage claim data~~ (Coming in v1.1!)
* ~~Module Four: Geospatial visualisation of journeys, destinations and bases~~ (Coming in v1.2!)

## Emailware

The COVE Tool is [emailware](https://en.wiktionary.org/wiki/emailware). Meaning, if you liked using this tool or it has helped you in any way, please send us an email at <kentcht.sustainability@nhs.net> about anything you'd want to say about this tool. We really appreciate it!

## Credits

This software uses the following packages:

- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org/)
- [Plotly](https://pypi.org/project/plotly/)

## You may also like...

- [Driver & Vehicle Standards Agency](https://github.com/dvsa)
- [NHS PyCom](https://github.com/nhs-pycom/nhs.pycom)
- [Kent Community Health NHS Foundation Trust](https://kentcht.nhs.uk)

## License

MIT

## Change log

* Context of Vehicle Emissions (COVE) Tool v1.0 - 28 June 2022
  - Initial public release sharing 1) The means of implementation to contextualise mileage claim datasets with the DoT's Vehicle Enquiry Service API, and 2) An approach to wrangling mileage claim data to facilitate contextualisation.

## Example report

<img src="https://github.com/danwrisar/COVE_ContextOfVehicleEmissionsTool/blob/main/img/COVEReportSample.png" alt="COVE Tool">
